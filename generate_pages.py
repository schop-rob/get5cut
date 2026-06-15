import os
import json

languages = {
    "en": {
        "dir": ".",
        "lang_code": "en",
        "title": "5cut – Record & Trim Lectures, Export Study Notes | iOS App",
        "description": "Record lectures in any language on your iPhone. 5cut removes silence, transcribes and live-translates in 30+ languages, and exports clean study notes to Anki, Notion, and Obsidian. Private, on-device.",
        "og_title": "5cut – Record & Trim Lectures, Export Study Notes",
        "og_description": "Record lectures. Trim silence. Translate live. Get a clean transcript and study notes. Private on iPhone.",
        "brand": "5cut",
        "brand_suffix": " — AI Lecture Recorder & Silence Trimmer",
        "tagline": "Keep up with lectures — in your language, at your pace.",
        "subhead_features": "Record lectures, trim silence automatically, translate live in 30+ languages, and export study notes on-device.",
        "proof1": "3-day free trial",
        "proof2": "5 exports/month free",
        "proof3": "No account required",
        "stat1_value": "Save up to 30%",
        "stat1_label": "of study time on average",
        "cta_pill1": "3-Day Premium Trial",
        "cta_pill2": "5 Free Exports/Mo",
        "cta_pill3": "No Account Required",
        "cta_subtext": "Free download · 3-day Premium trial · 5 exports/month free · No account",
        "creator_promise": "I built 5cut because re-listening to long, pause-filled lectures in a foreign language was eating up my study time. On-device translation and silence-trimming completely changed how I learn, and keeping it private means my coursework never goes to a cloud server.",
        "creator_signature": "Robin Schöppner, Creator of 5cut",
        "feat1_title": "In-App Recorder & Live Captions",
        "feat1_desc": "Record lectures, meetings, and interviews directly in the app. Add chapter bookmarks while recording. View live transcripts in real-time on iOS 26+ devices.",
        "feat2_title": "Smart Silence Removal",
        "feat2_desc": "Automatically detect and cut dead air from lectures and podcasts. Use Smart Mode presets (Gentle, Moderate, Aggressive) or customize thresholds manually.",
        "feat3_title": "On-Device Translation & AI summaries",
        "feat3_desc": "Follow lectures in your native tongue with live translation. Generate AI summaries, key points, and study questions — all powered by on-device AI, no internet required.",
        "feat4_title": "Export to Notion, Anki & Obsidian",
        "feat4_desc": "Export your trimmed transcripts with speaker labels directly to your favorite study tools, including Obsidian and auto-generated Anki study cards.",
        "feat5_title": "Multi-Speaker Identification",
        "feat5_desc": "Automatically identify up to 4 speakers in a single recording with color-coded, renamable labels — perfect for group discussions and seminars.",
        "how_it_works": "How it works",
        "step1": "<strong>Record or Import</strong> any audio or video directly on your iPhone",
        "step2": "<strong>Auto-detect silence</strong> — see speech in green and gaps in red",
        "step3": "<strong>Translate & summarize</strong> on-device using local AI models",
        "step4": "<strong>Export to study tools</strong> — send clean files to Anki, Notion, or Obsidian",
        "privacy_title": "Your Recordings Never Leave Your Phone",
        "privacy_desc": "We can't see your recordings — they never leave your phone. No account, no analytics, no ads.",
        "perfect_for": "Perfect for",
        "perfect_for_desc1": "International students attending lectures in a second language, study abroad participants, and expats watching local media. Also perfect for professionals who want to skip awkward pauses in Zoom recordings or speed up podcasts.",
        "perfect_for_desc2": "Need live translations? 5cut transcribes and translates lectures in 30+ languages entirely offline on your device.",
        "faq": "Frequently asked questions",
        "faq1_q": "How does silence detection work?",
        "faq1_a": "5cut analyzes the audio waveform of your video on-device. Segments below the silence threshold are color-coded red. You can drag a slider to adjust what counts as \"silence,\" or use one of three Smart Mode presets.",
        "faq2_q": "Can I add subtitles and translations to lectures?",
        "faq2_a": "Yes. 5cut includes on-device transcription and live translation supporting over 30 languages. You can burn subtitles directly into the video or export them as an SRT file. Everything is processed on your device.",
        "faq3_q": "Does it work with Zoom and online course recordings?",
        "faq3_a": "Yes. Import any MP4, MOV, or HEVC video. 5cut works with Zoom recordings, Microsoft Teams meetings, screen recordings, and any video file with an audio track.",
        "faq4_q": "Can I process a whole semester of lectures at once?",
        "faq4_a": "Yes. You can queue up multiple recordings and process them with individual or shared settings.",
        "faq5_q": "Is my data private?",
        "faq5_a": "Completely. All processing — silence detection, transcription, speaker identification — happens entirely on your device. No cloud uploads, no accounts, no data collection. Your videos never leave your phone.",
        "faq6_q": "Is there a premium plan?",
        "faq6_a": "Yes. Recording, silence removal, and transcript previews (up to 5 minutes) are free. You can upgrade to 5cut Premium for unlimited exports, speaker identification, full-length transcripts, and AI summaries. A 3-day free trial is available. Premium is a monthly subscription or a one-time lifetime purchase — prices are shown in the App Store and adjusted for your region.",
        "faq7_q": "What languages is the app available in?",
        "faq7_a": "The app interface is available in English, German, Spanish, French, Italian, Japanese, Korean, Portuguese (Brazil), Vietnamese, and Simplified Chinese.",
        "footer_use_cases": "Use Cases",
        "footer_alternatives": "Alternatives",
        "footer_legal": "Legal & Support",
        "footer_study_fields": "By Field of Study",
        "hero_note_desc": "Record, trim, transcribe, translate, and export — all on your device, without uploading your audio."
    },
    "de": {
        "dir": "de",
        "lang_code": "de",
        "title": "5cut – Vorlesungen aufnehmen & schneiden, Lernnotizen exportieren | iOS App",
        "description": "Nimm Vorlesungen direkt auf deinem iPhone auf. 5cut entfernt automatisch Stille, transkribiert in 30+ Sprachen und exportiert saubere Lernnotizen zu Anki, Notion und Obsidian.",
        "og_title": "5cut – Vorlesungen aufnehmen & schneiden, Lernnotizen exportieren",
        "og_description": "Vorlesungen aufnehmen. Stille entfernen. Live-Übersetzung. Sauberes Transkript und Lernnotizen exportieren. Privat auf dem iPhone.",
        "brand": "5cut",
        "brand_suffix": " – KI-Rekorder & Stille-Trimmer",
        "tagline": "Komm bei Vorlesungen mit – in deiner Sprache, in deinem Tempo.",
        "subhead_features": "Vorlesungen aufnehmen, Stille automatisch entfernen, live in 30+ Sprachen übersetzen und Lernnotizen auf dem Gerät exportieren.",
        "proof1": "100% auf dem Gerät (offline)",
        "proof2": "Kein Konto oder Anmeldung",
        "proof3": "Live-Übersetzung in 30+ Sprachen",
        "stat1_value": "Bis zu 30% sparen",
        "stat1_label": "an Lernzeit im Durchschnitt",
        "cta_pill1": "3 Tage Premium-Test",
        "cta_pill2": "5 kostenlose Exporte/Monat",
        "cta_pill3": "Kein Konto erforderlich",
        "cta_subtext": "Kostenloser Download · 3 Tage Premium-Test · 5 kostenlose Exporte/Monat · Kein Konto",
        "creator_promise": "Ich habe 5cut entwickelt, weil das Nachhören von langen, pausenreichen Vorlesungen in einer Fremdsprache meine Lernzeit aufgefressen hat. Die Übersetzung auf dem Gerät und das Entfernen von Stille haben mein Lernen komplett verändert – und da alles privat bleibt, landen meine Vorlesungen niemals auf einem Cloud-Server.",
        "creator_signature": "Robin Schöppner, Entwickler von 5cut",
        "feat1_title": "In-App Recorder & Live-Untertitel",
        "feat1_desc": "Nimm Vorlesungen und Meetings direkt auf. Füge Kapitelmarken hinzu und verfolge Live-Transkripte auf iOS 26+ Geräten.",
        "feat2_title": "Intelligente Stille-Entfernung",
        "feat2_desc": "Erkennt und schneidet Pausen automatisch aus Vorlesungen und Podcasts. Nutze Smart-Mode-Presets oder passe den Schwellenwert manuell an.",
        "feat3_title": "Lokale Übersetzung & KI-Analysen",
        "feat3_desc": "Folge Vorlesungen in deiner Muttersprache dank Live-Übersetzung. Erstelle KI-Zusammenfassungen und Fragen – alles lokal auf deinem iPhone.",
        "feat4_title": "Export zu Notion, Anki & Obsidian",
        "feat4_desc": "Exportiere saubere Transkripte mit Sprechernamen direkt in deine Lern-Tools, inklusive Obsidian und generierten Anki-Lernkarten.",
        "feat5_title": "Sprechererkennung für Gruppen",
        "feat5_desc": "Erkennt automatisch bis zu 4 Sprecher. Farbcodiert und umbenennbar – perfekt für Seminare, Interviews und Gruppengespräche.",
        "how_it_works": "So funktioniert's",
        "step1": "<strong>Aufnehmen oder Importieren</strong> einer Audiodatei oder eines Videos direkt auf deinem iPhone",
        "step2": "<strong>Stille automatisch erkennen</strong> – Sprache ist grün markiert, Pausen rot",
        "step3": "<strong>Übersetzen & Zusammenfassen</strong> auf dem Gerät mit lokaler KI",
        "step4": "<strong>Exportieren</strong> – saubere Notizen an Anki, Notion oder Obsidian senden",
        "privacy_title": "Deine Aufnahmen verlassen nie dein Gerät",
        "privacy_desc": "Wir können deine Aufnahmen weder sehen, hören noch speichern – alles wird direkt auf deinem Gerät verarbeitet. Kein Cloud-Upload, kein Konto, kein Tracking, keine Werbung. Deine Vorlesungen gehören nur dir.",
        "perfect_for": "Perfekt für",
        "perfect_for_desc1": "Internationale Studierende, die Vorlesungen in einer Fremdsprache nacharbeiten (z. B. im Auslandsstudium). Expats und Profis, die lästige Pausen aus Zoom-Meetings schneiden oder Podcasts schneller hören wollen.",
        "perfect_for_desc2": "Brauchst du Untertitel oder Live-Übersetzungen? 5cut transkribiert und übersetzt Vorlesungen offline in über 30 Sprachen direkt auf deinem Gerät.",
        "faq": "Häufig gestellte Fragen",
        "faq1_q": "Wie funktioniert die Stille-Erkennung?",
        "faq1_a": "5cut analysiert die Audiowellenform deines Videos direkt auf dem Gerät. Segmente unterhalb des Stille-Schwellenwerts werden rot markiert. Du kannst den Schwellenwert per Schieberegler anpassen.",
        "faq2_q": "Kann ich Untertitel und Übersetzungen für Vorlesungen erstellen?",
        "faq2_a": "Ja. 5cut bietet Transkription und Live-Übersetzung direkt auf dem Gerät in über 30 Sprachen. Untertitel können direkt ins Video eingebrannt oder als SRT exportiert werden.",
        "faq3_q": "Funktioniert es mit Zoom- und Online-Vorlesungen?",
        "faq3_a": "Ja. Importiere jedes MP4-, MOV- oder HEVC-Video. 5cut funktioniert mit Zoom-Aufnahmen, Microsoft-Teams-Meetings, Bildschirmaufnahmen und jedem Video mit Audiospur.",
        "faq4_q": "Kann ich ein ganzes semester auf einmal verarbeiten?",
        "faq4_a": "Ja. Du kannst mehrere Aufnahmen in die Warteschlange stellen und mit eigenen oder gemeinsamen Einstellungen verarbeiten.",
        "faq5_q": "Sind meine Daten sicher?",
        "faq5_a": "Absolut. Die gesamte Verarbeitung findet ausschließlich auf deinem Gerät statt. Kein Cloud-Upload, kein Account, keine Datenerfassung.",
        "faq6_q": "Gibt es eine Premium-Version?",
        "faq6_a": "Ja. Aufnahme, Stille-Erkennung und Transkript-Vorschauen (bis zu 5 Minuten) sind kostenlos. Du kannst auf 5cut Premium upgraden, um unbegrenzte Exporte, Sprechererkennung, vollständige Transkripte und KI-Zusammenfassungen freizuschalten. Ein kostenloser 3-Tage-Test ist verfügbar. Premium gibt es als Monatsabo oder einmaliges Lifetime-Upgrade — die Preise werden im App Store angezeigt und an deine Region angepasst.",
        "faq7_q": "In welchen Sprachen ist die App verfügbar?",
        "faq7_a": "Die App-Oberfläche ist verfügbar in Deutsch, Englisch, Spanisch, Französisch, Italienisch, Japanisch, Koreanisch, Portugiesisch, Vietnamesisch und vereinfachtem Chinesisch.",
        "footer_use_cases": "Use Cases",
        "footer_alternatives": "Alternativen",
        "footer_legal": "Rechtliches & Support",
        "footer_study_fields": "Nach Fachbereich",
        "hero_note_desc": "Aufnehmen, kürzen, transkribieren, übersetzen und exportieren – alles auf deinem Gerät, ohne Upload."
    },
    "zh": {
        "dir": "zh",
        "lang_code": "zh-Hans",
        "title": "5cut – 录制并剪辑网课，导出学习笔记 | iOS 应用",
        "description": "直接在 iPhone 上录制讲座和会议。5cut 自动裁剪静音部分，支持 30 多种语言转写，并可导出清晰的学习笔记至 Anki、Notion 和 Obsidian。",
        "og_title": "5cut – 录制并剪辑网课，导出学习笔记",
        "og_description": "录制讲座。去除静音。实时翻译。获取清晰的文本和学习笔记。在 iPhone 上私密处理。",
        "brand": "5cut",
        "brand_suffix": " – AI 课程录音与去静音工具",
        "tagline": "拒绝重复听课浪费时间。自动裁剪静音，实时翻译，本地生成学习笔记。",
        "proof1": "100% 设备端离线处理",
        "proof2": "无需注册账户",
        "proof3": "30+ 语言实时翻译",
        "stat1_value": "最多节省 30%",
        "stat1_label": "的学习时间",
        "cta_subtext": "免费下载 · 3 天 Premium 试用 · 每月 5 次免费导出 · 无需账户",
        "creator_promise": "我开发 5cut 是因为用外语听那些又长又多停顿的课非常浪费学习时间。设备端翻译和去静音功能彻底改变了我的学习方式，而且完全本地处理意味着我的课程资料永远不会被上传到云端服务器。",
        "creator_signature": "Robin Schöppner, 5cut 开发者",
        "feat1_title": "应用内录音与实时字幕",
        "feat1_desc": "直接录制课堂讲座或会议。录音时可添加章节标记。iOS 26+ 设备支持生成实时字幕。",
        "feat2_title": "智能去除静音",
        "feat2_desc": "自动检测并裁剪讲座和播客中的无声停顿。支持智能预设模式（温和、适中、激进）或手动调节阈值。",
        "feat3_title": "设备端翻译与 AI 摘要",
        "feat3_desc": "支持实时翻译，用母语轻松跟上外语课程。在本地生成 AI 摘要、核心要点与问答，无需上传云端。",
        "feat4_title": "导出至 Notion、Anki 与 Obsidian",
        "feat4_desc": "将整理好的干净文本及发言人标记直接导出至 Notion、Obsidian，并支持自动生成 Anki 学习卡片。",
        "feat5_title": "多发言人识别",
        "feat5_desc": "自动识别录音中多达 4 位发言人，并提供颜色标记与名称修改。非常适合研讨会和小组讨论。",
        "how_it_works": "使用方法",
        "step1": "<strong>录制或导入</strong>音频或视频文件至 iPhone",
        "step2": "<strong>自动检测静音</strong> — 绿色代表语音，红色代表静音",
        "step3": "<strong>离线翻译与总结</strong> — 在设备上运行本地 AI 模型处理",
        "step4": "<strong>导出学习资料</strong> — 将整理好的笔记发送至 Anki、Notion 或 Obsidian",
        "privacy_title": "你的录音永远不会离开你的手机",
        "privacy_desc": "我们无法看到、听到或存储你的录音 — 一切都在你的设备上处理。无云端上传、无需账户、无跟踪、无广告。你的课堂录音完全属于你。",
        "perfect_for": "适用人群",
        "perfect_for_desc1": "复旧外语课程的留学生、交换生、外派人员。也同样适用于希望去除 Zoom 会议录制尴尬停顿或加速收听播客的职场人士。",
        "perfect_for_desc2": "需要字幕或实时翻译？5cut 可以在设备上完全离线转写和翻译 30 多种语言的讲座。",
        "faq": "常见问题",
        "faq1_q": "静音检测是如何工作的？",
        "faq1_a": "5cut 在设备本地分析视频音频波形。低于阈值的片段标记为红色。您可以手动调整滑块，或选择三种智能模式。",
        "faq2_q": "我可以为课程生成字幕和翻译吗？",
        "faq2_a": "可以。5cut 支持 30 多种语言的设备端转写与实时翻译。字幕可嵌入视频或导出为 SRT。",
        "faq3_q": "支持 Zoom 或在线课程录制吗？",
        "faq3_a": "支持。可导入 MP4、MOV 或 HEVC 视频。适用于 Zoom 录制、Teams 会议、屏幕录像及任何带音轨的视频。",
        "faq4_q": "可以批量处理一整个学期的课吗？",
        "faq4_a": "可以。你可以将多个录音加入队列，并使用单独或共享设置进行处理。",
        "faq5_q": "我的数据隐私有保障吗？",
        "faq5_a": "绝对保障。所有处理过程均在本地完成。不上传云端，无需账号，不收集数据。",
        "faq6_q": "5cut 有 Premium 付费计划吗？",
        "faq6_a": "有的。录音、静音裁剪和转写预览（前 5 分钟）都是免费的。您可以升级到 5cut Premium 来解锁无限次数导出、说话人识别、完整长度转录以及 AI 总结。我们提供 3 天免费试用。5cut Premium 为月度订阅或一次性终身升级——价格在 App Store 中显示并按地区调整。",
        "faq7_q": "应用支持哪些语言？",
        "faq7_a": "应用界面支持简体中文、英语、德语、西班牙语、法语、意大利语、日语、韩语、葡萄牙语和越南语。",
        "footer_use_cases": "使用场景",
        "footer_alternatives": "替代方案",
        "footer_legal": "法律与支持",
        "footer_study_fields": "按学科分类",
        "hero_note_desc": "录制、裁剪、转写、翻译、导出 — 全部在设备上完成，无需上传音频。"
    },
    "fr": {
        "dir": "fr",
        "lang_code": "fr",
        "title": "5cut – Enregistrez, Coupez & Exportez vos Notes de Cours | Application iOS",
        "description": "Enregistrez vos cours directement sur votre iPhone. 5cut coupe automatiquement les silences, transcrit en plus de 30 langues et exporte vos notes vers Anki, Notion et Obsidian.",
        "og_title": "5cut – Enregistrez, Coupez & Exportez vos Notes de Cours",
        "og_description": "Enregistrez vos cours. Supprimez les silences. Traduisez en direct. Obtenez une transcription propre. Privé sur iPhone.",
        "brand": "5cut",
        "brand_suffix": " – Enregistreur de cours IA & Coupe-silence",
        "tagline": "Ne perdez plus d'heures à réécouter. Coupez les silences, traduisez en direct et générez vos notes.",
        "proof1": "100% local (hors ligne)",
        "proof2": "Sans création de compte",
        "proof3": "Traduction en direct dans 30+ langues",
        "stat1_value": "Économisez jusqu'à 30%",
        "stat1_label": "de temps d'étude en moyenne",
        "cta_subtext": "Téléchargement gratuit · Essai Premium de 3 jours · 5 exports/mois gratuits · Sans compte",
        "creator_promise": "J'ai créé 5cut parce que réécouter de longs cours remplis de blancs dans une langue étrangère dévorait mon temps d'étude. La traduction sur l'appareil et la suppression des silences ont totalement changé ma façon d'apprendre, et le traitement local garantit que mes cours ne sont jamais envoyés sur un serveur cloud.",
        "creator_signature": "Robin Schöppner, Créateur de 5cut",
        "feat1_title": "Enregistreur & Sous-titres en Direct",
        "feat1_desc": "Enregistrez vos cours et réunions. Ajoutez des signets et suivez la transcription en direct sur les appareils iOS 26+.",
        "feat2_title": "Suppression Intelligente des Silences",
        "feat2_desc": "Détectez et coupez automatiquement les blancs des cours et podcasts. Utilisez les préréglages intelligents ou ajustez le seuil à la main.",
        "feat3_title": "Traduction Locale & Résumés par IA",
        "feat3_desc": "Suivez les cours dans votre langue grâce à la traduction en direct. Obtenez des résumés IA et des questions-réponses générés localement.",
        "feat4_title": "Exportation vers Notion, Anki & Obsidian",
        "feat4_desc": "Exportez des transcriptions propres avec locuteurs directement vers vos outils d'étude favoris, y compris des cartes mémoires Anki.",
        "feat5_title": "Identification Multi-Locuteurs",
        "feat5_desc": "Identifiez automatiquement jusqu'à 4 locuteurs dans un enregistrement. Codes couleurs et étiquettes renommables — idéal pour les séminaires.",
        "how_it_works": "Comment ça marche",
        "step1": "<strong>Enregistrez ou Importez</strong> de l'audio ou de la vidéo directement sur votre iPhone",
        "step2": "<strong>Détectez les silences</strong> — parole en vert, temps morts en rouge",
        "step3": "<strong>Traduisez & résumez</strong> sur l'appareil avec l'IA locale",
        "step4": "<strong>Exportez</strong> — envoyez vos notes propres vers Anki, Notion ou Obsidian",
        "privacy_title": "Vos enregistrements ne quittent jamais votre téléphone",
        "privacy_desc": "Nous ne pouvons ni voir, ni écouter, ni stocker vos enregistrements — tout est traité sur votre appareil. Pas d'envoi vers le cloud, pas de compte, pas de suivi, pas de publicité. Vos cours restent entièrement les vôtres.",
        "perfect_for": "Parfait pour",
        "perfect_for_desc1": "Les étudiants internationaux suivant des cours dans une langue étrangère, les étudiants à l'étranger et les expatriés. Convient aussi aux professionnels pour couper les blancs des enregistrements Zoom ou accélérer les podcasts.",
        "perfect_for_desc2": "Besoin de traduction ? 5cut transcrit et traduit les cours dans plus de 30 langues directement sur votre appareil, sans connexion.",
        "faq": "Foire aux questions",
        "faq1_q": "Comment fonctionne la détection des silences ?",
        "faq1_a": "5cut analyse l'onde audio sur votre appareil. Les segments sous le seuil de silence sont colorés en rouge. Vous pouvez ajuster le curseur pour définir le \"silence\".",
        "faq2_q": "Puis-je ajouter des sous-titres et des traductions ?",
        "faq2_a": "Oui. 5cut inclut une transcription sur l'appareil et la traduction en direct pour plus de 30 langues. Vous pouvez intégrer les sous-titres à la vidéo ou exporter en SRT.",
        "faq3_q": "Cela fonctionne-t-il avec les enregistrements Zoom ?",
        "faq3_a": "Oui. Importez n'importe quelle vidéo MP4, MOV ou HEVC. 5cut fonctionne avec Zoom, Teams et les enregistrements d'écran.",
        "faq4_q": "Puis-je traiter tout un semestre de cours à la fois ?",
        "faq4_a": "Oui. Vous pouvez mettre en file d'attente plusieurs enregistrements et les traiter avec des réglages individuels ou partagés.",
        "faq5_q": "Mes données sont-elles privées ?",
        "faq5_a": "Complètement. Tout le traitement se fait sur votre appareil. Pas de cloud, pas de compte, pas de collecte de données.",
        "faq6_q": "Existe-t-il une version Premium ?",
        "faq6_a": "Oui. L'enregistrement, la suppression des silences et l'aperçu de transcription (5 premières minutes) sont gratuits. Vous pouvez passer à 5cut Premium pour un nombre d'exports illimité, l'identification des locuteurs, les transcriptions intégrales et les résumés IA. Un essai gratuit de 3 jours est disponible. Premium est un abonnement mensuel ou un achat à vie unique — les prix sont affichés dans l'App Store et adaptés à votre région.",
        "faq7_q": "Quelles sont les langues disponibles pour l'application ?",
        "faq7_a": "L'interface est disponible en anglais, allemand, espagnol, français, italien, japonais, coréen, portugais, vietnamien et chinois.",
        "footer_use_cases": "Cas d'utilisation",
        "footer_alternatives": "Alternatives",
        "footer_legal": "Légal & Support",
        "footer_study_fields": "Par domaine d'études",
        "hero_note_desc": "Enregistrez, coupez, transcrivez, traduisez et exportez — tout sur votre appareil, sans envoyer votre audio."
    },
    "vi": {
        "dir": "vi",
        "lang_code": "vi",
        "title": "5cut – Ghi Âm, Cắt Bỏ Khoảng Lặng & Xuất Ghi Chú | Ứng Dụng iOS",
        "description": "Ghi âm bài giảng trực tiếp trên iPhone. 5cut tự động cắt khoảng lặng, tạo phụ đề 30+ ngôn ngữ và xuất ghi chú học tập sạch sẽ sang Anki, Notion, và Obsidian. Riêng tư, trên thiết bị.",
        "og_title": "5cut – Ghi Âm & Cắt Khoảng Lặng, Xuất Ghi Chú Học Tập",
        "og_description": "Ghi âm bài giảng. Cắt bỏ khoảng lặng. Dịch trực tiếp. Nhận bản ghi chép và ghi chú học tập. Riêng tư trên iPhone.",
        "brand": "5cut",
        "brand_suffix": " – Máy ghi âm bài giảng AI & Cắt khoảng lặng",
        "tagline": "Không còn tốn hàng giờ nghe lại. Tự động cắt khoảng lặng, dịch trực tiếp và tạo ghi chú học tập.",
        "proof1": "100% trên thiết bị (ngoại tuyến)",
        "proof2": "Không cần đăng ký tài khoản",
        "proof3": "Dịch trực tiếp 30+ ngôn ngữ",
        "stat1_value": "Tiết kiệm lên đến 30%",
        "stat1_label": "thời gian học trung bình",
        "cta_subtext": "Tải xuống miễn phí · Dùng thử Premium 3 ngày · 5 xuất miễn phí/tháng · Không cần tài khoản",
        "creator_promise": "Tôi tạo ra 5cut vì việc nghe lại các bài giảng dài dòng, đầy khoảng lặng bằng tiếng nước ngoài đã ngốn hết thời gian học của tôi. Tính năng dịch thuật trên thiết bị và cắt khoảng lặng đã thay đổi hoàn toàn cách tôi học tập, và việc giữ mọi thứ riêng tư giúp tài liệu của tôi không bao giờ bị đưa lên máy chủ đám mây.",
        "creator_signature": "Robin Schöppner, Người sáng tạo 5cut",
        "feat1_title": "Máy Ghi Âm & Phụ Đề Trực Tiếp",
        "feat1_desc": "Ghi âm bài giảng và cuộc họp trực tiếp. Thêm dấu trang chương và xem phụ đề trực tiếp trên các thiết bị iOS 26+.",
        "feat2_title": "Tự Động Xóa Khoảng Lặng Thông Minh",
        "feat2_desc": "Phát hiện và cắt bỏ những khoảng trống từ bài giảng và podcast. Sử dụng các chế độ thông minh hoặc tự điều chỉnh thủ công.",
        "feat3_title": "Dịch Thuật & Tóm Tắt AI Trên Thiết Bị",
        "feat3_desc": "Theo dõi bài giảng bằng ngôn ngữ mẹ đẻ của bạn nhờ dịch trực tiếp. Nhận tóm tắt AI và Q&A được xử lý cục bộ trên iPhone.",
        "feat4_title": "Xuất Sang Notion, Anki & Obsidian",
        "feat4_desc": "Xuất bản ghi chép sạch sẽ với nhãn người nói trực tiếp sang các công cụ học tập yêu thích của bạn, bao gồm các thẻ ghi nhớ Anki.",
        "feat5_title": "Nhận Diện Nhiều Người Nói",
        "feat5_desc": "Tự động nhận diện tối đa 4 người nói trong một bản ghi âm với mã màu và nhãn có thể chỉnh sửa — hoàn hảo cho các hội thảo.",
        "how_it_works": "Cách hoạt động",
        "step1": "<strong>Ghi âm hoặc Nhập</strong> âm thanh hoặc video trực tiếp trên iPhone",
        "step2": "<strong>Tự động phát hiện khoảng lặng</strong> — giọng nói màu xanh, khoảng lặng màu đỏ",
        "step3": "<strong>Dịch thuật & tóm tắt</strong> trên thiết bị bằng AI cục bộ",
        "step4": "<strong>Xuất sang công cụ học tập</strong> — gửi ghi chú sạch sang Anki, Notion, hoặc Obsidian",
        "privacy_title": "Bản ghi âm của bạn không bao giờ rời khỏi điện thoại",
        "privacy_desc": "Chúng tôi không thể xem, nghe hoặc lưu trữ bản ghi âm của bạn — mọi thứ được xử lý trên thiết bị của bạn. Không tải lên đám mây, không cần tài khoản, không theo dõi, không quảng cáo. Bài giảng của bạn hoàn toàn thuộc về bạn.",
        "perfect_for": "Hoàn hảo cho",
        "perfect_for_desc1": "Du học sinh và sinh viên quốc tế học tập bằng ngoại ngữ, người định cư ở nước ngoài. Cũng rất phù hợp cho các chuyên gia muốn cắt bỏ khoảng lặng từ các bản ghi cuộc họp Zoom hoặc đẩy nhanh tốc độ nghe podcast.",
        "perfect_for_desc2": "Cần phụ đề hay dịch thuật? 5cut hỗ trợ chuyển ngữ và tạo phụ đề cho bài giảng ở hơn 30 ngôn ngữ hoàn toàn ngoại tuyến.",
        "faq": "Câu hỏi thường gặp",
        "faq1_q": "Tính năng phát hiện khoảng lặng hoạt động như thế nào?",
        "faq1_a": "5cut phân tích biểu đồ âm thanh trên thiết bị. Các phân đoạn dưới ngưỡng im lặng được tô màu đỏ. Bạn có thể kéo thanh trượt để điều chỉnh.",
        "faq2_q": "Tôi có thể tạo phụ đề và dịch thuật cho bài giảng không?",
        "faq2_a": "Có. 5cut bao gồm khả năng tạo phụ đề và dịch trực tiếp trên thiết bị hỗ trợ hơn 30 ngôn ngữ. Bạn có thể xuất dưới dạng tệp SRT.",
        "faq3_q": "Ứng dụng có hoạt động với các bản ghi Zoom không?",
        "faq3_a": "Có. Nhập bất kỳ video MP4, MOV hoặc HEVC nào. 5cut hoạt động với các bản ghi Zoom, Microsoft Teams và bất kỳ tệp video nào có rãnh âm thanh.",
        "faq4_q": "Tôi có thể xử lý toàn bộ bài giảng của một học kỳ cùng lúc không?",
        "faq4_a": "Có. Bạn có thể xếp hàng nhiều bản ghi âm và xử lý bằng cài đặt riêng hoặc cài đặt chung.",
        "faq5_q": "Dữ liệu của tôi có riêng tư không?",
        "faq5_a": "Hoàn toàn. Tất cả quá trình xử lý diễn ra hoàn toàn trên thiết bị của bạn. Không tải lên đám mây, không thu thập dữ liệu.",
        "faq6_q": "Có gói Premium không?",
        "faq6_a": "Có. Các tính năng ghi âm, cắt khoảng lặng và xem trước bản chép lời (5 phút đầu) đều miễn phí. Bạn có thể nâng cấp lên 5cut Premium để xuất không giới hạn, nhận diện người nói, dịch toàn bộ bài giảng và tạo tóm tắt AI. Có sẵn dùng thử miễn phí 3 ngày. Premium là gói đăng ký hằng tháng hoặc nâng cấp trọn đời một lần — giá hiển thị trong App Store và điều chỉnh theo khu vực.",
        "faq7_q": "Ứng dụng có sẵn bằng những ngôn ngữ nào?",
        "faq7_a": "Giao diện ứng dụng có sẵn bằng tiếng Anh, Đức, Tây Ban Nha, Pháp, Ý, Nhật Bản, Hàn Quốc, Bồ Đào Nha, Tiếng Việt và Tiếng Trung.",
        "footer_use_cases": "Trường hợp sử dụng",
        "footer_alternatives": "Các lựa chọn thay thế",
        "footer_legal": "Pháp lý & Hỗ trợ",
        "footer_study_fields": "Theo lĩnh vực học tập",
        "hero_note_desc": "Ghi âm, cắt khoảng lặng, chuyển ngữ, dịch thuật và xuất — tất cả trên thiết bị của bạn, không cần tải lên âm thanh."
    },
    "es": {
        "dir": "es",
        "lang_code": "es",
        "title": "5cut – Graba y Recorta Clases, Exporta Apuntes | App para iOS",
        "description": "Graba clases y reuniones en tu iPhone. 5cut recorta el silencio automáticamente, transcribe en más de 30 idiomas y exporta apuntes limpios a Anki, Notion y Obsidian. Privado, en el dispositivo.",
        "og_title": "5cut – Graba y Recorta Clases, Exporta Apuntes",
        "og_description": "Graba clases. Recorta silencios. Traduce en vivo. Obtén una transcripción limpia y apuntes. Privado en iPhone.",
        "brand": "5cut",
        "brand_suffix": " – Grabadora de clases con IA y Recorte de silencio",
        "tagline": "No pierdas más horas escuchando. Recorta silencios, traduce en vivo y genera apuntes de estudio.",
        "proof1": "100% en el dispositivo (sin internet)",
        "proof2": "Sin necesidad de cuenta",
        "proof3": "Traducción en vivo en 30+ idiomas",
        "stat1_value": "Ahorra 20-30%",
        "stat1_label": "de tiempo de estudio en promedio",
        "cta_subtext": "Descarga gratis · Incluye prueba Premium de 3 días · Sin registrarse",
        "creator_promise": "Creé 5cut porque volver a escuchar clases largas llenas de silencios en un idioma extranjero consumía mi tiempo de estudio. La traducción en el dispositivo y el recorte de silencios cambiaron por completo mi forma de aprender, y al ser privado, mis clases nunca se suben a un servidor en la nube.",
        "creator_signature": "Robin Schöppner, Creador de 5cut",
        "feat1_title": "Grabadora y Subtítulos en Vivo",
        "feat1_desc": "Graba clases y reuniones directamente. Añade marcadores de capítulo y sigue la transcripción en vivo en dispositivos iOS 26+.",
        "feat2_title": "Eliminación de Silencios Inteligente",
        "feat2_desc": "Detecta y corta automáticamente los silencios en clases y podcasts. Usa modos inteligentes o ajusta el umbral manualmente.",
        "feat3_title": "Traducción y Resúmenes IA Locales",
        "feat3_desc": "Sigue las clases en tu idioma materno con traducción en vivo. Obtén resúmenes de IA y preguntas clave de forma local en tu iPhone.",
        "feat4_title": "Exportar a Notion, Anki y Obsidian",
        "feat4_desc": "Exporta una transcripción limpia con etiquetas de hablantes directamente a tus herramientas de estudio, incluyendo tarjetas de repaso Anki.",
        "feat5_title": "Identificación de Múltiples Oradores",
        "feat5_desc": "Identifica de forma automática hasta 4 oradores en una grabación. Etiquetas con códigos de colores — ideal para seminarios y debates.",
        "how_it_works": "Cómo funciona",
        "step1": "<strong>Graba o Importa</strong> cualquier audio o video en tu iPhone",
        "step2": "<strong>Detecta los silencios</strong> — el verde es voz, el rojo es silencio",
        "step3": "<strong>Traduce y resume</strong> en el dispositivo usando la IA local",
        "step4": "<strong>Exporta apuntes</strong> — envía archivos limpios a Anki, Notion o Obsidian",
        "privacy_title": "Privacidad Ante Todo: 100% en el Dispositivo",
        "privacy_desc": "Creemos que tus grabaciones te pertenecen. 5cut procesa el audio, las transcripciones y los resúmenes IA completamente en tu iPhone o iPad. Nunca se sube audio ni video a ningún servidor, garantizando privacidad absoluta.",
        "perfect_for": "Perfecto para",
        "perfect_for_desc1": "Estudiantes internacionales que repasan clases en un idioma extranjero, estudiantes de intercambio y expatriados. También es ideal para profesionales que desean eliminar las pausas de grabaciones de Zoom o podcasts.",
        "perfect_for_desc2": "¿Necesitas subtítulos o traducciones? 5cut transcribe y traduce clases en más de 30 idiomas directamente en tu dispositivo y sin conexión.",
        "faq": "Preguntas frecuentes",
        "faq1_q": "¿Cómo funciona la detección de silencios?",
        "faq1_a": "5cut analiza la forma de onda de audio de tu video en el dispositivo. Los segmentos por debajo del umbral de silencio se marcan en rojo. Puedes ajustar el control deslizante para definir el \"silencia\".",
        "faq2_q": "¿Puedo añadir subtítulos y traducciones a mis clases?",
        "faq2_a": "Sí. 5cut incluye transcripción en el dispositivo y traducción en vivo compatible con más de 30 idiomas. Puedes incrustar subtítulos en el video o exportarlos como un archivo SRT.",
        "faq3_q": "¿Funciona con Zoom y grabaciones de cursos en línea?",
        "faq3_a": "Sí. Importa cualquier video MP4, MOV o HEVC. 5cut funciona con grabaciones de Zoom, Microsoft Teams y cualquier archivo de video con una pista de audio.",
        "faq4_q": "¿Puedo procesar todo un semestre de clases a la vez?",
        "faq4_a": "Sí. Puedes poner en cola varias grabaciones y procesarlas con ajustes individuales o compartidos.",
        "faq5_q": "¿Son privados mis datos?",
        "faq5_a": "Completamente. Todo el procesamiento ocurre en tu dispositivo. No hay subidas a la nube, cuentas, ni recopilación de datos.",
        "faq6_q": "¿Existe un plan Premium?",
        "faq6_a": "Sí. La grabación, la eliminación de silencios y las vistas previas de transcripción (primeros 5 minutos) son gratuitas. Puedes mejorar a 5cut Premium para obtener exportaciones ilimitadas, identificación de hablantes, transcripciones completas y resúmenes IA. Incluye una prueba gratuita de 3 días. Premium es una suscripción mensual o una compra de por vida con pago único — los precios se muestran en la App Store y se ajustan a tu región.",
        "faq7_q": "¿En qué idiomas está disponible la aplicación?",
        "faq7_a": "La interfaz está disponible en inglés, alemán, español, francés, italiano, japonés, coreano, portugués, vietnamita y chino simplificado.",
        "footer_use_cases": "Casos de uso",
        "footer_alternatives": "Alternativas",
        "footer_legal": "Legal y Soporte",
        "footer_study_fields": "Por área de estudio",
        "hero_note_desc": "Graba, recorta, transcribe, traduce y exporta — todo en tu dispositivo, sin subir tu audio."
    }
}

html_template = """<!DOCTYPE html>
<html lang="{lang_code}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="icon" type="image/svg+xml" href="/icon.svg">
    <link rel="icon" type="image/png" href="/favicon.png">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="canonical" href="https://get5cut.com{canonical_path}">
    <link rel="alternate" hreflang="en" href="https://get5cut.com/">
    <link rel="alternate" hreflang="de" href="https://get5cut.com/de/">
    <link rel="alternate" hreflang="zh-Hans" href="https://get5cut.com/zh/">
    <link rel="alternate" hreflang="fr" href="https://get5cut.com/fr/">
    <link rel="alternate" hreflang="vi" href="https://get5cut.com/vi/">
    <link rel="alternate" hreflang="es" href="https://get5cut.com/es/">
    <link rel="alternate" hreflang="x-default" href="https://get5cut.com/">
    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{og_description}">
    <meta property="og:url" content="https://get5cut.com{canonical_path}">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://get5cut.com/assets/og-card.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{og_title}">
    <meta name="twitter:description" content="{og_description}">
    <meta name="twitter:image" content="https://get5cut.com/assets/og-card.png">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "5cut",
        "operatingSystem": "iOS",
        "applicationCategory": "MultimediaApplication",
        "description": "{description}",
        "featureList": "In-app recorder, AI summaries, Export to Apple Notes/Anki/Notion/Obsidian, Silence removal, on-device transcription in 30+ languages, speaker identification",
        "screenshot": "https://get5cut.com/assets/iphone-transcript.png",
        "author": {{
            "@type": "Person",
            "name": "Robin Schöppner",
            "url": "https://get5cut.com/"
        }},
        "softwareVersion": "1.2.2"
    }}
    </script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif;
            background: #F5F5F5;
            color: #111;
            min-height: 100vh;
            padding: 40px 24px;
        }}
        .container {{
            max-width: 1040px;
            width: 100%;
            margin: 0 auto;
        }}
        .hero {{
            min-height: calc(100vh - 96px);
            display: grid;
            grid-template-columns: minmax(0, 0.9fr) minmax(360px, 1.1fr);
            gap: 56px;
            align-items: center;
        }}
        .hero-copy {{
            text-align: left;
        }}
        .brand {{
            font-family: Impact, 'Arial Black', sans-serif;
            font-size: 72px;
            font-weight: 900;
            letter-spacing: 0;
            text-transform: uppercase;
            line-height: 1;
            margin-bottom: 8px;
        }}
        .highlight {{
            position: relative;
            display: inline;
        }}
        .highlight::after {{
            content: '';
            position: absolute;
            bottom: 0.05em;
            left: -0.05em;
            right: -0.05em;
            height: 0.3em;
            background: #FFCC00;
            z-index: -1;
        }}
        .tagline {{
            font-size: 30px;
            line-height: 1.08;
            font-weight: 400;
            color: #555;
            margin-bottom: 28px;
            letter-spacing: 0;
        }}
        .hero-proof {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 24px;
        }}
        .proof-pill {{
            border: 1px solid #D7D1C6;
            border-radius: 999px;
            padding: 8px 12px;
            font-size: 13px;
            color: #333;
            background: #fff;
        }}
        .cta-container {{
            margin: 24px 0 32px 0;
            text-align: left;
        }}
        @media (max-width: 820px) {{
            .cta-container {{
                text-align: center;
            }}
        }}
        .cta-subtext {{
            font-size: 13px;
            color: #666;
            margin-bottom: 6px;
            font-weight: 500;
        }}
        .hero-visual {{
            position: relative;
            min-height: 570px;
        }}
        .phone-shot {{
            position: absolute;
            width: min(31vw, 250px);
            max-width: 250px;
            border-radius: 28px;
            box-shadow: 0 24px 64px rgba(17, 17, 17, 0.18);
        }}
        .phone-shot.recorder {{
            left: 0;
            top: 16px;
            transform: rotate(-4deg);
        }}
        .phone-shot.editor {{
            left: 30%;
            top: 58px;
            z-index: 2;
            box-shadow: 0 30px 80px rgba(17, 17, 17, 0.34), 0 10px 28px rgba(17, 17, 17, 0.24);
        }}
        .phone-shot.transcript {{
            right: 0;
            top: 16px;
            transform: rotate(4deg);
        }}
        .hero-note {{
            position: absolute;
            left: 12%;
            right: 12%;
            bottom: 12px;
            z-index: 10;
            background: #111;
            color: #fff;
            padding: 16px 18px;
            border-radius: 8px;
            font-size: 15px;
            line-height: 1.35;
            text-align: center;
        }}
        .features {{
            text-align: left;
            margin-bottom: 48px;
        }}
        .feature {{
            display: flex;
            align-items: flex-start;
            gap: 12px;
            margin-bottom: 20px;
        }}
        .feature-icon {{
            width: 32px;
            height: 32px;
            background: #111;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            font-size: 16px;
        }}
        .feature-text h3 {{
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 2px;
        }}
        .feature-text p {{
            font-size: 13px;
            color: #666;
            line-height: 1.4;
        }}
        .app-icon {{
            width: 128px;
            height: 128px;
            border-radius: 22.37%;
            box-shadow: 0 4px 24px rgba(0,0,0,0.12);
            margin-bottom: 24px;
        }}
        .use-cases {{
            text-align: left;
            margin-bottom: 48px;
        }}
        .use-cases h2 {{
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 8px;
        }}
        .use-cases p {{
            font-size: 13px;
            color: #666;
            line-height: 1.5;
            margin-bottom: 8px;
        }}
        .privacy-box {{
            background: #E8F5E9;
            border: 1px solid #4CAF50;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 48px;
            text-align: left;
        }}
        .privacy-box h2 {{
            font-size: 16px;
            font-weight: 700;
            color: #2E7D32;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .privacy-box p {{
            font-size: 13px;
            color: #388E3C;
            line-height: 1.5;
        }}
        .app-store-badge {{
            display: inline-block;
            margin-bottom: 32px;
        }}
        .app-store-badge img {{
            height: 54px;
        }}
        .divider {{
            width: 120px;
            height: 6px;
            background: #FFCC00;
            margin: 0 auto 32px;
        }}
        .lang-switch {{
            position: absolute;
            top: 16px;
            right: 24px;
            font-size: 13px;
            background: #fff;
            padding: 4px 12px;
            border-radius: 16px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }}
        .lang-switch a {{
            color: #666;
            text-decoration: none;
            margin: 0 4px;
        }}
        .lang-switch a.active {{
            font-weight: 700;
            color: #111;
        }}
        .lang-switch a:hover {{
            text-decoration: underline;
        }}
        footer {{
            margin: 64px auto 0;
            font-size: 13px;
            color: #777;
            text-align: left;
            width: 100%;
            max-width: 800px;
        }}
        .footer-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 32px;
            margin-bottom: 48px;
        }}
        .footer-col h4 {{
            font-size: 14px;
            color: #111;
            margin-bottom: 16px;
        }}
        .footer-col a {{
            display: block;
            color: #666;
            text-decoration: none;
            margin-bottom: 8px;
        }}
        .footer-col a:hover {{
            text-decoration: underline;
            color: #111;
        }}
        .copyright {{
            text-align: center;
            font-size: 12px;
            color: #999;
            border-top: 1px solid #eee;
            padding-top: 24px;
        }}
        .faq {{
            text-align: left;
            margin-bottom: 48px;
        }}
        .faq h2 {{
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 12px;
        }}
        .faq details {{
            margin-bottom: 8px;
            border-bottom: 1px solid #E0E0E0;
        }}
        .faq summary {{
            font-size: 14px;
            font-weight: 600;
            padding: 10px 0;
            cursor: pointer;
            list-style: none;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .faq summary::-webkit-details-marker {{ display: none; }}
        .faq summary::after {{
            content: '+';
            font-size: 18px;
            color: #999;
            transition: transform 0.2s;
        }}
        .faq details[open] summary::after {{
            content: '−';
        }}
        .faq details p {{
            font-size: 13px;
            color: #666;
            line-height: 1.5;
            padding: 0 0 12px;
        }}
        .how-it-works {{
            text-align: left;
            margin-bottom: 48px;
        }}
        .how-it-works h2 {{
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 12px;
        }}
        .step {{
            display: flex;
            align-items: flex-start;
            gap: 12px;
            margin-bottom: 16px;
        }}
        .step-number {{
            width: 24px;
            height: 24px;
            background: #FFCC00;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 13px;
            font-weight: 700;
            flex-shrink: 0;
        }}
        .step p {{
            font-size: 13px;
            color: #666;
            line-height: 1.4;
        }}
        .step strong {{
            color: #111;
        }}
        .callout {{
            background: #111;
            color: #fff;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 48px;
            text-align: center;
        }}
        .callout .stat {{
            font-family: Impact, 'Arial Black', sans-serif;
            font-size: 48px;
            letter-spacing: -0.03em;
            line-height: 1;
            margin-bottom: 4px;
        }}
        .callout .stat-label {{
            font-size: 14px;
            color: #999;
        }}
        @media (max-width: 820px) {{
            body {{ padding: 32px 18px; }}
            .hero {{
                min-height: auto;
                grid-template-columns: 1fr;
                gap: 28px;
            }}
            .hero-copy {{ text-align: center; }}
            .brand {{ font-size: 56px; }}
            .tagline {{ font-size: 25px; }}
            .hero-proof {{ justify-content: center; }}
            .hero-visual {{
                min-height: 500px;
                overflow: hidden;
            }}
            .phone-shot {{ width: 210px; }}
            .phone-shot.recorder {{ left: -6px; }}
            .phone-shot.editor {{ left: calc(50% - 105px); top: 46px; }}
            .phone-shot.transcript {{ right: -6px; }}
            .hero-note {{ left: 0; right: 0; bottom: 0; }}
        }}
    </style>
</head>
<body>
    <div class="lang-switch">
        <a href="/" class="{en_active}">EN</a> | 
        <a href="/de/" class="{de_active}">DE</a> | 
        <a href="/zh/" class="{zh_active}">ZH</a> | 
        <a href="/fr/" class="{fr_active}">FR</a> | 
        <a href="/vi/" class="{vi_active}">VI</a> | 
        <a href="/es/" class="{es_active}">ES</a>
    </div>
    <main class="container">
        <section class="hero">
            <div class="hero-copy">
                <img src="/icon.svg" alt="5cut app icon" class="app-icon">
                <h1 class="brand"><span class="highlight">{brand}</span>{brand_suffix}</h1>
                <h2 class="tagline">{tagline}</h2>
                <div class="hero-proof">
                    <span class="proof-pill">{proof1}</span>
                    <span class="proof-pill">{proof2}</span>
                    <span class="proof-pill">{proof3}</span>
                </div>
                <div class="cta-container">
                    <p class="cta-subtext">{cta_subtext}</p>
                    <a class="app-store-badge" href="https://apps.apple.com/app/5cut/id6758529319?ct=web_home">
                        <img src="https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg" alt="Download 5cut on the App Store">
                    </a>
                </div>
            </div>
            <div class="hero-visual" aria-label="5cut iPhone screenshots showing recording, editing, and transcript views">
                <img src="/assets/iphone-recorder.png" alt="5cut recorder screen" class="phone-shot recorder">
                <img src="/assets/iphone-transcript.png" alt="5cut transcript screen" class="phone-shot editor">
                <img src="/assets/iphone-editor.png" alt="5cut silence trimming editor" class="phone-shot transcript">
                <p class="hero-note">{hero_note_desc}</p>
            </div>
        </section>

        <div class="divider"></div>

        <article class="features">
            <div class="feature">
                <div class="feature-icon"><svg width="16" height="16" fill="none" stroke="white" stroke-width="2"><circle cx="8" cy="8" r="4"/><path d="M14 8a6 6 0 11-12 0 6 6 0 0112 0z"/></svg></div>
                <div class="feature-text">
                    <h3>{feat1_title}</h3>
                    <p>{feat1_desc}</p>
                </div>
            </div>
            <div class="feature">
                <div class="feature-icon"><svg width="16" height="16" fill="none" stroke="white" stroke-width="2"><path d="M4 2v12M12 2v12M1 8h14"/></svg></div>
                <div class="feature-text">
                    <h3>{feat2_title}</h3>
                    <p>{feat2_desc}</p>
                </div>
            </div>
            <div class="feature">
                <div class="feature-icon"><svg width="16" height="16" fill="none" stroke="white" stroke-width="2"><path d="M2 3h12v10H2z"/><path d="M5 7h6M5 9h4"/></svg></div>
                <div class="feature-text">
                    <h3>{feat3_title}</h3>
                    <p>{feat3_desc}</p>
                </div>
            </div>
            <div class="feature">
                <div class="feature-icon"><svg width="16" height="16" fill="none" stroke="white" stroke-width="2"><path d="M2 4h12M2 8h8M2 12h10"/></svg></div>
                <div class="feature-text">
                    <h3>{feat4_title}</h3>
                    <p>{feat4_desc}</p>
                </div>
            </div>
            <div class="feature">
                <div class="feature-icon"><svg width="16" height="16" fill="none" stroke="white" stroke-width="2"><circle cx="5" cy="6" r="3"/><circle cx="11" cy="6" r="3"/><path d="M2 14c0-2 2-3 3-3s3 1 3 3M8 14c0-2 2-3 3-3s3 1 3 3"/></svg></div>
                <div class="feature-text">
                    <h3>{feat5_title}</h3>
                    <p>{feat5_desc}</p>
                </div>
            </div>
        </article>

        <section class="how-it-works">
            <h2>{how_it_works}</h2>
            <div class="step">
                <div class="step-number">1</div>
                <p>{step1}</p>
            </div>
            <div class="step">
                <div class="step-number">2</div>
                <p>{step2}</p>
            </div>
            <div class="step">
                <div class="step-number">3</div>
                <p>{step3}</p>
            </div>
            <div class="step">
                <div class="step-number">4</div>
                <p>{step4}</p>
            </div>
        </section>

        <section class="use-cases">
            <h2>{perfect_for}</h2>
            <p>{perfect_for_desc1}</p>
            <p>{perfect_for_desc2}</p>
        </section>




        <section class="privacy-box">
            <h2><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>{privacy_title}</h2>
            <p>{privacy_desc}</p>
        </section>

        <div class="cta-container" style="text-align: center;">
            <p class="cta-subtext">{cta_subtext}</p>
            <a class="app-store-badge" href="https://apps.apple.com/app/5cut/id6758529319?ct=web_footer">
                <img src="https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg" alt="Download 5cut on the App Store">
            </a>
        </div>

        <section class="faq">
            <h2>{faq}</h2>
            <details>
                <summary>{faq1_q}</summary>
                <p>{faq1_a}</p>
            </details>
            <details>
                <summary>{faq2_q}</summary>
                <p>{faq2_a}</p>
            </details>
            <details>
                <summary>{faq3_q}</summary>
                <p>{faq3_a}</p>
            </details>
            <details>
                <summary>{faq4_q}</summary>
                <p>{faq4_a}</p>
            </details>
            <details>
                <summary>{faq5_q}</summary>
                <p>{faq5_a}</p>
            </details>
            <details>
                <summary>{faq6_q}</summary>
                <p>{faq6_a}</p>
            </details>
            <details>
                <summary>{faq7_q}</summary>
                <p>{faq7_a}</p>
            </details>
        </section>
    </main>

    <footer>
        <div class="footer-grid">
            <div class="footer-col">
                <h4>{footer_use_cases}</h4>
                <a href="{prefix}/use-cases/remove-silence-from-zoom/">Zoom Recordings</a>
                <a href="{prefix}/use-cases/remove-silence-from-obs/">OBS & Twitch VODs</a>
                <a href="{prefix}/remove-silence-from-lectures/">University Lectures</a>
                <a href="{prefix}/podcast-silence-remover/">Podcasts</a>
                <a href="{prefix}/free-jumpcut-app/">Jumpcut App</a>
                <a href="{prefix}/smartphone-video-editor/">Smartphone Editor</a>
            </div>
            <div class="footer-col">
                <h4>{footer_alternatives}</h4>
                <a href="{prefix}/alternatives/timebolt-alternative/">TimeBolt Alternative</a>
            </div>
            <div class="footer-col">
                <h4>{footer_study_fields}</h4>
                <a href="{prefix}/best-app-for-medical-school-lectures/">Medical School Lectures</a>
                <a href="{prefix}/best-app-for-law-school-recordings/">Law School Recordings</a>
            </div>
            <div class="footer-col">
                <h4>{footer_legal}</h4>
                <a href="/support/">Support & Contact</a>
                <a href="/privacy/">Privacy Policy</a>
                <a href="/terms/">Terms of Service</a>
                <a href="/impressum/">Impressum</a>
            </div>
        </div>
        <p class="copyright">&copy; 2026 Robin Sch&ouml;ppner</p>
    </footer>
</body>
</html>
"""

for lang, data in languages.items():
    directory = data["dir"]
    if directory != "." and not os.path.exists(directory):
        os.makedirs(directory)
    
    canonical_path = "/" if directory == "." else f"/{directory}/"
    
    # Setup active classes
    active_classes = {f"{l}_active": "active" if l == lang else "" for l in languages.keys()}
    
    prefix = "" if directory == "." else f"/{directory}"
    
    # Merge context
    context = {**data, **active_classes, "canonical_path": canonical_path, "prefix": prefix}
    
    output_html = html_template.format(**context)
    
    filepath = os.path.join(directory, "index.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(output_html)
        
    print(f"Generated {filepath}")
