/* One fixed camera, one painted clone, continuous shoulder/elbow/wrist rotation. */
function createEpisodeScene(ctx, images, reducedMotion) {
  const W = 1280, H = 720;
  const clamp = v => Math.max(0, Math.min(1, v));
  const smooth = v => { const x = clamp(v); return x*x*x*(10+x*(-15+6*x)); };
  const ramp = (t, a, b) => smooth((t-a)/(b-a));
  const mix = (a,b,t) => a+(b-a)*t;
  const P = {
    right: {shoulder:[611,405],elbow:[425,422],wrist:[223,414],
      upper:[[614,337],[614,466],[445,499],[397,456],[396,364],[462,343]],
      fore:[[461,344],[465,497],[270,481],[210,450],[210,375],[277,345]],
      hand:[[0,280],[239,280],[239,488],[0,488]]},
    left: {shoulder:[931,403],elbow:[1110,419],wrist:[1310,414],
      upper:[[928,332],[1088,343],[1145,363],[1145,489],[928,470]],
      fore:[[1079,345],[1269,341],[1324,375],[1324,456],[1271,486],[1079,498]],
      hand:[[1297,280],[1536,280],[1536,488],[1297,488]]}
  };
  const source = document.createElement('canvas'); source.width=1536; source.height=1024;
  source.getContext('2d').drawImage(images.rig,0,0,1536,1024);
  const makePart = points => {
    const minX=Math.max(0,Math.floor(Math.min(...points.map(p=>p[0]))));
    const minY=Math.max(0,Math.floor(Math.min(...points.map(p=>p[1]))));
    const maxX=Math.min(1536,Math.ceil(Math.max(...points.map(p=>p[0]))));
    const maxY=Math.min(1024,Math.ceil(Math.max(...points.map(p=>p[1]))));
    const canvas=document.createElement('canvas'); canvas.width=maxX-minX; canvas.height=maxY-minY;
    const c=canvas.getContext('2d'); c.translate(-minX,-minY);
    c.beginPath(); points.forEach((p,i)=>i?c.lineTo(...p):c.moveTo(...p)); c.closePath(); c.clip();
    c.drawImage(source,0,0); return {canvas,x:minX,y:minY};
  };
  for (const arm of Object.values(P)) {
    arm.upperImage=makePart(arm.upper); arm.foreImage=makePart(arm.fore); arm.handImage=makePart(arm.hand);
    arm.length1=Math.hypot(arm.elbow[0]-arm.shoulder[0],arm.elbow[1]-arm.shoulder[1]);
    arm.length2=Math.hypot(arm.wrist[0]-arm.elbow[0],arm.wrist[1]-arm.elbow[1]);
    arm.angle1=Math.atan2(arm.elbow[1]-arm.shoulder[1],arm.elbow[0]-arm.shoulder[0]);
    arm.angle2=Math.atan2(arm.wrist[1]-arm.elbow[1],arm.wrist[0]-arm.elbow[0]);
  }
  const torsoCanvas=document.createElement('canvas');torsoCanvas.width=1536;torsoCanvas.height=1024;
  torsoCanvas.getContext('2d').drawImage(images.body,0,0,1536,1024);
  const torso={canvas:torsoCanvas,x:0,y:0};
  const scene=document.createElement('canvas'); scene.width=W; scene.height=H;
  const bg=scene.getContext('2d');
  function paintBackground(c, panel) {
    const image=images.backgrounds, sw=image.width/2, sh=image.height;
    const scale=Math.max(W/sw,H/sh);
    c.drawImage(image,panel*sw,0,sw,sh,(W-sw*scale)/2,(H-sh*scale)/2,sw*scale,sh*scale);
  }
  paintBackground(bg,1);
  bg.save();bg.beginPath();bg.rect(0,0,250,H);bg.clip();paintBackground(bg,0);bg.restore();
  bg.fillStyle='#28594e';bg.fillRect(238,0,28,H);
  bg.fillStyle='#5b8071';bg.fillRect(250,0,5,H);
  const nativePaint = (part,pivot,point,rotation) => {
    ctx.save();ctx.translate(...point);ctx.rotate(rotation);
    ctx.drawImage(part.canvas,part.x-pivot[0],part.y-pivot[1]);ctx.restore();
  };
  function arm(geometry,upperAngle,foreAngle,handAngle) {
    const s=geometry.shoulder;
    const e=[s[0]+Math.cos(upperAngle)*geometry.length1,s[1]+Math.sin(upperAngle)*geometry.length1];
    const w=[e[0]+Math.cos(foreAngle)*geometry.length2,e[1]+Math.sin(foreAngle)*geometry.length2];
    // Overlapping joint areas stay under their neighbours so no backdrop opens at a bend.
    nativePaint(geometry.handImage,geometry.wrist,w,handAngle-geometry.angle2);
    nativePaint(geometry.foreImage,geometry.elbow,e,foreAngle-geometry.angle2);
    nativePaint(geometry.upperImage,geometry.shoulder,s,upperAngle-geometry.angle1);
    return {shoulder:s,elbow:e,wrist:w};
  }
  function pose(t) {
    const secondary=reducedMotion.matches?0:1;
    const lift=ramp(t,3.8,5.5), fore=ramp(t,4.0,5.7);
    const anticipation=Math.sin(Math.PI*ramp(t,3.0,3.8))*.016;
    const breath=secondary*Math.sin(t*1.9)*.002;
    const lean=secondary*(-.012*lift+anticipation+breath);
    return {
      lift,upper:mix(1.78,4.47,lift),fore:mix(1.53,4.72,fore),
      hand:mix(1.58,4.76,ramp(t,4.13,5.85))+secondary*Math.sin(t*2)*.008*lift,
      lean,bodyY:secondary*Math.sin(t*1.9)*1.2,
      leftUpper:1.35+secondary*Math.sin(t*1.9+1)*.006,
      leftFore:1.52+secondary*Math.sin(t*1.9+.5)*.008,
      peek:ramp(t,8.6,12.5),teacher:secondary*.007*Math.sin(t*1.4)
    };
  }
  function clone(t,p) {
    ctx.save();ctx.translate(644,920+p.bodyY);ctx.rotate(p.lean);ctx.scale(.68,.68);ctx.translate(-768,-1024);
    const joints=arm(P.right,p.upper,p.fore,p.hand);
    arm(P.left,p.leftUpper,p.leftFore,p.leftFore+.04);
    ctx.drawImage(torso.canvas,torso.x,torso.y);
    ctx.restore();return joints;
  }
  function atlasActor(index,cx,baseline,scale,angle) {
    const image=images.characters, sw=image.width/3,sh=image.height/2;
    ctx.save();ctx.translate(cx,baseline);ctx.rotate(angle);ctx.scale(scale,scale);
    ctx.drawImage(image,index%3*sw,Math.floor(index/3)*sh,sw,sh,-256,-512,512,512);ctx.restore();
  }
  function render(t) {
    const p=pose(t);ctx.clearRect(0,0,W,H);ctx.drawImage(scene,0,0);
    ctx.imageSmoothingEnabled=true;ctx.imageSmoothingQuality='high';
    // Teacher, clone and original retain their physical position throughout the shot.
    atlasActor(5,1090,804,1.38,p.teacher);
    const joints=clone(t,p);
    ctx.save();ctx.beginPath();ctx.rect(0,0,238,H);ctx.clip();
    const secondary=reducedMotion.matches?0:1;
    atlasActor(4,mix(-240,65,p.peek),858+secondary*3*p.peek,1.28,-secondary*.055*p.peek);
    ctx.restore();
    ctx.fillStyle='#28594e';ctx.fillRect(238,0,28,H);
    return {joints,pose:p};
  }
  return {render,pose};
}
