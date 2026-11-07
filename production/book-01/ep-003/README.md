# 第三集制作说明

第 003 集《同桌认出我，靠的是一句大实话。》交付为 [ep-003.html](../../../episodes/book-01/ep-003.html)，图片和文字均在单个 HTML 内，可离线阅读与交接。

## 内容

- 8 幅漫画、8 个故事段落、31 段角色对白参考。
- 202 词英文解说，22 组逐句对应的英文与简体中文字幕，以小帅第一人称叙述。
- 5 个新词：actually、differ、in person、frank、to be frank。每词有词义、故事例句、中文解释、用法、教材词表位置和回忆问题。
- 2 个主线旧词：confidence、goal。
- 3 个课后到期词回忆：volunteer、challenge、schedule，放在可展开区域，先思考再查看答案。

## 故事与连续性

接续第二集：苏小满已经收下活动表，仍在追问两个小帅的来历。分身准备一套漂亮说辞，小帅却承认害怕当众犯错，说明手机生成分身的经过。苏小满也讲出自己的广播策划，希望被认真听完。

小帅亲口完成简短英语介绍。三人约定次日一起向班主任说明，小帅也会亲自向父母解释；本集老师和家长尚未知情，广播项目也尚未获批。两人的目标不同，分身有自己的意愿，没有新增复制机会或额外能力。

原版始终为红内搭，分身为蓝内搭。唯一的活动夹板在苏小满手中，随后放到课桌上；分身的折叠便笺是单独的口袋物件。周五活动与月底篮球补选状态承接第二集。

## 解说与字幕

按各格“英文解说 · 中英字幕”栏朗读。英文行同时用作英文字幕，紧随的中文行为对应中文字幕，以 EN001 至 EN022 编号交接。角色对白是表演参考，另置于可展开区域。

本项目提供文本与图片；配音、剪辑、字幕时间轴及成片导出由另一个项目完成。

## 源文件与插画

- [episode.json](episode.json)：故事、英文解说、中英字幕、词汇与连续性记录。
- [storyboard.png](storyboard.png)：最终选用的八格插画原图，内置 imagegen 生成并修正最后一格。
- [image-prompt.txt](image-prompt.txt)：完整提示词记录，包括初始生成与最后一格修正。
- [image-prompt-v1.txt](image-prompt-v1.txt) 与 [image-edit-prompt.txt](image-edit-prompt.txt)：两次调用的精确提示词。
- [storyboard-generated-v1.png](storyboard-generated-v1.png)：修正前的生成记录。
- [page.template](page.template)：独立页面的模板源码。
- [build.py](build.py)：用 Python 标准库将剧本和原图嵌入 HTML。

第二集插画仅作人物与画风参考。最终原图不作栅格修改，HTML 以 CSS 背景窗口分别显示八格，按原有分格坐标隔开邻格。八格共用一份内嵌分镜原图，两张发布封面另行内嵌。三位人物的参考 WAV 与 Schibsted Grotesk 字体也内嵌；无外部运行资源。原生音频控件可离线播放，小段内嵌脚本实现试听互斥和阅读动效；禁用脚本后完整内容及原生音频控件仍可使用。

## 重建与检查

在项目根目录运行：

```bash
python3 production/book-01/ep-003/build.py
```

检查记录与手机、桌面预览见 [checks](checks)。验证包括剧本与字幕逐字一致、编号、页内链接、短语词条跳转、内嵌图片、旧词回忆、离线资源和不同屏幕宽度。前两集 HTML 的校验值见 [previous-episodes-sha256.json](checks/previous-episodes-sha256.json)。

## 抖音发布资料

2026-11-01 补充发布区，包含基于本集剧情的标题、描述、6 个话题及 30 个不重复关键词。横版 4:3 与竖版 3:4 封面分别构图，均以 PNG 内嵌到 HTML，同时提供原生离线下载链接。

- [发布文案与封面记录](publishing/publishing.json)
- [横版 PNG](publishing/cover-4x3.png) · [竖版 PNG](publishing/cover-3x4.png)
- [横版提示词](publishing/prompt-4x3.txt) · [竖版提示词](publishing/prompt-3x4.txt)
- [发布区检查结果](checks/publishing-verification.json)

封面使用内置 image_gen.imagegen，以本集分镜为角色与剧情参考、第 001 集封面为画风参考。最终图及生成原图路径保存在 publishing 目录；有修正的封面保留初稿和相应 correction 提示词。

修改发布文案时编辑 publishing/publishing.json。发布区共用[渲染模块](../publishing.py)、[样式](../publishing.css)与[区块模板](../publishing-section.template)，运行本集原有 build.py 即可重建，仍只输出一个独立 HTML。

## 2026-11-02 按当前项目规则更新

- 新增清楚可见的“人物与配音设定”，仅列本集涉及的小帅、小帅的分身、苏小满。姓名、性别、年龄感、性格、音色、参考文件名和项目路径均由 `voices/book-01/cast.json` 读取。小帅与分身为“已选定”，苏小满为“暂定采用”。
- 三段原始 WAV 内嵌在 HTML 中，提供原生播放控件、不自动播放；配有对应英文试听文本，播放另一人物时暂停上一段。音频用于固定音色参考，本集成片配音由后续视频项目录制。
- 全部英文解说和引语转述使用小帅的声音。EN019 的内心独白沿用同一音色；角色对白单独列明，各镜补充情绪和语气，同一角色的画外音、电话、采访回放沿用其固定声音。
- 按项目内 taste-skill 美化，采用 Colour chapters（seed 2095948025），以苏小满的广播策划笔记为资料夹导航。沿用第二集海军蓝、橙色和本地内嵌字体；完整保留 8 幅插画、31 段对白、22 组双语字幕、5 个新词、旧词复习和发布资料。
- 可重建源码新增 [page.css](page.css)、[page.js](page.js) 和 [字体与许可](assets/Schibsted-Grotesk-OFL.txt)。没有修改其他集 HTML、人物参考语音或音色采用记录。
- 浏览器测量及视觉复核见 [设计记录](../../../.taste-skill/ep-003/build-notes.md) 与 [最终测量](../../../.taste-skill/ep-003/final/report.json)。离线功能记录见 [current-rules-verification.json](checks/current-rules-verification.json)，涵盖原始语音字节一致性、实际播放、离线 PNG 下载、逐句字幕、页内链接、禁用脚本和减少动态效果。

离线功能复核（在项目根目录执行）：

```bash
node production/book-01/ep-003/checks/verify-offline.mjs
```
