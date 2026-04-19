from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, Indenter, PageBreak
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
style_pub_oneline = ParagraphStyle('PubOneline', fontName='Helvetica', fontSize=8, textColor=TEXT_SECONDARY, leading=11, spaceAfter=2, leftIndent=INDENT)
style_edu_desc = ParagraphStyle('EduDesc', fontName='Helvetica', fontSize=8.5, textColor=TEXT_SECONDARY, leading=12, spaceAfter=1, leftIndent=INDENT)

def build_resume():
    doc = SimpleDocTemplate(
        "/Users/bytedance/Documents/claude/yu-gong-homepage/Tim_Yu_Resume.pdf",
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
    story.append(Paragraph("Tim Yu", style_name))
    story.append(Paragraph("Director of Engineering @ TikTok  |  AI Search  |  LLM Agents  |  Recommender Systems", style_tagline))
    story.append(Paragraph(
        '<font color="#444444">gy910210@gmail.com  |  425-221-8131</font>',
        style_contact
    ))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=6))

    # === About ===
    story.append(Paragraph("ABOUT", style_section))
    story.append(Paragraph(
        "Director of Engineering at TikTok, leading a 40+ person team building <b>AI Search</b> and <b>Shopping Agent</b> "
        "for global e-commerce. 9+ years of experience in large-scale search and recommender systems, previously at ByteDance and Alibaba. "
        "My work spans search, recommendation, and agent systems. I am building toward an <b>AI-native shopping decision system</b> "
        "\u2014 unifying retrieval and ranking with multi-step reasoning and autonomous decision making.",
        style_body
    ))
    story.append(Paragraph(
        "Research interests: LLM-powered search, LLM agents (harness engineering, memory & personalization, post-training, agentic-RL, evaluation), and recommender systems. "
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
        "Lead a 40+ engineer organization owning AI Search and Shopping Agent systems for TikTok global e-commerce "
        "across multiple regions (US, Europe, Southeast Asia and more), driving end-to-end product and technical roadmap "
        "for search systems serving ~140M daily e-commerce queries in the US alone.",
        style_body_small
    ))

    story.append(Paragraph("LLM-powered Search", style_exp_label))
    story.append(Paragraph("Led the evolution of search systems toward LLM-based retrieval and ranking:", style_body_small))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Query Planning</b> \u2014 LLM multi-agent framework (Analyzer-Identifier-Rewriter-Judger) for resolving ambiguous queries into latent product intents.", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Generative Retrieval</b> \u2014 decode-only generative models for product retrieval.", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Large Search Model</b> \u2014 Transformer-based search model with parameter and behavior sequence scaling up across retrieval and ranking.", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Multi-Modality</b> \u2014 multi-modal representation fusion and co-training for retrieval and ranking.", style_bullet))

    story.append(Paragraph("Shopping Agent", style_exp_label))
    story.append(Paragraph("Built and launched TikTok's Shopping Agent from scratch:", style_body_small))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Agent Framework</b> \u2014 Planner-Executor-Verifier architecture (extended ReAct) with multi-turn context management and heterogeneous tool use (Web / Product / Video Search).", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Memory &amp; Personalization</b> \u2014 Memory-as-Tool design that leverages user behavioral signals for personalized responses.", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Post-Training</b> \u2014 rejection-sampling SFT with synthetic multi-turn data for model cold-start; RL fine-tuning with Rubric Reward &amp; Deep Search Reward. Research on Active Reasoning of LLM Agents (T3, AREW).", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Evaluation &amp; Benchmark</b> \u2014 built ShoppingBench (deep product search), APeB (personalized agent behavior), and rubric-based report evaluation.", style_bullet))
    # story.append(Paragraph(u"<bullet>\u2022</bullet><b>Impact</b> \u2014 improved conversion rate (+0.2%), reduced query reformulation rate by 3%, and improved user engagement by +34% in side-by-side (SBS) evaluation.", style_bullet))

    # --- ByteDance ---
    story.append(Spacer(1, 4))
    story.append(Indenter(left=INDENT))
    job_header2 = Table(
        [[Paragraph("<b>Senior Engineering Manager / Tech Lead</b>  |  ByteDance", style_job_title),
          Paragraph("2021 - 2024", style_job_period)]],
        colWidths=[(W - INDENT)*0.72, (W - INDENT)*0.28]
    )
    job_header2.setStyle(tbl_style)
    story.append(job_header2)
    story.append(Indenter(left=-INDENT))
    story.append(Paragraph(
        "Led a 20+ engineer team building <b>Douyin Mall</b>'s core recommendation and product growth systems from 0\u21921, "
        "defining the foundation for personalized e-commerce and contributing to its growth into "
        "<b>China's Top 3 largest e-commerce platform</b> by GMV. "
        "Owned end-to-end recommendation architecture supporting ~170M daily active users "
        "across products, short videos, and livestreams, spanning retrieval, ranking, and cold-start systems.",
        style_body_small
    ))

    story.append(Paragraph("Homepage Feed Recommendation", style_exp_label))
    story.append(Paragraph("Built and scaled the full-stack recommendation pipeline for Douyin Mall's homepage feed:", style_body_small))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Deep Retrieval</b> \u2014 Beyond-dual-tower retrieval with cross-tower feature interaction, multi-objective cascade for full-pipeline consistency with advanced loss optimization, and advanced i2i modeling.", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Large Ranking Model</b> \u2014 Pioneered Large Ranking Model with parameter scaling up across sparse and dense components, long-sequence-to-graph modeling, and scaling laws exploration.", style_bullet))

    story.append(Paragraph("Product Cold-Start System", style_exp_label))
    story.append(Paragraph("Led the design of a dedicated cold-start system to bootstrap new products at scale:", style_body_small))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Traffic Strategy</b> \u2014 Built a lane-separated serving architecture decoupled from the main traffic flow, enabling controlled exploration of new products; developed uplift modeling for personalized traffic allocation, balancing exploration efficiency and conversion impact.", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Efficiency Optimization</b> \u2014 Enhanced cold-start ranking with multi-modal representations, similar-product knowledge transfer, and cold-start-aware training strategies under sparse feedback.", style_bullet))
    # story.append(Paragraph(u"<bullet>\u2022</bullet><b>Impact</b> \u2014 Monthly transacting products +199% (6.4M \u2192 19M); new-product 0\u21921 sales +625%.", style_bullet))

    # --- Alibaba ---
    story.append(PageBreak())
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
        "Pioneered <b>EdgeRec</b> - the industry's first on-device AI recommender systems in a billion-scale commerce feed for Mobile Taobao. "
        "Invented the <b>Generator-Evaluator</b> two-stage re-ranking framework (GRN, GE), now the standard paradigm for listwise re-ranking. "
        "Created Alibaba's Edge-X-Platform (Edge-Cloud MLOps), powering 10+ business lines across Alibaba.",
        style_body_small
    ))

    # === Selected Publications ===
    story.append(Paragraph("SELECTED PUBLICATIONS", style_section))
    story.append(Paragraph('Total citations: 1,690  |  h-index: 16', style_body_small))

    # Helper: render one-line publication
    MUTED = TEXT_MUTED.hexval()
    def add_pub(title, venue, role=None):
        meta = f'<font color="#{MUTED[2:]}">, {venue}</font>'
        if role:
            meta += f'<font color="#{MUTED[2:]}">  |  {role}</font>'
        story.append(Paragraph(f"<b>{title}</b>{meta}", style_pub_oneline))

    # --- LLM Agents ---
    story.append(Paragraph("LLM Agents", style_pub_group))
    add_pub("On Information Self-Locking in RL for Active Reasoning of LLM Agents", "Submitted to ICML 2026", "Project Lead")
    add_pub("Reducing Belief Deviation in RL for Active Reasoning of LLM Agents", "ICLR 2026 | Oral", "Project Lead")
    add_pub("MemRerank: Preference Memory for Personalized Product Reranking", "arXiv 2026", "Project Lead")

    # --- Benchmarks ---
    story.append(Paragraph("Benchmarks", style_pub_group))
    add_pub("APeB: Benchmarking Personalization Ability of Large Language Model Agents", "Submitted to ICML 2026", "Project Lead")
    add_pub("ShoppingComp: Are LLMs Really Ready for Your Shopping Cart?", "Submitted to ICML 2026", "Joint Research")

    # --- Recommender Systems ---
    story.append(Paragraph("Recommender Systems", style_pub_group))
    add_pub("EdgeRec: Recommender System on Edge in Mobile Taobao", "CIKM 2020", "First Author")
    add_pub("Personalized Adaptive Meta Learning for Cold-start User Preference Prediction", "AAAI 2021", "Project Lead")
    add_pub("Exact-k Recommendation via Maximal Clique Optimization", "SIGKDD 2019", "First Author")
    add_pub("GRN: Generative Rerank Network for Context-wise Recommendation", "arXiv 2021", "Project Lead")
    add_pub("Revisit Recommender System in the Permutation Prospective", "arXiv 2021", "Project Lead")
    add_pub("Query-based Interactive Recommendation by Meta-path and Adapted Attention-GRU", "CIKM 2019", "Co-First Author")
    add_pub("Gift: Graph-guided Feature Transfer for Cold-start Video Click-through Rate Prediction", "CIKM 2022")

    # --- Information Retrieval & Search ---
    story.append(Paragraph("Information Retrieval &amp; Search", style_pub_group))
    add_pub("IRGAN: A Minimax Game for Unifying Generative and Discriminative IR Models", "SIGIR 2017", "Best Paper Honorable Mention | First Industry Author")
    add_pub("Conceptualize and Infer User Needs in E-commerce", "CIKM 2019")
    add_pub("Query Tracking for E-commerce Conversational Search", "CIKM 2018")
    add_pub("A Minimax Game for Instance Based Selective Transfer Learning", "SIGKDD 2019")

    # --- NLP & Text Generation ---
    story.append(Paragraph("NLP &amp; Text Generation", style_pub_group))
    add_pub("Deep Cascade Multi-task Learning for Slot Filling in Online Shopping Assistant", "AAAI 2019", "First Author")
    add_pub("Multi-Modal GAN for Short Product Title Generation in Mobile E-Commerce", "NAACL 2019")
    add_pub("Automatic Generation of Chinese Short Product Titles for Mobile Display", "AAAI 2019", "First Author")
    add_pub("Representing Verbs as Argument Concepts", "AAAI 2016", "First Author")

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
    print("Resume generated: Tim_Yu_Resume.pdf")

build_resume()
