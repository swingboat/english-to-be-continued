# 第十一集制作说明

第 011 集《设备清单很豪华，钱包不同意。》交付为 [ep-011.html](../../../episodes/book-01/ep-011.html)。完整剧本、图片与学习词汇收在单个离线 HTML。

## 内容

- 8 幅漫画、8 个故事段落、24 段角色对白参考。
- 156 词英文解说，22 组英文与简体中文字幕，小帅第一人称叙述。
- 6 个新词条：range、various、sort、all sorts of、quality、necessity，含词义、故事例句、中文解释、用法、教材位置和回忆问题。
- 2 个主线旧词：hardware、laptop。
- 10 个课后到期词回忆：第四集的 senior、secondary、previous、campus、junior，以及第九集的 chat、surf、surf the Internet、media、social media。
- 1 张实际需求表：清楚录音、已有电脑、安静桌位与本次不用的豪华设备。

sort 与 all sorts of、surf 与 surf the Internet、media 与 social media 各自设卡。标注优先匹配完整短语，锚点统一小写，学习内容中的 Internet 保留大写。六张新词卡按两列成对排版。

## 情节与连续性

时间从上集周六推进到周一放学后。周末借用电脑已于早上登记归还，下午三人在老师批准、家长知情的课后项目时段登记使用同一台电脑。分身把周末画的长清单带到学校；豪华设备都只是纸上图案。

小帅钱包里的一枚零钱形成喜剧反应，但他没有承诺垫付项目费用。苏小满把注意力拉回采访地点、能否听清以及与已有电脑的连接。指导老师登记借给项目组一支兼容的普通有线 USB 手持麦克风，图书馆老师批准在安静桌位测试，采访安排坐下进行。

第七至八集已经证明室内原有设备和电脑可用。本集检查的是这次图书馆旁桌边谈话的实际收音条件，并不推翻此前结论。三人使用借用麦克风作短试录、回放确认，达到本次采访需要后决定优先借用，今天没有购买。原计划中“预算用于可用麦克风”细化为：经费仅保留给必要且无法借用解决的收音问题，避免设备已可借却仍无故采购。

本次短测试单独保存，旧短试音、小帅个人口述草稿、准备笔记均保留。使用后电脑和麦克风交回老师保管，采访时再领用，设备未带回家。

周一午休已核对图书馆路线，并与愿意受访的高马尾同学及老师确认：周二放学后 16:40—16:50，在指定安静桌位采访。三问仍是在哪里迷路、谁帮了你、当时感觉怎样。正式采访尚未进行；采访前先约远程核对三问，下一集落实连线并处理延迟、提纲版本问题。周三 16:40—16:50 试播时段不变，节目尚未完成。

## 解说与字幕

朗读各格“英文解说 · 中英字幕”中的英文行；同一行作为英文字幕，紧接的中文行为对应中文字幕。编号 EN001 至 EN022，角色对白另收在可展开参考区。配音、剪辑、字幕时间轴和视频导出在另一个项目完成；剧情里的试录不在这里生成音频。

## 源文件与插画

- [episode.json](episode.json)：完整剧本、解说、字幕、词汇和连续性。
- [storyboard.png](storyboard.png)：内置 imagegen 生成的八格原图，以第十集为三位学生外观与画风参考，场景改为学校准备室、图书馆旁桌位。
- [image-prompt.txt](image-prompt.txt)：本次精确生成提示词。
- [page.template](page.template)、[build.py](build.py)：独立页面模板和标准库构建脚本。

原始生成结果：`/Users/huyin/.codex/generated_images/01a1911b-0335-73d1-9e32-69cfd0344a98/exec-2f49b065-719b-4dfe-a3af-4b73de36d36a.png`。原图保留，选图另存本集目录，不做栅格编辑。

三人短黑发、红蓝内搭与苏小满圆眼镜保持一致；小帅回放时可脱外套，红 T 恤不变。第二格分身被自己举起的清单挡住脸，仍只有三个人。全程一台电脑、第四格起一支实际麦克风，没有手机、耳机或额外录音设备。图片内只画图标，文字由 HTML 提供。单份 PNG 内嵌后通过八个带裁切区的 SVG 窗口显示分镜。

## 重建与检查

在项目根目录运行：

```bash
python3 production/book-01/ep-011/build.py
```

验证包含字幕与源稿一致、编号、短语和单词分别跳转、图片内嵌、复习卡展开，以及手机、平板、桌面排版。记录见 [verification.json](checks/verification.json)，截图见 [checks](checks)。前十集校验值记录在 [previous-episodes-sha256.json](checks/previous-episodes-sha256.json)。

## 抖音发布资料

2026-11-01 补充发布区，包含基于本集剧情的标题、描述、6 个话题及 30 个不重复关键词。横版 4:3 与竖版 3:4 封面分别构图，均以 PNG 内嵌到 HTML，同时提供原生离线下载链接。

- [发布文案与封面记录](publishing/publishing.json)
- [横版 PNG](publishing/cover-4x3.png) · [竖版 PNG](publishing/cover-3x4.png)
- [横版提示词](publishing/prompt-4x3.txt) · [竖版提示词](publishing/prompt-3x4.txt)
- [发布区检查结果](checks/publishing-verification.json)

封面使用内置 image_gen.imagegen，以本集分镜为角色与剧情参考、第 001 集封面为画风参考。最终图及生成原图路径保存在 publishing 目录；有修正的封面保留初稿和相应 correction 提示词。

修改发布文案时编辑 publishing/publishing.json。发布区共用[渲染模块](../publishing.py)、[样式](../publishing.css)与[区块模板](../publishing-section.template)，运行本集原有 build.py 即可重建，仍只输出一个独立 HTML。
