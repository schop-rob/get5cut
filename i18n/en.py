# English text for get5cut.com.
# English is the source: write it in ASD-STE100 (.claude/skills/ste100-writing).
# Translations follow the English meaning, with the same short, plain sentences.
# HOME fills the homepage; PAGES fills each inner page (a missing page falls back to English).

HOME = {'dir': '.',
 'lang_code': 'en',
 'title': '5cut – Record & Trim Lectures, Export Study Notes | iOS App',
 'description': 'Record lectures in any language on your iPhone. 5cut removes silence, transcribes and live-translates in 30+ languages, '
                'and exports clean study notes to Anki, Notion, and Obsidian. Private, on-device.',
 'og_title': '5cut – Record & Trim Lectures, Export Study Notes',
 'og_description': 'Record lectures. Trim silence. Translate live. Get a clean transcript and study notes. Private on iPhone.',
 'brand': '5cut',
 'brand_suffix': ' — AI Lecture Recorder & Silence Trimmer',
 'tagline': 'Keep up with lectures — in your language, at your pace.',
 'subhead_features': 'Record lectures, trim silence automatically, translate live in 30+ languages, and export study notes on-device.',
 'proof1': 'No 5cut server',
 'proof2': '5 exports/month free',
 'proof3': 'No account required',
 'stat1_value': '5 free exports',
 'stat1_label': 'every month',
 'cta_pill1': '5 free exports a month',
 'cta_pill2': '5 Free Exports/Mo',
 'cta_pill3': 'No Account Required',
 'cta_subtext': 'Free download · 5 exports/month free · No account',
 'creator_promise': 'I built 5cut because re-listening to long, pause-filled lectures in a foreign language was eating up my study time. '
                    'On-device translation and silence-trimming changed how I learn, and everything stays on the phone — my coursework '
                    'never leaves it.',
 'creator_signature': 'Creator of 5cut',
 'feat1_title': 'In-App Recorder & Bookmarks',
 'feat1_desc': 'Record lectures, meetings, and interviews directly in the app. Add chapter bookmarks while recording so important moments '
               'are easier to find later.',
 'feat2_title': 'Smart Silence Removal',
 'feat2_desc': 'Automatically detect and cut dead air from lectures and podcasts. Use Smart Mode presets (Gentle, Moderate, Aggressive) or '
               'customize thresholds manually.',
 'feat3_title': 'On-Device Translation & AI summaries',
 'feat3_desc': 'Follow lectures in your native tongue with live translation. Premium users on iOS 26+ can generate AI summaries, key '
               'points, and study questions using on-device models after the required model and language downloads.',
 'feat4_title': 'Export to Notion, Anki & Obsidian',
 'feat4_desc': 'Export your trimmed transcripts with speaker labels directly to your favorite study tools, including Obsidian and '
               'auto-generated Anki study cards.',
 'feat5_title': 'Multi-Speaker Identification (Premium)',
 'feat5_desc': 'Automatically identify up to 4 speakers in a single recording with color-coded, renamable labels — perfect for group '
               'discussions and seminars.',
 'how_it_works': 'How it works',
 'step1': '<strong>Record or Import</strong> any audio or video directly on your iPhone',
 'step2': '<strong>Auto-detect silence</strong> — see speech in green and gaps in red',
 'step3': '<strong>Translate & summarize</strong> on-device using local AI models (AI summaries require Premium and iOS 26+)',
 'step4': '<strong>Export to study tools</strong> — send clean files to Anki, Notion, or Obsidian',
 'privacy_title': 'No 5cut Server. No Cloud Copy.',
 'privacy_desc': 'Your recordings never leave your device. Every transcript is generated on your iPhone — there is no 5cut server, no '
                 'cloud processing, and no third-party transcription service. No account, no analytics, no ads.',
 'perfect_for': 'Perfect for',
 'perfect_for_desc1': 'International students attending lectures in a second language, study abroad participants, and expats watching '
                      'local media. Also perfect for professionals who want to skip awkward pauses in Zoom recordings or speed up '
                      'podcasts.',
 'perfect_for_desc2': 'Need live translations? 5cut transcribes and translates lectures in 30+ languages, with downloaded on-device '
                      'engines available for offline use.',
 'faq': 'Frequently asked questions',
 'faq_items': [{'q': 'How does silence detection work?',
                'a': '5cut analyzes the audio waveform of your video on-device. Segments below the silence threshold are color-coded red. '
                     'You can drag a slider to adjust what counts as "silence," or use one of three Smart Mode presets.'},
               {'q': 'Can I add subtitles and translations to lectures?',
                'a': 'Yes. 5cut includes transcription and live translation supporting over 30 languages. You can burn subtitles into the '
                     'video or export an SRT file. Offline availability depends on the selected engine, language, and required model '
                     'download.'},
               {'q': 'Does it work with Zoom and online course recordings?',
                'a': 'Yes. Import any MP4, MOV, or HEVC video. 5cut works with Zoom recordings, Microsoft Teams meetings, screen '
                     'recordings, and any video file with an audio track.'},
               {'q': 'Can I process a whole semester of lectures at once?',
                'a': 'Yes. You can queue up multiple recordings and process them with individual or shared settings.'},
               {'q': 'Is my data private?',
                'a': 'Your recordings never leave your device. 5cut has no server and no account system, so there is nothing for us to '
                     'see, hear, or store, and no third party receives your audio either. Every transcription engine runs on the device; '
                     'models download once, then work offline.'},
               {'q': 'Is there a premium plan?',
                'a': 'Yes. Recording, silence removal, and transcript previews (up to 5 minutes) are free. You can upgrade to 5cut Premium '
                     'for unlimited exports, speaker identification, full-length transcripts, and AI summaries on iOS 26+. Premium is a '
                     'monthly subscription or a one-time lifetime purchase — prices are shown in the App Store and adjusted for your '
                     'region.'},
               {'q': 'What languages is the app available in?',
                'a': 'The app interface is available in English, German, Spanish, French, Italian, Japanese, Korean, Portuguese (Brazil), '
                     'Vietnamese, and Simplified Chinese.'}],
 'footer_use_cases': 'Use Cases',
 'footer_alternatives': 'Alternatives',
 'footer_legal': 'Legal & Support',
 'footer_study_fields': 'By Field of Study',
 'hero_note_desc': 'Record, trim, transcribe, translate, and export — entirely on your iPhone. Your recordings never leave it.'}

PAGES = {'speed-up-zoom-recordings': {'title': 'Speed Up Zoom Recordings – Remove Dead Air | 5cut',
                              'desc': 'Remove awkward pauses and dead air from Zoom, Teams, and online course recordings. On-device '
                                      'processing for iOS.',
                              'h1': 'Speed Up Zoom Recordings',
                              'tagline': 'Cut out the dead air automatically.',
                              'intro': '<p>Long Zoom lectures often include dead air while the professor fixes a microphone or waits for '
                                       'students to answer. 5cut detects those quiet stretches so you can review the recording without '
                                       'speeding up speech.</p>'},
 'study-abroad': {'title': 'Essential Apps for Studying Abroad – Tools for Foreign Language Lectures | 5cut',
                  'desc': 'Essential iPhone app for international students. Remove silence from foreign language lectures, add subtitles '
                          'in 30+ languages, identify speakers.',
                  'h1': 'Essential Tool for Studying Abroad',
                  'tagline': 'Record, translate, and conquer your courses.',
                  'intro': '<p>Studying abroad is challenging, especially when lectures are in a foreign language. Record your lectures '
                           'with 5cut, generate transcripts in over 30 languages, and, with Premium on iOS 26+, create AI study notes on '
                           'your iPhone.</p>'},
 'transcribe-lectures': {'title': 'Transcribe Lectures on iPhone – Subtitles in 30+ Languages | 5cut',
                         'desc': 'Generate subtitles for lecture recordings in over 30 languages. On-device transcription — no uploads, no '
                                 'cloud.',
                         'h1': 'Transcribe Lectures on iPhone',
                         'tagline': 'On-device, private, and fast.',
                         'intro': '<p>Stop manually typing out lecture notes. With 5cut, you can generate lecture transcripts on your '
                                  'iPhone and, with Premium on iOS 26+, create AI summaries. Your recordings never leave your device; 5cut '
                                  'has no server of your recordings; downloaded on-device engines are available for offline '
                                  'transcription.</p>'},
 'remove-silence-from-lectures': {'title': 'Remove Silence from Lecture Recordings – 5cut for iOS',
                                  'desc': 'Automatically detect and remove silence and dead air from recorded university lectures while '
                                          'keeping speech at natural speed.',
                                  'h1': 'Remove Silence from Lectures',
                                  'tagline': 'Review the lecture, not the dead air.',
                                  'intro': '<p>Recorded lectures can contain silent gaps while professors pause, write on the board, or '
                                           'wait for responses. 5cut detects those quiet stretches and lets you remove them while keeping '
                                           'speech at natural speed.</p>'},
 'podcast-silence-remover': {'title': 'Remove Silence from Podcasts on iPhone – Edit Podcast Audio | 5cut',
                             'desc': 'Tighten podcast episodes by removing dead air and awkward pauses. On-device processing on iPhone.',
                             'h1': 'Remove Silence from Podcasts',
                             'tagline': 'Tighten your podcast episodes effortlessly.',
                             'intro': "<p>Dead air kills pacing. Whether you're editing your own podcast or listening to one, those 2–3 "
                                      'second pauses between sentences add up fast. A 45-minute episode might have 8–10 minutes of '
                                      'silence. 5cut removes it in one tap directly on your iPhone.</p>'},
 'use-cases/remove-silence-from-zoom': {'title': 'How to Remove Silence from Zoom Recordings Automatically | 5cut',
                                        'desc': 'Learn how to instantly cut silence from long Zoom meeting recordings using 5cut on your '
                                                'iPhone and iPad.',
                                        'h1': 'Remove Silence from Zoom Meetings',
                                        'tagline': 'Get straight to the point.',
                                        'intro': '<p>Zoom recordings are full of awkward pauses, waiting for attendees to join, and '
                                                 "microphone troubleshooting. 5cut's intelligent audio analysis instantly trims away the "
                                                 'silent gaps in your imported Zoom MP4 or MOV files, giving you a dense, actionable '
                                                 'recording.</p>'},
 'use-cases/remove-silence-from-obs': {'title': 'Remove Silence from OBS Streams & Recordings | 5cut',
                                       'desc': 'Edit your OBS Studio VODs faster. Automatically cut silence from your recordings on your '
                                               'iPhone.',
                                       'h1': 'Remove Silence from OBS VODs',
                                       'tagline': 'Speed up your editing workflow.',
                                       'intro': '<p>Streaming VODs recorded via OBS Studio often contain long stretches of silence during '
                                                'breaks or matchmaking queues. Transfer your OBS files to your iPhone and let 5cut '
                                                'automatically trim the dead air so your YouTube highlights are ready to post faster.</p>'},
 'alternatives/timebolt-alternative': {'title': 'The Best Free Mobile TimeBolt Alternative for iOS | 5cut',
                                       'desc': 'Looking for a mobile TimeBolt alternative? 5cut offers free automatic silence removal and '
                                               'on-device transcription previews on iPhone, with speaker identification in Premium.',
                                       'h1': 'The Best Mobile TimeBolt Alternative',
                                       'tagline': 'Remove silence automatically from your iPhone or iPad.',
                                       'intro': '<p>TimeBolt is a desktop tool for PC and Mac users. 5cut is a mobile alternative for '
                                                'editing video directly on an iPhone. Silence removal runs on-device, and downloaded '
                                                'transcription engines are available for offline use. Your recordings never leave your '
                                                'device; 5cut has no server of your recordings.</p>'},
 'free-jumpcut-app': {'title': 'Free Jumpcut App for iPhone – Auto Silence Remover | 5cut',
                      'desc': 'Download a jumpcut app for iOS. Automatically remove silence from videos, add subtitles, and export '
                              'directly from your iPhone.',
                      'h1': 'Free Jumpcut App for iPhone',
                      'tagline': 'Automatically cut silence on iPhone.',
                      'intro': '<p>Looking for a fast, automated jumpcutter? 5cut trims dead air from talking-head videos and vlogs, '
                               'creates subtitles, and keeps processing on your iPhone.</p>'},
 'smartphone-video-editor': {'title': 'Smartphone Video Editor for Talking Heads – AI Editor | 5cut',
                             'desc': 'Edit videos directly on your smartphone. The best iPhone editor for talking heads, vlogs, and '
                                     'TikToks. Record, cut silence, and export on-device.',
                             'h1': 'Smartphone Video Editor for Talking Heads',
                             'tagline': 'Record and edit directly on your iPhone.',
                             'intro': '<p>Transferring large video files to your PC to edit is slow and annoying. 5cut is the ultimate '
                                      'smartphone video editor for creators. Record your talking head or vlog, let AI automatically remove '
                                      'the silence, add subtitles, and export directly from your phone in seconds.</p>'},
 'best-app-for-law-school-recordings': {'desc': 'Condense law school lectures on iPhone. Remove silence, transcribe case discussions, and '
                                                'export notes. Your recordings never leave your device.',
                                        'h1': 'Best App for Law School Recordings',
                                        'intro': '<p>Law school lectures can contain long pauses while a professor reads from the '
                                                 'casebook, waits between Socratic questions, or gives students time to find a page.</p>\n'
                                                 '<p>5cut detects those quiet stretches on your iPhone. Then transcribe the recording, '
                                                 'identify speakers, and export notes.</p>\n'
                                                 '<h2>Why law students use 5cut</h2>\n'
                                                 '<ul>\n'
                                                 '    <li><strong>Trim detected silence</strong> — speech stays at natural speed</li>\n'
                                                 '    <li><strong>Socratic method tracking</strong> — speaker identification separates the '
                                                 'professor from student responses</li>\n'
                                                 '    <li><strong>Case name search</strong> — transcribe the lecture, then search the text '
                                                 'for specific case citations</li>\n'
                                                 '    <li><strong>On-device privacy</strong> — hypothetical client scenarios and case '
                                                 'discussions stay on your phone</li>\n'
                                                 "    <li><strong>Exam prep</strong> — batch-process a semester's lectures before "
                                                 'finals</li>\n'
                                                 '</ul>\n'
                                                 '<h2>The Socratic method problem</h2>\n'
                                                 '<p>In law school, the most important content is often buried in dialogue. The professor '
                                                 "asks a question, waits 10 seconds, a student responds, there's a 5-second pause, then "
                                                 'the professor unpacks the legal principle.</p>\n'
                                                 "<p>5cut's adjustable threshold lets you keep brief dramatic pauses while cutting the "
                                                 'longer dead air. You control exactly how aggressive the trimming is.</p>\n'
                                                 '<h2>The law school workflow</h2>\n'
                                                 '<ol>\n'
                                                 "    <li><strong>Record in class</strong> — use 5cut's built-in recorder or import from "
                                                 'Voice Memos</li>\n'
                                                 '    <li><strong>Auto-trim silence</strong> — Smart Mode "Moderate" works well for '
                                                 'Socratic-style classes.</li>\n'
                                                 '    <li><strong>Transcribe</strong> — generate a full transcript with timestamps and '
                                                 'speaker labels.</li>\n'
                                                 '    <li><strong>Export</strong> — save trimmed audio for commute listening, or export '
                                                 'transcript to your outlining tool</li>\n'
                                                 '</ol>\n'
                                                 '<h2>Privacy and professional responsibility</h2>\n'
                                                 '<p>Law school classes discuss hypothetical client scenarios, real case facts, and legal '
                                                 'strategies. 5cut processes everything locally on your iPhone. Your recordings never '
                                                 'leave your device; every transcription engine runs on the iPhone itself.</p>\n'
                                                 '<h2>Free to start</h2>\n'
                                                 '<p>5cut is free to download and includes in-app recording, silence removal, and '
                                                 'transcription previews (first 5 minutes). Upgrade to Premium to unlock unlimited '
                                                 'exports, full-length transcripts, speaker identification, and batch processing.</p>',
                                        'tagline': 'Remove detected pauses from law-school recordings.',
                                        'title': 'Best App for Law School Recordings – Trim & Transcribe Lectures | 5cut'},
 'best-app-for-medical-school-lectures': {'desc': 'Record and condense medical school lectures on iPhone. Remove silence, transcribe in '
                                                  '30+ languages, export to Anki. On-device processing keeps patient case discussions '
                                                  'private.',
                                          'h1': 'Best App for Medical School Lectures',
                                          'intro': '<p>Medical lectures can contain long stretches of dead air between explanations, '
                                                   'demonstrations, and questions.</p>\n'
                                                   '<p>5cut removes silence from lecture recordings automatically on your iPhone. A 2-hour '
                                                   'anatomy lecture becomes 80 minutes of actual content. Then you can transcribe it, '
                                                   'export notes to Anki, and review faster.</p>\n'
                                                   '<h2>Why med students use 5cut</h2>\n'
                                                   '<ul>\n'
                                                   '    <li><strong>Review less dead air</strong> — remove detected silence before '
                                                   'studying</li>\n'
                                                   '    <li><strong>Nothing you record leaves your device</strong> — Your recordings never '
                                                   'leave your device; every engine runs on the iPhone itself</li>\n'
                                                   '    <li><strong>Transcribe in 30+ languages</strong> — international med students can '
                                                   'generate subtitles in their native language</li>\n'
                                                   '    <li><strong>Export to Anki</strong> — turn transcribed lecture segments into Q&A '
                                                   'study cards</li>\n'
                                                   '    <li><strong>Batch processing</strong> — drop a week of recordings in and process '
                                                   'them in one batch (keep 5cut open while it runs)</li>\n'
                                                   '</ul>\n'
                                                   '<h2>Privacy matters in medicine</h2>\n'
                                                   '<p>Medical lectures often reference patient cases, clinical scenarios, and sensitive '
                                                   'health information. Cloud-based transcription means uploading those recordings to '
                                                   "someone else's server. 5cut processes everything on your iPhone — no upload and no "
                                                   'third-party access, and after a one-time model download it works offline. That matters '
                                                   'when lectures discuss patient cases.</p>\n'
                                                   '<h2>The med school workflow</h2>\n'
                                                   '<ol>\n'
                                                   "    <li><strong>Record</strong> — use 5cut's built-in recorder during the lecture, or "
                                                   'import a recording</li>\n'
                                                   '    <li><strong>Trim silence</strong> — 5cut analyzes the audio and removes dead air '
                                                   'automatically.</li>\n'
                                                   '    <li><strong>Transcribe</strong> — generate word-level subtitles. Speaker '
                                                   'identification separates the professor from student Q&A</li>\n'
                                                   '    <li><strong>Export</strong> — save the condensed video, export subtitles, or send '
                                                   'transcript segments to Anki for spaced repetition</li>\n'
                                                   '</ol>\n'
                                                   '<h2>Anatomy, pharmacology, pathology</h2>\n'
                                                   '<h3>Anatomy lectures</h3>\n'
                                                   '<p>Long pauses while the professor points at dissection specimens or rotates 3D '
                                                   'models. These silences are prime candidates for removal.</p>\n'
                                                   '<h3>Pharmacology</h3>\n'
                                                   '<p>Fast-paced drug mechanism explanations with occasional pauses for slide '
                                                   "transitions. 5cut's adjustable threshold lets you keep brief natural pauses.</p>\n"
                                                   '<h3>Clinical case discussions</h3>\n'
                                                   '<p>Multiple speakers — attending, residents, students. Speaker identification '
                                                   'color-codes up to 4 speakers.</p>\n'
                                                   '<h2>Free to start</h2>\n'
                                                   '<p>5cut is free to download and includes in-app recording, silence removal, and '
                                                   'transcription previews (first 5 minutes). Upgrade to Premium to unlock unlimited '
                                                   'exports, full-length transcripts, speaker identification, and batch processing.</p>',
                                          'tagline': 'Remove dead air before reviewing an anatomy lecture.',
                                          'title': 'Best App for Medical School Lectures – Record, Trim & Transcribe | 5cut'},
 'offline-lecture-transcription-iphone': {'desc': 'Transcribe lecture recordings offline on iPhone. No cloud, no upload — works offline '
                                                  'after a one-time model download. On-device AI in 30+ languages. Speaker identification. '
                                                  'Export as SRT or text. Free iOS app.',
                                          'h1': 'Offline Lecture Transcription on iPhone',
                                          'intro': '<p>Most transcription apps require internet. You upload your lecture to a server, wait '
                                                   'for processing, and hope the cloud service handles your data responsibly. With 5cut, '
                                                   'you can select a downloaded on-device engine for offline transcription. Availability '
                                                   'depends on the engine, language, device, and initial model download.</p>\n'
                                                   '<h2>How offline transcription works</h2>\n'
                                                   "<p>5cut uses on-device AI models that run directly on your iPhone's Neural Engine. The "
                                                   'first time you select a language, the model downloads (typically 40-600 MB depending '
                                                   'on the engine). After that, transcription works in airplane mode, on the subway, in a '
                                                   'lecture hall with terrible WiFi — anywhere.</p>\n'
                                                   '<h2>Six transcription engines</h2>\n'
                                                   '<p>5cut offers multiple AI engines so you can choose the right balance of speed, '
                                                   'accuracy, and model size:</p>\n'
                                                   '<table class="engine-table">\n'
                                                   '    <tr><th>Engine</th><th>Languages</th><th>Model size</th><th>Best for</th></tr>\n'
                                                   '    <tr><td>Apple SpeechAnalyzer</td><td>40+</td><td>Built-in</td><td>Quick '
                                                   'transcription, broadest language support</td></tr>\n'
                                                   '    <tr><td>WhisperKit</td><td>30+</td><td>39 MB – 1.5 GB</td><td>High accuracy, '
                                                   'word-level timestamps — imported files only, not available in the live '
                                                   'recorder</td></tr>\n'
                                                   '    <tr><td>Parakeet Ultra</td><td>25 European</td><td>~600 MB</td><td>European '
                                                   'languages, auto-detection</td></tr>\n'
                                                   '    <tr><td>Parakeet Lite</td><td>English</td><td>~220 MB</td><td>Faster and lighter — '
                                                   'good for older iPhones</td></tr>\n'
                                                   '    <tr><td>Moonshine Tiny Streaming</td><td>English</td><td>~49 '
                                                   'MB</td><td>Low-latency streaming transcription</td></tr>\n'
                                                   '    <tr><td>Phonon-2</td><td>English</td><td>~360 MB</td><td>Compact English model '
                                                   'tuned for iPhone, requires iOS 18+</td></tr>\n'
                                                   '</table>\n'
                                                   "<p>WhisperKit is available for imported files only — it isn't offered in the live "
                                                   'recorder.</p>\n'
                                                   '<h2>Why offline matters</h2>\n'
                                                   '<ul>\n'
                                                   '    <li><strong>Nothing you record leaves your device</strong> — Your recordings never '
                                                   'leave your device; every engine runs on the iPhone itself</li>\n'
                                                   '    <li><strong>No data caps</strong> — transcribe hours of recordings without eating '
                                                   'into your mobile data plan</li>\n'
                                                   '    <li><strong>Works everywhere</strong> — campus basements, trains, planes, '
                                                   'libraries with blocked WiFi</li>\n'
                                                   '    <li><strong>No per-minute costs</strong> — cloud transcription services charge per '
                                                   'minute. On-device is free after the model download</li>\n'
                                                   '    <li><strong>Speed</strong> — no upload/download wait. Transcription starts '
                                                   'immediately</li>\n'
                                                   '</ul>\n'
                                                   '<h2>Supported languages</h2>\n'
                                                   '<p>Between all six engines, 5cut supports transcription in over 40 languages. The '
                                                   'exact list depends on which engine you choose and the language models available for '
                                                   'your device.</p>\n'
                                                   '<h2>Beyond transcription: remove silence too</h2>\n'
                                                   '<p>5cut is primarily a silence removal tool. The typical workflow is:</p>\n'
                                                   '<ol>\n'
                                                   '    <li>Import or record a lecture</li>\n'
                                                   '    <li>Remove detected silence automatically</li>\n'
                                                   '    <li>Transcribe the condensed version offline</li>\n'
                                                   '    <li>Export: video with burned-in subtitles, SRT file, or plain text '
                                                   'transcript</li>\n'
                                                   '</ol>\n'
                                                   "<p>Silence removal also works fully offline — it's a waveform analysis that never "
                                                   'needs internet.</p>\n'
                                                   '<h2>Speaker identification</h2>\n'
                                                   '<p>5cut can identify up to 4 speakers in a recording and color-code them in the '
                                                   'transcript. This works offline too. Useful for lectures with Q&A, seminars, or group '
                                                   'presentations.</p>\n'
                                                   '<h2>Free to start</h2>\n'
                                                   '<p>5cut is free to download and includes in-app recording, silence removal, and '
                                                   'transcription previews (first 5 minutes). Upgrade to Premium to unlock unlimited '
                                                   'exports, full-length transcripts, speaker identification, and batch processing.</p>',
                                          'tagline': 'Transcribe offline on iPhone. No Internet Required.',
                                          'title': 'Offline Lecture Transcription on iPhone – No Internet Required | 5cut'},
 'offline-meeting-notes-iphone': {'desc': 'Generate meeting notes and transcripts offline on iPhone. Works offline after a one-time model '
                                          'download — no cloud, no uploads. Record meetings, identify speakers, and get a full transcript '
                                          '— all on-device.',
                                  'h1': 'Offline Meeting Notes on iPhone',
                                  'intro': "<p>You need meeting notes, but your company's security policy won't let you use Otter, "
                                           "Fireflies, or any cloud transcription service. Or you're in a conference room with no WiFi. Or "
                                           "you simply don't trust a third party with your meeting content.</p>\n"
                                           '<p>5cut generates meeting transcripts entirely offline on your iPhone. Record, transcribe, '
                                           'identify speakers — no internet connection required after the initial model download.</p>\n'
                                           '<h2>How offline meeting notes work</h2>\n'
                                           '<ol>\n'
                                           '    <li><strong>Download a language model once</strong> — this is the only step that needs '
                                           'internet (40-700 MB)</li>\n'
                                           '    <li><strong>Record the meeting</strong> — tap record. Works in airplane mode, underground, '
                                           'anywhere</li>\n'
                                           "    <li><strong>Transcribe on-device</strong> — the AI runs on your iPhone's Neural "
                                           'Engine.</li>\n'
                                           '    <li><strong>Speaker separation</strong> — up to 4 speakers are automatically identified '
                                           'and labeled.</li>\n'
                                           '    <li><strong>Export</strong> — copy the transcript, share as text, or export with '
                                           'timestamps</li>\n'
                                           '</ol>\n'
                                           '<h2>Why go offline for meeting notes</h2>\n'
                                           '<h3>Corporate security policies</h3>\n'
                                           '<p>Many companies prohibit uploading internal discussions to third-party services. Your '
                                           'recordings never leave your device, and every transcription engine runs on the iPhone itself, '
                                           "which can reduce third-party exposure. Always verify your organization's own recording and "
                                           'security requirements.</p>\n'
                                           '<h3>Regulated industries</h3>\n'
                                           '<p>Finance, healthcare, legal, defense — these sectors have strict data handling requirements. '
                                           'On-device processing means no vendor risk assessment.</p>\n'
                                           '<h3>Unreliable connectivity</h3>\n'
                                           '<p>Conference rooms in basements, meetings during travel, offsite retreats with spotty WiFi. '
                                           'Offline transcription just works regardless of your connection.</p>\n'
                                           '<h2>What you get</h2>\n'
                                           '<ul>\n'
                                           '    <li><strong>Full transcript</strong> with timestamps</li>\n'
                                           '    <li><strong>Speaker labels</strong> — color-coded, renameable</li>\n'
                                           '    <li><strong>Silence removal</strong> — strip the "ums" and long pauses</li>\n'
                                           '    <li><strong>Multiple export formats</strong> — plain text, SRT subtitles, or video</li>\n'
                                           "    <li><strong>30+ languages</strong> — multilingual teams can transcribe in the meeting's "
                                           'language</li>\n'
                                           '</ul>\n'
                                           '<h2>Free to start</h2>\n'
                                           '<p>5cut is free to download and includes in-app recording, silence removal, and transcription '
                                           'previews (first 5 minutes). Upgrade to Premium to unlock unlimited exports, full-length '
                                           'transcripts, speaker identification, and batch processing.</p>',
                                  'tagline': 'Transcribe meetings offline. Speaker identification included.',
                                  'title': 'Offline Meeting Notes on iPhone – Transcribe Without Internet | 5cut'},
 'record-meetings-privately-iphone': {'desc': 'Record meetings on iPhone. Your recordings never leave your device; every transcription '
                                              'engine runs on the iPhone itself.',
                                      'h1': 'Record Meetings Privately on iPhone',
                                      'intro': '<p>Your meeting contains proprietary strategy, client names, revenue numbers, or personnel '
                                               'decisions. Cloud-based meeting recorders like Otter, Fireflies, or Fathom upload '
                                               "everything to their servers. Their AI processes your words on someone else's "
                                               'infrastructure.</p>\n'
                                               '<p>Your meetings never leave your device. Every transcription engine runs on the iPhone '
                                               'itself, offline once you have the model for your language and device. Always follow your '
                                               "organization's recording and data-handling rules.</p>\n"
                                               '<h2>The compliance problem with cloud recorders</h2>\n'
                                               "<p>Every time you use a cloud transcription service, you're creating a data processing "
                                               'relationship. That means:</p>\n'
                                               '<ul>\n'
                                               '    <li>A third party now holds recordings of confidential discussions</li>\n'
                                               '    <li>You need a Data Processing Agreement (DPA) under GDPR</li>\n'
                                               '    <li>SOC 2 auditors will ask about it</li>\n'
                                               '    <li>If the service is breached, your meeting content is exposed</li>\n'
                                               '    <li>Client NDAs may prohibit sharing recordings with third parties</li>\n'
                                               '</ul>\n'
                                               '<p>On-device processing can reduce third-party exposure, but you must still follow your '
                                               "organization's recording and data-handling rules.</p>\n"
                                               '<h2>Who needs private meeting recording</h2>\n'
                                               '<h3>Legal professionals</h3>\n'
                                               '<p>Client meetings, case strategy discussions, settlement negotiations. Attorney-client '
                                               "privilege doesn't mix well with third-party cloud processing.</p>\n"
                                               '<h3>Healthcare</h3>\n'
                                               '<p>Clinical team meetings and patient case reviews are sensitive. Confirm authorization '
                                               'and applicable healthcare rules before recording.</p>\n'
                                               '<h3>Finance and banking</h3>\n'
                                               '<p>Investment discussions, client advisory meetings, compliance reviews. Material '
                                               "non-public information shouldn't exist on a transcription startup's servers.</p>\n"
                                               '<h3>HR and people operations</h3>\n'
                                               '<p>Performance reviews, disciplinary meetings, compensation discussions.</p>\n'
                                               '<h2>The 5cut workflow for meetings</h2>\n'
                                               '<ol>\n'
                                               '    <li><strong>Open the recorder</strong> — tap record when the meeting starts.</li>\n'
                                               '    <li><strong>Transcribe after recording</strong> — choose a supported downloaded '
                                               'on-device engine</li>\n'
                                               '    <li><strong>Speaker identification</strong> — up to 4 speakers are automatically '
                                               'identified</li>\n'
                                               '    <li><strong>Trim silence</strong> — remove the gaps between agenda items</li>\n'
                                               '    <li><strong>Export</strong> — transcript as text or SRT. Everything stays in your '
                                               'Files app</li>\n'
                                               '</ol>\n'
                                               '<h2>Compared to alternatives</h2>\n'
                                               '<p>Unlike cloud-first meeting tools, Your recordings never leave your device. Downloaded '
                                               'on-device engines can transcribe offline when supported for the selected language and '
                                               'device. 5cut also identifies speakers and removes silence.</p>\n'
                                               '<h2>Free to start</h2>\n'
                                               '<p>5cut is free to download and includes in-app recording, silence removal, and '
                                               'transcription previews (first 5 minutes). Upgrade to Premium to unlock unlimited exports, '
                                               'full-length transcripts, speaker identification, and batch processing.</p>',
                                      'tagline': 'Record and transcribe meetings on-device. No cloud upload.',
                                      'title': 'Record Meetings Privately on iPhone – No 5cut Cloud Copy | 5cut'}}
