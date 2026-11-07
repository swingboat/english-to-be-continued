# 第五集制作说明

第 005 集《他替我答应的晨跑，我来喊暂停。》交付为 [ep-005.html](../../../episodes/book-01/ep-005.html)。完整剧本、图片与学习词汇均内嵌在单个 HTML，可离线打开。

## 内容

- 8 幅漫画、8 个故事段落、30 段角色对白参考。
- 181 词英文解说，25 组逐句对应的英文与简体中文字幕，以小帅第一人称叙述。原稿中的三条多句字幕已按句拆开，英文内容完整保留。
- 6 位人物的完整配音设定、内嵌 WAV 参考语音与对应英文试听文本；苏小满标为“暂定采用”，其余五位均为“已选定”。
- 5 个新词：dynamic、lifestyle、drag、tend to do sth、leisure。每词有词义、故事例句、中文解释、用法、教材词表位置和回忆问题。
- 2 个主线旧词：schedule、volunteer。
- 5 个课后到期词回忆：actually、differ、in person、frank、to be frank，先回忆再展开答案。

学习条目 tend to do sth 在实际解说里用作 tend to say yes；词卡解释动作替换和 to 后接动词原形的用法。英文稿朗读完整自然的句子，不能把学习占位写法当作对白。

## 故事与连续性

承接第四集的晨间活动任务：分身在家准备秒表和便笺，小帅本人带到学校。小帅先问同学，四人在老师看护下同意试跑半圈。实际体验不同，刚坐下，十秒休息倒计时就响了。小帅主动停表，重新问清意愿和节奏；老师同意后，小组选择慢跑、步行或拉伸。

分身仅在第一格的家中出现，全程没有进校参加晨间活动；学校画面中的寸头男生和高马尾女生是普通同学。小帅自己承担协调与调整责任，没有把方案不合适全推给分身。

晨间活动正常结束，学生按时回班。课间，苏小满约小帅午休留十分钟听完广播提案；广播尚未获准试播，学校晨间活动与上课时间没有被替换。第六集继续争取一次可行的试播。

周五搬桌与英语分享的既定安排保留，月底篮球补选仍待申请。

## 解说与字幕

朗读各格“英文解说 · 中英字幕”中的英文行，同一行也用作英文字幕，紧接的中文行为对应中文字幕。按 EN001 至 EN025 与分镜交接；编号和类型标签不朗读。全部解说采用小帅的固定音色，人物引语由小帅转述；EN017 是他的自省心声。角色对白另置于参考区域，每格单列解说与人物表演语气。

本集人物为小帅、小帅的分身、苏小满、寸头同学、高马尾同学、班主任。画外音沿用本人音色，秒表“嘀”声归为音效。试听用于后续视频项目辨认和参考音色，不是本集成片配音；原生播放器不自动播放，同时只播放一段声音。

本项目提供文本与图片；配音、剪辑、字幕时间轴和视频导出由另一个项目完成。

## 源文件与插画

- [episode.json](episode.json)：剧本、英文解说、中英字幕、词汇和连续性状态。
- [storyboard.png](storyboard.png)：内置 imagegen 生成的八格原图，887 × 1774 像素。
- [image-prompt.txt](image-prompt.txt)：完整生成提示词。
- [page.template](page.template)：独立页面模板源码。
- [page.css](page.css)、[page.js](page.js)：页面样式、章节图片预览与音色互斥播放；字体与许可在 [assets](assets)。
- [build.py](build.py)：用 Python 标准库嵌入原图和文字，输出本集 HTML。

第四集插画作小帅、分身与老师的外貌参考，第三集插画作苏小满参考。原图保持不变，页面内嵌一份分镜原图供八格共用，两张发布封面另行内嵌；分镜通过 CSS 背景定位按原比例显示。页面开头的故事配图取自本集第四格的长椅笑点；发布封面使用原有横版与竖版图片，本次未重新生成插画。

页内短语链接使用无空格的锚点，支持 tend to say yes 跳转到 tend to do sth 词卡，以及 in person、to be frank 的课后回忆。图片、字体和参考音频均内嵌，无需联网。内联脚本支持章节图片预览、逐段入场与音色互斥播放；关闭脚本仍可阅读、展开内容与播放音频。支持减少动态效果偏好。

## 重建与检查

在项目根目录运行：

```bash
python3 production/book-01/ep-005/build.py
```

验证包括字幕与源稿逐字一致、编号、单词及短语跳转、图片数据、离线资源、回忆答案展开、手机和平板与桌面排版。记录见 [verification.json](checks/verification.json)，预览图见 [checks](checks)。前四集文件的校验值保存于 [previous-episodes-sha256.json](checks/previous-episodes-sha256.json)。

2026-11-05 最新规则检查见 [current-rules-verification.json](checks/current-rules-verification.json)：25 组字幕与源数据匹配，六段 WAV 与 cast.json 哈希一致、断网实际播放通过，两张封面实际下载与源文件一致，其他 14 集 HTML 未变。可用 `node production/book-01/ep-005/checks/verify-offline.mjs` 复核。

已按项目 taste-skill 完成美化与浏览器截图复核，1440、768、390 像素检查 0 FAIL、3 WARN。设计方向、逐轮评价及警告依据见 [.taste-skill/ep-005/build-notes.md](../../../.taste-skill/ep-005/build-notes.md)。

## 抖音发布资料

发布区包含基于本集剧情的标题、描述、5 个话题及 30 个不重复关键词。横版 4:3 与竖版 3:4 封面分别构图，均以 PNG 内嵌到 HTML，同时提供原生离线下载链接。按现行规则校验：标题 23 字，描述正文 177 字，含话题共 208 字；未自动截断。

2026-11-05 已重新公开搜索相关话题及官方活动，保留原有五个话题；候选活动的官方身份、资格和本集适用性尚未核实，没有作为官方活动采用。查询、来源、核验日期、候选有效期及投稿要求保存在 publishing.json 和 [topic-research.template](publishing/topic-research.template)，HTML 内也可展开阅读。实际发布当天复核。

- [发布文案与封面记录](publishing/publishing.json)
- [横版 PNG](publishing/cover-4x3.png) · [竖版 PNG](publishing/cover-3x4.png)
- [横版提示词](publishing/prompt-4x3.txt) · [竖版提示词](publishing/prompt-3x4.txt)
- [发布区检查结果](checks/publishing-verification.json)

封面使用内置 image_gen.imagegen，以本集分镜为角色与剧情参考、第 001 集封面为画风参考。最终图及生成原图路径保存在 publishing 目录；有修正的封面保留初稿和相应 correction 提示词。

修改发布文案时编辑 publishing/publishing.json。发布区共用[渲染模块](../publishing.py)、[样式](../publishing.css)与[区块模板](../publishing-section.template)，运行本集原有 build.py 即可重建，仍只输出一个独立 HTML。
