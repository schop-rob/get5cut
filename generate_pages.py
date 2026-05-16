import os
import json

languages = {
    "en": {
        "dir": ".",
        "lang_code": "en",
        "title": "5cut – Record & Trim Lectures, Export Study Notes | iOS App",
        "description": "Record lectures and meetings directly on your iPhone. 5cut automatically trims silence, transcribes in 30+ languages, and exports clean study notes to Anki, Notion, and Obsidian. Perfect for students.",
        "og_title": "5cut – Record & Trim Lectures, Export Study Notes",
        "og_description": "Record lectures. Trim silence. Get a clean transcript and study notes. Free for iOS.",
        "brand": "5cut",
        "tagline": "Record lectures. Trim silence. Export study notes.",
        "stat1_value": "Notes + Anki",
        "stat1_label": "Export clean study materials in seconds",
        "feat1_title": "In-App Recorder & Bookmarks",
        "feat1_desc": "Record lectures, meetings, and interviews directly in the app. Add chapter bookmarks while recording. Live transcript generated on iOS 26+ devices.",
        "feat2_title": "Automatic Silence Removal",
        "feat2_desc": "Detect and cut dead air from lectures and podcasts. Use Smart Mode presets (Gentle, Moderate, Aggressive) or fine-tune the decibel threshold manually.",
        "feat3_title": "On-Device Transcription & AI Summaries",
        "feat3_desc": "Generate captions in 30+ languages. Get AI summaries, key points, and Q&A powered by Apple Foundation Models. All processed locally on your iPhone — no cloud uploads.",
        "feat4_title": "Export to Apple Notes, Anki & Notion",
        "feat4_desc": "Export a clean transcript with speaker labels and chapter markers directly to your favorite study tools, including Obsidian and auto-generated Anki cloze flashcards.",
        "feat5_title": "Speaker Identification",
        "feat5_desc": "Automatically identify up to 4 speakers in a single recording. Color-coded and renamable labels — perfect for seminars and group discussions.",
        "how_it_works": "How it works",
        "step1": "<strong>Record or Import</strong> a lecture directly in-app or from Files",
        "step2": "<strong>See the waveform</strong> — green is speech, red is silence",
        "step3": "<strong>Adjust the threshold</strong> or pick a Smart Mode preset",
        "step4": "<strong>Export.</strong> Done. Silence removed, study notes generated.",
        "privacy_title": "Privacy First: 100% On-Device",
        "privacy_desc": "We believe your recordings are yours. 5cut processes all audio, transcription, and AI summaries entirely on your iPhone or iPad. No audio or video is ever uploaded to a server, ensuring absolute privacy and compliance for students and professionals.",
        "perfect_for": "Perfect for",
        "perfect_for_desc1": "<a href=\"/remove-silence-from-lectures/\">Students reviewing recorded lectures</a> in a foreign language — whether you are <a href=\"/study-abroad/\">studying abroad</a> or taking online courses. Expats watching local news, and professionals dealing with <a href=\"/speed-up-zoom-recordings/\">Zoom recordings with awkward pauses</a> or <a href=\"/podcast-silence-remover/\">podcasts</a>.",
        "perfect_for_desc2": "Need subtitles? 5cut can also <a href=\"/transcribe-lectures/\">transcribe lectures in 30+ languages</a> directly on your device.",
        "faq": "Frequently asked questions",
        "faq1_q": "How does silence detection work?",
        "faq1_a": "5cut analyzes the audio waveform of your video on-device. Segments below the silence threshold are color-coded red. You can drag a slider to adjust what counts as \"silence,\" or use one of three Smart Mode presets.",
        "faq2_q": "Can I add subtitles to foreign language lectures?",
        "faq2_a": "Yes. 5cut includes on-device transcription supporting over 30 languages. You can burn subtitles directly into the video or export them as an SRT file. Everything is processed on your device.",
        "faq3_q": "Does it work with Zoom and online course recordings?",
        "faq3_a": "Yes. Import any MP4, MOV, or HEVC video. 5cut works with Zoom recordings, Microsoft Teams meetings, screen recordings, and any video file with an audio track.",
        "faq4_q": "Can I process a whole semester of lectures at once?",
        "faq4_a": "Yes. With batch processing (Premium), you can queue up multiple recordings and process them with individual or shared settings.",
        "faq5_q": "Is my data private?",
        "faq5_a": "Completely. All processing — silence detection, transcription, speaker identification — happens entirely on your device. No cloud uploads, no accounts, no data collection. Your videos never leave your phone.",
        "faq6_q": "How much does 5cut cost?",
        "faq6_a": "5cut is free to use with 10 exports per month. Premium removes the export limit and watermark for $1.99/month or a one-time $6.99 lifetime purchase.",
        "faq7_q": "What languages is the app available in?",
        "faq7_a": "The app interface is available in English, German, Spanish, French, Italian, Japanese, Korean, Portuguese (Brazil), Vietnamese, and Simplified Chinese.",
        "footer_use_cases": "Use Cases",
        "footer_alternatives": "Alternatives",
        "footer_legal": "Legal & Support"
    },
    "de": {
        "dir": "de",
        "lang_code": "de",
        "title": "5cut – Vorlesungen aufnehmen & schneiden, Lernnotizen exportieren | iOS App",
        "description": "Nimm Vorlesungen direkt auf deinem iPhone auf. 5cut entfernt automatisch Stille, transkribiert in 30+ Sprachen und exportiert saubere Lernnotizen zu Anki, Notion und Obsidian.",
        "og_title": "5cut – Vorlesungen aufnehmen & schneiden, Lernnotizen exportieren",
        "og_description": "Vorlesungen aufnehmen. Stille entfernen. Sauberes Transkript und Lernnotizen exportieren. Kostenlos für iOS.",
        "brand": "5cut",
        "tagline": "Vorlesungen aufnehmen. Stille entfernen. Lernnotizen exportieren.",
        "stat1_value": "Notizen + Anki",
        "stat1_label": "Saubere Lernmaterialien in Sekunden exportieren",
        "feat1_title": "In-App Recorder & Lesezeichen",
        "feat1_desc": "Nimm Vorlesungen und Meetings direkt in der App auf. Füge Kapitelmarken während der Aufnahme hinzu. Live-Transkripte auf iOS 26+ Geräten.",
        "feat2_title": "Stille automatisch entfernen",
        "feat2_desc": "Erkennt und schneidet Pausen aus Vorlesungen und Podcasts. Nutze den Smart-Mode (Sanft, Moderat, Aggressiv) oder passe den Schwellenwert selbst an.",
        "feat3_title": "On-Device Transkription & KI-Zusammenfassungen",
        "feat3_desc": "Generiere Untertitel in 30+ Sprachen. Erhalte KI-Zusammenfassungen und Q&A. Alles lokal auf deinem iPhone verarbeitet – kein Cloud-Upload.",
        "feat4_title": "Export zu Apple Notes, Anki & Notion",
        "feat4_desc": "Exportiere ein sauberes Transkript mit Sprechernamen und Kapitelmarken direkt in deine Lern-Tools, inklusive Obsidian und generierten Anki-Lernkarten.",
        "feat5_title": "Sprechererkennung",
        "feat5_desc": "Erkennt automatisch bis zu 4 Sprecher. Farbcodiert und umbenennbar – perfekt für Seminare, Interviews und Gruppengespräche.",
        "how_it_works": "So funktioniert's",
        "step1": "<strong>Aufnehmen oder Importieren</strong> einer Vorlesung direkt in der App oder aus Dateien",
        "step2": "<strong>Sieh die Wellenform</strong> – grün ist Sprache, rot ist Stille",
        "step3": "<strong>Passe den Schwellenwert an</strong> oder wähle einen Smart-Mode",
        "step4": "<strong>Exportieren.</strong> Fertig. Stille entfernt, Lernnotizen erstellt.",
        "privacy_title": "Privacy First: 100% On-Device",
        "privacy_desc": "Wir glauben, dass deine Aufnahmen dir gehören. 5cut verarbeitet Audio, Transkription und KI-Zusammenfassungen vollständig auf deinem iPhone oder iPad. Kein Audio oder Video wird jemals auf einen Server hochgeladen, was absolute Privatsphäre garantiert.",
        "perfect_for": "Perfekt für",
        "perfect_for_desc1": "<a href=\"/de/remove-silence-from-lectures/\">Studierende, die aufgenommene Vorlesungen</a> in einer Fremdsprache nacharbeiten – egal ob beim <a href=\"/study-abroad/\">Auslandsstudium</a> oder an der Online-Uni. Expats und Profis mit <a href=\"/speed-up-zoom-recordings/\">Zoom-Aufnahmen</a> oder <a href=\"/podcast-silence-remover/\">Podcasts</a>.",
        "perfect_for_desc2": "Benötigst du Untertitel? 5cut kann auch <a href=\"/transcribe-lectures/\">Vorlesungen in über 30 Sprachen transkribieren</a> – direkt auf deinem Gerät.",
        "faq": "Häufig gestellte Fragen",
        "faq1_q": "Wie funktioniert die Stille-Erkennung?",
        "faq1_a": "5cut analysiert die Audiowellenform deines Videos direkt auf dem Gerät. Segmente unterhalb des Stille-Schwellenwerts werden rot markiert. Du kannst den Schwellenwert per Schieberegler anpassen.",
        "faq2_q": "Kann ich Untertitel für fremdsprachige Vorlesungen erstellen?",
        "faq2_a": "Ja. 5cut bietet Transkription direkt auf dem Gerät in über 30 Sprachen. Untertitel können direkt ins Video eingebrannt oder als SRT exportiert werden.",
        "faq3_q": "Funktioniert es mit Zoom- und Online-Vorlesungen?",
        "faq3_a": "Ja. Importiere jedes MP4-, MOV- oder HEVC-Video. 5cut funktioniert mit Zoom-Aufnahmen, Microsoft-Teams-Meetings, Bildschirmaufnahmen und jedem Video mit Audiospur.",
        "faq4_q": "Kann ich ein ganzes Semester auf einmal verarbeiten?",
        "faq4_a": "Ja. Mit Stapelverarbeitung (Premium) kannst du mehrere Aufnahmen in die Warteschlange stellen.",
        "faq5_q": "Sind meine Daten sicher?",
        "faq5_a": "Absolut. Die gesamte Verarbeitung findet ausschließlich auf deinem Gerät statt. Kein Cloud-Upload, kein Account, keine Datenerfassung.",
        "faq6_q": "Was kostet 5cut?",
        "faq6_a": "5cut ist kostenlos mit 10 Exporten pro Monat. Premium entfernt das Exportlimit für 1,99 €/Monat oder einmalig 6,99 € (lebenslang).",
        "faq7_q": "In welchen Sprachen ist die App verfügbar?",
        "faq7_a": "Die App-Oberfläche ist verfügbar in Deutsch, Englisch, Spanisch, Französisch, Italienisch, Japanisch, Koreanisch, Portugiesisch, Vietnamesisch und vereinfachtem Chinesisch.",
        "footer_use_cases": "Use Cases",
        "footer_alternatives": "Alternativen",
        "footer_legal": "Rechtliches & Support"
    },
    "zh": {
        "dir": "zh",
        "lang_code": "zh-Hans",
        "title": "5cut – 录制并剪辑网课，导出学习笔记 | iOS 应用",
        "description": "直接在 iPhone 上录制讲座和会议。5cut 自动裁剪静音部分，支持 30 多种语言转写，并可导出清晰的学习笔记至 Anki、Notion 和 Obsidian。",
        "og_title": "5cut – 录制并剪辑网课，导出学习笔记",
        "og_description": "录制讲座。去除静音。获取清晰的文本和学习笔记。iOS 版免费下载。",
        "brand": "5cut",
        "tagline": "录制讲座。去除静音。导出学习笔记。",
        "stat1_value": "笔记 + Anki",
        "stat1_label": "秒级导出清晰的学习资料",
        "feat1_title": "应用内录音与书签",
        "feat1_desc": "直接在应用内录制讲座、会议和采访。在录制时添加章节书签。iOS 26+ 设备支持实时转写。",
        "feat2_title": "自动移除静音",
        "feat2_desc": "识别并剪切讲座和播客中的空白部分。使用智能模式（温和、适中、激进）或手动微调阈值。",
        "feat3_title": "设备端转写与 AI 摘要",
        "feat3_desc": "生成 30 多种语言的字幕，并获得 AI 摘要、要点和问答。全部在您的 iPhone 上本地处理——无需云端上传。",
        "feat4_title": "导出至 Apple Notes、Anki 和 Notion",
        "feat4_desc": "直接将带有发言人标签和章节标记的干净转写文稿导出到您最喜欢的学习工具（包括 Obsidian 和 Anki 填空卡片）中。",
        "feat5_title": "发言人识别",
        "feat5_desc": "自动识别录音中多达 4 位发言人。颜色标记并支持重命名，非常适合研讨会和小组讨论。",
        "how_it_works": "使用方法",
        "step1": "<strong>录制或导入</strong>应用内直接录音，或从文件导入课程",
        "step2": "<strong>查看波形图</strong> – 绿色代表语音，红色代表静音",
        "step3": "<strong>调整阈值</strong>或选择智能模式预设",
        "step4": "<strong>导出。</strong> 完成。静音已移除，学习笔记已生成。",
        "privacy_title": "隐私至上：100% 本地处理",
        "privacy_desc": "我们认为您的录音属于您自己。5cut 的所有音频处理、转写和 AI 摘要均完全在您的 iPhone 或 iPad 上运行。没有任何音频或视频会被上传到服务器，确保学生和专业人士的绝对隐私。",
        "perfect_for": "适用人群",
        "perfect_for_desc1": "<a href=\"/zh/remove-silence-from-lectures/\">复习外语网课的留学生</a> – 无论是在<a href=\"/study-abroad/\">留学</a>还是上在线课程。观看当地新闻的外派人员，以及需要处理<a href=\"/speed-up-zoom-recordings/\">冗长 Zoom 录制</a>或<a href=\"/podcast-silence-remover/\">播客</a>的专业人士。",
        "perfect_for_desc2": "需要字幕？5cut 还可以直接在您的设备上 <a href=\"/transcribe-lectures/\">转写 30 多种语言的课程</a>。",
        "faq": "常见问题",
        "faq1_q": "静音检测是如何工作的？",
        "faq1_a": "5cut 在设备本地分析视频音频波形。低于阈值的片段标记为红色。您可以手动调整滑块，或选择三种智能模式。",
        "faq2_q": "我可以为外语课生成字幕吗？",
        "faq2_a": "可以。5cut 支持 30 多种语言的设备端转写。字幕可嵌入视频或导出为 SRT。",
        "faq3_q": "支持 Zoom 或在线课程录制吗？",
        "faq3_a": "支持。可导入 MP4、MOV 或 HEVC 视频。适用于 Zoom 录制、Teams 会议、屏幕录像及任何带音轨的视频。",
        "faq4_q": "可以批量处理一整个学期的课吗？",
        "faq4_a": "可以。高级版支持批量处理，可加入队列并在后台运行。",
        "faq5_q": "我的数据隐私有保障吗？",
        "faq5_a": "绝对保障。所有处理过程均在本地完成。不上传云端，无需账号，不收集数据。",
        "faq6_q": "5cut 是收费的吗？",
        "faq6_a": "5cut 提供免费版，每月可导出 10 次。高级版（1.99 美元/月或 6.99 美元终身买断）可移除导出限制。",
        "faq7_q": "应用支持哪些语言？",
        "faq7_a": "应用界面支持简体中文、英语、德语、西班牙语、法语、意大利语、日语、韩语、葡萄牙语和越南语。",
        "footer_use_cases": "使用场景",
        "footer_alternatives": "替代方案",
        "footer_legal": "法律与支持"
    },
    "fr": {
        "dir": "fr",
        "lang_code": "fr",
        "title": "5cut – Enregistrez, Coupez & Exportez vos Notes de Cours | Application iOS",
        "description": "Enregistrez vos cours directement sur votre iPhone. 5cut coupe automatiquement les silences, transcrit en plus de 30 langues et exporte vos notes vers Anki, Notion et Obsidian.",
        "og_title": "5cut – Enregistrez, Coupez & Exportez vos Notes de Cours",
        "og_description": "Enregistrez vos cours. Supprimez les silences. Obtenez une transcription propre. Gratuit sur iOS.",
        "brand": "5cut",
        "tagline": "Enregistrez vos cours. Coupez les silences. Exportez vos notes.",
        "stat1_value": "Notes + Anki",
        "stat1_label": "Exportez votre matériel d'étude en quelques secondes",
        "feat1_title": "Enregistreur Intégré & Signets",
        "feat1_desc": "Enregistrez des cours, réunions et entretiens directement dans l'application. Ajoutez des signets. Transcription en direct sur iOS 26+.",
        "feat2_title": "Suppression Automatique des Silences",
        "feat2_desc": "Détectez et coupez les temps morts des cours et podcasts. Utilisez le mode intelligent ou ajustez le seuil manuellement.",
        "feat3_title": "Transcription & Résumés IA Locaux",
        "feat3_desc": "Générez des sous-titres dans plus de 30 langues. Obtenez des résumés IA et Q&R. Tout est traité localement sur votre iPhone — aucun téléversement.",
        "feat4_title": "Exportation vers Apple Notes, Anki & Notion",
        "feat4_desc": "Exportez une transcription propre avec les noms des locuteurs et des signets directement vers vos outils préférés, y compris les cartes Anki.",
        "feat5_title": "Identification des Locuteurs",
        "feat5_desc": "Identifiez automatiquement jusqu'à 4 locuteurs dans un enregistrement. Codes couleurs et noms modifiables — parfait pour les séminaires.",
        "how_it_works": "Comment ça marche",
        "step1": "<strong>Enregistrez ou Importez</strong> un cours directement dans l'application ou depuis vos Fichiers",
        "step2": "<strong>Voyez l'onde</strong> — vert = parole, rouge = silence",
        "step3": "<strong>Ajustez le seuil</strong> ou choisissez un mode intelligent",
        "step4": "<strong>Exportez.</strong> Terminé. Les silences sont supprimés, les notes générées.",
        "privacy_title": "Confidentialité Absolue : 100% Local",
        "privacy_desc": "Nous pensons que vos enregistrements vous appartiennent. 5cut traite tout l'audio, les transcriptions et les résumés IA entièrement sur votre iPhone ou iPad. Aucune donnée n'est envoyée sur un serveur, garantissant une confidentialité totale.",
        "perfect_for": "Parfait pour",
        "perfect_for_desc1": "Les étudiants qui révisent des cours enregistrés dans une langue étrangère — que vous <a href=\"/study-abroad/\">étudiiez à l'étranger</a> ou suiviez des cours en ligne. Les professionnels confrontés à des <a href=\"/speed-up-zoom-recordings/\">enregistrements Zoom avec des blancs</a> ou des <a href=\"/podcast-silence-remover/\">podcasts</a>.",
        "perfect_for_desc2": "Besoin de sous-titres ? 5cut peut aussi <a href=\"/transcribe-lectures/\">transcrire des cours dans plus de 30 langues</a> directement sur votre appareil.",
        "faq": "Foire aux questions",
        "faq1_q": "Comment fonctionne la détection des silences ?",
        "faq1_a": "5cut analyse l'onde audio sur votre appareil. Les segments sous le seuil de silence sont colorés en rouge. Vous pouvez ajuster le curseur pour définir le \"silence\".",
        "faq2_q": "Puis-je ajouter des sous-titres à des cours en langue étrangère ?",
        "faq2_a": "Oui. 5cut inclut une transcription sur l'appareil pour plus de 30 langues. Vous pouvez intégrer les sous-titres à la vidéo ou exporter en SRT.",
        "faq3_q": "Cela fonctionne-t-il avec les enregistrements Zoom ?",
        "faq3_a": "Oui. Importez n'importe quelle vidéo MP4, MOV ou HEVC. 5cut fonctionne avec Zoom, Teams et les enregistrements d'écran.",
        "faq4_q": "Puis-je traiter tout un semestre de cours à la fois ?",
        "faq4_a": "Oui. Avec le traitement par lots (Premium), vous pouvez mettre en file d'attente plusieurs enregistrements.",
        "faq5_q": "Mes données sont-elles privées ?",
        "faq5_a": "Complètement. Tout le traitement se fait sur votre appareil. Pas de cloud, pas de compte, pas de collecte de données.",
        "faq6_q": "Combien coûte 5cut ?",
        "faq6_a": "5cut est gratuit avec 10 exportations par mois. La version Premium supprime la limite pour 1,99 $/mois ou un achat unique de 6,99 $.",
        "faq7_q": "Quelles sont les langues disponibles pour l'application ?",
        "faq7_a": "L'interface est disponible en anglais, allemand, espagnol, français, italien, japonais, coréen, portugais, vietnamien et chinois.",
        "footer_use_cases": "Cas d'utilisation",
        "footer_alternatives": "Alternatives",
        "footer_legal": "Légal & Support"
    },
    "vi": {
        "dir": "vi",
        "lang_code": "vi",
        "title": "5cut – Ghi Âm, Cắt Bỏ Khoảng Lặng & Xuất Ghi Chú | Ứng Dụng iOS",
        "description": "Ghi âm bài giảng trực tiếp trên iPhone. 5cut tự động cắt khoảng lặng, tạo phụ đề 30+ ngôn ngữ và xuất ghi chú học tập sạch sẽ sang Anki, Notion, và Obsidian.",
        "og_title": "5cut – Ghi Âm & Cắt Khoảng Lặng, Xuất Ghi Chú Học Tập",
        "og_description": "Ghi âm bài giảng. Cắt bỏ khoảng lặng. Nhận bản ghi chép và ghi chú học tập. Miễn phí cho iOS.",
        "brand": "5cut",
        "tagline": "Ghi âm bài giảng. Cắt bỏ khoảng lặng. Xuất ghi chú.",
        "stat1_value": "Ghi Chú + Anki",
        "stat1_label": "Xuất tài liệu học tập chỉ trong vài giây",
        "feat1_title": "Máy Ghi Âm Tích Hợp & Đánh Dấu",
        "feat1_desc": "Ghi âm bài giảng, cuộc họp và phỏng vấn ngay trong ứng dụng. Thêm dấu trang chương. Tạo bản ghi chép trực tiếp trên iOS 26+.",
        "feat2_title": "Tự Động Xóa Khoảng Lặng",
        "feat2_desc": "Phát hiện và cắt bỏ những khoảng trống từ bài giảng và podcast. Sử dụng chế độ Thông Minh hoặc tự điều chỉnh ngưỡng âm thanh.",
        "feat3_title": "Tạo Phụ Đề & Tóm Tắt AI Trên Thiết Bị",
        "feat3_desc": "Tạo phụ đề bằng 30+ ngôn ngữ. Nhận tóm tắt AI và Q&A. Tất cả được xử lý cục bộ trên iPhone của bạn — không cần tải lên đám mây.",
        "feat4_title": "Xuất Sang Apple Notes, Anki & Notion",
        "feat4_desc": "Xuất bản ghi chép sạch sẽ với nhãn người nói và dấu trang chương trực tiếp sang các công cụ học tập yêu thích của bạn, bao gồm thẻ ghi nhớ Anki.",
        "feat5_title": "Nhận Diện Người Nói",
        "feat5_desc": "Tự động nhận diện tối đa 4 người nói trong một bản ghi âm. Có mã màu và có thể đổi tên — hoàn hảo cho các cuộc hội thảo.",
        "how_it_works": "Cách hoạt động",
        "step1": "<strong>Ghi âm hoặc Nhập</strong> một bài giảng trực tiếp trong ứng dụng hoặc từ Tệp",
        "step2": "<strong>Xem biểu đồ âm thanh</strong> — xanh là giọng nói, đỏ là khoảng lặng",
        "step3": "<strong>Điều chỉnh ngưỡng</strong> hoặc chọn chế độ Thông Minh",
        "step4": "<strong>Xuất.</strong> Xong. Khoảng lặng đã được xóa, ghi chú học tập được tạo.",
        "privacy_title": "Quyền Riêng Tư: 100% Xử Lý Trên Thiết Bị",
        "privacy_desc": "Chúng tôi tin rằng bản ghi âm thuộc về bạn. 5cut xử lý tất cả âm thanh, tạo phụ đề và tóm tắt AI hoàn toàn trên iPhone hoặc iPad của bạn. Không có âm thanh hoặc video nào được tải lên máy chủ.",
        "perfect_for": "Hoàn hảo cho",
        "perfect_for_desc1": "Sinh viên ôn tập các bài giảng được ghi lại bằng ngoại ngữ — cho dù bạn đang <a href=\"/study-abroad/\">du học</a> hay học trực tuyến. Các chuyên gia xử lý <a href=\"/speed-up-zoom-recordings/\">các bản ghi Zoom có nhiều khoảng trống</a> hoặc <a href=\"/podcast-silence-remover/\">podcast</a>.",
        "perfect_for_desc2": "Cần phụ đề? 5cut cũng có thể <a href=\"/transcribe-lectures/\">tạo phụ đề cho bài giảng bằng 30+ ngôn ngữ</a> trực tiếp trên thiết bị của bạn.",
        "faq": "Câu hỏi thường gặp",
        "faq1_q": "Tính năng phát hiện khoảng lặng hoạt động như thế nào?",
        "faq1_a": "5cut phân tích biểu đồ âm thanh trên thiết bị. Các phân đoạn dưới ngưỡng im lặng được tô màu đỏ. Bạn có thể kéo thanh trượt để điều chỉnh.",
        "faq2_q": "Tôi có thể thêm phụ đề vào các bài giảng bằng tiếng nước ngoài không?",
        "faq2_a": "Có. 5cut bao gồm khả năng tạo phụ đề trên thiết bị hỗ trợ hơn 30 ngôn ngữ. Bạn có thể xuất dưới dạng tệp SRT.",
        "faq3_q": "Ứng dụng có hoạt động với các bản ghi Zoom không?",
        "faq3_a": "Có. Nhập bất kỳ video MP4, MOV hoặc HEVC nào. 5cut hoạt động với các bản ghi Zoom, Microsoft Teams và bất kỳ tệp video nào có rãnh âm thanh.",
        "faq4_q": "Tôi có thể xử lý toàn bộ bài giảng của một học kỳ cùng lúc không?",
        "faq4_a": "Có. Với tính năng xử lý hàng loạt (Premium), bạn có thể xếp hàng nhiều bản ghi âm.",
        "faq5_q": "Dữ liệu của tôi có riêng tư không?",
        "faq5_a": "Hoàn toàn. Tất cả quá trình xử lý diễn ra hoàn toàn trên thiết bị của bạn. Không tải lên đám mây, không thu thập dữ liệu.",
        "faq6_q": "5cut có giá bao nhiêu?",
        "faq6_a": "5cut miễn phí với 10 lần xuất mỗi tháng. Gói Premium loại bỏ giới hạn xuất với giá $1.99/tháng hoặc mua một lần trọn đời $6.99.",
        "faq7_q": "Ứng dụng có sẵn bằng những ngôn ngữ nào?",
        "faq7_a": "Giao diện ứng dụng có sẵn bằng tiếng Anh, Đức, Tây Ban Nha, Pháp, Ý, Nhật Bản, Hàn Quốc, Bồ Đào Nha, Tiếng Việt và Tiếng Trung.",
        "footer_use_cases": "Trường hợp sử dụng",
        "footer_alternatives": "Các lựa chọn thay thế",
        "footer_legal": "Pháp lý & Hỗ trợ"
    },
    "es": {
        "dir": "es",
        "lang_code": "es",
        "title": "5cut – Graba y Recorta Clases, Exporta Apuntes | App para iOS",
        "description": "Graba clases y reuniones en tu iPhone. 5cut recorta el silencio automáticamente, transcribe en más de 30 idiomas y exporta apuntes limpios a Anki, Notion y Obsidian.",
        "og_title": "5cut – Graba y Recorta Clases, Exporta Apuntes",
        "og_description": "Graba clases. Recorta silencios. Obtén una transcripción limpia y apuntes. Gratis para iOS.",
        "brand": "5cut",
        "tagline": "Graba clases. Recorta el silencio. Exporta apuntes.",
        "stat1_value": "Apuntes + Anki",
        "stat1_label": "Exporta material de estudio limpio en segundos",
        "feat1_title": "Grabadora Integrada y Marcadores",
        "feat1_desc": "Graba clases, reuniones y entrevistas en la app. Añade marcadores de capítulo al grabar. Transcripción en vivo en dispositivos iOS 26+.",
        "feat2_title": "Eliminación Automática de Silencios",
        "feat2_desc": "Detecta y recorta silencios en clases y podcasts. Usa modos inteligentes (Suave, Moderado, Agresivo) o ajusta el umbral manualmente.",
        "feat3_title": "Transcripción y Resúmenes IA Locales",
        "feat3_desc": "Genera subtítulos en más de 30 idiomas. Obtén resúmenes IA y preguntas y respuestas. Todo se procesa localmente en tu iPhone — sin la nube.",
        "feat4_title": "Exportar a Apple Notes, Anki y Notion",
        "feat4_desc": "Exporta una transcripción limpia con etiquetas de altavoz y marcadores directamente a tus herramientas de estudio favoritas, incluyendo tarjetas Anki.",
        "feat5_title": "Identificación de Oradores",
        "feat5_desc": "Identifica automáticamente hasta 4 oradores en una sola grabación. Etiquetas con códigos de colores y renombrables — ideal para seminarios.",
        "how_it_works": "Cómo funciona",
        "step1": "<strong>Graba o Importa</strong> una clase directamente en la app o desde Archivos",
        "step2": "<strong>Mira la forma de onda</strong> — el verde es habla, el rojo es silencio",
        "step3": "<strong>Ajusta el umbral</strong> o elige un modo inteligente",
        "step4": "<strong>Exporta.</strong> Listo. Silencios eliminados, apuntes generados.",
        "privacy_title": "Privacidad Ante Todo: 100% en el Dispositivo",
        "privacy_desc": "Creemos que tus grabaciones te pertenecen. 5cut procesa el audio, las transcripciones y los resúmenes IA completamente en tu iPhone o iPad. Nunca se sube audio ni video a ningún servidor, garantizando privacidad absoluta.",
        "perfect_for": "Perfecto para",
        "perfect_for_desc1": "Estudiantes que revisan clases grabadas en un idioma extranjero — ya sea que estés <a href=\"/study-abroad/\">estudiando en el extranjero</a> o tomando cursos en línea. Expatriados y profesionales que lidian con <a href=\"/speed-up-zoom-recordings/\">grabaciones de Zoom con pausas incómodas</a> o <a href=\"/podcast-silence-remover/\">podcasts</a>.",
        "perfect_for_desc2": "¿Necesitas subtítulos? 5cut también puede <a href=\"/transcribe-lectures/\">transcribir clases en más de 30 idiomas</a> directamente en tu dispositivo.",
        "faq": "Preguntas frecuentes",
        "faq1_q": "¿Cómo funciona la detección de silencios?",
        "faq1_a": "5cut analiza la forma de onda de audio de tu video en el dispositivo. Los segmentos por debajo del umbral de silencio se marcan en rojo. Puedes ajustar el control deslizante para definir el \"silencio\".",
        "faq2_q": "¿Puedo agregar subtítulos a clases en idiomas extranjeros?",
        "faq2_a": "Sí. 5cut incluye transcripción en el dispositivo compatible con más de 30 idiomas. Puedes incrustar subtítulos en el video o exportarlos como un archivo SRT.",
        "faq3_q": "¿Funciona con Zoom y grabaciones de cursos en línea?",
        "faq3_a": "Sí. Importa cualquier video MP4, MOV o HEVC. 5cut funciona con grabaciones de Zoom, Microsoft Teams y cualquier archivo de video con una pista de audio.",
        "faq4_q": "¿Puedo procesar todo un semestre de clases a la vez?",
        "faq4_a": "Sí. Con el procesamiento por lotes (Premium), puedes poner en cola varias grabaciones.",
        "faq5_q": "¿Son privados mis datos?",
        "faq5_a": "Completamente. Todo el procesamiento ocurre en tu dispositivo. No hay subidas a la nube, cuentas, ni recopilación de datos.",
        "faq6_q": "¿Cuánto cuesta 5cut?",
        "faq6_a": "5cut es gratis con 10 exportaciones al mes. Premium elimina el límite por $1.99/mes o una compra única de $6.99.",
        "faq7_q": "¿En qué idiomas está disponible la aplicación?",
        "faq7_a": "La interfaz está disponible en inglés, alemán, español, francés, italiano, japonés, coreano, portugués, vietnamita y chino simplificado.",
        "footer_use_cases": "Casos de uso",
        "footer_alternatives": "Alternativas",
        "footer_legal": "Legal y Soporte"
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
    <meta property="og:image" content="https://get5cut.com/apple-touch-icon.png">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{og_title}">
    <meta name="twitter:description" content="{og_description}">
    <meta name="twitter:image" content="https://get5cut.com/apple-touch-icon.png">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "5cut",
        "operatingSystem": "iOS",
        "applicationCategory": "MultimediaApplication",
        "description": "{description}",
        "offers": [
            {{
                "@type": "Offer",
                "price": "0",
                "priceCurrency": "USD",
                "description": "Free tier with 10 exports per month"
            }},
            {{
                "@type": "Offer",
                "price": "1.99",
                "priceCurrency": "USD",
                "description": "Monthly subscription for unlimited exports",
                "priceSpecification": {{
                    "@type": "UnitPriceSpecification",
                    "billingDuration": "P1M"
                }}
            }},
            {{
                "@type": "Offer",
                "price": "6.99",
                "priceCurrency": "USD",
                "description": "Lifetime one-time purchase"
            }}
        ],
        "featureList": "In-app recorder, AI summaries, Export to Apple Notes/Anki/Notion/Obsidian, Silence removal, on-device transcription in 30+ languages, speaker identification",
        "screenshot": "https://get5cut.com/apple-touch-icon.png",
        "softwareVersion": "1.0"
    }}
    </script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif;
            background: #F5F5F5;
            color: #111;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 40px 24px;
        }}
        .container {{
            max-width: 480px;
            width: 100%;
            text-align: center;
        }}
        .brand {{
            font-family: Impact, 'Arial Black', sans-serif;
            font-size: 96px;
            font-weight: 900;
            letter-spacing: -0.04em;
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
            font-size: 18px;
            font-weight: 400;
            color: #555;
            margin-bottom: 48px;
            letter-spacing: 0.02em;
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
        .use-cases h3 {{
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
        .privacy-box h3 {{
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
            margin-top: 64px;
            font-size: 13px;
            color: #777;
            text-align: left;
            width: 100%;
            max-width: 800px;
        }}
        .footer-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
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
        .faq h3 {{
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
        .how-it-works h3 {{
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
        <img src="/icon.svg" alt="5cut app icon" class="app-icon">
        <h1 class="brand"><span class="highlight">{brand}</span></h1>
        <h2 class="tagline">{tagline}</h2>

        <div class="divider"></div>

        <div class="callout">
            <div class="stat">{stat1_value}</div>
            <div class="stat-label">{stat1_label}</div>
        </div>

        <section class="privacy-box">
            <h3><svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>{privacy_title}</h3>
            <p>{privacy_desc}</p>
        </section>

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
            <h3>{how_it_works}</h3>
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
            <h3>{perfect_for}</h3>
            <p>{perfect_for_desc1}</p>
            <p>{perfect_for_desc2}</p>
        </section>

        <a class="app-store-badge" href="https://apps.apple.com/app/5cut/id6758529319">
            <img src="https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg" alt="Download 5cut on the App Store">
        </a>

        <section class="faq">
            <h3>{faq}</h3>
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
                <a href="/use-cases/remove-silence-from-zoom/">Zoom Recordings</a>
                <a href="/use-cases/remove-silence-from-obs/">OBS & Twitch VODs</a>
                <a href="/remove-silence-from-lectures/">University Lectures</a>
                <a href="/podcast-silence-remover/">Podcasts</a>
            </div>
            <div class="footer-col">
                <h4>{footer_alternatives}</h4>
                <a href="/alternatives/timebolt-alternative/">TimeBolt Alternative</a>
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
    
    # Merge context
    context = {**data, **active_classes, "canonical_path": canonical_path}
    
    output_html = html_template.format(**context)
    
    filepath = os.path.join(directory, "index.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(output_html)
        
    print(f"Generated {filepath}")
