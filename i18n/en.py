# English text for get5cut.com.
# English is the source: write it in ASD-STE100 (.claude/skills/asd-ste100-skill).
# Translations follow the English meaning, with the same short, plain sentences.
# HOME fills the homepage; PAGES fills each inner page (a missing page falls back to English).

HOME = {'dir': '.',
 'lang_code': 'en',
 'title': '5cut – Record & Trim Lectures, Export Study Notes | iOS App',
 'description': 'Record lectures on your iPhone. 5cut cuts the silence, transcribes in 30+ languages, translates live and exports study notes to '
                'Anki, Notion and Obsidian.',
 'og_title': '5cut – Record & Trim Lectures, Export Study Notes',
 'og_description': 'Record lectures. Cut the silence. Translate live. Get a transcript and study notes. Your recordings never leave your '
                   'iPhone.',
 'brand': '5cut',
 'brand_suffix': ' — AI Lecture Recorder & Silence Trimmer',
 'tagline': 'Follow every lecture in your language, at your speed.',
 'subhead_features': 'Record lectures, cut the silence, transcribe in 30+ languages, translate live and export study notes. All of it '
                     'happens on your iPhone.',
 'proof1': 'No 5cut server',
 'proof2': 'Record in 5cut: full transcript free',
 'proof3': 'No account',
 'stat1_value': '5 free exports',
 'stat1_label': 'every month',
 'cta_pill1': '5 free exports each month',
 'cta_pill2': '5 Free Exports/Month',
 'cta_pill3': 'No Account',
 'cta_subtext': 'Free download · Premium: monthly or one-time · No account',
 'creator_promise': 'I made 5cut because I listened to long lectures in a foreign language again and again. The pauses took a lot of my '
                    'study time. Translation and silence removal on the device changed how I learn. My recordings never leave my iPhone.',
 'creator_signature': 'Creator of 5cut',
 'feat1_title': 'Recorder with Chapter Bookmarks',
 'feat1_desc': 'Record lectures, meetings and interviews in the app. Tap to add a chapter bookmark while you record. Later, the bookmark '
               'takes you to that moment.',
 'feat2_title': 'Smart Silence Removal',
 'feat2_desc': '5cut finds the silence in lectures and podcasts and cuts it. Choose Gentle, Moderate or Aggressive, or set the threshold '
               'yourself.',
 'feat3_title': 'On-Device Translation & AI Summaries',
 'feat3_desc': 'Read the lecture in your language with live translation. With Premium, 5cut also makes AI summaries, key points and '
               'flashcards on your iPhone. For this, it uses Apple Intelligence or an AI model that you download one time.',
 'feat4_title': 'Export to Notion, Anki & Obsidian',
 'feat4_desc': 'Send the transcript and your notes to Apple Notes, Markdown, Anki, Notion or Obsidian. 5cut also makes Anki study cards '
               'from the transcript.',
 'feat5_title': 'Speaker Identification (Premium)',
 'feat5_desc': '5cut finds up to 4 speakers in one recording. Each speaker gets a color and a name that you can change. This helps with '
               'seminars and group discussions.',
 'how_it_works': 'How it works',
 'step1': '<strong>Record or import</strong> audio or video on your iPhone.',
 'step2': '<strong>Cut the silence</strong>. 5cut shows speech in green and silence in red.',
 'step3': '<strong>Transcribe and translate</strong> on your iPhone. With Premium, 5cut also makes AI summaries.',
 'step4': '<strong>Export to your study tools</strong>: Anki, Notion, Obsidian or Apple Notes.',
 'privacy_title': 'Your recordings never leave your iPhone',
 'privacy_desc': '5cut cuts, transcribes and makes notes on the device. There is no 5cut server. Test it yourself: download a '
                 'transcription model one time, then turn on Airplane Mode. 5cut works the same. The app has no account, no analytics '
                 'and no ads.',
 'perfect_for': 'Made for',
 'perfect_for_desc1': '5cut is for international students who attend lectures in a second language, and for students who study abroad. '
                      'It also helps professionals who want shorter Zoom recordings and podcasts without long pauses.',
 'perfect_for_desc2': 'Do you need live translation? 5cut transcribes lectures in more than 30 languages and translates them live. Each '
                      'engine downloads its model one time and then works offline.',
 'faq': 'Frequently asked questions',
 'faq_items': [{'q': 'How does silence detection work?',
                'a': '5cut measures the loudness of each recording on your iPhone. It sets a threshold between the background noise and '
                     'the voice. A small voice detector in the app also marks where someone speaks. 5cut shows the silence in red. You '
                     'can move the threshold or choose Gentle, Moderate or Aggressive.'},
               {'q': 'Does 5cut cut background noise?',
                'a': 'Yes, but only between the words. A small voice detector in the app marks where someone speaks. 5cut cuts the parts '
                     'where nobody speaks, also when they are loud, for example traffic or a train. 5cut does not filter the noise under '
                     'a voice. When someone speaks, the background noise stays. '
                     '<a href="/cut-background-noise-from-recordings/">Read more about noisy recordings</a>.'},
               {'q': 'Can I add subtitles and translations to lectures?',
                'a': 'Yes. 5cut transcribes in more than 30 languages and can translate the transcript. You can burn the subtitles into '
                     'the video or export an SRT file. The languages depend on the engine that you choose.'},
               {'q': 'Does it work with Zoom and online course recordings?',
                'a': 'Yes. Import an MP4, MOV or HEVC video. 5cut works with Zoom and Microsoft Teams recordings, screen recordings and '
                     'any video file with an audio track. You can also import audio files.'},
               {'q': 'Can I process a whole semester of lectures at once?',
                'a': 'Yes. Add many recordings to one batch, with the same settings for all or with settings for each video. 5cut '
                     'processes them one after the other. Keep 5cut open while the batch runs. In the free version, each export from a '
                     'batch counts toward the 5 free exports each month.'},
               {'q': 'Can I search my old lectures?',
                'a': 'Yes. In Recents, search finds your lectures by title. With Premium, search also finds words in every line of every '
                     'saved transcript. Tap a result, and 5cut opens the lecture at that moment.'},
               {'q': 'Is my data private?',
                'a': 'Your recordings never leave your iPhone. 5cut cuts, transcribes and makes notes on the device. There is no 5cut '
                     'server. Test it yourself: download a transcription model one time, then turn on Airplane Mode. 5cut works the '
                     'same.'},
               {'q': 'Can I check that my recordings stay on my iPhone?',
                'a': 'Yes. Download a transcription model one time. Turn on Airplane Mode. Then record and transcribe a lecture. 5cut '
                     'works the same, because it sends your recordings nowhere. There is no 5cut server that can receive them.'},
               {'q': 'Is there a premium plan?',
                'a': 'Yes. The free version includes the recorder, silence removal and 5 exports each month. Recordings that you make '
                     'in 5cut get a full transcript. Imported files get a transcript of the first 5 minutes. Premium adds unlimited '
                     'exports without a watermark, full transcripts of imported files, speaker identification, AI notes and flashcards, '
                     'and search in all transcripts. Premium is a monthly subscription or a one-time lifetime purchase, and the App '
                     'Store shows the price for your region.'},
               {'q': 'What languages is the app available in?',
                'a': 'The app interface is in English, German, Spanish, French, Italian, Japanese, Korean, Portuguese (Brazil), '
                     'Vietnamese and Simplified Chinese. Transcription works in more than 30 languages.'}],
 'footer_use_cases': 'Use Cases',
 'footer_alternatives': 'Alternatives',
 'footer_legal': 'Legal & Support',
 'footer_study_fields': 'By Field of Study',
 'hero_note_desc': 'Record, cut, transcribe, translate and export on your iPhone. Your recordings never leave it.',
 "footer_zoom": "Zoom Recordings",
 "footer_obs": "OBS & Twitch VODs",
 "footer_lectures": "University Lectures",
 "footer_podcasts": "Podcasts",
 "footer_jumpcut": "Jumpcut App",
 "footer_editor": "Smartphone Editor",
 "footer_timebolt": "TimeBolt Alternative",
 "footer_otter": "Otter.ai Alternative",
 "footer_medical": "Medical School Lectures",
 "footer_law": "Law School Recordings",
 "footer_support": "Support & Contact",
 "footer_privacy": "Privacy Policy",
 "footer_terms": "Terms of Service",
 "footer_noise": "Background Noise",
 "alt_icon": "5cut app icon",
 "alt_badge": "Download 5cut on the App Store",
 "alt_recorder": "5cut recorder screen",
 "alt_transcript": "5cut transcript screen",
 "alt_editor": "5cut silence cutting editor",
 "aria_screens": "5cut iPhone screenshots of the recorder, the editor and the transcript"
}

PAGES = {'speed-up-zoom-recordings': {'title': 'Speed Up Zoom Recordings – Cut Silence and Dead Air | 5cut',
                              'desc': 'Cut the silence and long pauses from Zoom, Teams and online course recordings on your iPhone. '
                                      'The speech stays at normal speed.',
                              'h1': 'Speed Up Zoom Recordings',
                              'tagline': 'Cut the silence, keep the speech.',
                              'intro': '<p>Long Zoom lectures have silent parts. The professor has a problem with the microphone, or '
                                       'waits for answers from students. 5cut finds these silent parts and cuts them. The speech stays at '
                                       'normal speed, so you review the lecture in less time.</p>'},
 'study-abroad': {'title': 'Study Abroad App for Foreign-Language Lectures | 5cut',
                  'desc': 'An iPhone app for international students. Record lectures in a foreign language, cut the silence, transcribe '
                          'in 30+ languages and translate live.',
                  'h1': 'Your Lecture App for Study Abroad',
                  'tagline': 'Record the lecture. Read it in your language.',
                  'intro': '<p>Lectures in a foreign language are hard to follow. Record each lecture with 5cut. 5cut transcribes it in '
                           'more than 30 languages and can translate it live. With Premium, 5cut also makes AI study notes on your '
                           'iPhone.</p>\n'
                           '<p>5cut also cuts the silence from each recording, so you review the lecture in less time. Your recordings '
                           'never leave your iPhone.</p>',
                  'faq': [{'q': 'Can 5cut translate a lecture while I listen?',
                           'a': 'Yes. Turn on live translation in the recorder. 5cut shows the translated text while it records. The '
                                'translation uses Apple Translation on your iPhone and needs iOS 18 or later.'},
                          {'q': 'Which languages can 5cut transcribe?',
                           'a': 'More than 30 languages. The list depends on the engine. Apple SpeechAnalyzer (iOS 26 or later) and '
                                'WhisperKit cover the most languages. Parakeet Ultra covers 25 European languages.'},
                          {'q': 'Can I follow a lecture without a recording?',
                           'a': 'Yes. On iOS 26 or later, Live Captions shows a live transcript and a translation. 5cut saves no audio, '
                                'and the captions disappear after about one minute. Live Captions is free.'},
                          {'q': 'Is 5cut free for students?',
                           'a': 'You can start for free. The free version includes the recorder, silence removal, full transcripts of '
                                'your own recordings and 5 exports each month. Premium adds more, for example full transcripts of '
                                'imported files and AI notes.'}]},
 'transcribe-lectures': {'title': 'Transcribe Lectures on iPhone – Subtitles, 30+ Languages | 5cut',
                         'desc': 'Transcribe lecture recordings on your iPhone in more than 30 languages and export subtitles as SRT. '
                                 'Every engine runs on the device.',
                         'h1': 'Transcribe Lectures on iPhone',
                         'tagline': 'Your lecture as text, made on your iPhone.',
                         'intro': '<p>Do not type your lecture notes by hand. 5cut makes a transcript of each lecture recording on your '
                                  'iPhone. With Premium, 5cut also makes AI summaries.</p>\n'
                                  '<p>Your recordings never leave your iPhone. 5cut cuts, transcribes and makes notes on the device. '
                                  'There is no 5cut server. Each engine downloads its model one time and then works offline.</p>',
                         'faq': [{'q': 'Is lecture transcription free?',
                                  'a': 'Recordings that you make in 5cut get a full transcript for free. For imported files, the free '
                                       'version transcribes the first 5 minutes. Premium transcribes imported files of any length.'},
                                 {'q': 'Which engine do I choose?',
                                  'a': 'It depends on the language. Parakeet Ultra covers 25 European languages and finds the language '
                                       'itself. Apple SpeechAnalyzer (iOS 26 or later) and WhisperKit cover the most languages. Parakeet '
                                       'Lite and Moonshine are smaller English engines for older iPhones.'},
                                 {'q': 'Can I export the transcript as subtitles?',
                                  'a': 'Yes. Export an SRT file, or burn the subtitles into the video. You can also send the transcript '
                                       'to Apple Notes, Markdown, Anki, Notion or Obsidian.'},
                                 {'q': 'Does transcription work without a connection?',
                                  'a': 'Yes, after a one-time download. Each engine downloads its model the first time you use it. '
                                       'Then turn on Airplane Mode. 5cut transcribes the same.'}]},
 'remove-silence-from-lectures': {'title': 'Remove Silence from Lecture Recordings – 5cut for iOS',
                                  'desc': 'Cut the silence and dead air from recorded university lectures on your iPhone. The speech stays '
                                          'at normal speed. Your recordings never leave your iPhone.',
                                  'h1': 'Remove Silence from Lectures',
                                  'tagline': 'Review the lecture, not the silence.',
                                  'intro': '<p>Lecture recordings have silent parts. The professor writes on the board, changes the slide '
                                           'or waits for answers. 5cut finds these silent parts and cuts them. The speech stays at normal '
                                           'speed.</p>\n'
                                           '<h2>How 5cut finds the silence</h2>\n'
                                           '<p>5cut measures the loudness of each recording. It sets its threshold between the background '
                                           'noise and the voice. A small voice detector in the app marks where someone speaks, so 5cut also '
                                           'cuts loud parts without a voice. Short pauses stay, so the speech sounds natural. Read more '
                                           'about <a href="/cut-background-noise-from-recordings/">noisy recordings</a>.</p>\n'
                                           '<h2>Gentle, Moderate or Aggressive</h2>\n'
                                           '<p>You choose how much 5cut cuts. Gentle cuts only long pauses. Aggressive cuts most of them. On '
                                           'a typical phone recording, Gentle keeps about 80% of the time, Moderate about 70% and Aggressive '
                                           'about 60%. A dense lecture keeps more, because it has fewer pauses.</p>',
                                  'faq': [{'q': 'Does 5cut make the speech faster?',
                                           'a': 'No. 5cut cuts the silence and keeps the speech at normal speed. You can also change the '
                                                'Playback Speed in Advanced Settings.'},
                                          {'q': 'How much time does 5cut save?',
                                           'a': 'It depends on the lecture. On a typical phone recording, Moderate keeps about 70% of the '
                                                'time. A dense lecture with few pauses keeps more.'},
                                          {'q': 'Can I undo a cut?',
                                           'a': 'Yes. 5cut does not change your original file. Move the threshold or choose another '
                                                'intensity, and 5cut shows the new result.'},
                                          {'q': 'Does silence removal work offline?',
                                           'a': 'Yes. Silence removal needs no download. The voice detector is in the app, so it also '
                                                'works in Airplane Mode.'}]},
 'podcast-silence-remover': {'title': 'Podcast Silence Remover for iPhone – Edit Podcast Audio | 5cut',
                             'desc': 'Cut the silence and long pauses from podcast episodes on your iPhone. 5cut finds them on the device, '
                                     'and the speech stays at normal speed.',
                             'h1': 'Remove Silence from Podcasts',
                             'tagline': 'Shorter podcast episodes, without long pauses.',
                             'intro': '<p>Long pauses make a podcast slow. Many short pauses between sentences also take time. 5cut finds '
                                      'the silence on your iPhone and cuts it, in your own podcast or in an episode that you import. The '
                                      'result depends on the recording. On a typical phone recording, Moderate keeps about 70% of the '
                                      'time.</p>'},
 'use-cases/remove-silence-from-zoom': {'title': 'How to Remove Silence from Zoom Recordings Automatically | 5cut',
                                        'desc': 'Cut the silence from long Zoom meeting recordings on your iPhone and iPad. 5cut finds the '
                                                'pauses on the device and keeps the speech.',
                                        'h1': 'Remove Silence from Zoom Meetings',
                                        'tagline': 'Hear only the parts where people speak.',
                                        'intro': '<p>Zoom recordings have long pauses. People wait for others to join, or they have problems '
                                                 'with the microphone. 5cut finds these silent parts in your Zoom MP4 or MOV file and cuts '
                                                 'them. The result is a shorter recording.</p>\n'
                                                 '<ol>\n'
                                                 '    <li>Save the Zoom recording to Files or Photos on your iPhone.</li>\n'
                                                 '    <li>In 5cut, tap Import or Record.</li>\n'
                                                 '    <li>Choose From Files or From Photos, and select the recording.</li>\n'
                                                 '    <li>Choose Gentle, Moderate or Aggressive.</li>\n'
                                                 '    <li>Export the shorter video.</li>\n'
                                                 '</ol>'},
 'use-cases/remove-silence-from-obs': {'title': 'Remove Silence from OBS Streams & Recordings | 5cut',
                                       'desc': 'Edit your OBS Studio recordings in less time. Move them to your iPhone, and 5cut cuts the '
                                               'silence on the device.',
                                       'h1': 'Remove Silence from OBS VODs',
                                       'tagline': 'Edit your stream recordings in less time.',
                                       'intro': '<p>Stream recordings from OBS Studio often have long silent parts, for example during '
                                                'breaks or while you wait for a match. Move your OBS files to your iPhone. 5cut cuts the '
                                                'silence, so your YouTube highlights are ready sooner.</p>'},
 'alternatives/timebolt-alternative': {'title': 'Free Mobile TimeBolt Alternative for iPhone | 5cut',
                                       'desc': 'A mobile TimeBolt alternative: 5cut cuts silence on iPhone for free and transcribes on the '
                                               'device. Speaker identification comes with Premium.',
                                       'h1': 'A Mobile TimeBolt Alternative',
                                       'tagline': 'Cut the silence on your iPhone or iPad.',
                                       'intro': '<p>TimeBolt is a desktop tool for PC and Mac. 5cut is a mobile alternative that edits '
                                                'video on your iPhone. 5cut cuts the silence on the device. Its transcription engines '
                                                'download one time and then work offline.</p>\n'
                                                '<p>Your recordings never leave your iPhone. There is no 5cut server.</p>'},
 'free-jumpcut-app': {'title': 'Free Jumpcut App for iPhone – Auto Silence Remover | 5cut',
                      'desc': 'A jumpcut app for iOS. 5cut cuts the silence from your videos, adds subtitles and exports from your '
                              'iPhone. 5 free exports each month.',
                      'h1': 'Free Jumpcut App for iPhone',
                      'tagline': 'Cut the silence on your iPhone, automatically.',
                      'intro': '<p>Do you want an automatic jumpcut tool? 5cut cuts the silence from talking-head videos and vlogs and '
                               'makes subtitles. All of this happens on your iPhone. The free version gives you 5 exports each month, '
                               'with a small watermark.</p>'},
 'smartphone-video-editor': {'title': 'Smartphone Video Editor for Talking Heads – AI Editor | 5cut',
                             'desc': 'Edit talking-head videos, vlogs and TikToks on your iPhone. 5cut cuts the silence, adds subtitles '
                                     'and exports on the device.',
                             'h1': 'Smartphone Video Editor for Talking Heads',
                             'tagline': 'Edit talking-head videos on your iPhone.',
                             'intro': '<p>It is slow to move large video files to a computer and edit them there. With 5cut, you edit on '
                                      'your iPhone. Film your talking-head video or vlog with the Camera app. Then import it into 5cut. '
                                      '5cut cuts the silence and adds subtitles. Then export the video from your phone.</p>'},
 'best-app-for-law-school-recordings': {'desc': 'Shorter law school lecture recordings on iPhone. Cut the silence, transcribe case '
                                                'discussions and export notes. Your recordings never leave your iPhone.',
                                        'h1': 'Best App for Law School Recordings',
                                        'intro': '<p>Law school lectures can have long pauses. The professor reads from the casebook, waits '
                                                 'between Socratic questions or gives students time to find a page.</p>\n'
                                                 '<p>5cut finds these silent parts on your iPhone and cuts them. Then transcribe the '
                                                 'recording, identify the speakers and export your notes.</p>\n'
                                                 '<h2>What 5cut does for law students</h2>\n'
                                                 '<ul>\n'
                                                 '    <li><strong>Cut the silence</strong>: the speech stays at normal speed.</li>\n'
                                                 '    <li><strong>Follow the Socratic method</strong>: with Premium, speaker identification '
                                                 'separates the professor from the students.</li>\n'
                                                 '    <li><strong>Find case names</strong>: transcribe the lecture, then search the '
                                                 'transcript for a case citation.</li>\n'
                                                 '    <li><strong>Keep discussions private</strong>: hypothetical client cases and case '
                                                 'discussions stay on your iPhone.</li>\n'
                                                 '    <li><strong>Prepare for exams</strong>: process the lectures of a semester in one '
                                                 'batch before finals.</li>\n'
                                                 '</ul>\n'
                                                 '<h2>The Socratic method problem</h2>\n'
                                                 '<p>In law school, the most important content often comes in dialogue. The professor asks a '
                                                 'question and waits 10 seconds. A student answers, and there is a 5-second pause. Then the '
                                                 'professor explains the legal principle.</p>\n'
                                                 '<p>5cut leaves short pauses alone and cuts the long ones. You choose how much it cuts: '
                                                 'Gentle, Moderate or Aggressive.</p>\n'
                                                 '<h2>The law school workflow</h2>\n'
                                                 '<ol>\n'
                                                 '    <li><strong>Record in class</strong>: use the recorder in 5cut, or import an audio file '
                                                 'from Files.</li>\n'
                                                 '    <li><strong>Cut the silence</strong>: start with Moderate. If 5cut cuts too much, '
                                                 'choose Gentle.</li>\n'
                                                 '    <li><strong>Transcribe</strong>: make a full transcript with timestamps. With Premium, '
                                                 'add speaker labels.</li>\n'
                                                 '    <li><strong>Export</strong>: save the shorter recording for your trip to campus, or '
                                                 'send the transcript to your outline tool.</li>\n'
                                                 '</ol>\n'
                                                 '<h2>Privacy and professional responsibility</h2>\n'
                                                 '<p>Law school classes discuss hypothetical client cases, real case facts and legal '
                                                 'strategy. Your recordings never leave your iPhone. 5cut cuts, transcribes and makes notes '
                                                 'on the device. There is no 5cut server.</p>\n'
                                                 '<h2>Free to start</h2>\n'
                                                 '<p>5cut is free to download. The free version includes the recorder, silence removal and 5 '
                                                 'exports each month. Recordings that you make in 5cut get a full transcript. Imported files '
                                                 'get a transcript of the first 5 minutes. Premium adds unlimited exports, full transcripts '
                                                 'of imported files, speaker identification, AI notes and search in all transcripts.</p>',
                                        'tagline': 'Cut the pauses from your law school recordings.',
                                        'title': 'Best App for Law School Recordings – Trim & Transcribe | 5cut'},
 'best-app-for-medical-school-lectures': {'desc': 'Record medical school lectures on iPhone. Cut the silence, transcribe in 30+ languages '
                                                  'and export to Anki. Patient case discussions stay on your iPhone.',
                                          'h1': 'Best App for Medical School Lectures',
                                          'intro': '<p>Medical lectures can have long silent parts between explanations, demonstrations and '
                                                   'questions.</p>\n'
                                                   '<p>5cut cuts the silence from lecture recordings on your iPhone. Then transcribe the '
                                                   'recording, export notes to Anki and review in less time. A dense lecture has fewer '
                                                   'pauses, so 5cut cuts less from it.</p>\n'
                                                   '<h2>What 5cut does for medical students</h2>\n'
                                                   '<ul>\n'
                                                   '    <li><strong>Less silence to review</strong>: 5cut cuts the silence before you '
                                                   'study.</li>\n'
                                                   '    <li><strong>Your recordings stay on your iPhone</strong>: every engine runs on the '
                                                   'device.</li>\n'
                                                   '    <li><strong>Transcripts in 30+ languages</strong>: international medical students can '
                                                   'transcribe the lecture and translate the transcript into their language.</li>\n'
                                                   '    <li><strong>Export to Anki</strong>: make study cards from the transcript.</li>\n'
                                                   '    <li><strong>Batches</strong>: add the recordings of one week to a batch and process '
                                                   'them together. Keep 5cut open while the batch runs.</li>\n'
                                                   '</ul>\n'
                                                   '<h2>Privacy matters in medicine</h2>\n'
                                                   '<p>Medical lectures often discuss patient cases, clinical scenarios and sensitive health '
                                                   'information. Cloud transcription uploads these recordings to the server of another '
                                                   'company. Your recordings never leave your iPhone. 5cut cuts, transcribes and makes notes '
                                                   'on the device. There is no 5cut server.</p>\n'
                                                   '<p>Test it yourself: download a transcription model one time, then turn on Airplane Mode. '
                                                   '5cut works the same.</p>\n'
                                                   '<h2>The medical school workflow</h2>\n'
                                                   '<ol>\n'
                                                   '    <li><strong>Record</strong>: use the recorder in 5cut during the lecture, or import a '
                                                   'recording.</li>\n'
                                                   '    <li><strong>Cut the silence</strong>: 5cut finds the silence and cuts it.</li>\n'
                                                   '    <li><strong>Transcribe</strong>: make a transcript with timestamps. With Premium, '
                                                   'speaker identification separates the professor from student questions.</li>\n'
                                                   '    <li><strong>Export</strong>: save the shorter video, export subtitles, or send the '
                                                   'transcript to Anki for spaced repetition.</li>\n'
                                                   '</ol>\n'
                                                   '<h2>Anatomy, pharmacology, pathology</h2>\n'
                                                   '<h3>Anatomy lectures</h3>\n'
                                                   '<p>The professor stops to point at specimens or to turn 3D models. 5cut can cut these '
                                                   'long pauses.</p>\n'
                                                   '<h3>Pharmacology</h3>\n'
                                                   '<p>Fast explanations of drug mechanisms, with short pauses at slide changes. 5cut leaves '
                                                   'short pauses alone, so the speech sounds natural.</p>\n'
                                                   '<h3>Clinical case discussions</h3>\n'
                                                   '<p>Many speakers: attending physicians, residents and students. With Premium, speaker '
                                                   'identification gives up to 4 speakers a color each.</p>\n'
                                                   '<h2>Free to start</h2>\n'
                                                   '<p>5cut is free to download. The free version includes the recorder, silence removal and '
                                                   '5 exports each month. Recordings that you make in 5cut get a full transcript. Imported '
                                                   'files get a transcript of the first 5 minutes. Premium adds unlimited exports, full '
                                                   'transcripts of imported files, speaker identification, AI notes and search in all '
                                                   'transcripts.</p>',
                                          'tagline': 'Cut the silence before you review an anatomy lecture.',
                                          'title': 'Best App for Medical School Lectures – Trim & Transcribe | 5cut',
                                          'faq': [{'q': 'Can I make Anki cards from a lecture?',
                                                   'a': 'Yes. Export the transcript to Anki. In the free version, 5cut makes fill-in-the-blank '
                                                        'cards from sentences of the lecture. With Premium, AI makes flashcards on your '
                                                        'iPhone.'},
                                                  {'q': 'How much shorter does a lecture get?',
                                                   'a': 'It depends on the lecture. A dense lecture has few pauses, so 5cut keeps most of it. '
                                                        'On a typical phone recording, Gentle keeps about 80% of the time, Moderate about '
                                                        '70% and Aggressive about 60%.'},
                                                  {'q': 'Do patient cases in my recordings leave my iPhone?',
                                                   'a': 'No. Your recordings never leave your iPhone. 5cut cuts, transcribes and makes notes '
                                                        'on the device. There is no 5cut server. Always follow the recording rules of your '
                                                        'school.'},
                                                  {'q': 'Can I process a week of lectures at once?',
                                                   'a': 'Yes. Add the recordings of one week to a batch. 5cut processes them one after the '
                                                        'other. Keep 5cut open while the batch runs.'}]},
 'offline-lecture-transcription-iphone': {'desc': 'Transcribe lecture recordings offline on iPhone. Download a model one time, then '
                                                  'transcribe in Airplane Mode. 30+ languages, SRT export, free app.',
                                          'h1': 'Offline Lecture Transcription on iPhone',
                                          'intro': '<p>Many transcription apps upload your lecture to a server. You wait for the result and '
                                                   'trust the service with your data. 5cut transcribes on your iPhone. Your recordings never '
                                                   'leave your iPhone.</p>\n'
                                                   '<h2>How offline transcription works</h2>\n'
                                                   '<p>5cut uses AI models that run on the Neural Engine of your iPhone. The first time you '
                                                   'use an engine, its model downloads one time. The size is from about 40 MB to 1.5 GB, by '
                                                   'engine. After that, transcription works in Airplane Mode, on the subway or in a lecture '
                                                   'hall with bad Wi-Fi.</p>\n'
                                                   '<h2>Six transcription engines</h2>\n'
                                                   '<p>5cut has six engines. Each engine has a different balance of speed, accuracy and '
                                                   'model size:</p>\n'
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
                                                   '<p>WhisperKit is for imported files only. The live recorder does not offer it.</p>\n'
                                                   '<h2>Why offline matters</h2>\n'
                                                   '<ul>\n'
                                                   '    <li><strong>Your recordings never leave your iPhone</strong>: every engine runs on the '
                                                   'device.</li>\n'
                                                   '    <li><strong>No mobile data</strong>: after the model download, hours of transcription '
                                                   'use no mobile data.</li>\n'
                                                   '    <li><strong>Works with a bad connection</strong>: in campus basements, on trains, on '
                                                   'planes and in libraries with blocked Wi-Fi.</li>\n'
                                                   '    <li><strong>No cost per minute</strong>: many cloud services charge for each minute. '
                                                   '5cut does not.</li>\n'
                                                   '    <li><strong>No upload wait</strong>: transcription starts on the iPhone, with no upload '
                                                   'first.</li>\n'
                                                   '</ul>\n'
                                                   '<h2>Supported languages</h2>\n'
                                                   '<p>Together, the six engines transcribe more than 30 languages. The exact list depends on '
                                                   'the engine and on the language models for your iPhone.</p>\n'
                                                   '<h2>Remove the silence too</h2>\n'
                                                   '<p>5cut also cuts the silence. A typical workflow is:</p>\n'
                                                   '<ol>\n'
                                                   '    <li>Record or import a lecture.</li>\n'
                                                   '    <li>Cut the silence.</li>\n'
                                                   '    <li>Transcribe the shorter version offline.</li>\n'
                                                   '    <li>Export a video with subtitles, an SRT file or a text transcript.</li>\n'
                                                   '</ol>\n'
                                                   '<p>Silence removal also works in Airplane Mode. It needs no download, because its voice '
                                                   'detector is in the app.</p>\n'
                                                   '<h2>Speaker identification</h2>\n'
                                                   '<p>With Premium, 5cut finds up to 4 speakers in a recording and gives each a color in the '
                                                   'transcript. The speaker model downloads one time, and then this also works offline. It '
                                                   'helps with lectures with questions, seminars and group presentations.</p>\n'
                                                   '<h2>Free to start</h2>\n'
                                                   '<p>5cut is free to download. The free version includes the recorder, silence removal and '
                                                   '5 exports each month. Recordings that you make in 5cut get a full transcript. Imported '
                                                   'files get a transcript of the first 5 minutes. Premium adds unlimited exports, full '
                                                   'transcripts of imported files, speaker identification, AI notes and search in all '
                                                   'transcripts.</p>',
                                          'tagline': 'Download a model one time. Then transcribe in Airplane Mode.',
                                          'title': 'Offline Lecture Transcription on iPhone – Airplane Mode | 5cut',
                                          'faq': [{'q': 'Does 5cut need the internet to transcribe?',
                                                   'a': 'Only for the first model download. Each engine downloads its model the first time '
                                                        'you use it. After that, transcription works in Airplane Mode.'},
                                                  {'q': 'How can I check that transcription is offline?',
                                                   'a': 'Download a transcription model one time. Then turn on Airplane Mode and transcribe '
                                                        'a recording. 5cut works the same.'},
                                                  {'q': 'Which engines work offline?',
                                                   'a': 'All six engines run on the iPhone. Each one works offline after its first download. '
                                                        'Apple SpeechAnalyzer needs iOS 26 or later and downloads its language files from '
                                                        'Apple.'},
                                                  {'q': 'How much storage do the models need?',
                                                   'a': 'From about 40 MB to 1.5 GB for each engine. You can see and delete each model in '
                                                        'Settings › Storage.'}]},
 'offline-meeting-notes-iphone': {'desc': 'Make meeting notes and transcripts offline on iPhone. Download a model one time, then record '
                                          'and transcribe in Airplane Mode. No cloud upload.',
                                  'h1': 'Offline Meeting Notes on iPhone',
                                  'intro': '<p>You need meeting notes, but the security rules of your company do not permit Otter, '
                                           'Fireflies or other cloud transcription services. Or the conference room has no Wi-Fi. Or you do '
                                           'not want to give your meetings to a third party.</p>\n'
                                           '<p>5cut makes meeting transcripts offline on your iPhone. Record, transcribe and identify the '
                                           'speakers. After the first model download, all of this works in Airplane Mode.</p>\n'
                                           '<h2>How offline meeting notes work</h2>\n'
                                           '<ol>\n'
                                           '    <li><strong>Download a language model one time</strong>: only this step needs the '
                                           'internet (about 40 MB to 1.5 GB).</li>\n'
                                           '    <li><strong>Record the meeting</strong>: tap Record. This works in Airplane Mode, '
                                           'underground and in any other place.</li>\n'
                                           '    <li><strong>Transcribe on the device</strong>: the AI runs on the Neural Engine of your '
                                           'iPhone.</li>\n'
                                           '    <li><strong>Separate the speakers</strong>: with Premium, 5cut finds up to 4 speakers and '
                                           'labels them.</li>\n'
                                           '    <li><strong>Export</strong>: copy the transcript, share it as text, or export it with '
                                           'timestamps.</li>\n'
                                           '</ol>\n'
                                           '<h2>Why offline meeting notes</h2>\n'
                                           '<h3>Company security rules</h3>\n'
                                           '<p>Many companies do not permit uploads of internal discussions to third-party services. Your '
                                           'recordings never leave your iPhone, and every transcription engine runs on the device. This can '
                                           'reduce third-party exposure. Always check the recording and security rules of your '
                                           'organization.</p>\n'
                                           '<h3>Regulated industries</h3>\n'
                                           '<p>Finance, healthcare, legal and defense have strict rules for data. 5cut sends no recording to '
                                           'a vendor, so no vendor keeps your audio. Check your own rules before you record.</p>\n'
                                           '<h3>Bad connections</h3>\n'
                                           '<p>Conference rooms in basements, meetings on trips and offsite events often have weak Wi-Fi. '
                                           'Offline transcription works with a bad connection or with no connection.</p>\n'
                                           '<h2>What you get</h2>\n'
                                           '<ul>\n'
                                           '    <li><strong>Full transcript</strong> with timestamps</li>\n'
                                           '    <li><strong>Speaker labels</strong> (Premium): each speaker has a color, and you can '
                                           'change the names</li>\n'
                                           '    <li><strong>Silence removal</strong>: 5cut cuts the long pauses</li>\n'
                                           '    <li><strong>Export formats</strong>: plain text, SRT subtitles or video</li>\n'
                                           '    <li><strong>30+ languages</strong>: teams with many languages can transcribe in the '
                                           'language of the meeting</li>\n'
                                           '</ul>\n'
                                           '<h2>Free to start</h2>\n'
                                           '<p>5cut is free to download. The free version includes the recorder, silence removal and 5 '
                                           'exports each month. Recordings that you make in 5cut get a full transcript. Imported files get '
                                           'a transcript of the first 5 minutes. Premium adds unlimited exports, full transcripts of '
                                           'imported files, speaker identification, AI notes and search in all transcripts.</p>',
                                  'tagline': 'Transcribe meetings offline. Speaker identification with Premium.',
                                  'title': 'Offline Meeting Notes on iPhone – On-Device Transcripts | 5cut'},
 'record-meetings-privately-iphone': {'desc': 'Record meetings on iPhone. Your recordings never leave your iPhone. 5cut transcribes and '
                                              'identifies speakers on the device. There is no 5cut server.',
                                      'h1': 'Record Meetings Privately on iPhone',
                                      'intro': '<p>Your meeting has confidential strategy, client names, revenue numbers or personnel '
                                               'decisions. Cloud meeting recorders like Otter, Fireflies or Fathom upload the audio to their '
                                               'servers. Their AI processes your words on the computers of another company.</p>\n'
                                               '<p>Your recordings never leave your iPhone. 5cut cuts, transcribes and makes notes on the '
                                               'device. There is no 5cut server. Test it yourself: download a transcription model one '
                                               'time, then turn on Airplane Mode. 5cut works the same.</p>\n'
                                               '<p>Always follow the recording and data rules of your organization.</p>\n'
                                               '<h2>The compliance problem with cloud recorders</h2>\n'
                                               '<p>Each time you use a cloud transcription service, you start a data processing '
                                               'relationship. This means:</p>\n'
                                               '<ul>\n'
                                               '    <li>A third party now keeps recordings of confidential discussions.</li>\n'
                                               '    <li>Under GDPR, you need a Data Processing Agreement (DPA).</li>\n'
                                               '    <li>SOC 2 auditors can ask about it.</li>\n'
                                               '    <li>If attackers break into the service, they can get your meeting content.</li>\n'
                                               '    <li>Client NDAs can prohibit the transfer of recordings to third parties.</li>\n'
                                               '</ul>\n'
                                               '<p>On-device transcription can reduce third-party exposure. But you must still follow the '
                                               'recording and data rules of your organization.</p>\n'
                                               '<h2>Who needs private meeting recordings</h2>\n'
                                               '<h3>Legal professionals</h3>\n'
                                               '<p>Client meetings, case strategy discussions and settlement negotiations. Cloud transcription '
                                               'by a third party can put attorney-client privilege at risk.</p>\n'
                                               '<h3>Healthcare</h3>\n'
                                               '<p>Clinical team meetings and patient case reviews are sensitive. Before you record, make '
                                               'sure that you have permission and that you follow the healthcare rules that apply.</p>\n'
                                               '<h3>Finance and banking</h3>\n'
                                               '<p>Investment discussions, client advisory meetings and compliance reviews. Material '
                                               'non-public information does not belong on the servers of a transcription startup.</p>\n'
                                               '<h3>HR and people operations</h3>\n'
                                               '<p>Performance reviews, disciplinary meetings and compensation discussions.</p>\n'
                                               '<h2>The 5cut workflow for meetings</h2>\n'
                                               '<ol>\n'
                                               '    <li><strong>Open the recorder</strong>: tap Record when the meeting starts.</li>\n'
                                               '    <li><strong>Transcribe after the meeting</strong>: choose an engine that you downloaded '
                                               'to your iPhone.</li>\n'
                                               '    <li><strong>Identify the speakers</strong>: with Premium, 5cut finds up to 4 '
                                               'speakers.</li>\n'
                                               '    <li><strong>Cut the silence</strong>: remove the pauses between agenda items.</li>\n'
                                               '    <li><strong>Export</strong>: save the transcript as text or SRT to a place that you '
                                               'choose.</li>\n'
                                               '</ol>\n'
                                               '<h2>Compared to alternatives</h2>\n'
                                               '<p>Cloud meeting tools upload your audio. With 5cut, your recordings never leave your '
                                               'iPhone. After a one-time model download, the engines transcribe offline. 5cut also '
                                               'identifies speakers and cuts the silence.</p>\n'
                                               '<h2>Free to start</h2>\n'
                                               '<p>5cut is free to download. The free version includes the recorder, silence removal and 5 '
                                               'exports each month. Recordings that you make in 5cut get a full transcript. Imported files '
                                               'get a transcript of the first 5 minutes. Premium adds unlimited exports, full transcripts '
                                               'of imported files, speaker identification, AI notes and search in all transcripts.</p>',
                                      'tagline': 'Record and transcribe meetings on the device. No cloud upload.',
                                      'title': 'Record Meetings Privately on iPhone – No Cloud Upload | 5cut',
                                      'faq': [{'q': 'Does 5cut upload my meeting recordings?',
                                               'a': 'No. Your recordings never leave your iPhone. 5cut cuts, transcribes and makes notes on '
                                                    'the device. There is no 5cut server.'},
                                              {'q': 'How can I check this?',
                                               'a': 'Test it yourself: download a transcription model one time, then turn on Airplane Mode. '
                                                    '5cut works the same.'},
                                              {'q': 'Does 5cut join my video calls?',
                                               'a': 'No. 5cut has no meeting bot. Record the meeting with the recorder in 5cut, or import a '
                                                    'recording from Zoom or Teams.'},
                                              {'q': 'Do I need an account?',
                                               'a': 'No. 5cut has no account system. You buy Premium in the App Store with your Apple '
                                                    'ID.'}]},
 'cut-background-noise-from-recordings': {'title': 'Cut Background Noise from Recordings – Voice Detection | 5cut',
                                          'desc': 'On noisy phone recordings, 5cut cuts the parts where nobody speaks, also when they '
                                                  'are loud. It does not filter the noise under a voice.',
                                          'h1': 'Cut Background Noise from Recordings',
                                          'tagline': 'Keep the voice. Cut the noise between the words.',
                                          'intro': '<p>You record on the street, in a train station or while you walk. The recording has '
                                                   'traffic, footsteps and announcements between the sentences. These parts are loud, so a '
                                                   'cutter that only measures loudness keeps them. 5cut cuts them, because nobody speaks in '
                                                   'them.</p>\n'
                                                   '<h2>How 5cut finds the voice</h2>\n'
                                                   '<p>A small voice detector is built into the app. It is about 1 MB and needs no download. '
                                                   'It marks each part of the recording where someone speaks. 5cut cuts the parts without a '
                                                   'voice, also when they are as loud as the speaker.</p>\n'
                                                   '<p>5cut also measures the loudness of each recording. It sets its threshold between the '
                                                   'background noise and the voice.</p>\n'
                                                   '<h2>What 5cut does not do</h2>\n'
                                                   '<p>5cut does not reduce or filter noise under speech. When someone speaks, 5cut keeps all '
                                                   'the sound of that part, also the noise behind the voice. 5cut removes only the parts '
                                                   'without a voice.</p>\n'
                                                   '<h2>Gentle, Moderate or Aggressive</h2>\n'
                                                   '<p>The more you cut, the more sure 5cut must be that someone speaks. On a typical phone '
                                                   'recording, the three intensities keep this much of the time:</p>\n'
                                                   '<ul>\n'
                                                   '    <li><strong>Gentle</strong>: about 80%</li>\n'
                                                   '    <li><strong>Moderate</strong>: about 70%</li>\n'
                                                   '    <li><strong>Aggressive</strong>: about 60%</li>\n'
                                                   '</ul>\n'
                                                   '<p>A dense lecture keeps more, because it has fewer pauses.</p>\n'
                                                   '<h2>Works in Airplane Mode</h2>\n'
                                                   '<p>The voice detector runs on your iPhone, so it also works in Airplane Mode. Your '
                                                   'recordings never leave your iPhone. There is no 5cut server.</p>\n'
                                                   '<p><a href="https://apps.apple.com/app/5cut/id6758529319?pt=128495158&ct=web_noise&mt=8">Download 5cut on '
                                                   'the App Store</a></p>',
                                          'faq': [{'q': 'Does 5cut remove noise while someone speaks?',
                                                   'a': 'No. 5cut does not filter the noise under a voice. It cuts only the parts where '
                                                        'nobody speaks.'},
                                                  {'q': 'Which noise does 5cut cut?',
                                                   'a': 'Noise in parts without a voice, for example traffic, footsteps, rustling or a train. '
                                                        '5cut cuts these parts also when they are loud.'},
                                                  {'q': 'Do I need to download the voice detector?',
                                                   'a': 'No. The voice detector is in the app. It is about 1 MB and works in Airplane '
                                                        'Mode.'},
                                                  {'q': 'Is this free?',
                                                   'a': 'Yes. Silence removal and the voice detector are free. The free version gives you 5 '
                                                        'exports each month.'}]}}
