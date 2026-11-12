#!/usr/bin/env python3
"""Static site generator for Avyra Company / شركة أفيرا (Arabic + English).

Run `python3 build.py` after editing the content below. It rewrites every
HTML page, sitemap.xml, robots.txt and 404.html. No dependencies beyond Python 3.
"""
import json, os, hashlib

def _v(p): return hashlib.md5(open(p, "rb").read()).hexdigest()[:8]
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
CSS = "/assets/css/style.css?v=" + _v("assets/css/style.css")
JS = "/assets/js/main.js?v=" + _v("assets/js/main.js")

# ---------------------------------------------------------------- settings (EDIT THESE)
SITE = "https://avyra.sa"            # PLACEHOLDER: set the real domain
EMAIL = "info@avyra.sa"              # PLACEHOLDER
PRIVACY_EMAIL = "privacy@avyra.sa"   # PLACEHOLDER
PHONE_DISPLAY = ""                   # e.g. "+966 5X XXX XXXX"; empty hides the phone rows
PHONE_TEL = ""                       # e.g. "+9665XXXXXXXX"
LINKEDIN_URL = ""                    # empty hides the LinkedIn row
BOOKING_URL = ""                     # Cal.com / Calendly link; empty hides the "book a call" button
CR = ""                              # commercial registration number; empty hides it
# Contact form: empty endpoint = opens the visitor's email app. For Web3Forms use
# FORM_ENDPOINT = "https://api.web3forms.com/submit" and put the access key in FORM_KEY.
FORM_ENDPOINT = ""
FORM_KEY = ""

_P = lambda f: f'<link rel="preload" href="/assets/fonts/{f}-normal.woff2" as="font" type="font/woff2" crossorigin>\n'
PRELOAD = {"ar": _P("ibm-plex-sans-arabic-arabic-400") + _P("reem-kufi-arabic-700"),
           "en": _P("ibm-plex-sans-latin-400") + _P("ibm-plex-sans-latin-600")}

ICONS = {
 "ai": '<svg class="icon" viewBox="0 0 48 48" aria-hidden="true"><rect x="12" y="12" width="24" height="24"/><rect x="19" y="19" width="10" height="10"/><path d="M18 12V5M24 12V5M30 12V5M18 43v-7M24 43v-7M30 43v-7M12 18H5M12 24H5M12 30H5M43 18h-7M43 24h-7M43 30h-7"/></svg>',
 "geo": '<svg class="icon" viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="16"/><path d="M8 24h32M24 8c-7 5-7 27 0 32M24 8c7 5 7 27 0 32"/></svg>',
}

# ---------------------------------------------------------------- content
T = {
"ar": {
 "dir": "rtl", "lang": "ar", "base": "/", "other": "en", "other_label": "English", "locale": "ar_SA", "other_locale": "en_US",
 "brand": "شركة أفيرا", "brand_core": "أفيرا", "co": "شركة", "skip": "انتقل إلى المحتوى", "home_label": "الرئيسية",
 "nav": [("about", "عن الشركة"), ("services", "خدماتنا"), ("projects", "خبراتنا"), ("team", "الفريق"), ("contact", "تواصل معنا")],
 "title": "شركة أفيرا | الذكاء الاصطناعي المؤسسي والذكاء الجيومكاني وحوكمة المحافظ في الرياض",
 "desc": "شركة أفيرا شركة سعودية في الرياض تجمع حلول الذكاء الاصطناعي المؤسسي، والذكاء الاصطناعي الجيومكاني (GeoAI)، وحوكمة المحافظ لدعم برامج التحول الرقمي والبيئة في رؤية 2030.",
 "eyebrow": "الرياض · المملكة العربية السعودية",
 "h1": "الابتكار محفظة، والقرار ذكاء",
 "lead": "استشارات متخصصة تجمع حلول الذكاء الاصطناعي، وحوكمة المحافظ، والذكاء الاصطناعي الجيومكاني (GeoAI)، ونشر الذكاء الاصطناعي المؤسسي، لدعم برامج التحول الرقمي والبيئة ضمن رؤية 2030.",
 "cta1": "تواصل معنا", "cta2": "خدماتنا", "logo_alt": "شعار أفيرا",
 "trust": ["محترفو إدارة المحافظ والبرامج والمشاريع: PfMP · PgMP · PMP", "شركة سعودية مسجلة في الرياض", "تصميم متوافق مع ضوابط NCA-ECC", "تنفيذ بالشراكة مع شركاء تقنيين من الولايات المتحدة وألمانيا"],
 "about_eyebrow": "عن الشركة", "about_h": "الرؤية والرسالة",
 "vision_h": "رؤيتنا", "vision": "أن نكون الشريك الموثوق للمملكة في تمكين القرار، عبر حلول ذكية ومستدامة وفعّالة اقتصاديًا تتحول إلى محافظ منظّمة تقودها البيانات.",
 "mission_h": "رسالتنا", "mission": "نطوّر وننشر أنظمة ذكاء الأعمال بالذكاء الاصطناعي وحلول GeoAI وأطر حوكمة المحافظ، لتساعد الجهات السعودية على التعامل مع المياه بوصفها أصلًا استراتيجيًا. وبدمج الهندسة المتقدمة للذكاء الاصطناعي المؤسسي مع GeoAI وإدارة المحافظ والبرامج والمشاريع المعتمدة، نحوّل البيانات البيئية المعقدة إلى معلومات جاهزة لمجلس الإدارة.",
 "gap_h": "لماذا وُجدنا", "gap": "معظم الجهات تقدّم قطعة واحدة من الصورة. شركات الاستشارات الهندسية التقليدية تقدّم دراسات فنية دون حوكمة للمحافظ، وشركات الذكاء الاصطناعي تبني النماذج دون فهم لعدم اليقين الهيدرولوجي أو لسياسات المياه. نحن نجمع الأمور الثلاثة: الحوكمة، وGeoAI، والنشر التشغيلي للذكاء الاصطناعي، في كيان سعودي واحد.",
 "svc_eyebrow": "خدماتنا", "svc_h": "ركيزتان متكاملتان",
 "pillars": [
  {"icon": "ai", "tag": "الركيزة أ", "h": "حلول الذكاء الاصطناعي المؤسسي والنشر السيادي",
   "items": [("وكلاء الذكاء الاصطناعي وأتمتة سير العمل", "أتمتة تحت إشراف بشري لعمليات مرافق المياه والموافقات وتنفيذ الخدمات، مع سجلات تدقيق مدمجة."),
             ("الذكاء المكاني والتشغيلي", "مراقبة البنية التحتية، والوعي بالعمليات الميدانية، ورؤية بيئية للأصول المائية الموزعة."),
             ("ذكاء المعرفة والمستندات", "استرجاع مستندات المؤسسة وذكاء محتوى متعدد اللغات (عربي/إنجليزي) للجهات التنظيمية التي تدير منظومات فنية ضخمة."),
             ("النشر الخاص والسيادي للذكاء الاصطناعي", "نشر على السحابة والسحابة الخاصة والبنية المحلية والهجينة، مصمَّم ليتوافق مع NCA-ECC وإرشادات سدايا ونظام حماية البيانات الشخصية، وهو أمر حاسم للجهات الحكومية.")],
   "outcome": "ذكاء اصطناعي مؤسسي يعمل داخل محيط الأمن والحوكمة لديك."},
  {"icon": "geo", "tag": "الركيزة ب", "h": "الاستشارات في الذكاء الاصطناعي الجيومكاني (GeoAI)",
   "items": [("النمذجة الهيدرولوجية المعززة بـ GeoAI", "دمج صور الأقمار الصناعية وبيانات الاستشعار عن بعد مع النماذج الهيدرولوجية لدعم قرارات الموارد المائية."),
             ("تصميم قواعد البيانات الجيومكانية والبنية المكانية", "تصميم قواعد بيانات جيومكانية وبنية بيانات مكانية (SDI) تجعل بيانات الجهة قابلة للمشاركة والتحليل."),
             ("مفاهيم التوأم الرقمي للبنية التحتية", "تقييم الجاهزية وتصميم البنية وخارطة طريق التنفيذ للتوائم الرقمية للبنية التحتية.")],
   "outcome": "من بيانات الأقمار الصناعية إلى قرار مجلس الإدارة، في أسابيع لا سنوات."},
 ],
 "proj_eyebrow": "خبراتنا", "proj_h": "نماذج من خبراتنا",
 "proj_note": "تحافظ أفيرا على السرية. تُشارك المراجع التفصيلية ودراسات الحالة مباشرة، بعد توقيع اتفاقيات السرية المناسبة. وتمثل الفئات أدناه الخبرة المجمّعة لقيادة الشركة وفرق شركائها.",
 "proj_cols": ("القطاع", "نوع المشروع", "دورنا"),
 "proj": [("الذكاء الاصطناعي المؤسسي (السعودية)", "وكلاء ذكاء اصطناعي لسير عمل الخدمات", "نشر تشغيلي للذكاء الاصطناعي"),
          ("أنظمة ذكاء اصطناعي مخصصة", "تطوير تطبيقات ذكاء اصطناعي متكاملة", "هندسة النظام ونشره"),
          ("أنظمة GeoAI مخصصة", "لوحات متابعة وخطوط بيانات GeoAI", "بناء النظام مع شريك التطوير")],
 "team_eyebrow": "الفريق", "team_h": "القيادة",
 "team": [("م. خالد عبدالرحمن", "الرئيس التنفيذي", ["الذكاء الاصطناعي المؤسسي والنشر السيادي", "وكلاء الذكاء الاصطناعي والذكاء المكاني ونشر الذكاء الاصطناعي الخاص", "مصمَّم ليتوافق مع NCA-ECC، وملتزم بنظام حماية البيانات الشخصية وإرشادات سدايا"]),
          ("د.-م. محمد عبدالله", "المدير الفني", [])],
 "network": "يدعمنا فريق موثوق من مطوّري الذكاء الاصطناعي والتطبيقات المتكاملة، ومحللي الاستشعار عن بعد ونظم المعلومات الجغرافية، وخبراء البيئة والبنية التحتية، ومنسّقي المشاريع، بما يتسع مع نطاق كل مشروع.",
 "why_eyebrow": "لماذا أفيرا", "why_h": "الميزة السعودية",
 "why": [("شركة سعودية مسجلة ومقرها الرياض", "نعمل داخل بيئتكم التنظيمية وبيئة المشتريات."),
         ("متوافقون مع رؤية 2030", "يدعم عملنا مباشرة أمن المياه والاستدامة البيئية وأهداف التحول الرقمي."),
         ("نشر سيادي للذكاء الاصطناعي", "تصميم متوافق مع NCA-ECC ونظام حماية البيانات الشخصية، وقابل للنشر محليًا أو على سحابة خاصة، وهو حاسم للجهات الحكومية."),
         ("ثلاث كفاءات في مكان واحد", "حوكمة المحافظ، وGeoAI، والذكاء الاصطناعي المؤسسي في فريق واحد."),
         ("تنفيذ بثلاث لغات", "العربية والإنجليزية والألمانية، مع ملخصات تنفيذية تناسب صانع القرار السعودي."),
         ("عمق تقني أمريكي وألماني", "تمنحنا شراكتنا التقنية في فرجينيا وألمانيا عمقًا هندسيًا، بينما تبقى المسؤولية والتنفيذ داخل المملكة.")],
 "contact_eyebrow": "تواصل معنا", "contact_h": "لنناقش مشروعك", "contact_p": "اكتب لنا عن احتياجك. يرد فريقنا في الرياض وفرجينيا خلال يوم عمل واحد، وتُعامل جميع الاستفسارات بسرية تامة.",
 "book": "احجز مكالمة تشخيصية مدتها 30 دقيقة", "linkedin": "لينكدإن",
 "labels": {"email": "البريد الإلكتروني", "phone": "الهاتف", "hq": "الموقع", "hq_val": "الرياض، المملكة العربية السعودية", "cr": "السجل التجاري",
            "contact_h": "تواصل", "company_h": "الشركة", "privacy": "سياسة الخصوصية", "rights": "جميع الحقوق محفوظة", "links_h": "روابط"},
 "form": {"h": "أرسل لنا طلبك", "name": "الاسم", "org": "الجهة أو الشركة", "email": "البريد الإلكتروني", "phone": "الهاتف (اختياري)",
          "interest": "الخدمة المطلوبة", "msg": "رسالتك", "msg_ph": "اكتب هنا عن احتياجك أو المشروع الذي تعمل عليه.",
          "consent": "أوافق على استخدام بياناتي للرد على طلبي وفق", "send": "إرسال", "sending": "جارٍ الإرسال...",
          "ok": "وصلنا طلبك، وسنعود إليك قريبًا.", "err": "تعذر الإرسال. أرسل لنا على البريد مباشرة: " + EMAIL,
          "mail_note": "سيفتح الإرسال تطبيق البريد لديك برسالة جاهزة.", "req": "هذا الحقل مطلوب", "subject": "استفسار جديد من موقع أفيرا",
          "opts": ["الذكاء الاصطناعي المؤسسي", "GeoAI", "إدارة المحافظ", "أخرى"]},
 "privacy": {
  "title": "سياسة الخصوصية | شركة أفيرا", "desc": "سياسة الخصوصية لشركة أفيرا: كيف نتعامل مع البيانات التي تصلنا عبر البريد الإلكتروني ونموذج التواصل، وما الذي لا نجمعه، وكيف تمارس حقوقك.",
  "h1": "سياسة الخصوصية", "effective": "تاريخ السريان: نوفمبر 2026",
  "body": [
   ("1. من نحن", "تُشغّل شركة أفيرا (الرياض، المملكة العربية السعودية) هذا الموقع والخدمات المرتبطة به. وتشير عبارتا «شركة أفيرا» و«نحن» إلى هذه الجهة."),
   ("2. المعلومات التي نجمعها", "لا يستخدم هذا الموقع ملفات تعريف الارتباط ولا أدوات تحليل أو تتبع إعلاني، وتُقدَّم الخطوط والملفات من خادمنا نفسه لا من أطراف ثالثة. ومثل أي موقع، يسجّل مزوّد الاستضافة بيانات تقنية معتادة (مثل عنوان الشبكة والتاريخ والوقت والصفحة المطلوبة) لأغراض الأمان والتشغيل. وإذا راسلتنا عبر البريد الإلكتروني أو النموذج، فإننا نستلم الاسم وجهة العمل وبيانات التواصل ومضمون رسالتك."),
   ("3. كيف نستخدم معلوماتك", "نستخدم المعلومات التي تصلنا للرد على استفسارك وتقييم فرص التعاون وحفظ سجل المراسلات المؤسسية. ولا نبيع بياناتك الشخصية ولا نؤجرها ولا نشاركها مع أطراف ثالثة لأغراض تسويقية."),
   ("4. مكان معالجة البيانات", "تُعالج البيانات التي تصلنا عبر هذا الموقع وفق متطلبات نظام حماية البيانات الشخصية (PDPL) وإرشادات الهيئة السعودية للبيانات والذكاء الاصطناعي (سدايا) المعمول بها."),
   ("5. حقوقك", "يحق لك طلب الاطلاع على بياناتك الشخصية أو تصحيحها أو حذفها أو تقييد معالجتها وفق الأنظمة المعمول بها. لممارسة هذه الحقوق تواصل معنا على " + PRIVACY_EMAIL + "."),
   ("6. التواصل", "لأي استفسار عن الخصوصية راسلنا على " + PRIVACY_EMAIL + "."),
  ]},
 "nf_h": "الصفحة غير موجودة",
},
"en": {
 "dir": "ltr", "lang": "en", "base": "/en/", "other": "ar", "other_label": "العربية", "locale": "en_US", "other_locale": "ar_SA",
 "brand": "Avyra Company", "brand_core": "AVYRA", "co": "Company", "skip": "Skip to content", "home_label": "Home",
 "nav": [("about", "About"), ("services", "Services"), ("projects", "Experience"), ("team", "Team"), ("contact", "Contact")],
 "title": "Avyra Company | Enterprise AI, GeoAI and Portfolio Governance in Riyadh",
 "desc": "Avyra Company is a Saudi company in Riyadh combining enterprise AI deployment, GeoAI and portfolio governance for Vision 2030 digital transformation and environmental programs.",
 "eyebrow": "Riyadh · Saudi Arabia",
 "h1": "Innovation as a portfolio. Decisions as intelligence.",
 "lead": "A focused advisory that integrates AI solutions, portfolio governance, GeoAI and enterprise-grade AI deployment for Vision 2030 digital transformation and environmental programs.",
 "cta1": "Contact us", "cta2": "Our services", "logo_alt": "Avyra logo",
 "trust": ["Certified portfolio, program and project professionals (PfMP · PgMP · PMP)", "Saudi-registered, Riyadh-based", "Designed to align with NCA-ECC", "Delivering with US and German technology partners"],
 "about_eyebrow": "About", "about_h": "Vision and mission",
 "vision_h": "Our vision", "vision": "To be the Kingdom's trusted partner in enabling decisions, through smart, sustainable and economically sound solutions that become governed, data-driven portfolios.",
 "mission_h": "Our mission", "mission": "We develop and deploy AI business-intelligence systems, GeoAI solutions and portfolio governance frameworks that help Saudi organizations treat water as a strategic asset. By combining enterprise-grade AI engineering, GeoAI, and certified portfolio, program and project management, we turn complex environmental data into boardroom-ready intelligence.",
 "gap_h": "Why we exist", "gap": "Most firms offer one piece of the puzzle. Traditional engineering consultancies deliver technical studies but lack portfolio governance. Pure AI firms build models but do not understand hydrological uncertainty or water politics. We bring all three together under one Saudi-registered entity: governance, GeoAI and operational AI deployment.",
 "svc_eyebrow": "Services", "svc_h": "Two integrated pillars",
 "pillars": [
  {"icon": "ai", "tag": "Pillar A", "h": "Enterprise AI solutions and sovereign deployment",
   "items": [("AI agents and workflow automation", "Human-supervised automation for water utility operations, approvals and service execution, with audit trails built in."),
             ("Spatial and operational intelligence", "Infrastructure monitoring, field operations awareness and environmental visibility for distributed water assets."),
             ("Knowledge and document intelligence", "Enterprise document retrieval and multilingual (Arabic/English) content intelligence for regulators managing large technical estates."),
             ("Private and sovereign AI deployment", "Cloud, private cloud, on-premises and hybrid deployment, designed to align with NCA-ECC, SDAIA guidance and PDPL. Critical for government clients.")],
   "outcome": "Enterprise-grade AI that operates inside your security and governance perimeter."},
  {"icon": "geo", "tag": "Pillar B", "h": "GeoAI advisory",
   "items": [("GeoAI-enabled hydrological modeling", "Combining satellite imagery and remote-sensing data with hydrological models to support water-resource decisions."),
             ("Geospatial database and SDI design", "Designing geospatial databases and spatial data infrastructure that make an organization's data shareable and analyzable."),
             ("Digital twin concepts for infrastructure", "Readiness assessment, architecture design and an implementation roadmap for infrastructure digital twins.")],
   "outcome": "From satellite data to a boardroom decision, in weeks, not years."},
 ],
 "proj_eyebrow": "Experience", "proj_h": "Representative experience",
 "proj_note": "Avyra prioritizes confidentiality. Specific organizational references and detailed case studies are shared directly under appropriate confidentiality agreements. The categories below represent the combined track record of our leadership and partner teams.",
 "proj_cols": ("Sector", "Project type", "Our role"),
 "proj": [("Enterprise AI (KSA)", "AI agents for service workflows", "Operational AI deployment"),
          ("Custom AI systems", "Full-stack AI application development", "System architecture and deployment"),
          ("Custom GeoAI systems", "GeoAI dashboards and data pipelines", "System build with our development partner")],
 "team_eyebrow": "Team", "team_h": "Leadership",
 "team": [("Eng. Khalid Abdelrahman", "Chief Executive Officer", ["Enterprise AI and sovereign deployment", "AI agents, spatial intelligence and private AI deployment", "Designed to align with NCA-ECC; PDPL and SDAIA guidance applied"]),
          ("Dr.-Ing. Mohammed Abdallah", "Technical Director", [])],
 "network": "We are supported by a vetted network of AI and full-stack developers, remote sensing and GIS analysts, environmental and infrastructure experts, and project coordinators, scaled to each engagement.",
 "why_eyebrow": "Why Avyra", "why_h": "The Saudi advantage",
 "why": [("Saudi-registered, Riyadh-based", "We operate inside your regulatory and procurement environment."),
         ("Vision 2030-aligned", "Our work directly supports water security, environmental sustainability and digital transformation goals."),
         ("Sovereign AI deployment", "Designed to align with NCA-ECC and PDPL, and deployable on-premises or in private cloud. Critical for government clients."),
         ("Three competencies in one team", "Portfolio governance, GeoAI and enterprise AI together."),
         ("Trilingual delivery", "English, German and Arabic, with executive summaries tailored for Saudi decision-makers."),
         ("US and German technology depth", "Our technology partnerships in Virginia and Germany bring engineering depth, while delivery and accountability stay in the Kingdom.")],
 "contact_eyebrow": "Contact", "contact_h": "Let's discuss your project", "contact_p": "Tell us what you need. Our teams in Riyadh and Virginia respond within one business day, and all inquiries are handled with strict confidentiality.",
 "book": "Book a 30-minute diagnostic call", "linkedin": "LinkedIn",
 "labels": {"email": "Email", "phone": "Phone", "hq": "Location", "hq_val": "Riyadh, Saudi Arabia", "cr": "C.R. number",
            "contact_h": "Contact", "company_h": "Company", "privacy": "Privacy policy", "rights": "All rights reserved", "links_h": "Links"},
 "form": {"h": "Send us a message", "name": "Name", "org": "Organization", "email": "Email", "phone": "Phone (optional)",
          "interest": "Service of interest", "msg": "Your message", "msg_ph": "Tell us about your need or the project you are working on.",
          "consent": "I agree that my data is used to answer my request, as described in the", "send": "Send", "sending": "Sending...",
          "ok": "We received your message and will get back to you shortly.", "err": "Could not send. Please email us directly: " + EMAIL,
          "mail_note": "Sending opens your email app with a ready message.", "req": "This field is required", "subject": "New enquiry from the Avyra website",
          "opts": ["Enterprise AI", "GeoAI", "Portfolio management", "Other"]},
 "privacy": {
  "title": "Privacy Policy | Avyra Company", "desc": "Avyra Company's privacy policy: how we handle data sent by email and through the contact form, what we do not collect, and how to exercise your rights.",
  "h1": "Privacy policy", "effective": "Effective: November 2026",
  "body": [
   ("1. Who we are", "Avyra Company (Riyadh, Saudi Arabia) operates this website and its related services. References to \"Avyra Company\" and \"we\" mean this entity."),
   ("2. Information we collect", "This website does not use cookies, analytics or advertising trackers, and its fonts and files are served from our own server, not third parties. Like any website, our hosting provider logs routine technical data (such as network address, date and time, and the page requested) for security and operations. If you write to us by email or the contact form, we receive your name, organization, contact details and the content of your message."),
   ("3. How we use your information", "We use the information we receive to answer your enquiry, assess collaboration opportunities and keep a record of business correspondence. We do not sell or rent your personal data, and we do not share it with third parties for marketing."),
   ("4. Where data is processed", "Data sent through this website is handled in line with the Personal Data Protection Law (PDPL) and applicable SDAIA guidance."),
   ("5. Your rights", "You may ask to access, correct, delete or restrict the processing of your personal data under applicable law. To exercise these rights, contact us at " + PRIVACY_EMAIL + "."),
   ("6. Contact", "For any privacy question, write to " + PRIVACY_EMAIL + "."),
  ]},
 "nf_h": "Page not found",
},
}

# ---------------------------------------------------------------- helpers
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
def path_for(lang, key):
    base = T[lang]["base"]; return base if key == "home" else f"{base}{key}/"
def url(lang, key): return SITE + path_for(lang, key)
def write(rel, content):
    p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(content)

def org_ld(lang):
    d = {"@context": "https://schema.org", "@type": "Organization", "name": "Avyra Company", "alternateName": "شركة أفيرا",
         "url": SITE + "/", "logo": SITE + "/assets/img/icon-512.png", "email": EMAIL,
         "address": {"@type": "PostalAddress", "addressLocality": "Riyadh", "addressCountry": "SA"}, "areaServed": "SA"}
    if PHONE_TEL: d["telephone"] = PHONE_TEL
    if CR: d["identifier"] = CR
    return d

def head(lang, key, title, desc, ld=None):
    t = T[lang]; o = t["other"]
    ldh = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in (ld or []))
    return f'''<!doctype html>
<html lang="{t["lang"]}" dir="{t["dir"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url(lang, key)}">
<link rel="alternate" hreflang="{lang}" href="{url(lang, key)}">
<link rel="alternate" hreflang="{o}" href="{url(o, key)}">
<link rel="alternate" hreflang="x-default" href="{url('ar', key)}">
<meta name="theme-color" content="#0b0b0d">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(t["brand"])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url(lang, key)}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{t["locale"]}">
<meta property="og:locale:alternate" content="{t["other_locale"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}/assets/img/og-image.png">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
{PRELOAD[lang]}<link rel="stylesheet" href="{CSS}">
<script>document.documentElement.classList.add("js")</script>
{ldh}</head>
'''

MENU = {"ar": ("القائمة", "إغلاق القائمة"), "en": ("Menu", "Close menu")}

def header(lang, key):
    t = T[lang]; b = t["base"]; o = t["other"]
    links = "".join(f'<a href="{b}#{k}">{n}</a>' for k, n in t["nav"])
    return f'''<a class="skip" href="#main">{t["skip"]}</a>
<header class="site">
  <a class="brand" href="{b}" aria-label="{esc(t["brand"])} - {t["home_label"]}"><img src="/assets/img/mark.png" alt="" width="46" height="48"><span class="brand-txt"><span class="brand-name">{esc(t["brand_core"])}</span><span class="brand-co">{t["co"]}</span></span></a>
  <button class="menu-btn" type="button" hidden aria-label="{MENU[lang][0]}" aria-expanded="false" aria-controls="site-nav" data-open="{MENU[lang][0]}" data-close="{MENU[lang][1]}"><span class="bars" aria-hidden="true"></span></button>
  <nav class="main" id="site-nav" aria-label="{'التنقل الرئيسي' if lang == 'ar' else 'Main'}">
    {links}
    <a class="lang" href="{path_for(o, key)}" hreflang="{o}" lang="{o}">{t["other_label"]}</a>
  </nav>
</header>
'''

def contact_items(lang):
    t = T[lang]; L = t["labels"]; rows = [(L["email"], f'<a href="mailto:{EMAIL}"><bdi>{EMAIL}</bdi></a>')]
    if PHONE_TEL: rows.append((L["phone"], f'<a href="tel:{PHONE_TEL}"><bdi>{PHONE_DISPLAY}</bdi></a>'))
    if LINKEDIN_URL: rows.append((t["linkedin"], f'<a href="{LINKEDIN_URL}" target="_blank" rel="noopener">LinkedIn</a>'))
    rows.append((L["hq"], L["hq_val"]))
    if CR: rows.append((L["cr"], f"<bdi>{CR}</bdi>"))
    return rows

def footer(lang):
    t = T[lang]; L = t["labels"]; b = t["base"]
    nav = "".join(f'<li><a href="{b}#{k}">{n}</a></li>' for k, n in t["nav"][:4])
    contact = "".join(f"<li>{v}</li>" for _, v in contact_items(lang))
    return f'''<footer class="site">
  <div class="wrap">
    <div class="stack g12"><a class="brand" href="{b}"><img src="/assets/img/mark.png" alt="" width="34" height="36" loading="lazy"><span class="brand-txt"><span class="brand-name" style="font-size:20px">{esc(t["brand_core"])}</span><span class="brand-co">{t["co"]}</span></span></a>
      <p>{L["hq_val"]}</p></div>
    <div><h2>{L["links_h"]}</h2><ul>{nav}</ul></div>
    <div><h2>{L["contact_h"]}</h2><ul>{contact}</ul></div>
    <div><h2>{L["company_h"]}</h2><ul><li><a href="{path_for(lang, "privacy")}">{L["privacy"]}</a></li></ul></div>
    <p class="fine">© 2026 {esc(t["brand"])}. {L["rights"]}.</p>
  </div>
</footer>
'''

def form_html(lang):
    f = T[lang]["form"]; t = T[lang]
    opts = "".join(f'<option value="{esc(o)}">{o}</option>' for o in f["opts"])
    action = FORM_ENDPOINT or f"mailto:{EMAIL}"
    return f'''<form class="form" id="f-home" method="post" action="{action}" data-endpoint="{FORM_ENDPOINT}" data-key="{FORM_KEY}" data-subject="{esc(f["subject"])}" data-ok="{esc(f["ok"])}" data-err="{esc(f["err"])}" data-sending="{esc(f["sending"])}" data-req="{esc(f["req"])}" novalidate>
  <h3>{f["h"]}</h3>
  <div class="fields">
    <label for="f-name">{f["name"]}<input id="f-name" name="name" type="text" autocomplete="name" required></label>
    <label for="f-org">{f["org"]}<input id="f-org" name="organization" type="text" autocomplete="organization"></label>
    <label for="f-email">{f["email"]}<input id="f-email" name="email" type="email" autocomplete="email" dir="ltr" required></label>
    <label for="f-phone">{f["phone"]}<input id="f-phone" name="phone" type="tel" autocomplete="tel" dir="ltr"></label>
    <label for="f-int" class="full">{f["interest"]}<select id="f-int" name="division">{opts}</select></label>
    <label for="f-msg" class="full">{f["msg"]}<textarea id="f-msg" name="message" rows="5" placeholder="{esc(f["msg_ph"])}" required></textarea></label>
  </div>
  <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
  <label class="consent" for="f-ok"><input id="f-ok" name="consent" type="checkbox" required><span>{f["consent"]} <a href="{path_for(lang, "privacy")}">{t["labels"]["privacy"]}</a></span></label>
  <div class="actions"><button class="btn gold" type="submit">{f["send"]}</button>{'' if FORM_ENDPOINT else '<p class="note">' + f["mail_note"] + '</p>'}</div>
  <p class="status" role="status" aria-live="polite"></p>
</form>'''

# ---------------------------------------------------------------- pages
def home(lang):
    t = T[lang]
    arrow = "←" if lang == "ar" else "→"
    trust = "".join("<li>" + esc(x).replace("PfMP · PgMP · PMP", "<bdi>PfMP · PgMP · PMP</bdi>") + "</li>" for x in t["trust"])
    logo = f"/assets/img/logo-{lang}.png"
    dims = {"ar": (440, 486), "en": (440, 573)}[lang]
    pillars = ""
    for p in t["pillars"]:
        items = "".join(f'<div class="principle"><h3>{esc(a)}</h3><p>{esc(c)}</p></div>' for a, c in p["items"])
        pillars += f'''<div class="card pillar">{ICONS[p["icon"]]}<p class="eyebrow">{p["tag"]}</p><h3>{esc(p["h"])}</h3><div class="stack">{items}</div><p class="outcome">{esc(p["outcome"])}</p></div>
'''
    c = t["proj_cols"]
    proj = "".join(f'<div class="card"><p class="eyebrow">{esc(a)}</p><h3>{esc(b)}</h3><p><strong>{c[2]}:</strong> {esc(r)}</p></div>' for a, b, r in t["proj"])
    team = ""
    for n, r, pts in t["team"]:
        lis = f'<ul>{"".join(f"<li>{esc(x)}</li>" for x in pts)}</ul>' if pts else ""
        team += f'<div class="card"><h3>{esc(n)}</h3><p class="eyebrow">{esc(r)}</p>{lis}</div>\n'
    why = "".join(f'<div class="card"><h3>{esc(a)}</h3><p>{esc(b)}</p></div>' for a, b in t["why"])
    rows = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in contact_items(lang))
    book = f'<div class="btns"><a class="btn" href="{BOOKING_URL}" target="_blank" rel="noopener">{t["book"]}</a></div>' if BOOKING_URL else ""
    body = f'''<body>
{header(lang, "home")}<main id="main">
<section class="hero">
  <div class="wrap cols" style="align-items:center">
    <div class="stack g28">
      <p class="eyebrow">{t["eyebrow"]}</p>
      <h1>{t["h1"]}</h1>
      <p class="lead">{t["lead"]}</p>
      <div class="btns"><a class="btn gold" href="#contact">{t["cta1"]}</a><a class="btn" href="#services">{t["cta2"]}</a></div>
    </div>
    <div class="hero-art"><div class="emb"><img src="{logo}" alt="{t["logo_alt"]}" width="{dims[0]}" height="{dims[1]}" fetchpriority="high"><span class="sheen" style="--m:url({logo})" aria-hidden="true"></span></div></div>
  </div>
</section>
<section class="trustbar"><div class="wrap"><ul>{trust}</ul></div></section>
<section id="about" class="alt"><div class="wrap stack g48">
  <div class="stack g12" style="max-width:640px"><p class="eyebrow">{t["about_eyebrow"]}</p><h2>{t["about_h"]}</h2></div>
  <div class="cols"><div class="stack g12"><h3>{t["vision_h"]}</h3><p class="muted">{t["vision"]}</p></div><div class="stack g12"><h3>{t["mission_h"]}</h3><p class="muted">{t["mission"]}</p></div></div>
  <div class="stack g12 gap-note"><h3>{t["gap_h"]}</h3><p class="muted">{t["gap"]}</p></div>
</div></section>
<section id="services"><div class="wrap stack g48">
  <div class="stack g12" style="max-width:640px"><p class="eyebrow">{t["svc_eyebrow"]}</p><h2>{t["svc_h"]}</h2></div>
  <div class="cards two">{pillars}</div>
</div></section>
<section id="projects" class="alt"><div class="wrap stack g48">
  <div class="stack g12" style="max-width:720px"><p class="eyebrow">{t["proj_eyebrow"]}</p><h2>{t["proj_h"]}</h2><p class="muted">{t["proj_note"]}</p></div>
  <div class="cards">{proj}</div>
</div></section>
<section id="team"><div class="wrap stack g48">
  <div class="stack g12" style="max-width:640px"><p class="eyebrow">{t["team_eyebrow"]}</p><h2>{t["team_h"]}</h2></div>
  <div class="cards">{team}</div>
  <p class="muted" style="max-width:70ch">{t["network"]}</p>
</div></section>
<section id="why" class="alt"><div class="wrap stack g48">
  <div class="stack g12" style="max-width:640px"><p class="eyebrow">{t["why_eyebrow"]}</p><h2>{t["why_h"]}</h2></div>
  <div class="cards">{why}</div>
</div></section>
<section id="contact">
  <div class="wrap cols">
    <div class="stack g28"><div class="stack g20"><p class="eyebrow">{t["contact_eyebrow"]}</p><h2>{t["contact_h"]}</h2><p class="muted">{t["contact_p"]}</p></div><dl class="rows">{rows}</dl>{book}</div>
    {form_html(lang)}
  </div>
</section>
</main>
{footer(lang)}<script src="{JS}" defer></script>
</body></html>
'''
    return head(lang, "home", t["title"], t["desc"], [org_ld(lang)]) + body

def privacy(lang):
    t = T[lang]; p = t["privacy"]
    paras = "".join(f"<h2>{a}</h2><p>{c}</p>" for a, c in p["body"])
    crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": t["home_label"], "item": url(lang, "home")},
        {"@type": "ListItem", "position": 2, "name": t["labels"]["privacy"], "item": url(lang, "privacy")}]}
    body = f'''<body>
{header(lang, "privacy")}<main id="main">
<section class="page-hero"><div class="wrap stack g20"><h1>{p["h1"]}</h1><p class="muted">{p["effective"]}</p></div></section>
<section><div class="wrap prose">{paras}</div></section>
</main>
{footer(lang)}<script src="{JS}" defer></script>
</body></html>
'''
    return head(lang, "privacy", p["title"], p["desc"], [crumb]) + body

def notfound():
    return f'''<!doctype html>
<html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>الصفحة غير موجودة | Page not found</title><meta name="robots" content="noindex">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="preload" href="/assets/fonts/ibm-plex-sans-arabic-arabic-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{CSS}"></head>
<body><main id="main" style="min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:40px 20px">
<div class="stack g20" style="align-items:center"><img src="/assets/img/mark.png" alt="" width="84" height="88">
<h1 style="font-size:44px">الصفحة غير موجودة</h1><p class="muted">Page not found</p>
<div class="btns" style="justify-content:center"><a class="btn gold" href="/">الرئيسية</a><a class="btn" href="/en/">Home (English)</a></div></div></main></body></html>
'''

def sitemap():
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for lang in ("ar", "en"):
        for k in ("home", "privacy"):
            o = T[lang]["other"]
            out.append(f'<url><loc>{url(lang, k)}</loc><xhtml:link rel="alternate" hreflang="{lang}" href="{url(lang, k)}"/>'
                       f'<xhtml:link rel="alternate" hreflang="{o}" href="{url(o, k)}"/><xhtml:link rel="alternate" hreflang="x-default" href="{url("ar", k)}"/></url>')
    out.append("</urlset>")
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    for lang in ("ar", "en"):
        b = T[lang]["base"].lstrip("/")
        write(f"{b}index.html", home(lang))
        write(f"{b}privacy/index.html", privacy(lang))
    write("404.html", notfound())
    write("sitemap.xml", sitemap())
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    write("site.webmanifest", json.dumps({"name": "Avyra Company | شركة أفيرا", "short_name": "Avyra", "start_url": "/", "display": "browser",
        "background_color": "#0b0b0d", "theme_color": "#0b0b0d",
        "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, ensure_ascii=False, indent=2) + "\n")
    write("_headers", """/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Content-Security-Policy: default-src 'self'; style-src 'self'; font-src 'self'; img-src 'self' data:; script-src 'self' 'unsafe-inline'; script-src-attr 'none'; base-uri 'self'; form-action 'self' mailto: https://formspree.io https://api.web3forms.com; connect-src 'self' https://formspree.io https://api.web3forms.com; frame-ancestors 'none'; object-src 'none'
/assets/*
  Cache-Control: public, max-age=31536000, immutable
""")
    print("built")
