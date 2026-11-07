# 第十集制作说明

第 010 集《为了戒手机，他差点删掉整个节目。》交付为 [ep-010.html](../../../episodes/book-01/ep-010.html)。完整剧本、内嵌图片和学习单词收在单个离线 HTML。

## 内容

- 8 幅漫画、8 个故事段落、25 段角色对白参考。
- 167 词英文解说，22 组逐句对应的英文与简体中文字幕，小帅第一人称叙述。
- 5 个新词：addict、reduce、remove、entirely、stressed。包含词义、故事例句、中文解释、用法、教材位置和回忆问题。
- 2 个主线旧词：social media、laptop。
- 到期清单共 10 项，其中 laptop 已在主线解说和复习卡呈现；课后另收其余 9 项：actually、differ、in person、frank、to be frank、digital、hardware、engine、search engine。
- 1 张选题范围表：同学经历为主线、地图辅助核对、小帅个人草稿留待以后。

同词只建一张复习卡，laptop 不重复设置锚点。第八集 engine 与 search engine、本集 remove 与 reduce 分别呈现，完整短语优先匹配。

## 情节与连续性

周六午饭、收拾和休息后，两点回到小帅家的工作桌。苏小满按约两点半回家，妈妈仍在家。电脑仍是学校登记借用、周一归还的那台银色笔记本，黑手机仍只有小帅原来的一部。

分身只获准整理他们自己的临时下载，但在批量选中聊天截图时，连旁边的广播准备工程一起选中。小帅发现后喊停并取消：删除确认尚未通过，没有文件消失，也没有恢复或重录来解围。打开工程核对，第八集短试音、第九集半分钟个人口述草稿和笔记都在。

小帅关闭自己的社交媒体提醒，分身关无关网页，三人保留工具和资料。学校软件、系统与别人的文件没有修改。他们不再花时间批量清理，先把提纲做好。

两点十分只剩二十分钟合作时间，三条线索无法同时展开。第一期收拢到高马尾帮忙同学首日找图书馆、得到帮助的经历；校园手册地图只供路线核对，小帅草稿另存待用。两点二十五保存三条问题，苏小满仍按约回家。正式采访具体时间与路线核对均待周一，不能把同意受访当作已经完成采访。

分身最后先问能否借便携麦克风，供未来图书馆附近的现场采访测试。这里没有实际麦克风、设备采购或录音制作，只有纸上的草图。下一集再讨论需要什么设备、借用测试是否足够。下周三放学后 16:40—16:50 的试播时段不变；周五搬桌、英语分享已完成，篮球月底补选仍待申请。

## 解说与字幕

逐格朗读“英文解说 · 中英字幕”中的英文行；同一行作为英文字幕，紧接的中文行为对应中文字幕。编号 EN001 至 EN022，角色对白另存于可展开的参考区。本项目不生成视频或音频，配音、剪辑及字幕时间轴在另一个项目完成。

## 源文件和插画

- [episode.json](episode.json)：剧本、词汇、逐句字幕与连续性状态。
- [storyboard.png](storyboard.png)：最终选用的八格原图，使用内置 imagegen，以第九集为人物和场景参考生成，再修正发型、重复人物与多余手机。
- [image-prompt.txt](image-prompt.txt)：完整调用提示词记录。
- [image-prompt-v1.txt](image-prompt-v1.txt)、[image-edit-prompt.txt](image-edit-prompt.txt)：初始与修正调用的精确提示词。
- [storyboard-generated-v1.png](storyboard-generated-v1.png)：修正前原图，保留过程记录。
- [page.template](page.template)、[build.py](build.py)：页面模板与独立构建脚本，无共享运行时依赖。

原始生成结果保留在 `/Users/huyin/.codex/generated_images/01a1911b-0335-73d1-9e32-69cfd0344a98/`，最终选图另存本集制作目录。图片不作栅格裁剪或修改；HTML 内嵌一份 PNG，用八个带裁切区域的 SVG 窗口显示分镜。图内界面是虚构图标，正文字幕与操作说明由 HTML 提供。

## 重建与检查

在项目根目录运行：

```bash
python3 production/book-01/ep-010/build.py
```

检查字幕与源稿一致、编号连续、图片内嵌、页内锚点、复习卡展开及手机、平板、桌面排版。记录见 [verification.json](checks/verification.json)，截图见 [checks](checks)。前九集文件校验值保存在 [previous-episodes-sha256.json](checks/previous-episodes-sha256.json)。

## 抖音发布资料

2026-11-01 补充发布区，包含基于本集剧情的标题、描述、6 个话题及 30 个不重复关键词。横版 4:3 与竖版 3:4 封面分别构图，均以 PNG 内嵌到 HTML，同时提供原生离线下载链接。

- [发布文案与封面记录](publishing/publishing.json)
- [横版 PNG](publishing/cover-4x3.png) · [竖版 PNG](publishing/cover-3x4.png)
- [横版提示词](publishing/prompt-4x3.txt) · [竖版提示词](publishing/prompt-3x4.txt)
- [发布区检查结果](checks/publishing-verification.json)

封面使用内置 image_gen.imagegen，以本集分镜为角色与剧情参考、第 001 集封面为画风参考。最终图及生成原图路径保存在 publishing 目录；有修正的封面保留初稿和相应 correction 提示词。

修改发布文案时编辑 publishing/publishing.json。发布区共用[渲染模块](../publishing.py)、[样式](../publishing.css)与[区块模板](../publishing-section.template)，运行本集原有 build.py 即可重建，仍只输出一个独立 HTML。
