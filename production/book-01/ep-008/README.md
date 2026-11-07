# 第八集制作说明

第 008 集《电脑没坏，是我们点错了地方。》交付为 [ep-008.html](../../../episodes/book-01/ep-008.html)。完整剧本、图片与学习词汇均内嵌在单个 HTML，可离线打开。

## 内容

- 8 幅漫画、8 个故事段落、30 段角色对白参考。
- 166 词英文解说，22 组逐句对应的英文与简体中文字幕，以小帅第一人称叙述。
- 5 个新词：laptop、digital、hardware、engine、search engine。每词有词义、故事例句、中文解释、用法、教材词表位置和回忆问题。
- 2 个主线旧词：function、professional。
- 10 个课后到期词回忆：第一集的 confidence、volunteer、goal、challenge、schedule，以及第六集的 aim、target、organise、voluntary、competence。题目展开后可逐个查看答案。

engine 与 search engine 分别设卡。实际解说先说 search engine，再用 This engine 指回搜索引擎；两处单独跳转，避免只出现复合短语却没有解释 engine。

## 故事与连续性

本集来到周五放学后。小帅已亲自完成原定 13:20—13:40 的搬桌和 14:00 的英语分享，再参加广播准备。分身得到家长许可并由家长接送，广播指导老师全程在场。

老师先用正常提示音确认音箱输出，上一集的连接仍正常。三人录一小段数字试音，小帅在回放时误触轨道播放静音。分身举起两页升级建议，还挡住了电脑屏幕；苏小满从波形旁的图标找到线索，小帅承认自己误点。

分身在老师指导下协助取消静音，播放同一段录音，音箱恢复出声。苏小满保存短文件，再记录检查点；音箱试听通过后，分身也用准备室已有耳机复核，小帅帮忙收好采购单。没有重录、换电脑、买设备或再修一次旧插头。

现有设备够完成眼前试录。三人随后用搜索引擎寻找“入学第一天得到的帮助”这一选题的采访问题思路，尚未完成节目。下周三放学后 16:40—16:50 的十分钟试播时段保留，月底篮球补选仍待申请。

## 解说与字幕

朗读各格“英文解说 · 中英字幕”中的英文行，同一行也作为英文字幕，紧接的中文行为对应中文字幕。按 EN001 至 EN022 与分镜交接，角色对白另置于参考区域。

本项目仅提供文本与图片，配音、剪辑、字幕时间轴和视频导出由另一个项目完成。故事里的短试音也是剧情内容，本项目不生成音频文件。

## 源文件与插画

- [episode.json](episode.json)：剧本、英文解说、中英字幕、词汇与连续性状态。
- [storyboard.png](storyboard.png)：最终八格原图，内置 imagegen 生成并修正第二格的红蓝内搭。
- [image-prompt.txt](image-prompt.txt)：完整提示词记录，含初始生成与局部修正。
- [image-prompt-v1.txt](image-prompt-v1.txt) 与 [image-edit-prompt.txt](image-edit-prompt.txt)：两次调用的精确提示词。
- [storyboard-generated-v1.png](storyboard-generated-v1.png)：修正前的生成记录。
- [page.template](page.template)：独立页面模板源码。
- [build.py](build.py)：用 Python 标准库嵌入原图和文字，输出本集 HTML。

第七集插画作人物和广播准备室参考。原版为红内搭，分身为蓝内搭，两人均不戴眼镜；苏小满戴圆眼镜，指导老师穿深蓝开衫与赭色上衣。第二格的小帅本人录音并误触，后面由分身协助恢复播放。

软件界面为无品牌示意，波形与静音图标用于说明本集情节。最终选用原图不作栅格改动，HTML 内嵌一份分镜原图供八格共用，两张发布封面另行内嵌，以带裁切区域的 SVG 窗口显示八格。正文可选择、复制，页面无在线资源、脚本或播放控件。

## 重建与检查

在项目根目录运行：

```bash
python3 production/book-01/ep-008/build.py
```

验证包含字幕与源稿逐字一致、编号、engine 与 search engine 分别跳转、图片数据、页内链接、两组旧词回忆展开，以及手机、平板和桌面排版。记录见 [verification.json](checks/verification.json)，预览图见 [checks](checks)。前七集文件校验值保存于 [previous-episodes-sha256.json](checks/previous-episodes-sha256.json)。

## 抖音发布资料

2026-11-01 补充发布区，包含基于本集剧情的标题、描述、6 个话题及 30 个不重复关键词。横版 4:3 与竖版 3:4 封面分别构图，均以 PNG 内嵌到 HTML，同时提供原生离线下载链接。

- [发布文案与封面记录](publishing/publishing.json)
- [横版 PNG](publishing/cover-4x3.png) · [竖版 PNG](publishing/cover-3x4.png)
- [横版提示词](publishing/prompt-4x3.txt) · [竖版提示词](publishing/prompt-3x4.txt)
- [发布区检查结果](checks/publishing-verification.json)

封面使用内置 image_gen.imagegen，以本集分镜为角色与剧情参考、第 001 集封面为画风参考。最终图及生成原图路径保存在 publishing 目录；有修正的封面保留初稿和相应 correction 提示词。

修改发布文案时编辑 publishing/publishing.json。发布区共用[渲染模块](../publishing.py)、[样式](../publishing.css)与[区块模板](../publishing-section.template)，运行本集原有 build.py 即可重建，仍只输出一个独立 HTML。
