# 第二集制作说明

第 002 集为《三个我才够用？先删掉一个承诺。》，交付文件是 [ep-002.html](../../../episodes/book-01/ep-002.html)，可单文件离线阅读。

## 内容

- 8 幅新漫画图片、8 个故事段落、33 段双语或中文对白。
- 35 条逐句英文解说及对应的 35 组中英字幕；以小帅第一人称讲故事。
- 5 个新词：stressful、challenging、arise、expectation、pressure。每个词含词义、故事例句、中文解释、用法提示和教材位置。
- 2 个旧词复现：schedule、challenge，均进入本集对白。
- 三张文字表格：原来的撞期邀请、体育组补选公告、小帅亲自确认后的安排。
- 本集结果、道具状态和第 003 集的承接。
- 清楚可见的“人物与配音设定”区：小帅、小帅的分身、苏小满、班主任，列明性别、年龄感、性格、音色、参考音频与文本的文件名及项目内路径、采用状态。
- 每镜解说语气、内心独白标记与角色对白语气；班主任画外音与办公室内对白沿用同一音色。

小帅亲自进办公室处理冲突，搬桌调整至周五 13:20—13:40，英语分享保留在 14:00，并决定暂不报名同一时间的篮球初选。月底开放补选为已有公告提供的机会，本集只决定后续另行申请。

苏小满已看见两个人，但尚未听到生成经过；班主任没有见到分身，完整自我介绍留到第 003 集。

成片采用小帅（Xiaoshuai）的第一人称英文解说，朗读各分镜“英文解说”栏，英文行同时作为英文字幕，中文行作为对应中文字幕。解说中的人物引语均由小帅转述；内心独白转述沿用小帅音色，语气放轻。编号与类型标签不朗读。角色对白收在参考区域，若单独录制则使用对应人物固定声音，配音、剪辑及字幕时间轴由视频项目完成。

音色信息在重建时直接读取 `voices/book-01/cast.json`。苏小满为“暂定采用”；小帅、分身与班主任按用户本次说明采用现有音色，标为“已选定”。参考 WAV 和对应 TXT 保存在人物目录，HTML 列明文件位置，并内嵌该 WAV 以便单文件离线试听，保留对应试听文本。

## 源文件与图片

- [episode.json](episode.json)：剧本、词汇、三张表和连续性记录。
- [storyboard.png](storyboard.png)：内置 imagegen 生成的本集八格原图，887 × 1774 像素。
- [image-prompt.txt](image-prompt.txt)：完整生成提示词。
- [page.template](page.template)：本集独立阅读页面模板。
- [build.py](build.py)：用 Python 标准库嵌入内容并输出本集 HTML。

图片以第一集分镜为角色与画风参考，本集另行生成。原图不作改动，显示范围记录在 art.panels 中，并为每格设置 CSS 背景裁切窗口，防止露出相邻画面。正式 HTML 的共享背景规则内嵌一份分镜原图供八格共用，两张发布封面另行内嵌，四段参考语音和字体也内嵌，所有必要内容都在单个文件中。

当前人物命名为小帅（Xiaoshuai）与分身。原始图片提示词保留生成时的英文角色代号用于溯源，后续创作遵循项目的当前命名规则。

## 重建与检查

在项目根目录运行：

```bash
python3 production/book-01/ep-002/build.py
```

本集采用 taste-skill 的纸张阅读设计，人物区提供四个原生语音播放器，默认不自动播放；切换人物时暂停其他播放器。检查涵盖八幅图片、全部对白、五个新词、旧词复现、单词复数 expectations 的跳转、表格、页内链接、离线资源，以及手机、平板和桌面宽度。

本次按 2026-11-02 项目规则修订的检查记录见 [current-rules-verification.json](checks/current-rules-verification.json)。[verification.json](checks/verification.json) 和 [publishing-verification.json](checks/publishing-verification.json) 保留此前制作与发布区补齐时的检查记录；其中旧字幕数量及旧 HTML 哈希不代表当前文件。

## 抖音发布资料

2026-11-01 补充发布区，包含基于本集剧情的标题、描述、6 个话题及 30 个不重复关键词。横版 4:3 与竖版 3:4 封面分别构图，均以 PNG 内嵌到 HTML，同时提供原生离线下载链接。

- [发布文案与封面记录](publishing/publishing.json)
- [横版 PNG](publishing/cover-4x3.png) · [竖版 PNG](publishing/cover-3x4.png)
- [横版提示词](publishing/prompt-4x3.txt) · [竖版提示词](publishing/prompt-3x4.txt)
- [发布区检查结果](checks/publishing-verification.json)

封面使用内置 image_gen.imagegen，以本集分镜为角色与剧情参考、第 001 集封面为画风参考。最终图及生成原图路径保存在 publishing 目录；有修正的封面保留初稿和相应 correction 提示词。

修改发布文案时编辑 publishing/publishing.json。发布区共用[渲染模块](../publishing.py)、[样式](../publishing.css)与[区块模板](../publishing-section.template)，运行本集原有 build.py 即可重建，仍只输出一个独立 HTML。

## 2026-11-02 规则对齐

本次同步更新剧本数据、模板、构建脚本与最终 HTML。字幕由原 22 个多句条目整理为 35 个逐句条目；剧情、五个新词和两项旧词复现保持对应。角色对白中的“老师”统一标为“班主任”，声音明确映射到同名人物目录。发布描述使用“英语分享确认由自己参加”，避免将本集决定写成后续活动已经发生；关键词以“活动确认表”替换不属于本集的“班长试任”，总数仍为 30 个。

## 人物语音播放与 taste-skill 美化

按用户本次说明补齐现有音色的采用记录，苏小满继续保留“暂定采用”；已保存该次说明的来源，不将其追记为之前逐人试听的历史。音频字节保持现有参考原样。

本集人物区提供小帅、分身、苏小满、班主任的四段 WAV 播放器，支持断网后播放和跳转，且一次只播放一个人物。展开“试听文本与参考文件”可读取对应原文与路径。这些音频是人物固定音色样本，完整本集配音仍由后续视频项目制作。

`taste-skill` 仅安装于当前项目的 `.agents/skills/taste-skill/`。设计方向为 The page is the object（seed 2094817229），配色 Navy on white，Schibsted Grotesk 的三个字重以 TTF 嵌入，中文使用系统字形。采用完整内容所需的两个区块重抽：分镜使用图片与正文并列，发布资料使用普通列排版。设计记录、前后截图与检查报告保存在项目 `.taste-skill/`。

页面样式在 [page.css](page.css)，播放互斥和渐入动效在 [page.js](page.js)，仍运行原 [build.py](build.py) 输出唯一交付 HTML。新检查记录见 [audio-taste-verification.json](checks/audio-taste-verification.json)；先前检查记录保留作为历史。
