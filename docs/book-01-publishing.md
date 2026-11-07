# 第一册抖音发布资料

第 001—015 集均在独立 HTML 的“抖音发布”区提供标题、描述、5 个话题、30 个不重复关键词，以及可离线下载的横版 4:3、竖版 3:4 PNG 封面。

## 当前发布限制（2026-11-02 核验）

本项目使用抖音创作者中心**网页端视频发布**。本次直接查看了[官方发布页](https://creator.douyin.com/creator-micro/content/post/video)的标题与简介计数器；没有上传、保存草稿或发布作品。

| 字段 | 执行上限 | 依据与计数口径 |
| --- | --- | --- |
| 标题 | 30 字 | 当前官方发布页显示 `0/30`，标题含系列名、集数也必须计入。建议将剧情钩子放前面，标题保持单行。 |
| 简介／作品描述 | 含话题共 1000 字 | 当前官方发布页显示 `0/1000`；在简介中输入 `#英语` 显示 `3/1000`，输入 `#高中英语` 显示 `5/1000`，说明话题文本计入此预算。 |
| 话题 | 最多 5 个，不重复 | 用户确认的当前入口限制；本项目按硬上限执行。本次没有逐一选择 6 个话题测试，不声称所有客户端均实测一致。 |
| 关键词 | 恰好 30 个，不重复 | 项目交付要求，供选词和检索，不是平台要求的 30 个标签，不全部粘贴到简介。 |

简介建议 80—200 字，是本项目的写作建议，不是抖音硬限制。生成校验按 UTF-16 code unit 保守计数：普通汉字、英文字母、数字、标点、空格和换行都计入，补充平面字符（如部分 emoji）按 2 计。最终仍以实际发布页计数器为准，不使用“英文单词算一个字”的算法。

`description` 只写简介正文，`topics` 单独存不带 `#` 的话题名。校验会把 `简介正文 + 换行 + #话题1 #话题2…` 合并计算，避免正文刚好 1000 字、加话题后超限；标题和简介内联 `#` 会报错，防止绕过数量统计。不能自动截断标题、词汇或话题，应重写超限文案。

网上常见的 55 字、10 个话题等说法涉及历史版本或不同发布入口，不作为本项目当前口径。抖音开放平台的[创建视频接口](https://open.douyin.com/platform/resource/docs/openapi/video-management/douyin/create/create-video/)与西瓜视频接口字段不同，不能将接口或其他平台的限制套用到当前网页端。规则变化时，先复核官方发布界面，再更新[机器可读规则](../data/douyin-publishing-policy.json)和本页。

## 话题搜索与官方活动

可以搜索官方话题，但要分别判断“平台已有话题”和“官方活动”。本次在官方发布页话题候选中确认了 `#高中英语`、`#高中英语单词`、`#高中英语词汇`、`#英语学习`、`#英语单词`。它们是可选的普通相关话题，**本次没有看到足以将其认定为官方扶持活动的证据**。候选旁的累计热度不是本集可获得的流量，不据此承诺播放量。

[抖音作者助手官方教程](https://www.douyin.com/video/7223294657524976953)介绍了站内热点榜、创作灵感、巨量算数和搜索推荐词等选题工具；其内容可在[搜索聚合页](https://www.douyin.com/shipin/7264805682406131764)核对。该教程为历史视频，聚合页显示的更新日期不代表原视频发布时间。使用时以当前 App 和网页实际入口为准。

每次生成发布资料时按下面流程搜索，发布当天再复核：

1. 在视频发布页“添加话题”中搜索本集对应的英语技能、词汇与剧情，发布时选中候选话题，确认形成可点击话题。
2. 查看发布页“官方活动”、创作者中心可用活动入口、抖音 App“创作灵感”，以及认证的 `抖音知识`、`抖音作者助手` 发布的信息。本次登录账号的网页“创作服务 → 活动管理”显示“暂无活动灵感”；这只代表当前账号和入口的观察，不代表全平台没有活动。
3. 对候选官方活动记录：准确话题名称、官方发起方、活动／规则链接、核验日期、起止日期、报名和投稿入口、账号资格、内容要求。只有仍在有效期且本集符合要求，才列入正式话题；如有扶持，准确记录获得条件。
4. 组合使用“1 个系列话题 + 2 个英语精准话题 + 1 个剧情话题 + 1 个机动话题”。匹配的官方活动替换机动话题，总数不超过 5；没有适合活动时，保留普通相关话题，不占位凑活动。

当前校园集的普通组合为 `#英语有续集 #高中英语 #英语单词 #英语学习 #校园故事`；第 015 集使用 `#家庭故事`。其中 `#英语有续集` 是系列自有话题，尚未核验同名话题页或占用情况；剧情话题也应在发布时确认候选。原第六个 `#北师大版英语` 已从话题中移除，仍保留在 30 个关键词中供检索。

本次找到 `抖音知识` 于 2025-04-25 发布的[抖音知识创作砥砺计划](https://jingxuan.douyin.com/m/video/7497085396724043060)，可以证实平台确有知识内容扶持方向，不能据此把计划名作为本集当前有效的投稿话题。**截至本次核验，没有找到同时具备当前有效期、明确投稿条件、适合本系列英语剧情的已验证官方活动话题**。后续按集搜索，不把历史的 DOU知计划、知识创作人等名称自动视为仍在扶持的活动。

官方活动、普通 `#话题`、页面“关联热点”以及创作者扶持计划是不同入口。参与活动可能提供额外曝光机会，仍取决于其规则及内容表现；不承诺添加标签就能上热门。

## 生成与校验

规则来源保存在 [douyin-publishing-policy.json](../data/douyin-publishing-policy.json)，共用校验在 [publishing_rules.py](../production/book-01/publishing_rules.py)。第 001 集构建脚本与第 002—015 集共用渲染模块已接入，超限会中止生成。

运行 `python3 production/book-01/verify-publishing-copy.py` 可同时核对各集源数据与实际 HTML 的标题、简介、话题及 30 个关键词；结果见 [发布限制校验](../production/book-01/publishing-limits-verification.json)。既有批量校验是历史交付记录；本次调整仅涉及发布区文字和话题，媒体和完整剧本保持原字节。

## 分集发布资料

封面以各集分镜和第 001 集封面为参考，使用内置 image_gen.imagegen 分别生成两种构图。每集完整提示词与生成原图路径保存在 publishing 目录。

| 集数 | 发布标题 | HTML | 横版 4:3 | 竖版 3:4 | 提示词 |
| --- | --- | --- | --- | --- | --- |
| 001 | 让分身替我说句Hello，他竟然当上班长？｜英语有续集001 | [打开](../episodes/book-01/ep-001.html) | [PNG](../production/book-01/ep-001/publishing/cover-4x3.png) | [PNG](../production/book-01/ep-001/publishing/cover-3x4.png) | [生成](../production/book-01/ep-001/publishing/image-prompts.txt) |
| 002 | 两个我三件事，这次我自己选｜英语有续集002 | [打开](../episodes/book-01/ep-002.html) | [PNG](../production/book-01/ep-002/publishing/cover-4x3.png) | [PNG](../production/book-01/ep-002/publishing/cover-3x4.png) | [横版](../production/book-01/ep-002/publishing/prompt-4x3.txt) · [竖版](../production/book-01/ep-002/publishing/prompt-3x4.txt) |
| 003 | 同桌看见两个我，我决定说实话｜英语有续集003 | [打开](../episodes/book-01/ep-003.html) | [PNG](../production/book-01/ep-003/publishing/cover-4x3.png) | [PNG](../production/book-01/ep-003/publishing/cover-3x4.png) | [横版](../production/book-01/ep-003/publishing/prompt-4x3.txt) · [竖版](../production/book-01/ep-003/publishing/prompt-3x4.txt) |
| 004 | 多了一个我，家务也多一份？｜英语有续集004 | [打开](../episodes/book-01/ep-004.html) | [PNG](../production/book-01/ep-004/publishing/cover-4x3.png) | [PNG](../production/book-01/ep-004/publishing/cover-3x4.png) | [横版](../production/book-01/ep-004/publishing/prompt-4x3.txt) · [竖版](../production/book-01/ep-004/publishing/prompt-3x4.txt) |
| 005 | 休息只有十秒？这场晨跑先暂停｜英语有续集005 | [打开](../episodes/book-01/ep-005.html) | [PNG](../production/book-01/ep-005/publishing/cover-4x3.png) | [PNG](../production/book-01/ep-005/publishing/cover-3x4.png) | [横版](../production/book-01/ep-005/publishing/prompt-4x3.txt) · [竖版](../production/book-01/ep-005/publishing/prompt-3x4.txt) |
| 006 | 分身想包全天，她只要十分钟｜英语有续集006 | [打开](../episodes/book-01/ep-006.html) | [PNG](../production/book-01/ep-006/publishing/cover-4x3.png) | [PNG](../production/book-01/ep-006/publishing/cover-3x4.png) | [横版](../production/book-01/ep-006/publishing/prompt-4x3.txt) · [竖版](../production/book-01/ep-006/publishing/prompt-3x4.txt) |
| 007 | 分工表上两个小帅，到底谁负责？｜英语有续集007 | [打开](../episodes/book-01/ep-007.html) | [PNG](../production/book-01/ep-007/publishing/cover-4x3.png) | [PNG](../production/book-01/ep-007/publishing/cover-3x4.png) | [横版](../production/book-01/ep-007/publishing/prompt-4x3.txt) · [竖版](../production/book-01/ep-007/publishing/prompt-3x4.txt) |
| 008 | 电脑有波形却没声？先放下采购单｜英语有续集008 | [打开](../episodes/book-01/ep-008.html) | [PNG](../production/book-01/ep-008/publishing/cover-4x3.png) | [PNG](../production/book-01/ep-008/publishing/cover-3x4.png) | [横版](../production/book-01/ep-008/publishing/prompt-4x3.txt) · [竖版](../production/book-01/ep-008/publishing/prompt-3x4.txt) |
| 009 | 搜了三小时，采访页还是空的？｜英语有续集009 | [打开](../episodes/book-01/ep-009.html) | [PNG](../production/book-01/ep-009/publishing/cover-4x3.png) | [PNG](../production/book-01/ep-009/publishing/cover-3x4.png) | [横版](../production/book-01/ep-009/publishing/prompt-4x3.txt) · [竖版](../production/book-01/ep-009/publishing/prompt-3x4.txt) |
| 010 | 戒手机差点把节目也删了？｜英语有续集010 | [打开](../episodes/book-01/ep-010.html) | [PNG](../production/book-01/ep-010/publishing/cover-4x3.png) | [PNG](../production/book-01/ep-010/publishing/cover-3x4.png) | [横版](../production/book-01/ep-010/publishing/prompt-4x3.txt) · [竖版](../production/book-01/ep-010/publishing/prompt-3x4.txt) |
| 011 | 麦克风清单很豪华，钱包不同意｜英语有续集011 | [打开](../episodes/book-01/ep-011.html) | [PNG](../production/book-01/ep-011/publishing/cover-4x3.png) | [PNG](../production/book-01/ep-011/publishing/cover-3x4.png) | [横版](../production/book-01/ep-011/publishing/prompt-4x3.txt) · [竖版](../production/book-01/ep-011/publishing/prompt-3x4.txt) |
| 012 | 我讲第三条，你怎么还在第一条？｜英语有续集012 | [打开](../episodes/book-01/ep-012.html) | [PNG](../production/book-01/ep-012/publishing/cover-4x3.png) | [PNG](../production/book-01/ep-012/publishing/cover-3x4.png) | [横版](../production/book-01/ep-012/publishing/prompt-4x3.txt) · [竖版](../production/book-01/ep-012/publishing/prompt-3x4.txt) |
| 013 | 采访台词全背熟，却接不上她的话｜英语有续集013 | [打开](../episodes/book-01/ep-013.html) | [PNG](../production/book-01/ep-013/publishing/cover-4x3.png) | [PNG](../production/book-01/ep-013/publishing/cover-3x4.png) | [横版](../production/book-01/ep-013/publishing/prompt-4x3.txt) · [竖版](../production/book-01/ep-013/publishing/prompt-3x4.txt) |
| 014 | 开播前十秒，怎么先感谢收听？｜英语有续集014 | [打开](../episodes/book-01/ep-014.html) | [PNG](../production/book-01/ep-014/publishing/cover-4x3.png) | [PNG](../production/book-01/ep-014/publishing/cover-3x4.png) | [横版](../production/book-01/ep-014/publishing/prompt-4x3.txt) · [竖版](../production/book-01/ep-014/publishing/prompt-3x4.txt) |
| 015 | 妈妈下夜班，我的采访先暂停｜英语有续集015 | [打开](../episodes/book-01/ep-015.html) | [PNG](../production/book-01/ep-015/publishing/cover-4x3.png) | [PNG](../production/book-01/ep-015/publishing/cover-3x4.png) | [横版](../production/book-01/ep-015/publishing/prompt-4x3.txt) · [竖版](../production/book-01/ep-015/publishing/prompt-3x4.txt) |

第 014 集为复习剧情，封面明确写“旧词复习 · 本集6词”，没有增加新词。其他集按对应的 5 个或 6 个核心词条标注，正式解说、双语字幕与词汇内容均保留。

修改发布文案时编辑各集 publishing/publishing.json，替换封面时同步记录实际宽高。第 002—015 集共用 [发布区渲染模块](../production/book-01/publishing.py)、[样式](../production/book-01/publishing.css)和[区块模板](../production/book-01/publishing-section.template)，运行各集原有 build.py 即可重建。

[批量校验结果](../production/book-01/publishing-batch-verification.json)记录关键词数量、图片比例、下载数据与原剧本完整性；各集 checks/publishing-verification.json 另记录浏览器排版检查。
