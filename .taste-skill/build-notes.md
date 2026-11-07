# Episode 002 design notes

Audience: high-school English learners and the downstream video maker. A complete offline episode, with playable character references. Read the story, return to five words, then reuse the voices and publishing packet.

Inventory: two identical Xiaoshuai students; red versus blue inner shirts; one-use clone button; Friday 14:00 three-way clash; the single activity confirmation clipboard; 13:20–13:40 revised desk setup; the existing month-end tryout notice; Su Xiaoman waiting for an explanation; eight original illustrated panels; five Unit 1 words; 35 paired captions; four existing character references.

Claims and proof: the hero shows the two students with three invitations; the narration note identifies Xiaoshuai and the 35 caption pairs; the story provides eight panels with full text; the printed vocabulary sheet connects all five words to the actions; the voice roster lets the reader hear four real reference files and read the complete casting information; the publication packet provides current-episode copy, 30 keywords and two offline covers; the last note preserves the unresolved explanation.

Direction: The page is the object, seed 2094817229. The episode’s single activity confirmation clipboard becomes the page’s invitation-shaped reading sheet. The live thing is the four-person voice roster, with exclusive native audio playback and a transcript fallback.

Redraws: showcase changed to square plate with spare text because a clipped paper-slip montage cannot contain eight complete scenes and bilingual captions. Proof changed to plain columns because a clipped guest list cannot contain the full publication packet and both covers. No palette or type redraw. Schibsted Grotesk is embedded locally as TTF in three weights, with system Chinese glyph fallback for offline reading.

Image sources: existing episode storyboard and publishing covers only; no found photographs, no stock stand-ins, no new illustrative claims. Raster panels are displayed by CSS windows over one embedded sheet, without modifying source pixels. No video: project delivery rules explicitly exclude video. Curtain footer, brief type entrances, picture settling and independent section entrances honor reduced motion and preserve text without JavaScript.

ROUND 0
Seen in one second: a complete illustrated lesson with a small picture and many production labels.
Idea (one sentence): the activity form is already in the plot but not yet expressed by the page.
Live thing: none beyond anchor links and downloads.
Layout words by section: hero=two columns / narration=boxed note / cast=repeated cards / story=repeated two columns / words=repeated cards / publishing=fields and covers
Scores: design 6 · usability 7 · creativity 5 · content 8 → overall 6.0
Caps applied: previous inspector FAILs, small text, ornaments, static page.
Top three problems (most visible first), each with the screenshot it shows in and the fix:
1. desktop-fold.jpg: small headline/image and tiny labels compete; use one large printed sheet.
2. mobile-fold.jpg: two buttons and tags dominate; use one action and a readable compact title.
3. tablet-fold.jpg: thin boxes and 20 type sizes fragment the content; use the dealt navy palette and five type steps.

ROUND 1
Seen in one second: a navy-and-white printed lesson sheet with an oversized title, but the first render has broken raster backgrounds and the sticky footer overlays it.
Idea (one sentence): the single activity clipboard becomes a complete printed lesson sheet.
Live thing: four real embedded voice samples, each with transcript and native controls.
Layout words by section: hero=invitation sheet / narration=title and note / story=image with transcript / words=printed menu / cast=voice roster / publishing=plain columns and covers
Scores: design 5 · usability 5 · creativity 7 · content 8 → overall 5.7
Caps applied: inspector FAILs and blank raster windows.
Top three problems (most visible first), each with the screenshot it shows in and the fix:
1. desktop-fold.jpg: sticky footer covers the reading button; replace the sticky curtain with a natural-flow footer reveal so it cannot overlay content.
2. mobile-page-01.jpg: all storyboard raster windows are blank because the large CSS custom property exceeds the browser value limit; put the embedded image directly in the shared background rule.
3. mobile-fold.jpg: support copy is small; raise it to 18px and remove duplicate confirmation labels before subsequent section headings.

ROUND 2
Seen in one second: a navy field holding one large white episode sheet, with a readable two-line title and the actual characters.
Idea (one sentence): the activity confirmation sheet becomes an offline reading and voice reference sheet.
Live thing: all four character reference WAVs play offline; a new voice pauses the previous one.
Layout words by section: hero=printed sheet / narration=paired columns / story=large panels with captions / words=menu sheet / cast=audio roster / publishing=labelled columns with two covers / footer=back of the sheet
Scores: design 7.8 · usability 8.2 · creativity 7.2 · content 9.0 → overall 6.0
Caps applied: one remaining inspector eyebrow FAIL caused by keyword punctuation, plus hidden disclosure text counted as preceding labels.
Top three problems (most visible first), each with the screenshot it shows in and the fix:
1. Publishing screenshot: helper copy crowds the cover heading; place the copying guidance after the cover downloads.
2. Inspector hidden disclosure rectangles: keep closed disclosure descendants out of layout explicitly, restoring them when opened.
3. Keyword separators are extracted as a run of commas by the inspector; keep each comma with its preceding keyword in one semantic span, preserving the visible copy.

Final check rationale: repeated filled rows are actual alternating bilingual subtitle groups, rather than decorative feature cards. No footage is included because project delivery rules exclude video. The name-only-title warning comes from space-delimited language heuristics: the visible Chinese support sentence explicitly says this is an English-learning story with three Friday invitations. These warnings do not imply missing content.

Motion adjustment: the proposed sticky curtain exposed the footer over a long document; a natural-flow back-of-sheet footer is used instead so no title or button is covered. Independent headings, illustrations and roster entries arrive as their sections are read; reduced motion switches off every animation.

ROUND 3 — final
Seen in one second: an illustrated English story presented as one printed episode sheet, with one clear reading action.
Idea (one sentence): the story’s activity confirmation sheet becomes the complete episode’s reading and voice reference sheet.
Live thing: four offline character WAV players with transcript disclosures and mutually exclusive playback.
Layout words by section: hero=invitation sheet / narration=title and note / story=paired illustration and transcript / words=printed menu / cast=voice roster / publishing=copy columns and two cover plates / footer=back of the sheet
Scores: design 7.8 · usability 8.2 · creativity 7.0 · content 9.0 → overall 7.9
Caps applied: creativity capped at 7 for a familiar printed-sheet concept. No inspector FAIL cap applies.
Top three problems (most visible first), each with the screenshot it shows in and the fix:
1. mobile-page-01.jpg: a complete eight-scene episode is a long read; the scene contents and separate words/voices navigation provide direct access. Keeping all required content takes priority over shortening it.
2. desktop-fold.jpg: the invitation title pushes the lower portion of the characters below the first fold; this intentionally previews a sheet that continues, while the phone shows the full first illustration.
3. tablet-page-02.jpg: bilingual text has a tighter measure beside the pictures at tablet size; all paragraphs are readable and do not overflow, while phones use the full-width single column.

Final inspector: 0 FAIL at 1440, 768 and 390; three warnings have the rationales recorded above. All inspector fold images and page contact sheets were opened, together with specific screenshots of vocabulary, publication covers, playable voices and expanded transcripts. Final functional checks also include 375px, offline playback of every voice, the play-pause exclusivity rule, both offline PNG downloads, transcript/dialogue disclosures, disabled-script content, reduced-motion behavior, exact embedded asset bytes, all 35 caption pairs and 30 unique publication keywords.

Before → after: headline 58 → 72px on desktop; 20 → 5 font sizes; 121 thin rules → no thin-rule findings; 112 text blocks under 13px → no small-text findings; 0 → 4 playable character references. No new photograph, video or invented content was added. The existing storyboard and two covers retain their original bytes; the source font license is in the episode assets folder and the font credit is in the footer. The page has no external runtime resources.

ROUND 1 — latest-rules audit, 2026-11-02
Seen in one second: a complete illustrated English lesson with a clear title and direct reading action.
Idea (one sentence): the episode’s activity form becomes a complete reading and voice-reference sheet.
Live thing: four offline character references with transcript disclosures and exclusive native audio playback.
Layout words by section: hero=invitation sheet / narration=paired columns / story=large panels with captions / words=printed menu / cast=audio roster / publishing=labelled copy and two covers / footer=back of sheet
Scores: design 7.8 · usability 8.2 · creativity 7.0 · content 9.0 → overall 7.9
Caps applied: creativity capped at 7 for the familiar printed-sheet approach; no FAIL cap.
Top three problems (most visible first), each with the screenshot it shows in and the fix:
1. mobile-page-01.jpg: the full episode requires a long scroll; section anchors and scene contents provide navigation. All required material remains complete.
2. desktop-fold.jpg: the first illustration continues below the first fold, deliberately signaling that the sheet continues. The reading action remains visible.
3. tablet-page-02.jpg: captions use a narrower column beside the pictures at tablet width; all text fits and phones use a single full-width column.

Current audit: final HTML 22 title units, 167 description units, 198 units including topics; 5 unique topics and 30 unique keywords. Four voices played from the actual standalone file with browser networking disabled, both PNG downloads matched originals, 13 disclosures opened and closed, 375/390/768/1440 widths had no overflow, and disabled-script content remained complete. Inspector: 0 FAIL and 3 justified WARN. All listed screenshots were opened. No HTML changes were needed. Full current-rule evidence is in production/book-01/ep-002/checks/latest-rules-verification.json; previous hashes refer to earlier publishing copy.
