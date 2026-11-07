# 第十五集制作说明

第 015 集《我妈下班了，我的录音才刚开始。》交付为 [ep-015.html](../../../episodes/book-01/ep-015.html)。完整剧本、内嵌图片、英文解说、中英字幕和词汇学习内容收在单个离线 HTML。

## 内容

- 8 幅漫画、8 个故事段落、24 段角色对白参考。
- 164 词英文解说，22 组逐句对应的英文与简体中文字幕，小帅第一人称叙述。
- 5 个新词条：apartment、living room、am、shift、from time to time，含词义、故事例句、中文解释、用法、教材位置和回忆问题。
- 2 个主线旧词：schedule、pressure。
- 11 个课后到期词：第八集的 laptop、digital、hardware、engine、search engine，以及第十三集的 teen、native、saying、ahead、get ahead、revise。
- 1 张时间调整表：周六先休息，另处整理提纲，周日上午十点的采访开始前再确认。

本集 am 明确表示上午的时间标记，也可写 a.m.，区别于 I am 中的动词。高亮只匹配时刻后面的 am，避免把动词误链到时间词卡。living room、from time to time 等完整短语分别设卡，页内锚点统一小写。

## 情节与连续性

第十四集第一期校园广播已完成，老师邀请准备家人生活选题。试播后的周四，小帅问过妈妈，她愿意以后分享，但说好本周六夜班后先休息，醒来再确认采访。

周六八点，三人经家长知情到小帅家准备提纲、试录小帅自己的开场，爸爸在家、画外知情。小帅把“八点开始准备”误写成“八点采访”，只记住妈妈到家的钟点。妈妈刚下夜班回来，分身又照纸表推进，苏小满提醒先看对方现在的状态。

小帅停下自己刚开始的试音，正式妈妈采访尚未开始。他问早餐最想要什么，妈妈带笑答“安静”，连分身也把笔放下。桌上已备简单早餐和水杯，但此刻更需要让客厅安静下来。

妈妈有时轮到夜班，三人的表却只填了自己准备什么，漏掉她上一班的工作时间。简短确认后，妈妈表示今晚不上夜班，改约周日 10:00—10:10，在家中客厅分享，开始前再确认一次是否方便。今天先收起手机与纸笔，苏小满 08:10 告辞，妈妈在沙发上先闭目休息。

小帅给别人的时间留了空格，仍担心自己的承诺，承接第十六集。第二期选题和播出安排尚未确定；第一期保持已完成状态。学校电脑、麦克风和调音台仍在学校，家中只有小帅原有的一部黑手机。

妈妈保持低马尾、米色开衫配绿色上衣，未新增具体职业。苏小满主编、小帅统筹、分身协助声音的分工保留；父母和老师知道分身来历。周五搬桌、英语分享已完成，月底篮球补选仍待申请。

## 解说与字幕

朗读各格“英文解说 · 中英字幕”中的英文行，同一行作为英文字幕，紧接的中文行为对应中文字幕。编号 EN001 至 EN022，角色对白另收在展开参考区。

本项目只交付文本与图片。试音是剧情中的小帅开场测试，配音、剪辑、字幕时间轴与视频导出在另一个项目完成，这里不生成音频或视频。

## 源文件与插画

- [episode.json](episode.json)：剧本、解说、字幕、词汇与连续性。
- [storyboard.png](storyboard.png)：内置 imagegen 生成的八格原图。
- [image-prompt.txt](image-prompt.txt)：精确生成提示词。
- [page.template](page.template)、[build.py](build.py)：独立页面模板和 Python 标准库构建脚本。

第九集提供妈妈、三位学生及家中环境参考，本集改为清晨归家与安排时间的场景。原始生成结果：`/Users/huyin/.codex/generated_images/01a1911b-0335-73d1-9e32-69cfd0344a98/exec-84fbc6e4-fde7-4159-8799-cbb30d138453.png`。保留原文件，选图另存本集目录，不做栅格编辑。

妈妈低马尾、无眼镜；小帅红 T 恤短黑发，分身蓝内搭校服短黑发，苏小满短发圆眼镜。每格至多一部手机，第三格停下，七格收起；没有电脑、外接麦克风或学校设备。时间与具体约定由 HTML 提供，图片只用纸表、月亮、太阳等符号。

单份 PNG 内嵌 HTML，以八个带裁切区的 SVG 窗口显示，离线阅读无网络依赖。

## 重建与检查

在项目根目录运行：

```bash
python3 production/book-01/ep-015/build.py
```

检查字幕与源稿一致、编号、时间标记 am 与动词 am 的区分、词与短语跳转、旧词展开、图片内嵌及手机、平板、桌面排版。记录见 [verification.json](checks/verification.json)，截图见 [checks](checks)。前十四集校验值见 [previous-episodes-sha256.json](checks/previous-episodes-sha256.json)。

## 抖音发布资料

2026-11-01 补充发布区，包含基于本集剧情的标题、描述、6 个话题及 30 个不重复关键词。横版 4:3 与竖版 3:4 封面分别构图，均以 PNG 内嵌到 HTML，同时提供原生离线下载链接。

- [发布文案与封面记录](publishing/publishing.json)
- [横版 PNG](publishing/cover-4x3.png) · [竖版 PNG](publishing/cover-3x4.png)
- [横版提示词](publishing/prompt-4x3.txt) · [竖版提示词](publishing/prompt-3x4.txt)
- [发布区检查结果](checks/publishing-verification.json)

封面使用内置 image_gen.imagegen，以本集分镜为角色与剧情参考、第 001 集封面为画风参考。最终图及生成原图路径保存在 publishing 目录；有修正的封面保留初稿和相应 correction 提示词。

修改发布文案时编辑 publishing/publishing.json。发布区共用[渲染模块](../publishing.py)、[样式](../publishing.css)与[区块模板](../publishing-section.template)，运行本集原有 build.py 即可重建，仍只输出一个独立 HTML。
