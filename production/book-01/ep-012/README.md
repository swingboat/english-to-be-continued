# 第十二集制作说明

第 012 集《我都说到第三句了，你还在第一句。》交付为 [ep-012.html](../../../episodes/book-01/ep-012.html)。完整剧本、内嵌图片与词汇学习内容收在单个离线 HTML。

## 内容

- 8 幅漫画、8 个故事段落、25 段角色对白参考。
- 166 词英文解说，22 组逐句对应的英文与简体中文字幕，小帅第一人称叙述。
- 5 个新词条：convenient、according to、update、meanwhile、distance，含词义、故事例句、中文解释、用法、教材位置和回忆问题。
- 2 个主线旧词：organise、schedule。
- 10 个课后到期词回忆：第五集的 dynamic、lifestyle、drag、tend to do sth、leisure，以及第十集的 addict、reduce、remove、entirely、stressed。
- 1 张“核对版 A”交接表：确认版本、逐条核对、没听清时确认、通话后再商议修改。

according to 作为完整短语设卡，update 的常见变形指向同一张词卡。页内锚点统一小写，以连字符连接词组。

## 情节与连续性

承接周一校内收音试录通过和设备归还。傍晚 17:15—17:25，三位学生经家长知情在小帅家，用他原有的一部黑色手机免提核对问题，妈妈在家。苏小满按约 17:30 回家；受访的高马尾同学在自己家，仅以电话声音出现。学校电脑、麦克风仍由老师保管，没有搬回家。

通话前已发送原三问照片：在哪里迷路、谁帮了你、当时感觉怎样。通话偶有延迟，小帅又没有逐条等确认，分身原本想补清晰照片，却顺手调整提问顺序并连发新版。小帅说原稿第三条时，对方仍在核对新图第一条，两人还同时说“你先说”。错位来自语音交接与版本变化叠加。

分身承认忘了上集“先别边聊边改”的约定。小帅协调、苏小满主编确认，恢复三问原顺序并标为“核对版 A”。最终照片发送后，请远端复述图中顺序，确认双方看同一版；旧照片仍在记录中，明确停止使用，修改想法留到通话后商议。

三人采用叫名字、一次核对一问、说完明确交接、等对方讲完再接的办法。延迟仍可能出现，核对因此能有序进行。只确认提问顺序与可讲范围，完整经历仍留到周二 16:40—16:50 正式采访；周三同一时段十分钟试播安排不变，节目尚未完成。

通话按时结束后，小帅开始练开场句，为第十三集面对真实回答时卡住的情节作准备。周五搬桌与英语分享已完成，月底篮球补选仍待申请。

## 解说与字幕

朗读各格“英文解说 · 中英字幕”中的英文行，同一行作为英文字幕，紧接的中文行为对应中文字幕。按 EN001 至 EN022 与分镜交接，角色对白另收在展开参考区。配音、剪辑、字幕时间轴及视频导出在另一个项目完成；这里不生成音频或视频。

## 源文件与插画

- [episode.json](episode.json)：剧本、解说、字幕、词汇与连续性状态。
- [storyboard.png](storyboard.png)：内置 imagegen 生成的八格原图，以第十集为人物和家中环境参考，改成手机通话与纸提纲场景。
- [image-prompt.txt](image-prompt.txt)：本次精确生成提示词。
- [page.template](page.template)、[build.py](build.py)：独立模板与 Python 标准库构建脚本。

原始生成结果：`/Users/huyin/.codex/generated_images/01a1911b-0335-73d1-9e32-69cfd0344a98/exec-190d938a-e666-4beb-a4a4-b8aee1d5a03c.png`。保留原始文件，选图另存本集目录，不做栅格编辑。

三位学生均保持既定外观：小帅短黑发红 T 恤、分身同脸短黑发蓝内搭校服、苏小满短发圆眼镜。全程只有一部黑手机，没有电脑、麦克风或耳机。远端同学不画成第四位到场人物；纸上人物图标只表示提问内容。图片界面只画图标，实际问题与版本名称由 HTML 文字提供。

单份 PNG 内嵌在 HTML 中，以八个带裁切区的 SVG 窗口显示分镜，离线阅读无网络依赖。

## 重建与检查

在项目根目录运行：

```bash
python3 production/book-01/ep-012/build.py
```

检查字幕与源稿一致、编号连续、词与短语跳转、图片数据、复习卡展开，以及手机、平板、桌面排版。记录见 [verification.json](checks/verification.json)，截图见 [checks](checks)。前十一集校验值见 [previous-episodes-sha256.json](checks/previous-episodes-sha256.json)。

## 抖音发布资料

2026-11-01 补充发布区，包含基于本集剧情的标题、描述、6 个话题及 30 个不重复关键词。横版 4:3 与竖版 3:4 封面分别构图，均以 PNG 内嵌到 HTML，同时提供原生离线下载链接。

- [发布文案与封面记录](publishing/publishing.json)
- [横版 PNG](publishing/cover-4x3.png) · [竖版 PNG](publishing/cover-3x4.png)
- [横版提示词](publishing/prompt-4x3.txt) · [竖版提示词](publishing/prompt-3x4.txt)
- [发布区检查结果](checks/publishing-verification.json)

封面使用内置 image_gen.imagegen，以本集分镜为角色与剧情参考、第 001 集封面为画风参考。最终图及生成原图路径保存在 publishing 目录；有修正的封面保留初稿和相应 correction 提示词。

修改发布文案时编辑 publishing/publishing.json。发布区共用[渲染模块](../publishing.py)、[样式](../publishing.css)与[区块模板](../publishing-section.template)，运行本集原有 build.py 即可重建，仍只输出一个独立 HTML。
