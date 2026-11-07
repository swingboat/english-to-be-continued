# 第一集制作说明

第一集为《替我说句 Hello，你怎么当上班长了？》。唯一交付页面是 [ep-001.html](../../../episodes/book-01/ep-001.html)，图片、字体、动画素材与人物参考音频全部内嵌，可单文件离线打开。

## 动画试演

2026-11-06 根据用户对旧版“不连贯”的反馈，改为首屏 16 秒连续动作试演。内容来自第 4 格：老师提问、分身举手、门外小帅探头。全程同一镜头，红内搭为小帅、蓝内搭为分身，小帅没有进入教室。

分身用同一身体、头部与手臂素材，围绕肩、肘、腕连续转动，保持比例与位置一致，移除旧版多张姿势图的硬切和逐条纹理拼接。采用 HTML Canvas 与本地音效合成，不依赖外部资源或库。支持播放、暂停、重播、拖动进度、剧情跳转与桌面全屏；不自动播放，播放参考音频会暂停动画。

这是二维剪纸式动作、音效与双语字幕预演。字幕复用原英文解说 EN008—EN011，共四组；**没有正式英文台词配音，也不把人物试听音频作为本集台词使用。** 正式英文解说使用小帅已选定音色，配音、剪辑、正式字幕时间轴与视频导出由视频项目完成。完整动画片仍需更丰富的中间动作与表演，本项目没有导出视频。

## 完整交付

- 8 格完整剧本、31 条角色对白参考、动作与音效说明。
- 小帅第一人称英文解说：23 句英文与逐句对应的简体中文字幕。
- 原有 8 格漫画完整保留。
- confidence、volunteer、goal、challenge、schedule 的词义、例句、翻译、教材位置与回忆提示。
- 小帅、小帅的分身、班主任、苏小满的人物与配音设定；内嵌当前参考 WAV 与对应试听文本。苏小满继续标为暂定采用，其余三人已选定；构建核对所选 WAV 的哈希。
- 保留既有发布标题、描述、5 个话题、恰好 30 个不重复备用关键词。构建使用 `publishing_rules.py` 校验，不截断。此次未新写发布文案，实际发布当天仍需复核话题与有效官方活动。
- 两张内嵌 PNG 封面：横版 4:3 与竖版 3:4，均可离线下载。
- 本集结果与后续承接，不提前兑现下集剧情。

## 制作源文件

- [episode.json](episode.json)：原有完整剧情、23 组解说、词汇和连续性设定，剧情文本未改变。
- [storyboard.png](storyboard.png)：原有八格漫画，887 × 1774。
- [image-prompt.txt](image-prompt.txt)：原漫画提示词。
- [page.template](page.template)、[page.css](page.css)、[build.py](build.py)：页面源文件与构建。
- [voice-settings.json](voice-settings.json)：本集配音用途与逐镜语气；固定音色与确认状态仍以 `voices/book-01/cast.json` 为准。
- [animation/README.md](animation/README.md)：样片素材、时序与交接说明。
- [publishing/publishing.json](publishing/publishing.json)：既有发布文案、话题、关键词与封面资料。

## 重新生成与检查

从项目根目录运行：

```sh
python3 production/book-01/ep-001/build.py
node production/book-01/ep-001/animation/verify.mjs
node .agents/skills/taste-skill/scripts/inspect.mjs episodes/book-01/ep-001.html --out .taste-skill/ep-001-animation/inspect-continuous
```

浏览器检查包括完整播放 16 秒、帧间隔、481 个画面的相邻帧变化、file:// 离线打开、播放暂停、重播、键盘进度、剧情跳转、音效、参考音频解码、减少动态、封面下载与完整内容。结果见 [checks/continuous/verification.json](checks/continuous/verification.json)；视觉对照见 [动作联系表](checks/continuous/contact-sheet.jpg)。检查通过不等于表演质量达到完整动画片标准。

美化使用项目内 `design-taste-frontend`。1440、768、390 像素执行实浏览器检查，375 像素额外检查溢出；最终设计记录和截图在 `.taste-skill/ep-001-animation/`。无外部资源请求，无自动播放。
