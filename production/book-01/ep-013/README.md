# 第十三集制作说明

第 013 集《背熟了台词，忘了听别人说什么。》交付为 [ep-013.html](../../../episodes/book-01/ep-013.html)。完整剧本、内嵌图片与学习词汇收在单个离线 HTML。

## 内容

- 8 幅漫画、8 个故事段落、25 段角色对白参考。
- 162 词英文解说，22 组逐句对应的英文与简体中文字幕，小帅第一人称叙述。
- 6 个新词条：teen、native、saying、ahead、get ahead、revise，含词义、故事例句、中文解释、用法、教材位置和回忆问题。
- 2 个主线旧词：confidence、chat。
- 11 个课后到期词回忆：第六集的 aim、target、organise、voluntary、competence，以及第十一集的 range、various、sort、all sorts of、quality、necessity。
- 1 张主持稿调整表：从真实回答追问，确认事实与感受，再修改结语。

ahead 与 get ahead 分别进入解说并设词卡，完整短语优先匹配。teen 与 revise 的常见变形指向原词卡。六张新词卡按两列成对排版。

## 情节与连续性

周二 16:35，三人和高马尾受访同学来到老师批准的图书馆旁安静桌位。第十一集测试通过的同一台学校电脑和一支 USB 手持麦克风按登记领用，家长知情。16:40 开始、16:50 前结束采访与确认；使用后交回老师。

三问沿用第十二集核对版 A：在哪里迷路、谁帮了你、当时感觉怎样。此前只核对问题，没有要求同学照台词回答。小帅在准备时把自己想象的接话写成长稿，期待英语说得自然，还备了句“Practice makes perfect.”。

真实回答中，同学承认不敢问路，另一个新生也迷路。小帅没听完，差点接上励志格言；对方一句“Practice getting lost?”让他卡住。苏小满征得大家同意暂停，提醒他回到刚听见的“不敢问路”。小帅自己折起逐字稿，保留三问，分身等待，没有代答。

恢复后，小帅用“What did you do next?”接住回答。受访同学补全事实：两位迷路新生一起向高年级同学问路，后者带她们找到图书馆。这样延续了第九集已说明的走错楼、被同学带路经历。小帅再问感受，听见“一起问就没那么孤单了”，复述确认。

结尾回听关键片段，同学确认可用于周三试播，并愿意保留原本的紧张。正式采访独立保存，旧试音、小帅半分钟个人草稿与准备工程保留。主持结语根据实际回答修改，节目仍未完成或播出。周三 16:40—16:50 试播时段不变，提示卡留待整理，承接第十四集。

本集把原计划“对方临时改答”具体化为“真实回答与小帅预设接话不同”，保留采访的合理性。能力提升来自小帅亲自练习、倾听和追问；分身保持声音协助的分工。周五搬桌、英语分享已完成，月底篮球补选仍待申请。

## 解说与字幕

朗读各格“英文解说 · 中英字幕”的英文行，同一行作为英文字幕，紧接的中文行为对应中文字幕，编号 EN001 至 EN022。角色对白收在可展开参考区。

本项目只提供文本与图片；配音、剪辑、字幕时间轴和视频导出在另一个项目完成。正式录音与回放是故事情节，这里不生成音频文件。

## 源文件与插画

- [episode.json](episode.json)：完整剧本、解说、字幕、词汇与连续性状态。
- [storyboard.png](storyboard.png)：内置 imagegen 生成的最终八格原图。
- [image-prompt.txt](image-prompt.txt)：全部精确调用提示词。
- [image-prompt-v1.txt](image-prompt-v1.txt)、[image-edit-prompt.txt](image-edit-prompt.txt)：初始生成和去除重复麦克风的局部修正提示词。
- [storyboard-generated-v1.png](storyboard-generated-v1.png)：修正前原图，保留过程记录。
- [page.template](page.template)、[build.py](build.py)：独立模板和 Python 标准库构建脚本。

第十一集提供三位主角、图书馆场景和借用设备参考；第七集第一格的高马尾学生提供受访同学外观参考。最终画面保持四位学生：两位短黑发男生以红蓝内搭区分，苏小满短发圆眼镜，受访者棕色高马尾、无眼镜。回忆中的两位帮助者不在采访现场另行入镜。

全程一台银色电脑、一支黑色有线手持麦克风。麦克风在说话者手里时，盒子不再另放一支。小帅在后半段可脱外套，仍保持红 T 恤；设备未带回家。图片内的稿纸与界面使用图标和空行，字幕由 HTML 文字提供。

原始生成结果保留在 `/Users/huyin/.codex/generated_images/01a1911b-0335-73d1-9e32-69cfd0344a98/`，最终选图另存本集目录。不做栅格编辑，单份 PNG 内嵌后通过八个带裁切区的 SVG 窗口显示分镜。

## 重建与检查

在项目根目录运行：

```bash
python3 production/book-01/ep-013/build.py
```

检查字幕与源稿一致、编号、单词和短语跳转、复习卡展开、图片内嵌及手机、平板、桌面排版。记录见 [verification.json](checks/verification.json)，截图见 [checks](checks)。前十二集校验值见 [previous-episodes-sha256.json](checks/previous-episodes-sha256.json)。

## 抖音发布资料

2026-11-01 补充发布区，包含基于本集剧情的标题、描述、6 个话题及 30 个不重复关键词。横版 4:3 与竖版 3:4 封面分别构图，均以 PNG 内嵌到 HTML，同时提供原生离线下载链接。

- [发布文案与封面记录](publishing/publishing.json)
- [横版 PNG](publishing/cover-4x3.png) · [竖版 PNG](publishing/cover-3x4.png)
- [横版提示词](publishing/prompt-4x3.txt) · [竖版提示词](publishing/prompt-3x4.txt)
- [发布区检查结果](checks/publishing-verification.json)

封面使用内置 image_gen.imagegen，以本集分镜为角色与剧情参考、第 001 集封面为画风参考。最终图及生成原图路径保存在 publishing 目录；有修正的封面保留初稿和相应 correction 提示词。

修改发布文案时编辑 publishing/publishing.json。发布区共用[渲染模块](../publishing.py)、[样式](../publishing.css)与[区块模板](../publishing-section.template)，运行本集原有 build.py 即可重建，仍只输出一个独立 HTML。
