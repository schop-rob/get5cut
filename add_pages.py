import os
import ast

def add_translations():
    target_file = '/Users/robinschoppner/Downloads/StudyTrim/get5cut/data_pages.py'
    
    # Read the current content
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_pages = {
        "offline-lecture-transcription-iphone": {
            "en": {
                "title": "Offline Lecture Transcription on iPhone – No Internet Required | 5cut",
                "desc": "Transcribe lecture recordings offline on iPhone. No cloud, no upload, no internet needed. On-device AI in 30+ languages. Speaker identification. Export as SRT or text. Free iOS app.",
                "h1": "Offline Lecture Transcription on iPhone",
                "tagline": "Transcribe offline on iPhone. No Internet Required.",
                "intro": """<p>Most transcription apps require internet. You upload your lecture to a server, wait for processing, and hope the cloud service handles your data responsibly. 5cut works differently: it transcribes entirely on your iPhone, with no internet connection required after the initial model download.</p>
<h2>How offline transcription works</h2>
<p>5cut uses on-device AI models that run directly on your iPhone's Neural Engine. The first time you select a language, the model downloads (typically 40-600 MB depending on the engine). After that, transcription works in airplane mode, on the subway, in a lecture hall with terrible WiFi — anywhere.</p>
<h2>Four transcription engines</h2>
<p>5cut offers multiple AI engines so you can choose the right balance of speed, accuracy, and model size:</p>
<table class="engine-table">
    <tr><th>Engine</th><th>Languages</th><th>Model size</th><th>Best for</th></tr>
    <tr><td>Apple Speech</td><td>40+</td><td>Built-in</td><td>Quick transcription, broadest language support</td></tr>
    <tr><td>WhisperKit</td><td>30+</td><td>39 MB – 1.5 GB</td><td>High accuracy, word-level timestamps</td></tr>
    <tr><td>Parakeet</td><td>25 European</td><td>~200 MB</td><td>European languages, auto-detection</td></tr>
    <tr><td>Qwen3-ASR</td><td>30+</td><td>~700 MB</td><td>Multilingual, large vocabulary</td></tr>
</table>
<h2>Why offline matters</h2>
<ul>
    <li><strong>Privacy</strong> — lecture recordings with sensitive content never leave your device</li>
    <li><strong>No data caps</strong> — transcribe hours of recordings without eating into your mobile data plan</li>
    <li><strong>Works everywhere</strong> — campus basements, trains, planes, libraries with blocked WiFi</li>
    <li><strong>No per-minute costs</strong> — cloud transcription services charge per minute. On-device is free after the model download</li>
    <li><strong>Speed</strong> — no upload/download wait. Transcription starts immediately</li>
</ul>
<h2>Supported languages</h2>
<p>Between all four engines, 5cut supports transcription in over 40 languages. The exact list depends on which engine you choose and the language models available for your device.</p>
<h2>Beyond transcription: remove silence too</h2>
<p>5cut is primarily a silence removal tool. The typical workflow is:</p>
<ol>
    <li>Import or record a lecture</li>
    <li>Remove silence automatically (saves 20-35% of the recording)</li>
    <li>Transcribe the condensed version offline</li>
    <li>Export: video with burned-in subtitles, SRT file, or plain text transcript</li>
</ol>
<p>Silence removal also works fully offline — it's a waveform analysis that never needs internet.</p>
<h2>Speaker identification</h2>
<p>5cut can identify up to 4 speakers in a recording and color-code them in the transcript. This works offline too. Useful for lectures with Q&A, seminars, or group presentations.</p>
<h2>Free to start</h2>
<p>5cut combines on-device transcription, silence removal, subtitles, and batch processing so long recordings can become searchable study material.</p>"""
            },
            "de": {
                "title": "Offline Vorlesungen transkribieren auf dem iPhone – Kein Internet nötig | 5cut",
                "desc": "Vorlesungsaufnahmen offline auf dem iPhone transkribieren. Keine Cloud, kein Upload, kein Internet nötig. On-Device-KI in 30+ Sprachen. Sprechererkennung. Export als SRT oder Text. Kostenlose iOS-App.",
                "h1": "Offline Vorlesungen transkribieren auf dem iPhone",
                "tagline": "Offline auf dem iPhone transkribieren. Kein Internet erforderlich.",
                "intro": """<p>Die meisten Transkriptions-Apps brauchen Internet. Du lädst deine Vorlesung auf einen Server hoch, wartest auf die Verarbeitung und hoffst, dass der Cloud-Dienst verantwortungsvoll mit deinen Daten umgeht. 5cut funktioniert anders: Es transkribiert vollständig auf deinem iPhone, ohne Internetverbindung nach dem einmaligen Modell-Download.</p>
<h2>Wie Offline-Transkription funktioniert</h2>
<p>5cut nutzt On-Device-KI-Modelle, die direkt auf der Neural Engine deines iPhones laufen. Beim ersten Mal, wenn du eine Sprache auswählst, wird das Modell heruntergeladen (typischerweise 40-600 MB je nach Engine). Danach funktioniert die Transkription im Flugmodus, in der U-Bahn, in einem Hörsaal mit schlechtem WLAN – überall.</p>
<h2>Vier Transkriptions-Engines</h2>
<p>5cut bietet mehrere KI-Engines, damit du die richtige Balance aus Geschwindigkeit, Genauigkeit und Modellgröße wählen kannst:</p>
<table class="engine-table">
    <tr><th>Engine</th><th>Sprachen</th><th>Modellgröße</th><th>Ideal für</th></tr>
    <tr><td>Apple Speech</td><td>40+</td><td>Integriert</td><td>Schnelle Transkription, breiteste Sprachunterstützung</td></tr>
    <tr><td>WhisperKit</td><td>30+</td><td>39 MB – 1,5 GB</td><td>Hohe Genauigkeit, Wort-Level-Zeitstempel</td></tr>
    <tr><td>Parakeet</td><td>25 europäische</td><td>~200 MB</td><td>Europäische Sprachen, Auto-Erkennung</td></tr>
    <tr><td>Qwen3-ASR</td><td>30+</td><td>~700 MB</td><td>Multilingual, großes Vokabular</td></tr>
</table>
<h2>Warum Offline wichtig ist</h2>
<ul>
    <li><strong>Datenschutz</strong> – Vorlesungsaufnahmen mit sensiblen Inhalten verlassen nie dein Gerät</li>
    <li><strong>Keine Datenvolumen-Kosten</strong> – stundenlange Aufnahmen transkribieren ohne mobiles Datenvolumen zu verbrauchen</li>
    <li><strong>Funktioniert überall</strong> – Kellerräume, Züge, Flugzeuge, Bibliotheken mit gesperrtem WLAN</li>
    <li><strong>Keine Minutenkosten</strong> – Cloud-Dienste berechnen pro Minute. On-Device ist kostenlos</li>
    <li><strong>Geschwindigkeit</strong> – kein Upload-/Download-Warten. Transkription startet sofort</li>
</ul>
<h2>Unterstützte Sprachen</h2>
<p>5cut unterstützt die Transkription in über 40 Sprachen. Die genaue Liste hängt von der gewählten Engine ab.</p>
<h2>Über Transkription hinaus: auch Stille entfernen</h2>
<p>5cut ist primär ein Stille-Entfernungs-Tool. Der typische Workflow ist:</p>
<ol>
    <li>Vorlesung importieren oder aufnehmen</li>
    <li>Stille automatisch entfernen (spart 20-35% der Aufnahme)</li>
    <li>Die gekürzte Version offline transkribieren</li>
    <li>Exportieren: Video mit eingebrannten Untertiteln, SRT-Datei oder Text-Transkript</li>
</ol>
<p>Die Stille-Entfernung funktioniert ebenfalls komplett offline.</p>
<h2>Sprechererkennung</h2>
<p>5cut kann bis zu 4 Sprecher identifizieren und im Transkript farblich markieren. Dies funktioniert ebenfalls offline.</p>
<h2>Kostenlos starten</h2>
<p>5cut kombiniert On-Device-Transkription, Stille-Entfernung, Untertitel und Stapelverarbeitung.</p>"""
            },
            "fr": {
                "title": "Transcription de Cours Hors Ligne sur iPhone – Sans Internet | 5cut",
                "desc": "Transcrivez vos cours hors ligne sur iPhone. Pas de cloud, pas de téléversement, pas d'internet. IA locale en 30+ langues. App iOS gratuite.",
                "h1": "Transcription de Cours Hors Ligne sur iPhone",
                "tagline": "Transcrivez hors ligne. Sans internet.",
                "intro": """<p>La plupart des applications de transcription nécessitent internet. 5cut fonctionne différemment : il transcrit entièrement sur votre iPhone, sans connexion requise après le téléchargement initial du modèle.</p>
<h2>Comment fonctionne la transcription hors ligne</h2>
<p>5cut utilise des modèles d'IA locaux qui s'exécutent sur le Neural Engine de votre iPhone. La transcription fonctionne en mode avion, dans le métro, n'importe où.</p>
<h2>Quatre moteurs de transcription</h2>
<table class="engine-table">
    <tr><th>Moteur</th><th>Langues</th><th>Taille</th><th>Idéal pour</th></tr>
    <tr><td>Apple Speech</td><td>40+</td><td>Intégré</td><td>Transcription rapide, large choix de langues</td></tr>
    <tr><td>WhisperKit</td><td>30+</td><td>39 MB – 1,5 GB</td><td>Haute précision, horodatage</td></tr>
    <tr><td>Parakeet</td><td>25 européennes</td><td>~200 MB</td><td>Détection automatique</td></tr>
    <tr><td>Qwen3-ASR</td><td>30+</td><td>~700 MB</td><td>Multilingue, grand vocabulaire</td></tr>
</table>
<h2>Pourquoi le hors ligne est important</h2>
<ul>
    <li><strong>Confidentialité</strong> – les enregistrements ne quittent jamais votre appareil</li>
    <li><strong>Sans frais de données</strong> – transcrivez sans consommer votre forfait mobile</li>
    <li><strong>Fonctionne partout</strong> – sous-sols, trains, avions</li>
    <li><strong>Sans coût à la minute</strong> – le traitement local est gratuit</li>
    <li><strong>Vitesse</strong> – pas d'attente de téléchargement</li>
</ul>
<h2>Au-delà de la transcription : suppression des silences</h2>
<ol>
    <li>Importez ou enregistrez un cours</li>
    <li>Supprimez les silences automatiquement</li>
    <li>Transcrivez la version condensée hors ligne</li>
    <li>Exportez les sous-titres, SRT ou texte</li>
</ol>
<h2>Identification des locuteurs</h2>
<p>5cut identifie jusqu'à 4 locuteurs. Utile pour les questions/réponses et séminaires.</p>
<h2>Gratuit pour commencer</h2>
<p>5cut combine transcription locale, suppression des silences, sous-titres et traitement par lots.</p>"""
            },
            "zh": {
                "title": "在 iPhone 上离线转写讲座 – 无需互联网 | 5cut",
                "desc": "在 iPhone 上离线转写讲座录音。无云端，无上传，无需网络。支持 30+ 种语言的设备端 AI。免费 iOS 应用。",
                "h1": "在 iPhone 上离线转写讲座",
                "tagline": "在 iPhone 上离线转写。无需互联网。",
                "intro": """<p>大多数转写应用都需要连接互联网。5cut 与众不同：它完全在您的 iPhone 上进行转写，在初始模型下载之后无需任何网络连接。</p>
<h2>离线转写的工作原理</h2>
<p>5cut 使用直接在 iPhone 神经网络引擎上运行的设备端 AI 模型。转写功能可以在飞行模式、地铁或没有 WiFi 的教室中完美运行。</p>
<h2>四种转写引擎</h2>
<table class="engine-table">
    <tr><th>引擎</th><th>语言</th><th>模型大小</th><th>最佳用途</th></tr>
    <tr><td>Apple Speech</td><td>40+</td><td>内置</td><td>快速转写，支持最广泛</td></tr>
    <tr><td>WhisperKit</td><td>30+</td><td>39 MB – 1.5 GB</td><td>高精度，词级时间戳</td></tr>
    <tr><td>Parakeet</td><td>25 种欧洲语言</td><td>~200 MB</td><td>自动检测</td></tr>
    <tr><td>Qwen3-ASR</td><td>30+</td><td>~700 MB</td><td>多语言，大词汇量</td></tr>
</table>
<h2>为什么离线很重要</h2>
<ul>
    <li><strong>隐私</strong> – 敏感录音绝不离开您的设备</li>
    <li><strong>无数据限制</strong> – 转写数小时的录音而不用担心流量</li>
    <li><strong>随处可用</strong> – 校园地下室、火车、飞机上</li>
    <li><strong>无按分钟收费</strong> – 设备端处理完全免费</li>
    <li><strong>速度</strong> – 无需等待上传/下载</li>
</ul>
<h2>超越转写：自动去除静音</h2>
<ol>
    <li>导入或录制讲座</li>
    <li>自动去除静音</li>
    <li>离线转写精简后的版本</li>
    <li>导出：带字幕的视频、SRT 或文本</li>
</ol>
<h2>说话人识别</h2>
<p>5cut 可识别多达 4 位说话人并在转写中标记。这同样在离线状态下运行。</p>
<h2>免费开始使用</h2>
<p>5cut 将设备端转写、静音移除、字幕和批量处理结合在一起。</p>"""
            },
            "vi": {
                "title": "Phiên Âm Bài Giảng Ngoại Tuyến Trên iPhone – Không Cần Internet | 5cut",
                "desc": "Phiên âm bản ghi bài giảng ngoại tuyến trên iPhone. Không cần đám mây, không tải lên, không cần internet. Ứng dụng iOS miễn phí.",
                "h1": "Phiên Âm Bài Giảng Ngoại Tuyến Trên iPhone",
                "tagline": "Phiên âm ngoại tuyến trên iPhone. Không cần Internet.",
                "intro": """<p>Hầu hết các ứng dụng phiên âm đều yêu cầu internet. 5cut hoạt động khác biệt: nó phiên âm hoàn toàn trên iPhone của bạn, không cần kết nối internet sau lần tải mô hình ban đầu.</p>
<h2>Phiên âm ngoại tuyến hoạt động như thế nào</h2>
<p>5cut sử dụng các mô hình AI chạy trực tiếp trên iPhone. Phiên âm hoạt động ngay cả ở chế độ trên máy bay, dưới tầng hầm hoặc trên tàu.</p>
<h2>Bốn công cụ phiên âm</h2>
<table class="engine-table">
    <tr><th>Công cụ</th><th>Ngôn ngữ</th><th>Kích thước</th><th>Tốt nhất cho</th></tr>
    <tr><td>Apple Speech</td><td>40+</td><td>Tích hợp</td><td>Phiên âm nhanh</td></tr>
    <tr><td>WhisperKit</td><td>30+</td><td>39 MB – 1.5 GB</td><td>Độ chính xác cao</td></tr>
    <tr><td>Parakeet</td><td>25 ngôn ngữ Âu</td><td>~200 MB</td><td>Tự động phát hiện</td></tr>
    <tr><td>Qwen3-ASR</td><td>30+</td><td>~700 MB</td><td>Đa ngôn ngữ, từ vựng lớn</td></tr>
</table>
<h2>Tại sao ngoại tuyến lại quan trọng</h2>
<ul>
    <li><strong>Quyền riêng tư</strong> – bản ghi âm không bao giờ rời khỏi thiết bị</li>
    <li><strong>Không giới hạn dữ liệu</strong> – phiên âm hàng giờ mà không tốn dung lượng mạng</li>
    <li><strong>Hoạt động mọi nơi</strong> – tầng hầm, máy bay, tàu hỏa</li>
    <li><strong>Không phí theo phút</strong> – miễn phí sau khi tải mô hình</li>
    <li><strong>Tốc độ</strong> – không cần chờ tải lên/tải xuống</li>
</ul>
<h2>Vượt ra ngoài phiên âm: xóa khoảng lặng</h2>
<ol>
    <li>Nhập hoặc ghi âm bài giảng</li>
    <li>Tự động xóa khoảng lặng</li>
    <li>Phiên âm phiên bản đã rút gọn ngoại tuyến</li>
    <li>Xuất: video có phụ đề, tệp SRT hoặc văn bản</li>
</ol>
<h2>Nhận diện người nói</h2>
<p>5cut nhận diện tối đa 4 người nói trong một bản ghi và đánh dấu bằng màu sắc.</p>
<h2>Bắt đầu miễn phí</h2>
<p>5cut kết hợp phiên âm trên thiết bị, xóa khoảng lặng, phụ đề và xử lý hàng loạt.</p>"""
            },
            "es": {
                "title": "Transcripción de Clases Offline en iPhone – Sin Internet | 5cut",
                "desc": "Transcribe grabaciones de clases offline en iPhone. Sin nube, sin subidas, sin internet. IA local en 30+ idiomas. App iOS gratuita.",
                "h1": "Transcripción de Clases Offline en iPhone",
                "tagline": "Transcribe offline en iPhone. Sin internet.",
                "intro": """<p>La mayoría de las apps de transcripción requieren internet. 5cut funciona de manera diferente: transcribe completamente en tu iPhone, sin conexión a internet después de descargar el modelo inicial.</p>
<h2>Cómo funciona la transcripción offline</h2>
<p>5cut utiliza modelos de IA locales que se ejecutan directamente en tu iPhone. La transcripción funciona en modo avión, en el metro o en cualquier lugar.</p>
<h2>Cuatro motores de transcripción</h2>
<table class="engine-table">
    <tr><th>Motor</th><th>Idiomas</th><th>Tamaño</th><th>Ideal para</th></tr>
    <tr><td>Apple Speech</td><td>40+</td><td>Integrado</td><td>Transcripción rápida</td></tr>
    <tr><td>WhisperKit</td><td>30+</td><td>39 MB – 1.5 GB</td><td>Alta precisión, marcas de tiempo</td></tr>
    <tr><td>Parakeet</td><td>25 europeos</td><td>~200 MB</td><td>Detección automática</td></tr>
    <tr><td>Qwen3-ASR</td><td>30+</td><td>~700 MB</td><td>Multilingüe, gran vocabulario</td></tr>
</table>
<h2>Por qué importa que sea offline</h2>
<ul>
    <li><strong>Privacidad</strong> – las grabaciones nunca salen de tu dispositivo</li>
    <li><strong>Sin consumo de datos</strong> – transcribe horas de grabaciones sin gastar tus datos móviles</li>
    <li><strong>Funciona en todas partes</strong> – sótanos, trenes, aviones</li>
    <li><strong>Sin costos por minuto</strong> – el procesamiento local es gratuito</li>
    <li><strong>Velocidad</strong> – sin esperas de subida/bajada</li>
</ul>
<h2>Más allá de la transcripción: eliminar silencios</h2>
<ol>
    <li>Importa o graba una clase</li>
    <li>Elimina silencios automáticamente</li>
    <li>Transcribe la versión condensada offline</li>
    <li>Exporta video con subtítulos, archivo SRT o texto</li>
</ol>
<h2>Identificación de hablantes</h2>
<p>5cut identifica hasta 4 hablantes en una grabación y los diferencia por colores. Todo offline.</p>
<h2>Comienza gratis</h2>
<p>5cut combina transcripción local, eliminación de silencios, subtítulos y procesamiento por lotes.</p>"""
            }
        },
        "best-app-for-medical-school-lectures": {
            "en": {
                "title": "Best App for Medical School Lectures – Record, Trim & Transcribe | 5cut",
                "desc": "Record and condense medical school lectures on iPhone. Remove silence, transcribe in 30+ languages, export to Anki. On-device processing keeps patient case discussions private.",
                "h1": "Best App for Medical School Lectures",
                "tagline": "Turn a 2-hour anatomy lecture into 80 minutes of content.",
                "intro": """<p>Medical school means 4-6 hours of lectures daily. Anatomy, pharmacology, pathology — each recorded lecture is 60-120 minutes, but up to 30% is silence. That's hours of dead air every week.</p>
<p>5cut removes silence from lecture recordings automatically on your iPhone. A 2-hour anatomy lecture becomes 80 minutes of actual content. Then you can transcribe it, export notes to Anki, and review faster.</p>
<h2>Why med students use 5cut</h2>
<ul>
    <li><strong>Save 6-10 hours per week</strong> — remove silence from every lecture recording before review</li>
    <li><strong>On-device processing</strong> — recordings with patient case discussions never leave your phone</li>
    <li><strong>Transcribe in 30+ languages</strong> — international med students can generate subtitles in their native language</li>
    <li><strong>Export to Anki</strong> — turn transcribed lecture segments into flashcards</li>
    <li><strong>Batch processing</strong> — drop a week of recordings in and process them all overnight</li>
</ul>
<h2>Privacy matters in medicine</h2>
<p>Medical lectures often reference patient cases, clinical scenarios, and sensitive health information. Cloud-based transcription means uploading those recordings to someone else's server. 5cut processes everything on your iPhone — no internet, no upload, no third-party access. This matters for HIPAA-adjacent content and for respecting patient privacy.</p>
<h2>The med school workflow</h2>
<ol>
    <li><strong>Record</strong> — use 5cut's built-in recorder during the lecture, or import a recording</li>
    <li><strong>Trim silence</strong> — 5cut analyzes the audio and removes dead air automatically.</li>
    <li><strong>Transcribe</strong> — generate word-level subtitles. Speaker identification separates the professor from student Q&A</li>
    <li><strong>Export</strong> — save the condensed video, export subtitles, or send transcript segments to Anki for spaced repetition</li>
</ol>
<h2>Anatomy, pharmacology, pathology</h2>
<h3>Anatomy lectures</h3>
<p>Long pauses while the professor points at dissection specimens or rotates 3D models. These silences are prime candidates for removal.</p>
<h3>Pharmacology</h3>
<p>Fast-paced drug mechanism explanations with occasional pauses for slide transitions. 5cut's adjustable threshold lets you keep brief natural pauses.</p>
<h3>Clinical case discussions</h3>
<p>Multiple speakers — attending, residents, students. Speaker identification color-codes up to 4 speakers.</p>
<h2>Free to start</h2>
<p>5cut supports semester-long lecture workflows with recording, transcription, silence removal, and batch processing.</p>"""
            },
            "de": {
                "title": "Beste App für Medizin-Vorlesungen – Aufnehmen, Schneiden & Transkribieren | 5cut",
                "desc": "Nehmen Sie Medizin-Vorlesungen auf dem iPhone auf und kürzen Sie sie. Stille entfernen, transkribieren, in Anki exportieren. On-Device-Verarbeitung schützt Patientendaten.",
                "h1": "Beste App für Medizin-Vorlesungen",
                "tagline": "Mache aus einer 2-stündigen Anatomie-Vorlesung 80 Minuten Inhalt.",
                "intro": """<p>Medizinstudium bedeutet 4-6 Stunden Vorlesungen täglich. Anatomie, Pharmakologie, Pathologie — bis zu 30% davon sind Stille. Das sind Stunden an verlorener Zeit pro Woche.</p>
<p>5cut entfernt Stille automatisch auf deinem iPhone. Eine 2-stündige Anatomie-Vorlesung wird zu 80 Minuten echtem Inhalt. Danach kannst du sie transkribieren, Notizen zu Anki exportieren und schneller lernen.</p>
<h2>Warum Medizinstudierende 5cut nutzen</h2>
<ul>
    <li><strong>6-10 Stunden pro Woche sparen</strong> — Stille aus jeder Vorlesungsaufnahme entfernen</li>
    <li><strong>On-Device-Verarbeitung</strong> — Aufnahmen mit Patientenfällen verlassen nie dein iPhone</li>
    <li><strong>In 30+ Sprachen transkribieren</strong> — Untertitel in der Muttersprache generieren</li>
    <li><strong>Export zu Anki</strong> — Transkribierte Segmente in Karteikarten umwandeln</li>
    <li><strong>Stapelverarbeitung</strong> — Aufnahmen einer ganzen Woche über Nacht verarbeiten</li>
</ul>
<h2>Datenschutz in der Medizin ist wichtig</h2>
<p>Medizinische Vorlesungen beziehen sich oft auf Patientenfälle und sensible Gesundheitsdaten. 5cut verarbeitet alles auf deinem iPhone — kein Upload auf fremde Server.</p>
<h2>Der Medizinstudium-Workflow</h2>
<ol>
    <li><strong>Aufnehmen</strong> — integrierten Rekorder nutzen oder Aufnahme importieren</li>
    <li><strong>Stille schneiden</strong> — 5cut entfernt leere Pausen automatisch</li>
    <li><strong>Transkribieren</strong> — Untertitel generieren. Sprechererkennung trennt Professor von Studierenden</li>
    <li><strong>Exportieren</strong> — gekürztes Video speichern, Untertitel exportieren oder zu Anki senden</li>
</ol>
<h2>Kostenlos starten</h2>
<p>5cut unterstützt semesterlange Vorlesungs-Workflows mit Aufnahme, Transkription, Stille-Entfernung und Stapelverarbeitung.</p>"""
            },
            "fr": {
                "title": "Meilleure Application pour les Cours de Médecine – Enregistrez et Transcrivez | 5cut",
                "desc": "Enregistrez et condensez vos cours de médecine sur iPhone. Supprimez les silences, transcrivez et exportez vers Anki. Le traitement local protège la confidentialité des patients.",
                "h1": "Meilleure Application pour les Cours de Médecine",
                "tagline": "Transformez un cours d'anatomie de 2h en 80 minutes.",
                "intro": """<p>Les études de médecine impliquent 4 à 6 heures de cours par jour. Jusqu'à 30% de ces cours sont des silences. Ce sont des heures perdues chaque semaine.</p>
<p>5cut supprime automatiquement les silences sur votre iPhone. Ensuite, vous pouvez transcrire le cours et exporter vers Anki pour réviser plus vite.</p>
<h2>Pourquoi les étudiants en médecine utilisent 5cut</h2>
<ul>
    <li><strong>Gagnez 6-10h par semaine</strong> — supprimez les silences avant de réviser</li>
    <li><strong>Traitement local</strong> — les cas cliniques des patients restent sur votre téléphone</li>
    <li><strong>Transcrivez en 30+ langues</strong> — créez des sous-titres dans votre langue maternelle</li>
    <li><strong>Export vers Anki</strong> — transformez les transcriptions en flashcards</li>
    <li><strong>Traitement par lots</strong> — traitez une semaine de cours pendant la nuit</li>
</ul>
<h2>La confidentialité compte en médecine</h2>
<p>Les cours de médecine abordent des cas cliniques et des données de santé sensibles. 5cut traite tout localement — pas de cloud, pas de téléversement.</p>
<h2>Le flux de travail en médecine</h2>
<ol>
    <li><strong>Enregistrez</strong> ou importez un cours</li>
    <li><strong>Coupez les silences</strong> automatiquement avec 5cut</li>
    <li><strong>Transcrivez</strong> et identifiez les locuteurs (professeur vs étudiants)</li>
    <li><strong>Exportez</strong> la vidéo, les sous-titres, ou vers Anki</li>
</ol>
<h2>Gratuit pour commencer</h2>
<p>5cut est conçu pour gérer les flux de travail de tout un semestre.</p>"""
            },
            "zh": {
                "title": "医学生最佳讲座应用 – 录制、剪切与转写 | 5cut",
                "desc": "在 iPhone 上录制并精简医学院讲座。去除静音、30多种语言转写、导出至 Anki。设备端处理保护患者案例讨论隐私。",
                "h1": "医学生最佳讲座应用",
                "tagline": "将 2 小时的解剖学讲座缩减为 80 分钟。",
                "intro": """<p>医学院意味着每天 4-6 小时的讲座。解剖学、药理学、病理学——其中高达 30% 是静音。这相当于每周数小时的空白时间。</p>
<p>5cut 可以在您的 iPhone 上自动去除讲座录音中的静音。然后您可以转写内容，将笔记导出到 Anki，并更快地复习。</p>
<h2>为什么医学生使用 5cut</h2>
<ul>
    <li><strong>每周节省 6-10 小时</strong> — 复习前去除每次讲座录音的静音</li>
    <li><strong>设备端处理</strong> — 涉及患者案例的录音绝不离开您的手机</li>
    <li><strong>30+ 语言转写</strong> — 留学生可以生成母语字幕</li>
    <li><strong>导出至 Anki</strong> — 将讲座片段转化为闪卡</li>
    <li><strong>批量处理</strong> — 一次性处理一整周的录音</li>
</ul>
<h2>医学中的隐私至关重要</h2>
<p>医学讲座经常涉及患者案例和敏感的健康信息。5cut 在您的 iPhone 上处理所有内容——无云端上传，无第三方访问。</p>
<h2>医学院工作流</h2>
<ol>
    <li><strong>录制</strong> — 使用 5cut 的内置录音机，或导入录音</li>
    <li><strong>去除静音</strong> — 5cut 自动分析并移除空白</li>
    <li><strong>转写</strong> — 说话人识别可区分教授和学生提问</li>
    <li><strong>导出</strong> — 保存视频、导出字幕或发送至 Anki</li>
</ol>
<h2>免费开始使用</h2>
<p>5cut 支持整个学期的讲座工作流处理。</p>"""
            },
            "vi": {
                "title": "Ứng Dụng Tốt Nhất Cho Sinh Viên Y Khoa – Ghi Âm & Phiên Âm | 5cut",
                "desc": "Ghi âm và rút gọn các bài giảng y khoa trên iPhone. Xóa khoảng lặng, phiên âm 30+ ngôn ngữ, xuất sang Anki. Xử lý trên thiết bị bảo vệ thông tin bệnh nhân.",
                "h1": "Ứng Dụng Tốt Nhất Cho Bài Giảng Y Khoa",
                "tagline": "Biến bài giảng giải phẫu 2 giờ thành 80 phút nội dung.",
                "intro": """<p>Trường y đồng nghĩa với 4-6 giờ nghe giảng mỗi ngày. Lên đến 30% thời gian là khoảng lặng. Đó là hàng giờ lãng phí mỗi tuần.</p>
<p>5cut tự động xóa khoảng lặng trên iPhone của bạn. Sau đó, bạn có thể phiên âm, xuất ghi chú sang Anki và ôn tập nhanh hơn.</p>
<h2>Tại sao sinh viên y khoa sử dụng 5cut</h2>
<ul>
    <li><strong>Tiết kiệm 6-10 giờ mỗi tuần</strong> — xóa khoảng lặng trước khi ôn tập</li>
    <li><strong>Xử lý trên thiết bị</strong> — bảo mật tuyệt đối cho các trường hợp bệnh nhân</li>
    <li><strong>Phiên âm 30+ ngôn ngữ</strong> — hỗ trợ sinh viên quốc tế tạo phụ đề</li>
    <li><strong>Xuất sang Anki</strong> — chuyển đoạn bài giảng thành flashcard</li>
    <li><strong>Xử lý hàng loạt</strong> — xử lý bản ghi của cả tuần chỉ trong một đêm</li>
</ul>
<h2>Quyền riêng tư trong y khoa rất quan trọng</h2>
<p>Các bài giảng y khoa thường đề cập đến các trường hợp bệnh nhân. 5cut xử lý mọi thứ trên iPhone của bạn — không tải lên đám mây.</p>
<h2>Quy trình cho trường y</h2>
<ol>
    <li><strong>Ghi âm</strong> hoặc nhập bản ghi có sẵn</li>
    <li><strong>Cắt khoảng lặng</strong> tự động với 5cut</li>
    <li><strong>Phiên âm</strong> và phân biệt giọng nói của giáo sư và sinh viên</li>
    <li><strong>Xuất</strong> video, phụ đề hoặc xuất trực tiếp sang Anki</li>
</ol>
<h2>Bắt đầu miễn phí</h2>
<p>5cut hỗ trợ quy trình làm việc cho cả học kỳ.</p>"""
            },
            "es": {
                "title": "Mejor App para Clases de Medicina – Grabar y Transcribir | 5cut",
                "desc": "Graba y condensa clases de medicina en iPhone. Elimina silencios, transcribe en 30+ idiomas, exporta a Anki. El procesamiento local protege los casos de pacientes.",
                "h1": "Mejor App para Clases de Medicina",
                "tagline": "Convierte una clase de anatomía de 2 horas en 80 minutos.",
                "intro": """<p>La escuela de medicina requiere 4-6 horas de clases diarias. Hasta el 30% es silencio. Eso suma horas de tiempo muerto cada semana.</p>
<p>5cut elimina automáticamente los silencios en tu iPhone. Luego puedes transcribir, exportar a Anki y repasar mucho más rápido.</p>
<h2>Por qué los estudiantes de medicina usan 5cut</h2>
<ul>
    <li><strong>Ahorra 6-10 horas a la semana</strong> — elimina silencios antes de repasar</li>
    <li><strong>Procesamiento local</strong> — los casos clínicos nunca salen de tu teléfono</li>
    <li><strong>Transcribe en 30+ idiomas</strong> — genera subtítulos en tu idioma nativo</li>
    <li><strong>Exporta a Anki</strong> — convierte transcripciones en tarjetas de estudio</li>
    <li><strong>Procesamiento por lotes</strong> — procesa grabaciones de toda la semana durante la noche</li>
</ul>
<h2>La privacidad importa en medicina</h2>
<p>Las clases de medicina suelen discutir casos de pacientes y datos sensibles. 5cut procesa todo en tu iPhone — sin nubes ni subidas.</p>
<h2>El flujo de trabajo en medicina</h2>
<ol>
    <li><strong>Graba</strong> o importa una grabación</li>
    <li><strong>Recorta el silencio</strong> automáticamente con 5cut</li>
    <li><strong>Transcribe</strong> e identifica quién habla (profesor vs alumnos)</li>
    <li><strong>Exporta</strong> el video, los subtítulos o envíalo a Anki</li>
</ol>
<h2>Comienza gratis</h2>
<p>5cut soporta flujos de trabajo de todo un semestre.</p>"""
            }
        },
        "best-app-for-law-school-recordings": {
            "en": {
                "title": "Best App for Law School Recordings – Trim & Transcribe Lectures | 5cut",
                "desc": "Condense law school lectures on iPhone. Remove silence from recorded classes, transcribe case discussions, export notes. All processing stays on-device for confidentiality.",
                "h1": "Best App for Law School Recordings",
                "tagline": "Condense a 90-minute law lecture into 60 minutes. On-device.",
                "intro": """<p>Law school lectures run long. A 90-minute contracts class has 15-25 minutes of silence: the professor reading from the casebook, pausing between Socratic questions, waiting for students to flip to the right page. That silence adds up to hours every week — hours you could spend briefing cases or outlining.</p>
<p>5cut removes silence from lecture recordings on your iPhone. Your 90-minute class becomes 65 minutes of actual instruction. Then transcribe it, identify speakers, and export notes — all without uploading anything to the cloud.</p>
<h2>Why law students use 5cut</h2>
<ul>
    <li><strong>Condense lectures by 20-35%</strong> — cut dead air while keeping speech at natural speed</li>
    <li><strong>Socratic method tracking</strong> — speaker identification separates the professor from student responses</li>
    <li><strong>Case name search</strong> — transcribe the lecture, then search the text for specific case citations</li>
    <li><strong>On-device privacy</strong> — hypothetical client scenarios and case discussions stay on your phone</li>
    <li><strong>Exam prep</strong> — batch-process a semester's lectures before finals</li>
</ul>
<h2>The Socratic method problem</h2>
<p>In law school, the most important content is often buried in dialogue. The professor asks a question, waits 10 seconds, a student responds, there's a 5-second pause, then the professor unpacks the legal principle.</p>
<p>5cut's adjustable threshold lets you keep brief dramatic pauses while cutting the longer dead air. You control exactly how aggressive the trimming is.</p>
<h2>The law school workflow</h2>
<ol>
    <li><strong>Record in class</strong> — use 5cut's built-in recorder or import from Voice Memos</li>
    <li><strong>Auto-trim silence</strong> — Smart Mode "Moderate" works well for Socratic-style classes.</li>
    <li><strong>Transcribe</strong> — generate a full transcript with timestamps and speaker labels.</li>
    <li><strong>Export</strong> — save trimmed audio for commute listening, or export transcript to your outlining tool</li>
</ol>
<h2>Privacy and professional responsibility</h2>
<p>Law school classes discuss hypothetical client scenarios, real case facts, and legal strategies. 5cut processes everything locally on your iPhone — the recording never leaves your device.</p>
<h2>Free to start</h2>
<p>5cut supports a full exam-season workflow with recording, transcription, silence removal, and batch processing.</p>"""
            },
            "de": {
                "title": "Beste App für Jura-Vorlesungen – Aufnehmen & Transkribieren | 5cut",
                "desc": "Kürzen Sie Jura-Vorlesungen auf dem iPhone. Stille entfernen, Falldiskussionen transkribieren, Notizen exportieren. Komplett lokal für höchste Vertraulichkeit.",
                "h1": "Beste App für Jura-Vorlesungen",
                "tagline": "Mache aus einer 90-minütigen Jura-Vorlesung 60 Minuten.",
                "intro": """<p>Eine 90-minütige Jura-Vorlesung hat oft 15-25 Minuten Stille: Pausen zwischen sokratischen Fragen, Warten auf Antworten. Diese Stille summiert sich auf Stunden pro Woche.</p>
<p>5cut entfernt die Stille aus Vorlesungsaufnahmen auf deinem iPhone. Dann kannst du sie transkribieren, Sprecher identifizieren und Notizen exportieren – alles lokal.</p>
<h2>Warum Jurastudierende 5cut nutzen</h2>
<ul>
    <li><strong>Vorlesungen um 20-35% kürzen</strong> — Leere Pausen entfernen, Sprechtempo beibehalten</li>
    <li><strong>Sokratische Methode tracken</strong> — Sprechererkennung trennt Professor von Studierenden</li>
    <li><strong>Fälle durchsuchen</strong> — Transkript nach bestimmten Urteilen durchsuchen</li>
    <li><strong>On-Device Datenschutz</strong> — Falldiskussionen bleiben auf dem Smartphone</li>
    <li><strong>Klausurvorbereitung</strong> — Ein Semester an Vorlesungen im Batch verarbeiten</li>
</ul>
<h2>Datenschutz und rechtliche Verantwortung</h2>
<p>In Jura-Vorlesungen werden hypothetische Klienten und echte Fallfakten diskutiert. 5cut verarbeitet alles lokal auf deinem iPhone – keine Uploads.</p>
<h2>Kostenlos starten</h2>
<p>5cut unterstützt den gesamten Workflow für die Klausurvorbereitung.</p>"""
            },
            "fr": {
                "title": "Meilleure Application pour les Cours de Droit | 5cut",
                "desc": "Condensez les cours de droit sur iPhone. Supprimez les silences, transcrivez les débats, exportez vos notes. Traitement local pour la confidentialité.",
                "h1": "Meilleure Application pour les Cours de Droit",
                "tagline": "Condensez un cours de droit de 90 minutes en 60 minutes.",
                "intro": """<p>Un cours de droit de 90 minutes contient souvent 15 à 25 minutes de silence : le professeur lisant un cas, des pauses socratiques... Ces silences s'accumulent.</p>
<p>5cut supprime les silences sur votre iPhone. Transcrivez, identifiez les locuteurs et exportez vos notes – sans rien envoyer sur le cloud.</p>
<h2>Pourquoi les étudiants en droit l'utilisent</h2>
<ul>
    <li><strong>Condensez les cours de 20-35%</strong> — coupez les blancs</li>
    <li><strong>Suivi de la méthode socratique</strong> — différenciez le professeur des étudiants</li>
    <li><strong>Recherche de jurisprudence</strong> — cherchez des cas spécifiques dans la transcription</li>
    <li><strong>Confidentialité locale</strong> — les scénarios juridiques restent sur votre téléphone</li>
    <li><strong>Préparation aux examens</strong> — traitement par lots pour un semestre entier</li>
</ul>
<h2>Confidentialité et responsabilité</h2>
<p>Les cours de droit discutent de stratégies légales. 5cut traite tout localement sur votre iPhone.</p>
<h2>Gratuit pour commencer</h2>
<p>5cut prend en charge tout votre flux de travail pour la période des examens.</p>"""
            },
            "zh": {
                "title": "法学院讲座最佳录音应用 – 剪切与转写 | 5cut",
                "desc": "在 iPhone 上精简法学院讲座。去除静音、转写案例讨论、导出笔记。全部在设备端处理，确保机密性。",
                "h1": "法学院讲座最佳录音应用",
                "tagline": "将 90 分钟的法学讲座缩减为 60 分钟。完全在设备端进行。",
                "intro": """<p>法学院的讲座时间很长。一节 90 分钟的合同法课往往有 15-25 分钟的静音：教授阅读案例、苏格拉底式提问之间的停顿等。这些静音每周会浪费大量时间。</p>
<p>5cut 可以在 iPhone 上自动去除讲座录音中的静音。然后进行转写、识别说话人并导出笔记——这一切都不需要上传到云端。</p>
<h2>为什么法学生使用 5cut</h2>
<ul>
    <li><strong>精简讲座 20-35%</strong> — 剪切空白，保留自然语速</li>
    <li><strong>追踪苏格拉底式问答</strong> — 说话人识别可区分教授和学生的回答</li>
    <li><strong>案例检索</strong> — 转写后搜索特定的案件引用</li>
    <li><strong>设备端隐私</strong> — 假设的客户场景和案例讨论留在您的手机上</li>
    <li><strong>备考</strong> — 批量处理一整个学期的讲座录音</li>
</ul>
<h2>隐私与专业责任</h2>
<p>法学院课程经常讨论案件细节和法律策略。5cut 完全在 iPhone 上进行本地处理——录音绝不离开设备。</p>
<h2>免费开始使用</h2>
<p>5cut 支持备考季的完整工作流，包括录制、转写、静音移除和批量处理。</p>"""
            },
            "vi": {
                "title": "Ứng Dụng Tốt Nhất Cho Bài Giảng Luật – Ghi Âm & Phiên Âm | 5cut",
                "desc": "Rút gọn các bài giảng luật trên iPhone. Xóa khoảng lặng, phiên âm thảo luận tình huống, xuất ghi chú. Xử lý trên thiết bị đảm bảo tính bảo mật.",
                "h1": "Ứng Dụng Tốt Nhất Cho Sinh Viên Luật",
                "tagline": "Rút gọn bài giảng luật 90 phút xuống còn 60 phút.",
                "intro": """<p>Một lớp học hợp đồng 90 phút có 15-25 phút im lặng: giáo sư đọc án lệ, tạm dừng giữa các câu hỏi theo phương pháp Socrates. Những khoảng trống này cộng dồn thành nhiều giờ mỗi tuần.</p>
<p>5cut xóa khoảng lặng từ các bản ghi trên iPhone. Sau đó, phiên âm, xác định người nói và xuất ghi chú – mà không cần tải lên đám mây.</p>
<h2>Tại sao sinh viên luật sử dụng 5cut</h2>
<ul>
    <li><strong>Rút gọn bài giảng 20-35%</strong> — cắt bỏ khoảng trống</li>
    <li><strong>Theo dõi phương pháp Socrates</strong> — phân biệt giáo sư và sinh viên trả lời</li>
    <li><strong>Tìm kiếm tên vụ án</strong> — tìm kiếm các trích dẫn vụ án cụ thể trong bản ghi</li>
    <li><strong>Quyền riêng tư trên thiết bị</strong> — các tình huống khách hàng giả định ở lại trên điện thoại của bạn</li>
    <li><strong>Luyện thi</strong> — xử lý hàng loạt các bài giảng của cả học kỳ</li>
</ul>
<h2>Bảo mật và trách nhiệm nghề nghiệp</h2>
<p>Các lớp học luật thường thảo luận về các chiến lược pháp lý. 5cut xử lý mọi thứ cục bộ trên iPhone của bạn.</p>
<h2>Bắt đầu miễn phí</h2>
<p>5cut hỗ trợ quy trình làm việc đầy đủ cho mùa thi.</p>"""
            },
            "es": {
                "title": "Mejor App para Clases de Derecho – Grabar y Transcribir | 5cut",
                "desc": "Condensa clases de derecho en iPhone. Elimina silencios, transcribe debates, exporta apuntes. Procesamiento local para máxima confidencialidad.",
                "h1": "Mejor App para Clases de Derecho",
                "tagline": "Condensa una clase de derecho de 90 minutos en 60 minutos.",
                "intro": """<p>Las clases de derecho son largas. Una clase de 90 minutos tiene 15-25 minutos de silencio: el profesor leyendo, pausas entre preguntas socráticas... Ese silencio suma horas cada semana.</p>
<p>5cut elimina los silencios en tu iPhone. Luego puedes transcribir, identificar hablantes y exportar apuntes – sin subir nada a la nube.</p>
<h2>Por qué los estudiantes de derecho usan 5cut</h2>
<ul>
    <li><strong>Condensa clases un 20-35%</strong> — recorta espacios en blanco manteniendo la velocidad</li>
    <li><strong>Seguimiento del método socrático</strong> — separa al profesor de las respuestas de los alumnos</li>
    <li><strong>Búsqueda de jurisprudencia</strong> — busca citas de casos específicos en la transcripción</li>
    <li><strong>Privacidad local</strong> — los escenarios de casos se quedan en tu teléfono</li>
    <li><strong>Preparación de exámenes</strong> — procesa por lotes todo un semestre</li>
</ul>
<h2>Privacidad y responsabilidad</h2>
<p>Las clases de derecho discuten estrategias legales y hechos de casos reales. 5cut procesa todo localmente en tu iPhone.</p>
<h2>Comienza gratis</h2>
<p>5cut soporta el flujo de trabajo completo para la temporada de exámenes.</p>"""
            }
        },
        "record-meetings-privately-iphone": {
            "en": {
                "title": "Record Meetings Privately on iPhone – No Cloud, Full Compliance | 5cut",
                "desc": "Record and transcribe business meetings without uploading to the cloud. On-device processing keeps sensitive discussions completely private. GDPR and SOC 2 friendly.",
                "h1": "Record Meetings Privately on iPhone",
                "tagline": "Record and transcribe meetings on-device. No cloud upload.",
                "intro": """<p>Your meeting contains proprietary strategy, client names, revenue numbers, or personnel decisions. Cloud-based meeting recorders like Otter, Fireflies, or Fathom upload everything to their servers. Their AI processes your words on someone else's infrastructure.</p>
<p>5cut records and transcribes meetings entirely on your iPhone. Nothing leaves your device. No cloud. No third-party servers. No data processing agreements needed.</p>
<h2>The compliance problem with cloud recorders</h2>
<p>Every time you use a cloud transcription service, you're creating a data processing relationship. That means:</p>
<ul>
    <li>A third party now holds recordings of confidential discussions</li>
    <li>You need a Data Processing Agreement (DPA) under GDPR</li>
    <li>SOC 2 auditors will ask about it</li>
    <li>If the service is breached, your meeting content is exposed</li>
    <li>Client NDAs may prohibit sharing recordings with third parties</li>
</ul>
<p>On-device processing eliminates all of these concerns.</p>
<h2>Who needs private meeting recording</h2>
<h3>Legal professionals</h3>
<p>Client meetings, case strategy discussions, settlement negotiations. Attorney-client privilege doesn't mix well with third-party cloud processing.</p>
<h3>Healthcare</h3>
<p>Clinical team meetings, patient case reviews, administrative discussions involving PHI. HIPAA compliance is simpler when recordings stay on-device.</p>
<h3>Finance and banking</h3>
<p>Investment discussions, client advisory meetings, compliance reviews. Material non-public information shouldn't exist on a transcription startup's servers.</p>
<h3>HR and people operations</h3>
<p>Performance reviews, disciplinary meetings, compensation discussions.</p>
<h2>The 5cut workflow for meetings</h2>
<ol>
    <li><strong>Open the recorder</strong> — tap record when the meeting starts.</li>
    <li><strong>Live transcription</strong> — see words appear in real-time as people speak</li>
    <li><strong>Speaker identification</strong> — up to 4 speakers are automatically identified</li>
    <li><strong>Trim silence</strong> — remove the gaps between agenda items</li>
    <li><strong>Export</strong> — transcript as text or SRT. Everything stays in your Files app</li>
</ol>
<h2>Compared to alternatives</h2>
<p>Unlike Otter.ai or Fireflies which upload to their cloud, 5cut is fully offline after model download. Unlike Voice Memos, 5cut transcribes, identifies speakers, and removes silence.</p>
<h2>Free to start</h2>
<p>5cut combines private recording, on-device transcription, and silence removal.</p>"""
            },
            "de": {
                "title": "Meetings privat auf dem iPhone aufnehmen – Keine Cloud, volle Compliance | 5cut",
                "desc": "Meetings aufnehmen und transkribieren ohne Cloud-Upload. On-Device-Verarbeitung hält vertrauliche Diskussionen sicher. GDPR- und Compliance-freundlich.",
                "h1": "Meetings privat auf dem iPhone aufnehmen",
                "tagline": "Meetings lokal aufnehmen und transkribieren. Kein Cloud-Upload.",
                "intro": """<p>Dein Meeting enthält vertrauliche Strategien, Kundennamen oder Personalentscheidungen. Cloud-basierte Recorder wie Otter oder Fireflies laden alles auf ihre Server hoch.</p>
<p>5cut nimmt Meetings vollständig auf deinem iPhone auf und transkribiert sie. Nichts verlässt dein Gerät. Keine Cloud. Keine Drittanbieter-Server. Keine Auftragsverarbeitungsverträge (AVV) nötig.</p>
<h2>Das Compliance-Problem mit Cloud-Recordern</h2>
<p>Jedes Mal, wenn du einen Cloud-Dienst nutzt, gehst du ein Risiko ein:</p>
<ul>
    <li>Ein Dritter speichert Aufnahmen vertraulicher Gespräche</li>
    <li>Du benötigst einen AVV nach DSGVO</li>
    <li>Kunden-NDAs könnten das Teilen von Aufnahmen untersagen</li>
    <li>Bei einem Datenleck sind deine Meeting-Inhalte gefährdet</li>
</ul>
<p>Lokale Verarbeitung eliminiert all diese Bedenken.</p>
<h2>Wer private Meeting-Aufnahmen braucht</h2>
<h3>Rechtsanwälte & Kanzleien</h3>
<p>Mandantengespräche und Fallstrategien. Das Anwaltsgeheimnis verträgt sich nicht mit Cloud-Verarbeitung.</p>
<h3>Gesundheitswesen</h3>
<p>Klinische Teambesprechungen und Patientenbesprechungen. Datenschutz ist einfacher, wenn Aufnahmen auf dem Gerät bleiben.</p>
<h3>Finanzen & Banken</h3>
<p>Investitionsgespräche und Compliance-Reviews. Nicht-öffentliche Informationen gehören nicht auf fremde Server.</p>
<h3>HR & Personalwesen</h3>
<p>Leistungsbeurteilungen und Gehaltsgespräche erfordern höchste Vertraulichkeit.</p>
<h2>Der 5cut-Workflow für Meetings</h2>
<ol>
    <li><strong>Rekorder öffnen</strong> — einfach Aufnahme starten.</li>
    <li><strong>Live-Transkription</strong> — Text erscheint in Echtzeit</li>
    <li><strong>Sprechererkennung</strong> — bis zu 4 Sprecher werden erkannt</li>
    <li><strong>Stille schneiden</strong> — Pausen zwischen Tagesordnungspunkten entfernen</li>
    <li><strong>Export</strong> — alles bleibt sicher in deiner Dateien-App</li>
</ol>
<h2>Kostenlos starten</h2>
<p>5cut kombiniert private Aufnahme, lokale Transkription und Stille-Entfernung.</p>"""
            },
            "fr": {
                "title": "Enregistrez vos Réunions en Privé sur iPhone – Sans Cloud | 5cut",
                "desc": "Enregistrez et transcrivez vos réunions d'affaires sans cloud. Le traitement local garde les discussions sensibles totalement privées. Compatible RGPD.",
                "h1": "Enregistrez vos Réunions en Privé sur iPhone",
                "tagline": "Enregistrez et transcrivez localement. Aucun téléchargement cloud.",
                "intro": """<p>Votre réunion aborde des stratégies confidentielles ou des données clients. Les enregistreurs cloud comme Otter ou Fireflies envoient tout sur leurs serveurs.</p>
<p>5cut enregistre et transcrit entièrement sur votre iPhone. Rien ne quitte votre appareil. Pas de serveurs tiers. Pas besoin de contrats de traitement des données.</p>
<h2>Le problème de conformité des enregistreurs cloud</h2>
<ul>
    <li>Un tiers détient les enregistrements de discussions confidentielles</li>
    <li>Vous avez besoin d'un accord de traitement (DPA) sous le RGPD</li>
    <li>Les accords de confidentialité (NDA) peuvent interdire le cloud</li>
    <li>En cas de piratage, vos réunions sont exposées</li>
</ul>
<p>Le traitement local élimine toutes ces préoccupations.</p>
<h2>Qui a besoin d'enregistrements privés</h2>
<h3>Professions juridiques</h3>
<p>Le secret professionnel ne fait pas bon ménage avec le cloud.</p>
<h3>Santé et RH</h3>
<p>Discussions sur les patients ou les employés. La conformité est assurée si les données restent sur l'appareil.</p>
<h3>Finance</h3>
<p>Informations privilégiées et stratégie financière.</p>
<h2>Le flux de travail 5cut</h2>
<ol>
    <li><strong>Ouvrez l'enregistreur</strong> — appuyez sur enregistrer</li>
    <li><strong>Transcription en direct</strong> — le texte apparaît en temps réel</li>
    <li><strong>Identification des locuteurs</strong> — jusqu'à 4 personnes</li>
    <li><strong>Coupez les silences</strong> — supprimez les blancs</li>
    <li><strong>Exportez</strong> — tout reste sécurisé sur votre appareil</li>
</ol>
<h2>Gratuit pour commencer</h2>
<p>5cut combine enregistrement privé, transcription locale et suppression des silences.</p>"""
            },
            "zh": {
                "title": "在 iPhone 上私密录制会议 – 无云端，完全合规 | 5cut",
                "desc": "录制和转写商务会议，无需上传云端。设备端处理确保敏感讨论完全保密。符合 GDPR 标准。",
                "h1": "在 iPhone 上私密录制会议",
                "tagline": "在设备端录制和转写会议。无云端上传。",
                "intro": """<p>您的会议包含专有战略、客户名单、收入数据或人事决策。Otter 或 Fireflies 等基于云端的会议记录工具会将所有内容上传到其服务器。</p>
<p>5cut 完全在您的 iPhone 上录制和转写会议。没有任何数据会离开您的设备。无云端，无第三方服务器，无需数据处理协议。</p>
<h2>云端录音工具的合规性问题</h2>
<ul>
    <li>第三方现在持有您机密讨论的录音</li>
    <li>在 GDPR 下您需要数据处理协议（DPA）</li>
    <li>客户 NDA 可能禁止与第三方分享录音</li>
    <li>如果服务遭到黑客攻击，您的会议内容将面临风险</li>
</ul>
<p>设备端处理消除了所有这些顾虑。</p>
<h2>谁需要私密会议录音</h2>
<h3>法律专业人士</h3>
<p>律师-客户特权与第三方云处理不相容。</p>
<h3>医疗保健与人力资源</h3>
<p>患者病例审查或员工绩效评估。录音留在设备上更容易合规。</p>
<h3>金融与银行业</h3>
<p>非公开的重大财务信息不应存在于转写初创公司的服务器上。</p>
<h2>5cut 会议工作流</h2>
<ol>
    <li><strong>打开录音机</strong> — 会议开始时点击录音</li>
    <li><strong>实时转写</strong> — 在设备上实时查看转写文本</li>
    <li><strong>说话人识别</strong> — 自动识别多达 4 位说话人</li>
    <li><strong>去除静音</strong> — 移除议程项目之间的空白</li>
    <li><strong>导出</strong> — 所有内容均保留在您的“文件”应用中</li>
</ol>
<h2>免费开始使用</h2>
<p>5cut 结合了私密录制、设备端转写和静音移除功能。</p>"""
            },
            "vi": {
                "title": "Ghi Âm Cuộc Họp Riêng Tư Trên iPhone – Bảo Mật Tuyệt Đối | 5cut",
                "desc": "Ghi âm và phiên âm cuộc họp mà không tải lên đám mây. Xử lý trên thiết bị giữ cho các cuộc thảo luận nhạy cảm hoàn toàn riêng tư. Thân thiện với GDPR.",
                "h1": "Ghi Âm Cuộc Họp Riêng Tư Trên iPhone",
                "tagline": "Ghi âm và phiên âm trên thiết bị. Không tải lên đám mây.",
                "intro": """<p>Cuộc họp của bạn chứa chiến lược, danh sách khách hàng hoặc quyết định nhân sự. Các công cụ ghi âm đám mây tải mọi thứ lên máy chủ của họ.</p>
<p>5cut ghi âm và phiên âm hoàn toàn trên iPhone của bạn. Không có dữ liệu nào rời khỏi thiết bị. Không có đám mây. Không có máy chủ của bên thứ ba.</p>
<h2>Vấn đề tuân thủ với ghi âm đám mây</h2>
<ul>
    <li>Bên thứ ba nắm giữ các bản ghi âm bí mật</li>
    <li>Bạn cần có Thỏa thuận xử lý dữ liệu (DPA) theo GDPR</li>
    <li>NDA có thể cấm chia sẻ với bên thứ ba</li>
    <li>Nguy cơ rò rỉ dữ liệu nếu dịch vụ bị tấn công</li>
</ul>
<p>Xử lý trên thiết bị loại bỏ tất cả những lo ngại này.</p>
<h2>Ai cần ghi âm cuộc họp riêng tư</h2>
<h3>Luật sư</h3>
<p>Đặc quyền luật sư-khách hàng không phù hợp với xử lý đám mây.</p>
<h3>Y tế & Nhân sự</h3>
<p>Đánh giá hồ sơ bệnh án hoặc thảo luận nhân sự. An toàn hơn khi dữ liệu ở trên thiết bị.</p>
<h3>Tài chính & Ngân hàng</h3>
<p>Thông tin không công khai không nên tồn tại trên máy chủ của bên thứ ba.</p>
<h2>Quy trình của 5cut</h2>
<ol>
    <li><strong>Mở máy ghi âm</strong> — nhấn ghi âm khi cuộc họp bắt đầu</li>
    <li><strong>Phiên âm trực tiếp</strong> — xem văn bản xuất hiện theo thời gian thực</li>
    <li><strong>Nhận diện người nói</strong> — tối đa 4 người</li>
    <li><strong>Cắt khoảng lặng</strong> — xóa các khoảng trống</li>
    <li><strong>Xuất</strong> — mọi thứ được giữ an toàn trên thiết bị</li>
</ol>
<h2>Bắt đầu miễn phí</h2>
<p>5cut kết hợp ghi âm riêng tư, phiên âm và xóa khoảng lặng.</p>"""
            },
            "es": {
                "title": "Grabar Reuniones en Privado en iPhone – Sin Nube, Cumplimiento Total | 5cut",
                "desc": "Graba y transcribe reuniones sin subir a la nube. El procesamiento local mantiene las discusiones sensibles completamente privadas. Cumple con GDPR.",
                "h1": "Grabar Reuniones en Privado en iPhone",
                "tagline": "Graba y transcribe localmente. Sin nube.",
                "intro": """<p>Tu reunión contiene estrategias confidenciales o datos de clientes. Las grabadoras en la nube como Otter o Fireflies suben todo a sus servidores.</p>
<p>5cut graba y transcribe reuniones completamente en tu iPhone. Nada sale de tu dispositivo. Sin nube. Sin servidores de terceros. Sin necesidad de acuerdos de procesamiento de datos.</p>
<h2>El problema de cumplimiento con las grabadoras en la nube</h2>
<ul>
    <li>Un tercero posee grabaciones de discusiones confidenciales</li>
    <li>Necesitas un acuerdo DPA bajo el GDPR</li>
    <li>Los NDA de clientes pueden prohibir compartir grabaciones</li>
    <li>Si el servicio es hackeado, tu contenido queda expuesto</li>
</ul>
<p>El procesamiento en el dispositivo elimina estas preocupaciones.</p>
<h2>Quién necesita grabación privada</h2>
<h3>Profesionales legales</h3>
<p>El privilegio abogado-cliente no se mezcla bien con la nube.</p>
<h3>Salud y Recursos Humanos</h3>
<p>Revisiones de casos de pacientes o evaluaciones de empleados. El cumplimiento es más fácil cuando las grabaciones se quedan en el teléfono.</p>
<h3>Finanzas</h3>
<p>Información financiera confidencial no debería existir en servidores externos.</p>
<h2>El flujo de trabajo de 5cut</h2>
<ol>
    <li><strong>Abre la grabadora</strong> — toca grabar cuando empiece la reunión</li>
    <li><strong>Transcripción en vivo</strong> — ve las palabras en tiempo real</li>
    <li><strong>Identificación de hablantes</strong> — hasta 4 personas</li>
    <li><strong>Recorta el silencio</strong> — elimina los tiempos muertos</li>
    <li><strong>Exporta</strong> — todo se guarda seguro en tus Archivos</li>
</ol>
<h2>Comienza gratis</h2>
<p>5cut combina grabación privada, transcripción local y eliminación de silencios.</p>"""
            }
        },
        "offline-meeting-notes-iphone": {
            "en": {
                "title": "Offline Meeting Notes on iPhone – Transcribe Without Internet | 5cut",
                "desc": "Generate meeting notes and transcripts offline on iPhone. No internet, no cloud, no uploads. Record meetings, identify speakers, and get a full transcript — all on-device.",
                "h1": "Offline Meeting Notes on iPhone",
                "tagline": "Transcribe meetings offline. Speaker identification included.",
                "intro": """<p>You need meeting notes, but your company's security policy won't let you use Otter, Fireflies, or any cloud transcription service. Or you're in a conference room with no WiFi. Or you simply don't trust a third party with your meeting content.</p>
<p>5cut generates meeting transcripts entirely offline on your iPhone. Record, transcribe, identify speakers — no internet connection required at any point.</p>
<h2>How offline meeting notes work</h2>
<ol>
    <li><strong>Download a language model once</strong> — this is the only step that needs internet (40-700 MB)</li>
    <li><strong>Record the meeting</strong> — tap record. Works in airplane mode, underground, anywhere</li>
    <li><strong>Transcribe on-device</strong> — the AI runs on your iPhone's Neural Engine.</li>
    <li><strong>Speaker separation</strong> — up to 4 speakers are automatically identified and labeled.</li>
    <li><strong>Export</strong> — copy the transcript, share as text, or export with timestamps</li>
</ol>
<h2>Why go offline for meeting notes</h2>
<h3>Corporate security policies</h3>
<p>Many companies prohibit uploading internal discussions to third-party services. IT security reviews for new SaaS tools take months. 5cut needs no security review — data never leaves the device.</p>
<h3>Regulated industries</h3>
<p>Finance, healthcare, legal, defense — these sectors have strict data handling requirements. On-device processing means no vendor risk assessment.</p>
<h3>Unreliable connectivity</h3>
<p>Conference rooms in basements, meetings during travel, offsite retreats with spotty WiFi. Offline transcription just works regardless of your connection.</p>
<h2>What you get</h2>
<ul>
    <li><strong>Full transcript</strong> with timestamps</li>
    <li><strong>Speaker labels</strong> — color-coded, renameable</li>
    <li><strong>Silence removal</strong> — strip the "ums" and long pauses</li>
    <li><strong>Multiple export formats</strong> — plain text, SRT subtitles, or video</li>
    <li><strong>30+ languages</strong> — multilingual teams can transcribe in the meeting's language</li>
</ul>
<h2>Free to start</h2>
<p>5cut combines private recording, on-device transcription, silence removal, and batch processing.</p>"""
            },
            "de": {
                "title": "Offline Meeting-Notizen auf dem iPhone – Transkribieren ohne Internet | 5cut",
                "desc": "Erstellen Sie Meeting-Notizen offline auf dem iPhone. Kein Internet, keine Cloud. Nehmen Sie Meetings auf, identifizieren Sie Sprecher – alles lokal.",
                "h1": "Offline Meeting-Notizen auf dem iPhone",
                "tagline": "Meetings offline transkribieren. Inklusive Sprechererkennung.",
                "intro": """<p>Du brauchst Meeting-Notizen, aber die Sicherheitsrichtlinien deiner Firma verbieten Cloud-Dienste. Oder du bist in einem Raum ohne WLAN. Oder du vertraust Drittanbietern nicht.</p>
<p>5cut generiert Meeting-Transkripte komplett offline auf deinem iPhone. Aufnehmen, transkribieren, Sprecher erkennen – alles ohne Internetverbindung.</p>
<h2>Wie Offline-Meeting-Notizen funktionieren</h2>
<ol>
    <li><strong>Sprachmodell einmalig laden</strong> — nur dieser Schritt benötigt Internet (40-700 MB)</li>
    <li><strong>Meeting aufnehmen</strong> — funktioniert im Flugmodus, überall</li>
    <li><strong>Lokal transkribieren</strong> — die KI läuft auf deinem iPhone</li>
    <li><strong>Sprechererkennung</strong> — bis zu 4 Sprecher werden automatisch erkannt</li>
    <li><strong>Exportieren</strong> — als Text, SRT oder mit Zeitstempeln</li>
</ol>
<h2>Warum Offline für Meeting-Notizen?</h2>
<h3>Firmenrichtlinien</h3>
<p>Viele Unternehmen verbieten Uploads. 5cut benötigt keinen Security-Review, da die Daten das Gerät nie verlassen.</p>
<h3>Regulierte Branchen</h3>
<p>Finanzen, Gesundheit, Recht – hier gelten strenge Datenschutzvorgaben.</p>
<h3>Schlechtes WLAN</h3>
<p>Meetingräume im Keller, Besprechungen auf Reisen. Offline-Transkription funktioniert immer.</p>
<h2>Was du bekommst</h2>
<ul>
    <li><strong>Vollständiges Transkript</strong> mit Zeitstempeln</li>
    <li><strong>Sprecher-Labels</strong> — farbcodiert und umbenennbar</li>
    <li><strong>Stille-Entfernung</strong> — Ähms und lange Pausen entfernen</li>
    <li><strong>30+ Sprachen</strong> — perfekt für internationale Teams</li>
</ul>
<h2>Kostenlos starten</h2>
<p>5cut kombiniert lokale Aufnahme, Transkription und Stille-Entfernung.</p>"""
            },
            "fr": {
                "title": "Notes de Réunion Hors Ligne sur iPhone – Sans Internet | 5cut",
                "desc": "Générez des notes de réunion hors ligne sur iPhone. Sans internet, ni cloud. Enregistrez, identifiez les locuteurs, et obtenez une transcription locale.",
                "h1": "Notes de Réunion Hors Ligne sur iPhone",
                "tagline": "Transcrivez hors ligne. Identification des locuteurs incluse.",
                "intro": """<p>Vous avez besoin de notes, mais la politique de sécurité de votre entreprise interdit les services cloud. Ou vous êtes dans une salle sans WiFi.</p>
<p>5cut génère des transcriptions entièrement hors ligne sur votre iPhone. Enregistrez, transcrivez, identifiez les locuteurs – sans connexion internet.</p>
<h2>Comment ça fonctionne</h2>
<ol>
    <li><strong>Téléchargez un modèle linguistique</strong> une seule fois (avec internet)</li>
    <li><strong>Enregistrez la réunion</strong> — fonctionne en mode avion</li>
    <li><strong>Transcrivez localement</strong> — l'IA tourne sur votre iPhone</li>
    <li><strong>Séparation des locuteurs</strong> — jusqu'à 4 personnes reconnues</li>
    <li><strong>Exportez</strong> — copiez ou partagez la transcription</li>
</ol>
<h2>Pourquoi le hors ligne ?</h2>
<h3>Sécurité d'entreprise</h3>
<p>Les données ne quittent jamais l'appareil, aucun examen de sécurité informatique n'est requis.</p>
<h3>Secteurs réglementés</h3>
<p>Finance, santé, droit – le traitement local simplifie la conformité.</p>
<h3>Connexion instable</h3>
<p>La transcription hors ligne fonctionne quelle que soit votre connexion.</p>
<h2>Ce que vous obtenez</h2>
<ul>
    <li><strong>Transcription complète</strong> avec horodatage</li>
    <li><strong>Noms des locuteurs</strong> — modifiables et colorés</li>
    <li><strong>Suppression des silences</strong> — gagnez du temps</li>
    <li><strong>30+ langues</strong> — pour les équipes internationales</li>
</ul>
<h2>Gratuit pour commencer</h2>
<p>5cut combine enregistrement privé et transcription locale.</p>"""
            },
            "zh": {
                "title": "iPhone 上的离线会议笔记 – 无需网络即可转写 | 5cut",
                "desc": "在 iPhone 上离线生成会议笔记。无需网络，无需云端。录制会议、识别说话人，并获得完整的设备端转写文本。",
                "h1": "iPhone 上的离线会议笔记",
                "tagline": "离线转写会议。包含说话人识别功能。",
                "intro": """<p>您需要会议笔记，但公司的安全政策不允许使用云端转写服务。或者您在没有 WiFi 的会议室里。或者您根本不信任第三方处理您的会议内容。</p>
<p>5cut 完全在您的 iPhone 上离线生成会议转写。录制、转写、识别说话人——全程无需网络连接。</p>
<h2>离线会议笔记如何工作</h2>
<ol>
    <li><strong>下载一次语言模型</strong> — 这是唯一需要网络的一步 (40-700 MB)</li>
    <li><strong>录制会议</strong> — 在飞行模式、地下室等任何地方均可运行</li>
    <li><strong>设备端转写</strong> — AI 在您的 iPhone 神经网络引擎上运行</li>
    <li><strong>说话人分离</strong> — 自动识别并标记多达 4 位说话人</li>
    <li><strong>导出</strong> — 复制转写文本或导出带时间戳的文件</li>
</ol>
<h2>为什么选择离线会议笔记</h2>
<h3>企业安全政策</h3>
<p>许多公司禁止将内部讨论上传到第三方服务。5cut 不需要安全审查——数据永远不会离开设备。</p>
<h3>受监管的行业</h3>
<p>金融、医疗保健、法律——这些行业对数据处理有严格要求。设备端处理意味着没有合规风险。</p>
<h3>网络不稳定</h3>
<p>无论您的网络连接如何，离线转写都能正常工作。</p>
<h2>您将获得什么</h2>
<ul>
    <li><strong>完整转写文本</strong>（带时间戳）</li>
    <li><strong>说话人标签</strong> — 颜色编码，可重命名</li>
    <li><strong>去除静音</strong> — 剥离长停顿</li>
    <li><strong>30+ 种语言</strong> — 多语言团队可轻松转写</li>
</ul>
<h2>免费开始使用</h2>
<p>5cut 结合了私密录制和设备端转写功能。</p>"""
            },
            "vi": {
                "title": "Ghi Chú Cuộc Họp Ngoại Tuyến Trên iPhone – Không Cần Internet | 5cut",
                "desc": "Tạo ghi chú cuộc họp ngoại tuyến trên iPhone. Không cần internet, không đám mây. Ghi âm, nhận diện người nói và nhận bản ghi cục bộ.",
                "h1": "Ghi Chú Cuộc Họp Ngoại Tuyến",
                "tagline": "Phiên âm cuộc họp ngoại tuyến. Bao gồm nhận diện người nói.",
                "intro": """<p>Bạn cần ghi chú cuộc họp, nhưng chính sách bảo mật của công ty cấm dịch vụ đám mây. Hoặc bạn đang ở trong phòng họp không có WiFi.</p>
<p>5cut tạo bản ghi chép hoàn toàn ngoại tuyến trên iPhone. Ghi âm, phiên âm, nhận diện người nói – không cần kết nối internet.</p>
<h2>Ghi chú ngoại tuyến hoạt động thế nào</h2>
<ol>
    <li><strong>Tải mô hình ngôn ngữ một lần</strong> — bước duy nhất cần internet</li>
    <li><strong>Ghi âm cuộc họp</strong> — hoạt động cả ở chế độ máy bay</li>
    <li><strong>Phiên âm cục bộ</strong> — AI chạy trên thiết bị của bạn</li>
    <li><strong>Nhận diện người nói</strong> — tối đa 4 người</li>
    <li><strong>Xuất</strong> — chia sẻ văn bản với dấu thời gian</li>
</ol>
<h2>Tại sao chọn ngoại tuyến?</h2>
<h3>Chính sách bảo mật công ty</h3>
<p>Dữ liệu không bao giờ rời khỏi thiết bị, không cần đánh giá rủi ro an ninh mạng.</p>
<h3>Ngành công nghiệp được quản lý</h3>
<p>Tài chính, y tế, luật pháp – xử lý trên thiết bị đảm bảo tính tuân thủ cao nhất.</p>
<h3>Kết nối không ổn định</h3>
<p>Phiên âm ngoại tuyến luôn hoạt động bất kể mạng WiFi.</p>
<h2>Bạn nhận được gì</h2>
<ul>
    <li><strong>Bản ghi chép đầy đủ</strong> với dấu thời gian</li>
    <li><strong>Nhãn người nói</strong> — có màu sắc, có thể đổi tên</li>
    <li><strong>Xóa khoảng lặng</strong> — tiết kiệm thời gian nghe lại</li>
    <li><strong>30+ ngôn ngữ</strong> — cho các nhóm đa quốc gia</li>
</ul>
<h2>Bắt đầu miễn phí</h2>
<p>5cut kết hợp ghi âm riêng tư và phiên âm trên thiết bị.</p>"""
            },
            "es": {
                "title": "Notas de Reuniones Offline en iPhone – Sin Internet | 5cut",
                "desc": "Genera notas de reuniones offline en iPhone. Sin internet, sin nubes. Graba, identifica hablantes y obtén una transcripción local completa.",
                "h1": "Notas de Reuniones Offline en iPhone",
                "tagline": "Transcribe reuniones offline. Identificación de hablantes incluida.",
                "intro": """<p>Necesitas apuntes, pero la política de seguridad de tu empresa prohíbe servicios en la nube. O estás en una sala sin WiFi.</p>
<p>5cut genera transcripciones completamente offline en tu iPhone. Graba, transcribe, identifica hablantes – sin conexión a internet en ningún momento.</p>
<h2>Cómo funcionan las notas offline</h2>
<ol>
    <li><strong>Descarga un modelo de idioma</strong> una sola vez (requiere internet)</li>
    <li><strong>Graba la reunión</strong> — funciona en modo avión</li>
    <li><strong>Transcribe localmente</strong> — la IA se ejecuta en tu iPhone</li>
    <li><strong>Identificación de hablantes</strong> — hasta 4 personas reconocidas</li>
    <li><strong>Exporta</strong> — copia el texto o exporta con marcas de tiempo</li>
</ol>
<h2>¿Por qué offline?</h2>
<h3>Políticas de seguridad corporativas</h3>
<p>Los datos nunca salen del dispositivo, por lo que no se requiere revisión de seguridad de TI.</p>
<h3>Sectores regulados</h3>
<p>Finanzas, salud, legal – el procesamiento local simplifica el cumplimiento.</p>
<h3>Conectividad poco confiable</h3>
<p>La transcripción offline siempre funciona, independientemente de la señal.</p>
<h2>Lo que obtienes</h2>
<ul>
    <li><strong>Transcripción completa</strong> con marcas de tiempo</li>
    <li><strong>Nombres de hablantes</strong> — con colores y editables</li>
    <li><strong>Eliminación de silencios</strong> — ahorra tiempo al revisar</li>
    <li><strong>30+ idiomas</strong> — para equipos internacionales</li>
</ul>
<h2>Comienza gratis</h2>
<p>5cut combina grabación privada y transcripción en el dispositivo.</p>"""
            }
        }
    }
    
    # We find the insertion point just before the last closing brace in data_pages.py
    import json
    # Let's read the file and find the last closing brace
    last_brace_idx = content.rfind('}')
    if last_brace_idx == -1:
        print("Error: Could not find closing brace.")
        return

    # We need to format the dictionary as a python string that we can insert
    # Let's use json.dumps and format it carefully, or just pprint
    import pprint
    
    # Alternatively, just inject a string representation
    dict_str = pprint.pformat(new_pages, width=200)
    
    # Remove the first '{' and last '}' from dict_str to merge into the existing dict
    dict_str = dict_str.strip()
    if dict_str.startswith('{'): dict_str = dict_str[1:]
    if dict_str.endswith('}'): dict_str = dict_str[:-1]
    
    # Add a comma before appending if not already there
    insertion = ",\\n" + dict_str
    
    # Construct new content
    new_content = content[:last_brace_idx] + insertion + "\\n}"
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully added the pages to data_pages.py!")

if __name__ == '__main__':
    add_translations()
