from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, Indenter
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

# Colors
ACCENT = HexColor('#2563eb')
TEXT_PRIMARY = HexColor('#1a1a2e')
TEXT_SECONDARY = HexColor('#444444')
TEXT_MUTED = HexColor('#777777')
AWARD_BG = HexColor('#fef3c7')
AWARD_TEXT = HexColor('#d97706')

# Styles
style_name = ParagraphStyle('Name', fontName='Helvetica-Bold', fontSize=20, textColor=TEXT_PRIMARY, spaceAfter=2, leading=24)
style_tagline = ParagraphStyle('Tagline', fontName='Helvetica', fontSize=10, textColor=TEXT_MUTED, spaceAfter=2)
style_contact = ParagraphStyle('Contact', fontName='Helvetica', fontSize=9, textColor=ACCENT, spaceAfter=6)
style_section = ParagraphStyle('Section', fontName='Helvetica-Bold', fontSize=11, textColor=ACCENT, spaceBefore=10, spaceAfter=4)
style_subsection = ParagraphStyle('Subsection', fontName='Helvetica-Bold', fontSize=9.5, textColor=TEXT_PRIMARY, spaceBefore=2, spaceAfter=0)
style_body = ParagraphStyle('Body', fontName='Helvetica', fontSize=9, textColor=TEXT_SECONDARY, leading=13, spaceAfter=2)
INDENT = 12
style_body_small = ParagraphStyle('BodySmall', fontName='Helvetica', fontSize=8.5, textColor=TEXT_SECONDARY, leading=12, spaceAfter=2, leftIndent=INDENT)
style_bullet = ParagraphStyle('Bullet', fontName='Helvetica', fontSize=8.5, textColor=TEXT_SECONDARY, leading=12, leftIndent=INDENT+14, spaceAfter=1, bulletIndent=INDENT)
style_pub_title = ParagraphStyle('PubTitle', fontName='Helvetica-Bold', fontSize=8.5, textColor=TEXT_PRIMARY, leading=11, spaceAfter=0, leftIndent=INDENT)
style_pub_meta = ParagraphStyle('PubMeta', fontName='Helvetica', fontSize=7.5, textColor=TEXT_MUTED, leading=10, spaceAfter=3, leftIndent=INDENT)
style_job_title = ParagraphStyle('JobTitle', fontName='Helvetica-Bold', fontSize=10, textColor=TEXT_PRIMARY, spaceAfter=0)
style_job_period = ParagraphStyle('JobPeriod', fontName='Helvetica', fontSize=9, textColor=TEXT_MUTED, alignment=TA_RIGHT)
style_exp_label = ParagraphStyle('ExpLabel', fontName='Helvetica-Bold', fontSize=9, textColor=TEXT_PRIMARY, spaceBefore=4, spaceAfter=1, leftIndent=INDENT)
style_pub_group = ParagraphStyle('PubGroup', fontName='Helvetica-Oblique', fontSize=9, textColor=TEXT_SECONDARY, spaceBefore=6, spaceAfter=2, leftIndent=INDENT)
style_edu_desc = ParagraphStyle('EduDesc', fontName='Helvetica', fontSize=8.5, textColor=TEXT_SECONDARY, leading=12, spaceAfter=1, leftIndent=INDENT)

def build_resume():
    doc = SimpleDocTemplate(
        "/Users/bytedance/Documents/claude/yu-gong-homepage/Yu_Gong_Resume.pdf",
        pagesize=letter,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch,
        leftMargin=0.65*inch,
        rightMargin=0.65*inch
    )

    story = []
    W = doc.width

    tbl_style = TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ])

    # === Header ===
    story.append(Paragraph("Yu Gong", style_name))
    story.append(Paragraph("Director of Engineering @ TikTok  |  AI Search  |  LLM Agents  |  Recommender Systems", style_tagline))
    story.append(Paragraph(
        '<font color="#444444">gy910210@gmail.com  |  425-221-8131</font>  |  '
        '<a href="https://gongyu.vercel.app/">Homepage</a>  |  '
        '<a href="https://scholar.google.com/citations?user=QseahYcAAAAJ">Google Scholar</a>  |  '
        '<a href="https://www.linkedin.com/in/gongyu210/">LinkedIn</a>  |  '
        '<a href="https://x.com/gy910210">X / Twitter</a>',
        style_contact
    ))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=6))

    # === About ===
    story.append(Paragraph("ABOUT", style_section))
    story.append(Paragraph(
        "Director of Engineering at TikTok, leading a 35+ person team building <b>AI Search</b> and <b>AI Shopping Agent</b> "
        "for global e-commerce. 9+ years of experience in large-scale search and recommender systems, previously at ByteDance and Alibaba. "
        "My work spans search, recommendation, and agent systems, which I view as different forms of large-scale decision systems "
        "for resolving user intent under uncertainty \u2014 from retrieval and ranking to multi-step reasoning and decision making.",
        style_body
    ))
    story.append(Paragraph(
        "Research interests: LLM-powered search, LLM agents (post-training, personalization, evaluation), and recommender systems. "
        "Recipient of the <b>SIGIR 2017 Best Paper Honorable Mention</b> (IRGAN, 800+ citations).",
        style_body
    ))

    # === Experience ===
    story.append(Paragraph("EXPERIENCE", style_section))

    # --- TikTok ---
    story.append(Indenter(left=INDENT))
    job_header = Table(
        [[Paragraph("<b>Director of Engineering</b>  |  TikTok", style_job_title),
          Paragraph("2024 - Present", style_job_period)]],
        colWidths=[(W - INDENT)*0.72, (W - INDENT)*0.28]
    )
    job_header.setStyle(tbl_style)
    story.append(job_header)
    story.append(Indenter(left=-INDENT))
    story.append(Paragraph(
        "Leading a 35+ person team owning full-stack search algorithms (retrieval, pre-ranking, ranking, mix-ranking) "
        "and <b>AI Shopping Agent</b> for TikTok's global e-commerce across the US, Southeast Asia, Europe, and more.",
        style_body_small
    ))

    story.append(Paragraph("LLM-powered Search", style_exp_label))
    story.append(Paragraph("Drove significant GMV gains through LLM-powered search innovations:", style_body_small))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Generative Retrieval</b> \u2014 decode-only generative models for product retrieval.", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Large Search Model (LSM)</b> \u2014 Transformer-based search model with parameter scaling across retrieval and ranking.", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Multi-Modality</b> \u2014 multi-modal representation fusion and co-training for retrieval and ranking.", style_bullet))

    story.append(Paragraph("AI Shopping Agent", style_exp_label))
    story.append(Paragraph("Built from scratch and launched TikTok's AI Shopping Agent:", style_body_small))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Agent Framework</b> \u2014 Planner-Executor-Verifier architecture (extended ReAct) with multi-turn context management and heterogeneous tool use (Web / Product / Video Search).", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Memory &amp; Personalization</b> \u2014 Memory-as-Tool design that leverages user behavioral signals for personalized responses.", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Post-Training</b> \u2014 rejection-sampling SFT with synthetic multi-turn data for model cold-start; RL fine-tuning with Rubric Reward &amp; Deep Search Reward. Research on Active Reasoning of LLM Agents (T3, AREW).", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Evaluation &amp; Benchmark</b> \u2014 built ShoppingBench (deep product search), APeB (personalized agent behavior, with public leaderboard), and rubric-based report evaluation.", style_bullet))

    # --- ByteDance ---
    story.append(Spacer(1, 4))
    story.append(Indenter(left=INDENT))
    job_header2 = Table(
        [[Paragraph("<b>Senior Engineering Manager</b>  |  ByteDance", style_job_title),
          Paragraph("2021 - 2024", style_job_period)]],
        colWidths=[(W - INDENT)*0.72, (W - INDENT)*0.28]
    )
    job_header2.setStyle(tbl_style)
    story.append(job_header2)
    story.append(Indenter(left=-INDENT))
    story.append(Paragraph(
        "Led a 20+ person team. Built <b>Douyin Mall</b>'s <b>homepage feed recommendation system</b> from scratch - "
        "the full-stack personalized pipeline covering retrieval, ranking, and mix-ranking across heterogeneous "
        "content types (products, short videos, and livestreams). Laid the technical foundation for Douyin's "
        "personalized e-commerce recommendations, contributing to Douyin E-commerce's growth into "
        "<b>China's second-largest e-commerce platform</b> by GMV.",
        style_body_small
    ))

    # --- Alibaba ---
    story.append(Spacer(1, 4))
    story.append(Indenter(left=INDENT))
    job_header3 = Table(
        [[Paragraph("<b>Tech Lead</b>  |  Alibaba Group", style_job_title),
          Paragraph("2017 - 2021", style_job_period)]],
        colWidths=[(W - INDENT)*0.72, (W - INDENT)*0.28]
    )
    job_header3.setStyle(tbl_style)
    story.append(job_header3)
    story.append(Indenter(left=-INDENT))
    story.append(Paragraph(
        "Pioneered <b>EdgeRec</b> - the industry's first on-device AI recommender in a billion-scale commerce feed for Mobile Taobao. "
        "Invented the <b>Generator-Evaluator</b> two-stage re-ranking framework (GRN, GE), now the standard paradigm for listwise re-ranking. "
        "Created Alibaba's Edge-X-Platform (Edge-Cloud MLOps), powering 10+ business lines across Alibaba.",
        style_body_small
    ))

    # === Selected Publications ===
    story.append(Paragraph("SELECTED PUBLICATIONS", style_section))
    story.append(Paragraph('Total citations: 1,690  |  h-index: 16  |  Full list on <a href="https://scholar.google.com/citations?user=QseahYcAAAAJ">Google Scholar</a>', style_body_small))

    # --- Reasoning & Reinforcement Learning ---
    story.append(Paragraph("Reasoning &amp; Reinforcement Learning", style_pub_group))
    pubs_reasoning = [
        ("On Information Self-Locking in Reinforcement Learning for Active Reasoning of LLM Agents",
         "D Zou, Y Chen, F Feng, M Li, P Li, <b>Y Gong</b>, J Cheng",
         "Submitted to ICML 2026", "Project Lead", None),
        ("Reducing Belief Deviation in Reinforcement Learning for Active Reasoning of LLM Agents",
         "D Zou, Y Chen, J Wang, G Yang, M Li, Q Da, J Cheng, P Li, <b>Y Gong</b>",
         "ICLR 2026 | Oral", "Project Lead", "1"),
        ("A Minimax Game for Instance Based Selective Transfer Learning",
         "B Wang, M Qiu, X Wang, Y Li, <b>Y Gong</b>, X Zeng, J Huang, B Zheng, D Cai, ...",
         "SIGKDD 2019", None, "60"),
    ]
    for title, authors, venue, role, cited in pubs_reasoning:
        story.append(Paragraph(title, style_pub_title))
        parts = [f"{authors}  |  {venue}"]
        if role:
            parts.append(f"  |  <b>{role}</b>")
        if cited:
            parts.append(f"  |  Cited by {cited}")
        story.append(Paragraph("".join(parts), style_pub_meta))

    # --- Recommender Systems ---
    story.append(Paragraph("Recommender Systems", style_pub_group))
    pubs_recsys = [
        ("EdgeRec: Recommender System on Edge in Mobile Taobao",
         "<b>Y Gong</b>, Z Jiang, Y Feng, B Hu, K Zhao, Q Liu, W Ou",
         "CIKM 2020", "First Author", "110"),
        ("Personalized Adaptive Meta Learning for Cold-start User Preference Prediction",
         "R Yu, <b>Y Gong</b>, X He, Y Zhu, Q Liu, W Ou, B An",
         "AAAI 2021", None, "101"),
        ("Exact-k Recommendation via Maximal Clique Optimization",
         "<b>Y Gong</b>, Y Zhu, L Duan, Q Liu, Z Guan, F Sun, W Ou, KQ Zhu",
         "SIGKDD 2019", "First Author", "63"),
        ("GRN: Generative Rerank Network for Context-wise Recommendation",
         "Y Feng, B Hu, <b>Y Gong</b>, F Sun, Q Liu, W Ou",
         "arXiv 2021", None, "32"),
        ("Revisit Recommender System in the Permutation Prospective",
         "Y Feng, <b>Y Gong</b>, F Sun, Q Liu, W Ou",
         "arXiv 2021", None, "31"),
        ("Query-based Interactive Recommendation by Meta-path and Adapted Attention-GRU",
         "Y Zhu, <b>Y Gong</b>, Q Liu, Y Ma, W Ou, J Zhu, B Wang, Z Guan, D Cai",
         "CIKM 2019", "Co-First Author", "21"),
        ("Gift: Graph-guided Feature Transfer for Cold-start Video Click-through Rate Prediction",
         "Y Cao, S Hu, <b>Y Gong</b>, Z Li, Y Yang, Q Liu, S Ji",
         "CIKM 2022", None, "18"),
    ]
    for title, authors, venue, role, cited in pubs_recsys:
        story.append(Paragraph(title, style_pub_title))
        parts = [f"{authors}  |  {venue}"]
        if role:
            parts.append(f"  |  <b>{role}</b>")
        if cited:
            parts.append(f"  |  Cited by {cited}")
        story.append(Paragraph("".join(parts), style_pub_meta))

    # --- Information Retrieval & Search ---
    story.append(Paragraph("Information Retrieval &amp; Search", style_pub_group))
    pubs_ir = [
        ("IRGAN: A Minimax Game for Unifying Generative and Discriminative Information Retrieval Models",
         "J Wang, L Yu, W Zhang, <b>Y Gong</b>, Y Xu, B Wang, Z Peng, D Zhang",
         "ACM SIGIR 2017", "Best Paper Honorable Mention | First Industry Author", "829"),
        ("Conceptualize and Infer User Needs in E-commerce",
         "X Luo, Y Yang, KQ Zhu, <b>Y Gong</b>, K Yang",
         "CIKM 2019", None, "21"),
        ("Query Tracking for E-commerce Conversational Search: A Machine Comprehension Perspective",
         "Y Yang, <b>Y Gong</b>, X Chen",
         "CIKM 2018", None, "13"),
    ]
    for title, authors, venue, role, cited in pubs_ir:
        story.append(Paragraph(title, style_pub_title))
        parts = [f"{authors}  |  {venue}"]
        if role:
            parts.append(f"  |  <b>{role}</b>")
        if cited:
            parts.append(f"  |  Cited by {cited}")
        story.append(Paragraph("".join(parts), style_pub_meta))

    # --- NLP & Text Generation ---
    story.append(Paragraph("NLP &amp; Text Generation", style_pub_group))
    pubs_nlp = [
        ("Deep Cascade Multi-task Learning for Slot Filling in Online Shopping Assistant",
         "<b>Y Gong</b>, X Luo, Y Zhu, W Ou, Z Li, M Zhu, KQ Zhu, L Duan, X Chen",
         "AAAI 2019", "First Author", "42"),
        ("Multi-Modal Generative Adversarial Network for Short Product Title Generation in Mobile E-Commerce",
         "J Zhang, P Zou, Z Li, Y Wan, X Pan, <b>Y Gong</b>, PS Yu",
         "NAACL 2019", None, "35"),
        ("Automatic Generation of Chinese Short Product Titles for Mobile Display",
         "<b>Y Gong</b>, X Luo, KQ Zhu, W Ou, Z Li, L Duan",
         "AAAI 2019", "First Author", "35"),
        ("Representing Verbs as Argument Concepts",
         "<b>Y Gong</b>, K Zhao, KQ Zhu",
         "AAAI 2016", "First Author", "20"),
    ]
    for title, authors, venue, role, cited in pubs_nlp:
        story.append(Paragraph(title, style_pub_title))
        parts = [f"{authors}  |  {venue}"]
        if role:
            parts.append(f"  |  <b>{role}</b>")
        if cited:
            parts.append(f"  |  Cited by {cited}")
        story.append(Paragraph("".join(parts), style_pub_meta))

    # === Education ===
    story.append(Paragraph("EDUCATION", style_section))

    story.append(Indenter(left=INDENT))
    edu1 = Table(
        [[Paragraph("<b>M.S. in Computer Science</b>  |  Shanghai Jiao Tong University", style_subsection),
          Paragraph("2014 - 2017", style_job_period)]],
        colWidths=[(W - INDENT)*0.72, (W - INDENT)*0.28]
    )
    edu1.setStyle(tbl_style)
    story.append(edu1)
    story.append(Indenter(left=-INDENT))
    story.append(Paragraph("Research Assistant in ADAPT Lab. Research areas: Information Retrieval, NLP, Machine Learning.", style_edu_desc))

    story.append(Spacer(1, 3))
    story.append(Indenter(left=INDENT))
    edu2 = Table(
        [[Paragraph("<b>B.S. in Computer Software Engineering</b>  |  Xi'an Jiaotong University", style_subsection),
          Paragraph("2010 - 2014", style_job_period)]],
        colWidths=[(W - INDENT)*0.72, (W - INDENT)*0.28]
    )
    edu2.setStyle(tbl_style)
    story.append(edu2)
    story.append(Indenter(left=-INDENT))
    story.append(Paragraph("Google Excellent Scholarship recipient (awarded to 100 students in China).", style_edu_desc))

    # === Honors & Awards ===
    story.append(Paragraph("HONORS &amp; AWARDS", style_section))
    story.append(Paragraph("ACM SIGIR 2017 Best Paper Award Honorable Mention", style_body_small))
    story.append(Paragraph("Google Excellent Scholarship - awarded to 100 students in China (2013)", style_body_small))

    doc.build(story)
    print("Resume generated: Yu_Gong_Resume.pdf")

build_resume()
