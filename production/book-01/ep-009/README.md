# 第九集制作说明

第 009 集《搜了三小时，收获二十个聊天群。》交付为 [ep-009.html](../../../episodes/book-01/ep-009.html)。完整剧本、图片与学习词汇均内嵌在单个 HTML，可离线打开。

## 内容

- 8 幅漫画、8 个故事段落、31 段角色对白参考。
- 183 词英文解说，22 组逐句对应的英文与简体中文字幕，以小帅第一人称叙述。
- 5 个新词：chat、surf、surf the Internet、media、social media。每词有词义、故事例句、中文解释、用法、教材词表位置和回忆问题。
- 2 个主线旧词：search engine、digital。
- 10 个课后到期词回忆：第二集的 stressful、challenging、arise、expectation、pressure，以及第七集的 responsible、be responsible for、function、seek、professional。
- 1 张线索表：本人经历、受访意愿、待到校核对的手册地图。

surf 与 surf the Internet、media 与 social media 分别在解说中独立使用并设词卡。页内锚点统一小写，学习条目显示仍保留 Internet 的首字母大写。

## 故事与连续性

时间来到周六上午九点至中午，地点在小帅家。学校登记同意周末借用电脑、周一归还，苏小满与家长说好后来合作，妈妈在家。分身没有周末擅自进校，学校麦克风、音箱和耳机也没有搬回家。

三人从查采访思路转到看猫视频、回复争论和收藏群入口。妈妈端来午饭时，分身已有二十个群聊邀请入口，采访页却仍几乎空白。二十个指收藏的入口，不表示实际加入或采访了二十个群，三人都承认分心。

小帅重新要求每人留下有明确来源的一条线索。本人首日经历可直接分享，高马尾同学在短电话中同意受访，手册里的图书馆地图留待周一实地核对；具体采访时间也要周一再约。故事保留了已确认信息与待核对线索的区别。

收尾时小帅自愿用电脑内置麦克风留半分钟个人口述草稿，与第八集短试音一起保存到广播准备工程。正式同学采访尚未进行，十分钟节目还没完成。手机新通知亮起，下一集清理干扰时误选的工程因此有了明确内容。

苏小满主编、小帅本人统筹、分身协助声音的分工保留，下周三放学后 16:40—16:50 的试播时段不变；周五原有搬桌与英语分享已在第八集记录为完成，月底篮球补选仍待申请。

## 解说与字幕

朗读各格“英文解说 · 中英字幕”中的英文行，同一行也作为英文字幕，紧接的中文行为对应中文字幕。按 EN001 至 EN022 与分镜交接，角色对白另收在参考区域。

本项目提供文本与图片，配音、剪辑、字幕时间轴和视频导出由另一个项目完成。口述录音是剧情中的准备成果，本项目不生成音频文件。

## 源文件与插画

- [episode.json](episode.json)：剧本、英文解说、中英字幕、词汇与连续性状态。
- [storyboard.png](storyboard.png)：最终八格原图，内置 imagegen 生成，并统一第四格的笔记本电脑与分身配色。
- [image-prompt.txt](image-prompt.txt)：完整提示词记录，含初始生成与局部修正。
- [image-prompt-v1.txt](image-prompt-v1.txt) 与 [image-edit-prompt.txt](image-edit-prompt.txt)：两次调用的精确提示词。
- [storyboard-generated-v1.png](storyboard-generated-v1.png)：修正前的生成记录。
- [page.template](page.template)：独立页面模板源码。
- [build.py](build.py)：用 Python 标准库嵌入原图和文字，输出本集 HTML。

第八集插画作三位学生参考，第四集家中分镜作妈妈参考。家中小帅可脱下外套，保持红色 T 恤；分身蓝内搭，苏小满戴圆眼镜。妈妈为低马尾、米色开衫配绿色上衣。

全程只有一台借用笔记本电脑与原版的一部黑色手机。第六格手机经同意借给苏小满打电话，随后归还。校园手册地图是虚构校园的道具，没有真实学校网址、群聊链接或账号数据。

最终选用原图不作栅格改动，HTML 内嵌一份分镜原图供八格共用，两张发布封面另行内嵌，以带裁切区域的 SVG 窗口显示八格。正文可选择、复制，页面无网络依赖、脚本或播放控件。

## 重建与检查

在项目根目录运行：

```bash
python3 production/book-01/ep-009/build.py
```

验证包含字幕与源稿逐字一致、编号、词与短语分别跳转、线索表、图片数据、页内链接、两组旧词回忆展开，以及手机、平板和桌面排版。记录见 [verification.json](checks/verification.json)，预览图见 [checks](checks)。前八集文件校验值保存于 [previous-episodes-sha256.json](checks/previous-episodes-sha256.json)。

## 抖音发布资料

2026-11-01 补充发布区，包含基于本集剧情的标题、描述、6 个话题及 30 个不重复关键词。横版 4:3 与竖版 3:4 封面分别构图，均以 PNG 内嵌到 HTML，同时提供原生离线下载链接。

- [发布文案与封面记录](publishing/publishing.json)
- [横版 PNG](publishing/cover-4x3.png) · [竖版 PNG](publishing/cover-3x4.png)
- [横版提示词](publishing/prompt-4x3.txt) · [竖版提示词](publishing/prompt-3x4.txt)
- [发布区检查结果](checks/publishing-verification.json)

封面使用内置 image_gen.imagegen，以本集分镜为角色与剧情参考、第 001 集封面为画风参考。最终图及生成原图路径保存在 publishing 目录；有修正的封面保留初稿和相应 correction 提示词。

修改发布文案时编辑 publishing/publishing.json。发布区共用[渲染模块](../publishing.py)、[样式](../publishing.css)与[区块模板](../publishing-section.template)，运行本集原有 build.py 即可重建，仍只输出一个独立 HTML。
