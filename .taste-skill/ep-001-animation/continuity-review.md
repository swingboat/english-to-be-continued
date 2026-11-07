# 2026-11-06 连贯性修订复核

用户评价是本轮依据：旧版“不连贯”。此前页面通过排版与按钮检查，只证明交付能打开、能操作，不能据此认为动画表演达到预期。

方向沿用 Colour chapters，seed 1548411302，保留原字体、配色、正文结构与媒体优先构图；本轮没有新抽设计方向。新增图片通过内置 imagegen 按原人物参考制作，提示词分别保存在分集 `animation/rig-prompt.json` 与 `animation/body-prompt.json`，项目使用副本并全部内嵌 HTML。没有图库照片、图库视频或外部音乐。

ROUND 1
Seen in one second: 同一教室里的分身和班主任。
Idea (one sentence): 让同一个人物在同一镜头里完整举起一只手。
Live thing: 可拖动查看完整连续动作的 16 秒播放器。
Layout words by section: hero=cinema / script=sequential image-and-text / words=vocabulary / cast=voice profiles / publishing=copy and covers。
Scores: design 6.8 · usability 8.0 · creativity 7.0 · content 8.5 → overall 7.4
Caps applied: 无排版 FAIL；动画表演尚有可见缺点，不能把页面分数当成影片分数。
Top three problems (most visible first), each with the screenshot it shows in and the fix:
1. checks/continuous/desktop-0.jpg：直接从 T 形姿势裁身体，会留下突出的肩部残片。补绘独立无手臂身体层，在同一头部、身体与比例上衔接袖子。
2. checks/continuous/desktop-4-8.jpg：手臂必须保持肩、肘、腕衔接。用同一组部件按连续角度绘制，保持根部锚点和肢体长度，删除旧版整张姿势替换。
3. inspect-continuous/desktop-fold.jpg：默认居中播放按钮遮住分身的脸。按钮移到画面左侧空处，继续保留顶部文字播放按钮与完整控件。

ROUND 2
Seen in one second: 课堂举手片段的预演页面。
Idea (one sentence): 相同人物、相同构图，只让手臂与门外探头动作推进剧情。
Live thing: 连续动作播放器，支持暂停、拖动、重播、键盘操作与离线参考音色。
Layout words by section: hero=cinema / script=sequential image-and-text / words=vocabulary / cast=voice profiles / publishing=copy and covers。
Scores: design 7.2 · usability 8.0 · creativity 7.0 · content 8.5 → overall 7.5
Caps applied: 无页面 FAIL。分数仅评价页面呈现，不作为完整动画片的质量评价。
Top three problems (most visible first), each with the screenshot it shows in and the fix:
1. checks/continuous/contact-sheet.jpg：身体和脸仍较静，属于二维剪纸式动作预演。当前明确标注制作边界；完整动画还需面部、衣服与身体中间画，不能靠按钮测试消除这一限制。
2. checks/continuous/390-5-8.jpg：手机画面较小，人物表演的细节有限。保留清晰字幕与单词提示，目标只验证一段举手，避免堆更多快速切镜头。
3. checks/continuous/desktop-12.jpg：小帅从画面边缘探入仍以平移和转动表现，尚非全身动作。保持同一空间关系与连续曲线，不承诺这一版已达到自然角色表演。

## 当前验证范围

- 完整 16 秒实播，约 16 秒结束；本地浏览器帧间隔中位数约 16.7 ms，p95 约 16.8 ms。此为本机实测，不保证所有设备相同。
- 每秒 30 帧抽样，481 个实际 Canvas 画面。相邻帧最大平均归一化 RGB 差约 0.009，未超过用于识别大幅跳变的 0.015 阈值。该数值只能检查跳变，不评价美术与表演。
- 18 项功能与资源检查通过；0 浏览器异常、0 外部资源请求；375、390、768 像素没有横向溢出。
- 页面按项目 taste-skill 在 1440、768、390 像素执行实浏览器检查。唯一保留的 no-footage 告警符合项目不导出视频的交付范围。
- 当前完整 8 格剧情、23 组解说、5 个词、4 位人物参考语音、既有发布资料与两张离线封面均保留。
- 目前只有音效与字幕，无正式英文台词配音；这一次也没有制作或导出视频。

当前实播、连续帧与资源检查结果：`production/book-01/ep-001/checks/continuous/verification.json`。前一版 `checks/animation` 下的结果为历史记录，不代表本次连续动作版本。

最终检查完成后，已逐张打开 `inspect-continuous` 列出的全部 10 张最终截图：三个首屏及全部七张页面合成图；并另查看动作联系表与手机举手关键帧。最终排版检查为 0 FAIL、1 WARN（项目要求不制作视频）；已修复首屏播放按钮遮脸。
