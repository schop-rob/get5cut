# Simplified Chinese text for get5cut.com.
# English is the source: write it in ASD-STE100 (.claude/skills/ste100-writing).
# Translations follow the English meaning, with the same short, plain sentences.
# HOME fills the homepage; PAGES fills each inner page (a missing page falls back to English).

HOME = {'dir': 'zh',
 'lang_code': 'zh-Hans',
 'title': '5cut – 录制并剪辑网课，导出学习笔记 | iOS 应用',
 'description': '直接在 iPhone 上录制讲座和会议。5cut 自动裁剪静音部分，支持 30 多种语言转写，并可导出清晰的学习笔记至 Anki、Notion 和 Obsidian。',
 'og_title': '5cut – 录制并剪辑网课，导出学习笔记',
 'og_description': '录制讲座。去除静音。实时翻译。获取清晰的文本和学习笔记。在 iPhone 上私密处理。',
 'brand': '5cut',
 'brand_suffix': ' – AI 课程录音与去静音工具',
 'tagline': '拒绝重复听课浪费时间。自动裁剪静音，实时翻译，本地生成学习笔记。',
 'proof1': '无 5cut 服务器',
 'proof2': '无需注册账户',
 'proof3': '30+ 语言实时翻译',
 'stat1_value': '每月 5 次',
 'stat1_label': '免费导出',
 'cta_subtext': '免费下载 · 每月 5 次免费导出 · 无需账户',
 'creator_promise': '我开发 5cut，是因为反复听外语长课和停顿会浪费大量学习时间。设备端翻译和去静音改变了我的学习方式；5cut 没有服务器，因此无法保存我的课程资料云端副本。',
 'creator_signature': '5cut 开发者',
 'feat1_title': '应用内录音与章节标记',
 'feat1_desc': '直接录制课堂讲座或会议。录音时添加章节标记，之后可以更轻松地找到重要内容。',
 'feat2_title': '智能去除静音',
 'feat2_desc': '自动检测并裁剪讲座和播客中的无声停顿。支持智能预设模式（温和、适中、激进）或手动调节阈值。',
 'feat3_title': '设备端翻译与 AI 摘要',
 'feat3_desc': '支持实时翻译，用母语轻松跟上外语课程。Premium 用户可在 iOS 26+ 上通过本地模型生成 AI 摘要、核心要点与问答。',
 'feat4_title': '导出至 Notion、Anki 与 Obsidian',
 'feat4_desc': '将整理好的干净文本及发言人标记直接导出至 Notion、Obsidian，并支持自动生成 Anki 学习卡片。',
 'feat5_title': '多发言人识别（Premium）',
 'feat5_desc': '自动识别录音中多达 4 位发言人，并提供颜色标记与名称修改。非常适合研讨会和小组讨论。',
 'how_it_works': '使用方法',
 'step1': '<strong>录制或导入</strong>音频或视频文件至 iPhone',
 'step2': '<strong>自动检测静音</strong> — 绿色代表语音，红色代表静音',
 'step3': '<strong>在设备端翻译与总结</strong> — AI 摘要需要 Premium 和 iOS 26+',
 'step4': '<strong>导出学习资料</strong> — 将整理好的笔记发送至 Anki、Notion 或 Obsidian',
 'privacy_title': '无 5cut 服务器，无云端副本',
 'privacy_desc': '你的录音绝不会离开设备。每份转录都在你的 iPhone 上生成——没有 5cut 服务器，没有云端处理，也没有第三方转录服务。无需账户，无应用内分析，无广告。',
 'perfect_for': '适用人群',
 'perfect_for_desc1': '复旧外语课程的留学生、交换生、外派人员。也同样适用于希望去除 Zoom 会议录制尴尬停顿或加速收听播客的职场人士。',
 'perfect_for_desc2': '需要字幕或实时翻译？5cut 支持 30 多种语言；下载所需模型后，可使用设备端引擎离线处理。',
 'faq': '常见问题',
 'faq_items': [{'q': '静音检测是如何工作的？', 'a': '5cut 在设备本地分析视频音频波形。低于阈值的片段标记为红色。您可以手动调整滑块，或选择三种智能模式。'},
               {'q': '我可以为课程生成字幕和翻译吗？', 'a': '可以。5cut 支持 30 多种语言的设备端转写与实时翻译。字幕可嵌入视频或导出为 SRT。'},
               {'q': '支持 Zoom 或在线课程录制吗？', 'a': '支持。可导入 MP4、MOV 或 HEVC 视频。适用于 Zoom 录制、Teams 会议、屏幕录像及任何带音轨的视频。'},
               {'q': '可以批量处理一整个学期的课吗？', 'a': '可以。你可以将多个录音加入队列，并使用单独或共享设置进行处理。'},
               {'q': '我的数据隐私有保障吗？', 'a': '5cut 没有服务器、账户系统，也不会保存你的录音云端副本，因此我们无法查看、收听或存储录音。所有转录引擎都在设备上运行；模型只需下载一次，之后即可离线使用。'},
               {'q': '5cut 有 Premium 付费计划吗？',
                'a': '有的。录音、静音裁剪和转写预览（前 5 分钟）都是免费的。您可以升级到 5cut Premium 来解锁无限次数导出、说话人识别、完整长度转录以及 iOS 26+ 上的 AI 总结。5cut Premium '
                     '为月度订阅或一次性终身升级——价格在 App Store 中显示并按地区调整。'},
               {'q': '应用支持哪些语言？', 'a': '应用界面支持简体中文、英语、德语、西班牙语、法语、意大利语、日语、韩语、葡萄牙语和越南语。'}],
 'footer_use_cases': '使用场景',
 'footer_alternatives': '替代方案',
 'footer_legal': '法律与支持',
 'footer_study_fields': '按学科分类',
 'hero_note_desc': '录制、裁剪、转写、翻译和导出 — 全部在你的 iPhone 上完成。你的录音绝不会离开设备。'}

PAGES = {'speed-up-zoom-recordings': {'title': '加速 Zoom 录音 – 移除静音 | 5cut',
                              'desc': '移除 Zoom、Teams 和在线课程录音中的尴尬停顿和空白。iOS 本地处理。',
                              'h1': '加速 Zoom 录音',
                              'tagline': '自动剪切空白部分。',
                              'intro': '<p>较长的 Zoom 讲座常包含调试麦克风或等待回答时的空白。5cut 可检测这些安静片段，帮助你在不加快语速的情况下复习录音。</p>'},
 'study-abroad': {'title': '留学生必备 App – 外语网课神器 | 5cut',
                  'desc': '国际学生的必备 iPhone 应用。去除外语讲座的静音，添加 30 多种语言的字幕。',
                  'h1': '留学生必备神器',
                  'tagline': '录制、转写，轻松搞定课程。',
                  'intro': '<p>出国留学是一项挑战，尤其是在听外语讲座时。使用 5cut 录制讲座并生成 30 多种语言的转写文本；Premium 用户还可在 iOS 26+ 上创建 AI 学习笔记。</p>'},
 'transcribe-lectures': {'title': '在 iPhone 上转写讲座 – 30+ 语言字幕 | 5cut',
                         'desc': '生成超过 30 种语言的讲座录音字幕。设备端转写——无上传，无云端。',
                         'h1': '在 iPhone 上转写讲座',
                         'tagline': '本地处理，保护隐私，速度极快。',
                         'intro': '<p>不要再手动打字记录讲座笔记了。使用 5cut，您可以直接在 iPhone 上生成讲座转写文本；Premium 用户还可在 iOS 26+ 上创建 AI 摘要。5cut '
                                  '没有服务器，也不会保存录音的云端副本；下载后的设备端引擎可用于离线转写。</p>'},
 'remove-silence-from-lectures': {'title': '如何去除网课录音中的静音 – 5cut iOS 版',
                                  'desc': '自动移除网课录制中的空白部分和静音。节省备考复习时间。',
                                  'h1': '去除讲座录音中的静音',
                                  'tagline': '复习讲座内容，而不是空白。',
                                  'intro': '<p>录制的讲座常包含教师停顿、写板书或等待回答时的静音片段。5cut 可检测并移除这些空白，同时保留自然语速。</p>'},
 'podcast-silence-remover': {'title': '在 iPhone 上去除播客中的静音 | 5cut',
                             'desc': '通过消除死气沉沉和尴尬的停顿来紧凑播客节目。iPhone 本地处理。',
                             'h1': '去除播客中的静音',
                             'tagline': '轻松紧凑您的播客内容。',
                             'intro': '<p>死气沉沉会破坏节奏。无论您是编辑自己的播客还是收听播客，句子之间 2-3 秒的停顿很快就会累积起来。一集 45 分钟的播客可能会有 8-10 分钟的静音。5cut 可在 iPhone '
                                      '上一键去除静音。</p>'},
 'use-cases/remove-silence-from-zoom': {'title': '如何自动去除 Zoom 会议录音中的静音 | 5cut',
                                        'desc': '了解如何使用 5cut 在您的 iPhone 上即时去除长 Zoom 会议录音中的静音。',
                                        'h1': '去除 Zoom 会议中的静音',
                                        'tagline': '直奔主题。',
                                        'intro': '<p>Zoom 录音中充满了尴尬的停顿、等待与会者加入的时间以及麦克风故障排除。5cut 智能的音频分析可即时修剪导入的 Zoom MP4 或 MOV '
                                                 '文件中的静音间隙，为您提供紧凑的录音内容。</p>'},
 'use-cases/remove-silence-from-obs': {'title': '去除 OBS 直播和录屏中的静音 | 5cut',
                                       'desc': '更快地编辑您的 OBS Studio VOD。自动从您的 iPhone 录制中剪切静音。',
                                       'h1': '去除 OBS VOD 中的静音',
                                       'tagline': '加速您的剪辑工作流。',
                                       'intro': '<p>通过 OBS Studio 录制的直播 VOD 在休息或匹配队列期间通常包含很长的静音时间。将您的 OBS 文件传输到您的 iPhone，让 5cut '
                                                '自动修剪无声内容，以便更快地发布您的 YouTube 集锦。</p>'},
 'alternatives/timebolt-alternative': {'title': '适用于 iOS 的最佳免费 TimeBolt 替代方案 | 5cut',
                                       'desc': '寻找移动版 TimeBolt 替代方案？5cut 在 iPhone 上免费提供自动静音消除和转写预览。',
                                       'h1': '最佳移动端 TimeBolt 替代方案',
                                       'tagline': '在您的 iPhone 或 iPad 上自动去除静音。',
                                       'intro': '<p>TimeBolt 是一款出色的桌面工具。但是，如果您正在寻找一种可以直接在 iPhone 上编辑视频的移动替代方案，5cut 是您的最佳选择。5cut '
                                                '完全在设备端处理视频，保护隐私。</p>'},
 'free-jumpcut-app': {'title': '免费 iPhone 自动剪切应用 – 去除静音 | 5cut',
                      'desc': '下载 iOS 跳剪应用。自动去除视频静音，生成字幕，并直接从 iPhone 导出。',
                      'h1': '适用于 iPhone 的免费自动剪切应用',
                      'tagline': '在 iPhone 上自动去除视频空白。',
                      'intro': '<p>正在寻找快速、自动的剪切工具？5cut 可自动修剪视频中的空白内容，生成字幕，并在 iPhone 上完成处理。</p>'},
 'smartphone-video-editor': {'title': '适用于口播视频的智能手机视频编辑器 | 5cut',
                             'desc': '直接在智能手机上编辑视频。适合 Vlog 和 TikTok 的最佳 iPhone 编辑器。本地录制、去除静音并导出。',
                             'h1': '适用于口播视频的手机视频编辑器',
                             'tagline': '直接在 iPhone 上录制和编辑。',
                             'intro': '<p>将大型视频文件传输到电脑进行编辑非常缓慢且烦人。5cut 是创作者的终极智能手机视频编辑器。录制您的口播或 Vlog，让 AI 自动去除静音，添加字幕，并在几秒钟内直接从手机导出。</p>'},
 'best-app-for-law-school-recordings': {'desc': '在 iPhone 上精简法学院讲座。去除静音、转写案例讨论、导出笔记。全部在设备端处理，确保机密性。',
                                        'h1': '法学院讲座最佳录音应用',
                                        'intro': '<p>法学讲座在教授阅读案例、苏格拉底式提问之间或等待回答时，可能包含较长的静音片段。</p>\n'
                                                 '<p>5cut 可以在 iPhone 上自动去除讲座录音中的静音。然后进行转写、识别说话人并导出笔记——这一切都不需要上传到云端。</p>\n'
                                                 '<h2>为什么法学生使用 5cut</h2>\n'
                                                 '<ul>\n'
                                                 '    <li><strong>剪掉检测到的静音</strong> — 保留自然语速</li>\n'
                                                 '    <li><strong>追踪苏格拉底式问答</strong> — 说话人识别可区分教授和学生的回答</li>\n'
                                                 '    <li><strong>案例检索</strong> — 转写后搜索特定的案件引用</li>\n'
                                                 '    <li><strong>设备端隐私</strong> — 假设的客户场景和案例讨论留在您的手机上</li>\n'
                                                 '    <li><strong>备考</strong> — 批量处理一整个学期的讲座录音</li>\n'
                                                 '</ul>\n'
                                                 '<h2>隐私与专业责任</h2>\n'
                                                 '<p>法学院课程经常讨论案件细节和法律策略。5cut 没有服务器或录音云端副本；如需离线转写，请选择受支持的已下载模型。</p>\n'
                                                 '<h2>免费开始使用</h2>\n'
                                                 '<p>5cut 可免费下载，包含应用内录音、静音裁剪和转写预览功能。升级至 Premium 尊享版即可解锁无限次导出、完整长度转写、说话人识别以及批量处理功能。</p>',
                                        'tagline': '去除法学讲座录音中检测到的停顿。',
                                        'title': '法学院讲座最佳录音应用 – 剪切与转写 | 5cut'},
 'best-app-for-medical-school-lectures': {'desc': '在 iPhone 上录制并精简医学院讲座。去除静音、30多种语言转写、导出至 Anki。设备端处理保护患者案例讨论隐私。',
                                          'h1': '医学生最佳讲座应用',
                                          'intro': '<p>医学讲座在讲解、演示和提问之间可能包含较长的静音片段。</p>\n'
                                                   '<p>5cut 可以在您的 iPhone 上自动去除讲座录音中的静音。然后您可以转写内容，将笔记导出到 Anki，并更快地复习。</p>\n'
                                                   '<h2>为什么医学生使用 5cut</h2>\n'
                                                   '<ul>\n'
                                                   '    <li><strong>少复习空白片段</strong> — 学习前去除检测到的静音</li>\n'
                                                   '    <li><strong>无 5cut 云端副本</strong> — 如需离线转写，请选择受支持的已下载模型</li>\n'
                                                   '    <li><strong>30+ 语言转写</strong> — 留学生可以生成母语字幕</li>\n'
                                                   '    <li><strong>导出至 Anki</strong> — 将讲座片段转化为问答（Q&A）学习卡片</li>\n'
                                                   '    <li><strong>批量处理</strong> — 一次性处理一整周的录音</li>\n'
                                                   '</ul>\n'
                                                   '<h2>医学中的隐私至关重要</h2>\n'
                                                   '<p>医学讲座经常涉及患者案例和敏感的健康信息。5cut 在您的 iPhone 上处理所有内容——无云端上传，无第三方访问。</p>\n'
                                                   '<h2>医学院工作流</h2>\n'
                                                   '<ol>\n'
                                                   '    <li><strong>录制</strong> — 使用 5cut 的内置录音机，或导入录音</li>\n'
                                                   '    <li><strong>去除静音</strong> — 5cut 自动分析并移除空白</li>\n'
                                                   '    <li><strong>转写</strong> — 说话人识别可区分教授和学生提问</li>\n'
                                                   '    <li><strong>导出</strong> — 保存视频、导出字幕或发送至 Anki</li>\n'
                                                   '</ol>\n'
                                                   '<h2>免费开始使用</h2>\n'
                                                   '<p>5cut 可免费下载，包含应用内录音、静音裁剪和转写预览功能。升级至 Premium 尊享版即可解锁无限次导出、完整长度转写、说话人识别以及批量处理功能。</p>',
                                          'tagline': '复习解剖学讲座前去除空白片段。',
                                          'title': '医学生最佳讲座应用 – 录制、剪切与转写 | 5cut'},
 'offline-lecture-transcription-iphone': {'desc': '在 iPhone 上离线转写讲座录音。无云端，无上传，无需网络。支持 30+ 种语言的设备端 AI。免费 iOS 应用。',
                                          'h1': '在 iPhone 上离线转写讲座',
                                          'intro': '<p>大多数转写应用都需要连接互联网。5cut 与众不同：它完全在您的 iPhone 上进行转写，在初始模型下载之后无需任何网络连接。</p>\n'
                                                   '<h2>离线转写的工作原理</h2>\n'
                                                   '<p>5cut 使用直接在 iPhone 神经网络引擎上运行的设备端 AI 模型。转写功能可以在飞行模式、地铁或没有 WiFi 的教室中完美运行。</p>\n'
                                                   '<h2>六种转写引擎</h2>\n'
                                                   '<table class="engine-table">\n'
                                                   '    <tr><th>引擎</th><th>语言</th><th>模型大小</th><th>最佳用途</th></tr>\n'
                                                   '    <tr><td>Apple '
                                                   'SpeechAnalyzer</td><td>40+</td><td>内置</td><td>快速转写，支持语言最广泛</td></tr>\n'
                                                   '    <tr><td>WhisperKit</td><td>30+</td><td>39 MB – 1.5 GB</td><td>高精度，词级时间戳 — '
                                                   '仅支持导入文件，实时录音器中不可用</td></tr>\n'
                                                   '    <tr><td>Parakeet Ultra</td><td>25 种欧洲语言</td><td>~600 '
                                                   'MB</td><td>欧洲语言，自动检测</td></tr>\n'
                                                   '    <tr><td>Parakeet Lite</td><td>英语</td><td>~220 MB</td><td>更快更轻量 — 适合旧款 '
                                                   'iPhone</td></tr>\n'
                                                   '    <tr><td>Moonshine Tiny Streaming</td><td>英语</td><td>~49 '
                                                   'MB</td><td>低延迟流式转写</td></tr>\n'
                                                   '    <tr><td>Phonon-2</td><td>英语</td><td>~360 MB</td><td>为 iPhone 优化的紧凑英语模型，需要 iOS '
                                                   '18+</td></tr>\n'
                                                   '</table>\n'
                                                   '<p>WhisperKit 仅支持导入文件 — 实时录音器中不提供此引擎。</p>\n'
                                                   '<h2>为什么离线很重要</h2>\n'
                                                   '<ul>\n'
                                                   '    <li><strong>无 5cut 云端副本</strong> – 如需离线转写，请选择受支持的已下载模型</li>\n'
                                                   '    <li><strong>无数据限制</strong> – 转写数小时的录音而不用担心流量</li>\n'
                                                   '    <li><strong>随处可用</strong> – 校园地下室、火车、飞机上</li>\n'
                                                   '    <li><strong>无按分钟收费</strong> – 设备端处理完全免费</li>\n'
                                                   '    <li><strong>速度</strong> – 无需等待上传/下载</li>\n'
                                                   '</ul>\n'
                                                   '<h2>超越转写：自动去除静音</h2>\n'
                                                   '<ol>\n'
                                                   '    <li>导入或录制讲座</li>\n'
                                                   '    <li>自动去除静音</li>\n'
                                                   '    <li>离线转写精简后的版本</li>\n'
                                                   '    <li>导出：带字幕的视频、SRT 或文本</li>\n'
                                                   '</ol>\n'
                                                   '<h2>说话人识别</h2>\n'
                                                   '<p>5cut 可识别多达 4 位说话人并在转写中标记。这同样在离线状态下运行。</p>\n'
                                                   '<h2>免费开始使用</h2>\n'
                                                   '<p>5cut 可免费下载，包含应用内录音、静音裁剪和转写预览功能。升级至 Premium 尊享版即可解锁无限次导出、完整长度转写、说话人识别以及批量处理功能。</p>',
                                          'tagline': '在 iPhone 上离线转写。无需互联网。',
                                          'title': '在 iPhone 上离线转写讲座 – 无需互联网 | 5cut'},
 'offline-meeting-notes-iphone': {'desc': '在 iPhone 上离线生成会议笔记。无需网络，无需云端。录制会议、识别说话人，并获得完整的设备端转写文本。',
                                  'h1': 'iPhone 上的离线会议笔记',
                                  'intro': '<p>您需要会议笔记，但公司的安全政策不允许使用云端转写服务。或者您在没有 WiFi 的会议室里。或者您根本不信任第三方处理您的会议内容。</p>\n'
                                           '<p>5cut 完全在您的 iPhone 上离线生成会议转写。录制、转写、识别说话人——在下载初始模型后，全程无需网络连接。</p>\n'
                                           '<h2>离线会议笔记如何工作</h2>\n'
                                           '<ol>\n'
                                           '    <li><strong>下载一次语言模型</strong> — 这是唯一需要网络的一步 (40-700 MB)</li>\n'
                                           '    <li><strong>录制会议</strong> — 在飞行模式、地下室等任何地方均可运行</li>\n'
                                           '    <li><strong>设备端转写</strong> — AI 在您的 iPhone 神经网络引擎上运行</li>\n'
                                           '    <li><strong>说话人分离</strong> — 自动识别并标记多达 4 位说话人</li>\n'
                                           '    <li><strong>导出</strong> — 复制转写文本或导出带时间戳的文件</li>\n'
                                           '</ol>\n'
                                           '<h2>为什么选择离线会议笔记</h2>\n'
                                           '<h3>企业安全政策</h3>\n'
                                           '<p>许多公司禁止将内部讨论上传到第三方服务。5cut 没有服务器或云端副本，下载后的设备端模型可减少第三方接触。请始终核对所在机构的安全要求。</p>\n'
                                           '<h3>受监管的行业</h3>\n'
                                           '<p>金融、医疗保健和法律行业对数据处理有严格要求。设备端处理可减少第三方接触，但仍需遵守所在机构的规则。</p>\n'
                                           '<h3>网络不稳定</h3>\n'
                                           '<p>无论您的网络连接如何，离线转写都能正常工作。</p>\n'
                                           '<h2>您将获得什么</h2>\n'
                                           '<ul>\n'
                                           '    <li><strong>完整转写文本</strong>（带时间戳）</li>\n'
                                           '    <li><strong>说话人标签</strong> — 颜色编码，可重命名</li>\n'
                                           '    <li><strong>去除静音</strong> — 剥离长停顿</li>\n'
                                           '    <li><strong>30+ 种语言</strong> — 多语言团队可轻松转写</li>\n'
                                           '</ul>\n'
                                           '<h2>免费开始使用</h2>\n'
                                           '<p>5cut 可免费下载，包含应用内录音、静音裁剪和转写预览功能。升级至 Premium 尊享版即可解锁无限次导出、完整长度转写、说话人识别以及批量处理功能。</p>',
                                  'tagline': '离线转写会议。包含说话人识别功能。',
                                  'title': 'iPhone 上的离线会议笔记 – 无需网络即可转写 | 5cut'},
 'record-meetings-privately-iphone': {'desc': '在 iPhone 上录制会议。5cut 没有服务器或云端副本；如需离线转写，请选择受支持的已下载模型。',
                                      'h1': '在 iPhone 上私密录制会议',
                                      'intro': '<p>您的会议包含专有战略、客户名单、收入数据或人事决策。Otter 或 Fireflies 等基于云端的会议记录工具会将所有内容上传到其服务器。</p>\n'
                                               '<p>5cut 没有服务器，也不会保存会议的云端副本。如需离线转写，请选择支持当前语言和设备的已下载模型，并始终遵守所在机构的录音与数据规定。</p>\n'
                                               '<h2>云端录音工具的合规性问题</h2>\n'
                                               '<ul>\n'
                                               '    <li>第三方现在持有您机密讨论的录音</li>\n'
                                               '    <li>在 GDPR 下您需要数据处理协议（DPA）</li>\n'
                                               '    <li>客户 NDA 可能禁止与第三方分享录音</li>\n'
                                               '    <li>如果服务遭到黑客攻击，您的会议内容将面临风险</li>\n'
                                               '</ul>\n'
                                               '<p>设备端处理可减少第三方接触，但您仍须遵守所在机构的规定。</p>\n'
                                               '<h2>谁需要私密会议录音</h2>\n'
                                               '<h3>法律专业人士</h3>\n'
                                               '<p>律师-客户特权与第三方云处理不相容。</p>\n'
                                               '<h3>医疗保健与人力资源</h3>\n'
                                               '<p>患者病例审查或员工绩效评估。录音留在设备上更容易合规。</p>\n'
                                               '<h3>金融与银行业</h3>\n'
                                               '<p>非公开的重大财务信息不应存在于转写初创公司的服务器上。</p>\n'
                                               '<h2>5cut 会议工作流</h2>\n'
                                               '<ol>\n'
                                               '    <li><strong>打开录音机</strong> — 会议开始时点击录音</li>\n'
                                               '    <li><strong>录制后转写</strong> — 选择受支持的已下载模型</li>\n'
                                               '    <li><strong>说话人识别</strong> — 自动识别多达 4 位说话人</li>\n'
                                               '    <li><strong>去除静音</strong> — 移除议程项目之间的空白</li>\n'
                                               '    <li><strong>导出</strong> — 所有内容均保留在您的“文件”应用中</li>\n'
                                               '</ol>\n'
                                               '<h2>免费开始使用</h2>\n'
                                               '<p>5cut 可免费下载，包含应用内录音、静音裁剪和转写预览功能。升级至 Premium 尊享版即可解锁无限次导出、完整长度转写、说话人识别以及批量处理功能。</p>',
                                      'tagline': '在设备端录制和转写会议。无云端上传。',
                                      'title': '在 iPhone 上私密录制会议 – 无 5cut 云端副本 | 5cut'}}
