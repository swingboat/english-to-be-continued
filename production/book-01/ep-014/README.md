# 第十四集制作说明

第 014 集《直播前十秒，谁把提词卡翻过去了？》交付为 [ep-014.html](../../../episodes/book-01/ep-014.html)。完整剧本、内嵌图片、英文解说、中英字幕与词汇复习内容收在单个离线 HTML。

## 本集是复习剧情

- 8 幅漫画、8 个故事段落、22 段角色对白或动作参考。
- 168 词英文解说，22 组逐句对应的英文与简体中文字幕，小帅第一人称叙述。
- **0 个新词；6 个重点复习词**：confidence、volunteer、goal、schedule、organise、quality。
- 六张重点复习卡先显示故事回忆问题，展开后可看词义、故事例句、中文解释和用法，同时标明首次学习集数与教材词表位置。
- 10 个课后到期词：第七集的 responsible、be responsible for、function、seek、professional，以及第十二集的 convenient、according to、update、meanwhile、distance。
- 1 张十分钟试播流程表，五段合计 10 分钟。

`episode.json` 的 `words` 在本集表示六张重点复习卡，`vocabulary_mode` 为 `review`，`new_words` 为空，`review_words` 不重复放卡。十个补充词另收在展开区，合计复习 16 个不同词条。词汇台账只追加实际复习集数，首次已教词条数仍为 67。

## 情节与连续性

周三 16:35，三位学生和女广播指导老师在学校广播室准备第一次试播。老师确认流程与设备，家长知情。使用第十三集受访同学同意的采访片段，实际分工为苏小满主编、小帅主持统筹、分身声音协助。图书馆借用的手持麦克风已归还，本集用广播室原有固定台式麦克风、调音台和同一台电脑。

分身逐张检查纸卡，顺手把每张看过的卡叠到新一沓最上面，因此顺序反了。16:39:50，小帅翻起第一张，先看到“感谢收听”。内容与音频文件没有变。小帅明确自己开场，苏小满把三张卡排回开场、录音、结语，分身等主持信号再播放，老师按原时段开播。

十秒内的现场只有简短交接和快速排三张卡；英文解说为旁述，可配定格或回看，不要求人物在十秒内读完全部解说。剧本按本集约两分钟的叙事规模呈现十分钟广播事件，流程表标明剧情中的完整时段。

16:40 开场，16:43 交给已获同意的采访片段，16:46 回顾受助经历与感受，16:50 按时结束。结语呼应“一起开口，会没那么孤单”，实际分工列入节目单。没有重录采访、临时添加设备或改变受访者的经历，声音由指导老师监看。

收尾时老师确认第一期完成，邀请先准备“家人的一天”采访提案。小帅决定先问妈妈愿不愿意、什么时间方便，尚未约好采访或下一次播出时段。分身等小帅说完再询问如何协助，回扣第一集替别人抢先报名的起点。第十五集将进入家人的时间与真实生活。

周五搬桌、英语分享已完成，月底篮球补选仍待申请。父母和老师知情，分身只参加获准课后项目。

## 解说与字幕

朗读各格“英文解说 · 中英字幕”中的英文行；同一行作为英文字幕，紧接的中文行为对应中文字幕。编号 EN001 至 EN022，角色对白与动作参考另收在展开区。

本项目只提供文本与图片，不生成实际广播音频或视频。配音、剪辑、字幕时间轴与视频导出在另一个项目完成。

## 源文件与插画

- [episode.json](episode.json)：剧本、复习词卡、解说、字幕与连续性状态。
- [storyboard.png](storyboard.png)：内置 imagegen 生成的最终八格原图。
- [image-prompt.txt](image-prompt.txt)：全部精确调用提示词。
- [image-prompt-v1.txt](image-prompt-v1.txt)、[image-edit-prompt.txt](image-edit-prompt.txt)：初始生成与三张卡、收尾时钟的修正提示词。
- [storyboard-generated-v1.png](storyboard-generated-v1.png)：修正前原图，保留过程记录。
- [page.template](page.template)、[build.py](build.py)：本集独立模板与 Python 标准库构建脚本。

第七集为三位学生、女广播指导老师与广播室设备提供参考。老师保持短卷棕发、深蓝开衫与赭色上衣、无眼镜；小帅红内搭、分身蓝内搭、苏小满短发圆眼镜。现场只有这四人，高马尾受访同学以录音参与，不画成第五人。

提示卡只有三张，分别用麦克风、波形和挥手图标表示段落。指示灯在开场前未亮，试播中亮起，结束后熄灭。原始生成文件保留在 `/Users/huyin/.codex/generated_images/01a1911b-0335-73d1-9e32-69cfd0344a98/`；最终选图另存本集目录，不做栅格编辑。

一份 PNG 内嵌到 HTML，通过八个带裁切区的 SVG 窗口显示分镜。图片里的符号与正文角色对白对应，实际字幕由可选择复制的 HTML 文本提供，无网络依赖。

## 重建与检查

在项目根目录运行：

```bash
python3 production/book-01/ep-014/build.py
```

检查复习词与新词数的区分、六张核心卡和十张补充卡展开、字幕与源稿一致、页内链接、内嵌图片，以及手机、平板、桌面排版。记录见 [verification.json](checks/verification.json)，截图见 [checks](checks)。前十三集校验值见 [previous-episodes-sha256.json](checks/previous-episodes-sha256.json)。

## 抖音发布资料

2026-11-01 补充发布区，包含基于本集剧情的标题、描述、6 个话题及 30 个不重复关键词。横版 4:3 与竖版 3:4 封面分别构图，均以 PNG 内嵌到 HTML，同时提供原生离线下载链接。

- [发布文案与封面记录](publishing/publishing.json)
- [横版 PNG](publishing/cover-4x3.png) · [竖版 PNG](publishing/cover-3x4.png)
- [横版提示词](publishing/prompt-4x3.txt) · [竖版提示词](publishing/prompt-3x4.txt)
- [发布区检查结果](checks/publishing-verification.json)

封面使用内置 image_gen.imagegen，以本集分镜为角色与剧情参考、第 001 集封面为画风参考。最终图及生成原图路径保存在 publishing 目录；有修正的封面保留初稿和相应 correction 提示词。

修改发布文案时编辑 publishing/publishing.json。发布区共用[渲染模块](../publishing.py)、[样式](../publishing.css)与[区块模板](../publishing-section.template)，运行本集原有 build.py 即可重建，仍只输出一个独立 HTML。
