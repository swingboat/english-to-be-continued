# 最终视觉与功能复核

ROUND 1
Seen in one second: 暖色走廊里红蓝内搭的两个小帅。
Idea (one sentence): 分身举起的手把“只说 Hello”的保证变成反转。
Live thing: 30 秒有限动画可播放、暂停、拖动和按剧情跳转。
Layout words by section: hero=cinema / script=sequential image-and-text / words=two-column vocabulary / cast=voice profiles / publishing=copy and covers。
Scores: design 7.0 · usability 7.0 · creativity 7.6 · content 8.6 → overall 6.0
Caps applied: 首轮 inspector 的 covered-text FAIL。
Top three problems (most visible first), each with the screenshot it shows in and the fix:
1. mobile-fold.jpg：单词提示盖住小帅的脸。手机把提示移至画面下方，仅覆盖衣服区域。
2. desktop-fold.jpg：画面过高，字幕和暂停按钮在首屏之外。桌面改为画面在左、字幕与控制在右，共用一个播放器；手机保留下方字幕。
3. 首轮 inspector 错把尚未到达的结尾题字作为屏上大字检测：它只用透明度隐藏。改为真实 hidden 状态，仅在结尾时解除；静止阅读不包含未出现的题字。

ROUND 2
Seen in one second: 校园动画播放器和两个熟悉的人物。
Idea (one sentence): 自信的拇指与举起的手形成动作反差。
Live thing: 播放器整套控制与离线人物试听。
Layout words by section: hero=cinema / script=sequential image-and-text / words=two-column vocabulary / cast=voice profiles / publishing=copy and covers。
Scores: design 7.5 · usability 8.0 · creativity 7.6 · content 8.6 → overall 7.8
Caps applied: 无；inspector 0 FAIL。
Top three problems (most visible first), each with the screenshot it shows in and the fix:
1. desktop-arm-in-motion.jpg：刚体旋转时肩部出现破口。改为单独手臂纹理层的连续网格形变，肩部固定，移除头部硬裁切产生的接缝。
2. desktop-confidence.jpg：暂停后的状态句仍显示“正在试演”。暂停与跳转显示清楚的暂停状态。
3. desktop-cast.jpg：参考文件路径紧接用途说明，阅读拥挤。增加路径组的间距。

ROUND 3
Seen in one second: 小帅与分身的暖色校园动画试演，播放动作明显。
Idea (one sentence): 同一张脸、不同颜色的内搭与一只举起的手，把英语单词变成戏剧行动。
Live thing: 完整 30 秒样片，播放暂停、重播、键盘进度、三段剧情定位和音效开关均有效。
Layout words by section: hero=cinema / script=sequential image-and-text / words=two-column vocabulary / cast=voice profiles / publishing=copy and covers / continuity=disclosure。
Scores: design 7.7 · usability 8.1 · creativity 7.6 · content 8.6 → overall 7.9
Caps applied: 无；最终 inspector 在 1440、768、390 像素均 0 FAIL。375 像素另验证无横向溢出。
Top three problems (most visible first), each with the screenshot it shows in and the fix:
1. desktop-arm-in-motion.jpg：六个姿势限制了表演的细腻程度。肩部衔接已修复；更多动作过渡留给后续动画制作，当前明确交付有限动画试演。
2. desktop-fold.jpg：较长英文句在侧栏会折成多行。保持 22px 正文与固定栏宽便于阅读；全屏和手机改为画面下方显示。
3. mobile-page-01.jpg：完整剧本篇幅较长。保留必需的完整内容，以顶部导航、词汇链接和八格目录帮助定位，不用隐藏正文缩短页面。

最后一轮已逐张打开最终 inspector 列出的 10 张截图，包括三个首屏和全部七张页面合成图；另查看关键动作、手机、单词、人物和发布区截图。

## 检查证据与保留告警

- 功能检查：`production/book-01/ep-001/checks/animation/verification.json`，20 项通过，0 浏览器异常、0 外部请求。
- 页面检查：`inspect/report.json`，最终 0 FAIL / 1 WARN。
- 保留 no-footage WARN：AGENTS.md 明确当前项目不制作和导出视频。此处为真实可播放的 Canvas 动画，不为消除告警添加无关视频。
- 源码 lint：4 个文件，0 FAIL / 1 WARN。保留的零填充用于真实播放时钟 0:06，与装饰序号无关。
- 配音边界：尚无正式英文语音；页面与最终交付均如实标注，未使用人物试听文本替代剧情台词。

## 素材与方向报告

方向 Colour chapters，seed 1548411302。两次 hero 改抽及最终为了连续样片而采用媒体优先构图的理由见 `build-notes.md`。

原漫画、两张封面与四份声音参考沿用项目已有资产。新增两张图集通过内置 imagegen 按原漫画参考生成，文件、尺寸和哈希见 `production/book-01/ep-001/animation/assets.json`，完整提示词见同目录 `image-prompts.json`。没有使用图库照片、图库视频、外部音乐或虚构数据；无需要替换的占位内容。没有任何以 SVG 冒充照片的素材。

网页所用 Schibsted Grotesk 来自项目已有字体文件，SIL OFL 随源文件保留。所有素材已内嵌唯一分集 HTML。
