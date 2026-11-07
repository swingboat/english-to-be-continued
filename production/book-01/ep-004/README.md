# 第四集制作说明

第 004 集《两张脸，只能领一张学生任务单。》交付为 [ep-004.html](../../../episodes/book-01/ep-004.html)。剧本、图片和词汇均在单个 HTML 内，可离线阅读。

## 内容

- 8 幅漫画、8 个故事段落、33 段角色对白参考。
- 214 词英文解说，24 组逐句对应的英文与简体中文字幕，以小帅第一人称叙述。
- 5 个新词：senior、secondary、previous、campus、junior。每词有词义、故事例句、中文解释、用法、教材词表位置和回忆问题。
- 2 个主线旧词：volunteer、goal。
- 5 个课后到期词回忆：stressful、challenging、arise、expectation、pressure。题目与答案置于可展开区域。

## 故事与连续性

苏小满兑现陪同约定，小帅与分身向班主任说明来历；苏小满作证后回班早读。老师联系妈妈，小帅再当面解释。母亲先接分身回家，小帅本人留校上课；当晚，他也向爸爸说明，兑现向父母亲自交代的承诺。

老师把唯一的学生任务单交给本人。上课、作业和班长试任由小帅承担；分身不能代课，只能在自己愿意、家长同意并有老师在场时，参与已经获准的课后项目。广播提案尚未获批。父母给分身安排备用房间，两人共同洗碗，体现分身也有日常需要与独立意愿。

为接续第五集，本集明确晨跑提议的来处：老师请小帅协调次日晨间活动，分身当场提出带跑，小帅本人接受协调责任，并决定先询问同学。分身只能在家协助准备计时，明早仍由小帅和老师在现场协调；具体强度与参加方式没有提前确定。第五集的未制作梗概同步了这一条件。

周五搬桌与英语分享安排保留，月底篮球补选尚未申请。第二集的活动表仍由苏小满收存，本集的学生任务单是另一份不同用途的纸，不能混成同一道具。

## 解说与字幕

各格“英文解说 · 中英字幕”中的英文是实际朗读稿，也作为英文字幕，中文行为对应中文字幕。按 EN001 至 EN024 编号与分镜交接；角色对白另收在参考区域。

本项目提供剧本与图片，配音、剪辑、字幕时间轴和视频导出在另一个项目完成。

## 源文件与插画

- [episode.json](episode.json)：剧本、英文解说、中英字幕、词汇与连续性状态。
- [storyboard.png](storyboard.png)：内置 imagegen 生成的八格原图，887 × 1774 像素。
- [image-prompt.txt](image-prompt.txt)：完整生成提示词。
- [page.template](page.template)、[page.css](page.css)、[page.js](page.js)：独立页面模板、样式及试听互斥与动效源码。
- [assets](assets)：用于内嵌的本地 Schibsted Grotesk 字体与 OFL 许可。
- [build.py](build.py)：用 Python 标准库嵌入文字与原图，输出本集 HTML。

第三集插画作学生外貌与画风参考，第二集插画作老师外貌参考。母亲首次出现，形象固定为低马尾、米色开衫与绿色上衣。父亲在家听说明，以画外对白呈现。

原图不作栅格修改，HTML 内嵌一份分镜原图供八格共用，通过精确的 CSS 背景裁切显示各分镜；两张发布封面另行内嵌。页面不依赖外网。参考音色使用原生音频控件播放；少量内联脚本用于防止多个试听同时播放和提供可关闭的进场动效，禁用脚本仍可阅读全部内容、手动试听和下载封面。

## 重建与检查

在项目根目录运行：

```bash
python3 production/book-01/ep-004/build.py
```

验证覆盖字幕与源稿逐字对应、编号、单词跳转、页内链接、图片数据、离线资源、课后答案展开及手机、平板、桌面宽度。记录见 [verification.json](checks/verification.json)，预览图见 [checks](checks)。前三集的原文件校验值保存于 [previous-episodes-sha256.json](checks/previous-episodes-sha256.json)。

## 抖音发布资料

2026-11-01 补充发布区，2026-11-04 按当前规则复核：包含基于本集剧情的标题、描述、5 个话题及 30 个不重复关键词。标题 22 字，简介连同话题合计 198 字，按共用 publishing_rules.py 校验通过。横版 4:3 与竖版 3:4 封面分别构图，均以 PNG 内嵌到 HTML，同时提供原生离线下载链接。

- [发布文案与封面记录](publishing/publishing.json)
- [横版 PNG](publishing/cover-4x3.png) · [竖版 PNG](publishing/cover-3x4.png)
- [横版提示词](publishing/prompt-4x3.txt) · [竖版提示词](publishing/prompt-3x4.txt)
- [发布区检查结果](checks/publishing-verification.json)

封面使用内置 image_gen.imagegen，以本集分镜为角色与剧情参考、第 001 集封面为画风参考。最终图及生成原图路径保存在 publishing 目录；有修正的封面保留初稿和相应 correction 提示词。

修改发布文案时编辑 publishing/publishing.json。发布区共用[渲染模块](../publishing.py)、[样式](../publishing.css)与[区块模板](../publishing-section.template)，运行本集原有 build.py 即可重建，仍只输出一个独立 HTML。

## 2026-11-04 当前规则更新

- 新增可导航的“人物与配音设定”，逐人列出性别、年龄感、性格、音色、本集用途、文件名、项目路径、采用状态及英文试听文本。
- 内嵌小帅、小帅的分身、苏小满、班主任、小帅妈妈、小帅爸爸共六位人物的原始参考 WAV。苏小满为“暂定采用”，其他五位“已选定”；同一时刻只播放一个试听，不自动播放。
- 24 条英文解说统一用小帅声音。人物引语仍由他转述，EN021 单独标为内心独白；独立角色对白、爸爸的画外音及电话沿用各人物固定音色。八格均补齐解说情绪和对白表演方向。
- 按项目 taste-skill 美化，使用编辑式任务单版面、完整插画与清楚的单词语境。所有剧本、字幕、词汇、复习内容、连续性和原始图片字节保持一致。
- 2026-11-04 搜索相关话题和官方活动，候选及核验局限见 [publishing.json](publishing/publishing.json) 和 HTML 内的核验记录；未核实的候选活动未加入正式话题。实际发布当天仍需复核。

功能校验：[current-rules-verification.json](checks/current-rules-verification.json)。发布文案校验：[publishing-current-rules.json](checks/publishing-current-rules.json)。浏览器排版与设计记录：[build-notes.md](../../../.taste-skill/ep-004/build-notes.md)。

可复跑离线功能检查：

```bash
node production/book-01/ep-004/checks/verify-offline.mjs
```

历史 checks/verification.json 和 checks/publishing-verification.json 是原交付记录；本次规则更新以 current-rules 记录为准。

最终 taste-skill 浏览器检查：1440 / 768 / 390 像素均为 0 FAIL；3 条提示及其说明见设计记录。摘要见 [current-rules-layout.json](checks/current-rules-layout.json)。
