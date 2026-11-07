# 第七集制作说明

第 007 集《负责人的名字，不能写两个小帅。》交付为 [ep-007.html](../../../episodes/book-01/ep-007.html)。完整剧本、图片与学习词汇均内嵌在单个 HTML，可离线打开。

## 内容

- 8 幅漫画、8 个故事段落、34 段角色对白参考。
- 194 词英文解说，22 组逐句对应的英文与简体中文字幕，以小帅第一人称叙述。
- 5 个新词：responsible、be responsible for、function、seek、professional。每词有词义、故事例句、中文解释、用法、教材词表位置和回忆问题。
- 2 个主线旧词：organise、voluntary。
- 5 个课后到期词回忆：dynamic、lifestyle、drag、tend to do sth、leisure，先回忆再展开答案。
- 1 张结果表：正式分工、十分钟试播时段与待准备内容。

## 故事与连续性

承接第六集的条件许可，三人于次日放学后先提交分工草稿，在老师监督下试机。草稿写了两个“小帅”，口头先明确本人统筹、苏小满主编、分身协助声音检查，最终表格需补清身份、职责与签名。

室内试听没有声音。分身问按钮功能，三人先读说明；小帅留下说明问题并寻求帮助。班主任联系广播指导老师，后者发现小音箱的低压音频线没接牢，指导接妥后试听通过。没有拆机或自动获得技术能力。

三人正式确认分工，各自为自己的工作签名。广播协助同学与指导老师均知道分身来历。指导老师确认下周三放学后 16:40—16:50 的十分钟试播时段；稿件、采访素材与电脑试录仍需准备，本集没有正式播出。

分身由家长许可并接送，只参与有老师在场的课后项目。新增的女性广播指导老师与原男性班主任明确区分，前者为短卷棕发、无眼镜、深蓝开衫与赭色上衣。

本集的音箱连接问题已解决。下一集转入电脑试录，软件静音是另一问题，未制作梗概已同步区别。周五搬桌与英语分享仍需小帅本人履行，月底篮球补选仍待申请。

## 解说与字幕

朗读各格“英文解说 · 中英字幕”中的英文行，同一行也作为英文字幕，紧接的中文行为对应中文字幕。按 EN001 至 EN022 与分镜交接；角色对白另置于参考区域。

本项目提供文本与图片，配音、剪辑、字幕时间轴和视频导出由另一个项目完成。

## 源文件与插画

- [episode.json](episode.json)：剧本、英文解说、中英字幕、词汇与连续性状态。
- [storyboard.png](storyboard.png)：最终八格原图，内置 imagegen 生成并修正第二格误加的眼镜。
- [image-prompt.txt](image-prompt.txt)：完整提示词记录，含初始生成与局部修正。
- [image-prompt-v1.txt](image-prompt-v1.txt) 与 [image-edit-prompt.txt](image-edit-prompt.txt)：两次调用的精确提示词。
- [storyboard-generated-v1.png](storyboard-generated-v1.png)：修正前的生成记录。
- [page.template](page.template)：独立页面模板源码。
- [build.py](build.py)：用 Python 标准库嵌入原图和文字，输出本集 HTML。

第六集插画作主角、分身和班主任参考，第五集插画作高马尾协助同学参考。小帅与分身均不戴眼镜，苏小满戴圆眼镜，班主任戴方框眼镜。最终选用原图不作栅格改动，HTML 内嵌一份分镜原图供八格共用，两张发布封面另行内嵌，以带裁切区域的 SVG 窗口显示八格。正文文字可选择、复制，无网络资源、脚本或播放控件。

## 重建与检查

在项目根目录运行：

```bash
python3 production/book-01/ep-007/build.py
```

验证包含字幕与源稿逐字一致、编号、单词和短语跳转、结果表、图片数据、页内链接、回忆答案展开，以及手机、平板和桌面排版。记录见 [verification.json](checks/verification.json)，预览图见 [checks](checks)。前六集文件校验值保存于 [previous-episodes-sha256.json](checks/previous-episodes-sha256.json)。

## 抖音发布资料

2026-11-01 补充发布区，包含基于本集剧情的标题、描述、6 个话题及 30 个不重复关键词。横版 4:3 与竖版 3:4 封面分别构图，均以 PNG 内嵌到 HTML，同时提供原生离线下载链接。

- [发布文案与封面记录](publishing/publishing.json)
- [横版 PNG](publishing/cover-4x3.png) · [竖版 PNG](publishing/cover-3x4.png)
- [横版提示词](publishing/prompt-4x3.txt) · [竖版提示词](publishing/prompt-3x4.txt)
- [发布区检查结果](checks/publishing-verification.json)

封面使用内置 image_gen.imagegen，以本集分镜为角色与剧情参考、第 001 集封面为画风参考。最终图及生成原图路径保存在 publishing 目录；有修正的封面保留初稿和相应 correction 提示词。

修改发布文案时编辑 publishing/publishing.json。发布区共用[渲染模块](../publishing.py)、[样式](../publishing.css)与[区块模板](../publishing-section.template)，运行本集原有 build.py 即可重建，仍只输出一个独立 HTML。
