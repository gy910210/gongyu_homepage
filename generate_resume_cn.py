from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, Indenter, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# Register Chinese fonts (Songti SC on macOS)
FONT_REG = 'SongtiSC'
FONT_BOLD = 'SongtiSC-Bold'
pdfmetrics.registerFont(TTFont(FONT_REG, '/System/Library/Fonts/Supplemental/Songti.ttc', subfontIndex=6))
pdfmetrics.registerFont(TTFont(FONT_BOLD, '/System/Library/Fonts/Supplemental/Songti.ttc', subfontIndex=1))
registerFontFamily(FONT_REG, normal=FONT_REG, bold=FONT_BOLD, italic=FONT_REG, boldItalic=FONT_BOLD)

# Colors
ACCENT = HexColor('#2563eb')
TEXT_PRIMARY = HexColor('#1a1a2e')
TEXT_SECONDARY = HexColor('#444444')
TEXT_MUTED = HexColor('#777777')

# Styles
style_name = ParagraphStyle('Name', fontName=FONT_BOLD, fontSize=20, textColor=TEXT_PRIMARY, spaceAfter=2, leading=24)
style_tagline = ParagraphStyle('Tagline', fontName=FONT_REG, fontSize=10, textColor=TEXT_MUTED, spaceAfter=2)
style_contact = ParagraphStyle('Contact', fontName=FONT_REG, fontSize=9, textColor=ACCENT, spaceAfter=6)
style_section = ParagraphStyle('Section', fontName=FONT_BOLD, fontSize=11, textColor=ACCENT, spaceBefore=10, spaceAfter=4)
style_subsection = ParagraphStyle('Subsection', fontName=FONT_BOLD, fontSize=9.5, textColor=TEXT_PRIMARY, spaceBefore=2, spaceAfter=0)
style_body = ParagraphStyle('Body', fontName=FONT_REG, fontSize=9, textColor=TEXT_SECONDARY, leading=14, spaceAfter=2)
INDENT = 12
style_body_small = ParagraphStyle('BodySmall', fontName=FONT_REG, fontSize=8.5, textColor=TEXT_SECONDARY, leading=13, spaceAfter=2, leftIndent=INDENT)
style_bullet = ParagraphStyle('Bullet', fontName=FONT_REG, fontSize=8.5, textColor=TEXT_SECONDARY, leading=13, leftIndent=INDENT+14, spaceAfter=1, bulletIndent=INDENT)
style_job_title = ParagraphStyle('JobTitle', fontName=FONT_BOLD, fontSize=10, textColor=TEXT_PRIMARY, spaceAfter=0)
style_job_period = ParagraphStyle('JobPeriod', fontName=FONT_REG, fontSize=9, textColor=TEXT_MUTED, alignment=TA_RIGHT)
style_exp_label = ParagraphStyle('ExpLabel', fontName=FONT_BOLD, fontSize=9, textColor=TEXT_PRIMARY, spaceBefore=4, spaceAfter=1, leftIndent=INDENT)
style_pub_group = ParagraphStyle('PubGroup', fontName=FONT_REG, fontSize=9, textColor=TEXT_SECONDARY, spaceBefore=6, spaceAfter=2, leftIndent=INDENT)
style_pub_oneline = ParagraphStyle('PubOneline', fontName=FONT_REG, fontSize=8, textColor=TEXT_SECONDARY, leading=11, spaceAfter=2, leftIndent=INDENT)
style_edu_desc = ParagraphStyle('EduDesc', fontName=FONT_REG, fontSize=8.5, textColor=TEXT_SECONDARY, leading=13, spaceAfter=1, leftIndent=INDENT)

def build_resume():
    doc = SimpleDocTemplate(
        "/Users/bytedance/Documents/claude/yu-gong-homepage/Yu_Gong_Resume_CN.pdf",
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
    story.append(Paragraph("龚禹 (Yu Gong)", style_name))
    story.append(Paragraph("TikTok 工程总监  |  AI 搜索  |  大模型 Agent  |  推荐系统", style_tagline))
    story.append(Paragraph(
        '<font color="#444444">gy910210@gmail.com  |  425-221-8131</font>  |  '
        '<a href="https://gongyu.vercel.app/">个人主页</a>  |  '
        '<a href="https://scholar.google.com/citations?user=QseahYcAAAAJ">Google Scholar</a>  |  '
        '<a href="https://www.linkedin.com/in/gongyu210/">LinkedIn</a>  |  '
        '<a href="https://x.com/gy910210">X / Twitter</a>',
        style_contact
    ))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=6))

    # === About ===
    story.append(Paragraph("关于", style_section))
    story.append(Paragraph(
        "TikTok 工程总监，带领 40+ 人团队构建面向全球电商的 <b>AI 搜索</b> 与 <b>购物 Agent</b>。"
        "在大规模搜索与推荐系统领域拥有 9+ 年经验，此前曾就职于字节跳动和阿里巴巴。"
        "我的工作覆盖搜索、推荐与 Agent 系统。我正在推动构建 <b>AI-native 购物决策系统</b> "
        "—— 将召回、排序与多步推理、自主决策统一到一起。",
        style_body
    ))
    story.append(Paragraph(
        "研究兴趣：基于大模型的搜索、大模型 Agent（Harness Engineering、记忆与个性化、后训练、Agentic-RL、评测）、以及推荐系统。"
        "获得 <b>SIGIR 2017 最佳论文荣誉提名奖</b>（IRGAN，800+ 引用）。",
        style_body
    ))

    # === Experience ===
    story.append(Paragraph("工作经历", style_section))

    # --- TikTok ---
    story.append(Indenter(left=INDENT))
    job_header = Table(
        [[Paragraph("<b>Director of Engineering</b>  |  TikTok", style_job_title),
          Paragraph("2024 - 至今", style_job_period)]],
        colWidths=[(W - INDENT)*0.72, (W - INDENT)*0.28]
    )
    job_header.setStyle(tbl_style)
    story.append(job_header)
    story.append(Indenter(left=-INDENT))
    story.append(Paragraph(
        "带领 40+ 人工程团队，负责 TikTok 全球电商（美国、欧洲、东南亚等多个地区）的 AI 搜索与购物 Agent 系统，"
        "推动搜索系统端到端的产品与技术路线规划，仅美国地区每日服务约 1.4 亿电商查询。",
        style_body_small
    ))

    story.append(Paragraph("LLM-powered Search", style_exp_label))
    story.append(Paragraph("主导搜索系统向基于大模型的召回与排序演进：", style_body_small))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>查询规划 (Query Planning)</b> \u2014 基于大模型的多 Agent 框架（Analyzer-Identifier-Rewriter-Judger），将模糊查询解析为潜在的商品意图。", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>生成式召回 (Generative Retrieval)</b> \u2014 面向商品召回的 decode-only 生成式模型。", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>大搜索模型 (Large Search Model)</b> \u2014 基于 Transformer 的搜索模型，在召回与排序上进行参数规模与行为序列规模的扩展。", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>多模态 (Multi-Modality)</b> \u2014 面向召回与排序的多模态表征融合与联合训练。", style_bullet))

    story.append(Paragraph("Shopping Agent", style_exp_label))
    story.append(Paragraph("从 0 到 1 构建并上线 TikTok 购物 Agent：", style_body_small))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>Agent 框架</b> \u2014 Planner-Executor-Verifier 架构（Harness），支持多轮上下文管理与异构工具调用（网页 / 商品 / 视频搜索）。", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>记忆与个性化</b> \u2014 Memory-as-Tool 设计：基于长期用户行为信号提炼分层记忆（session \u2192 summary \u2192 profile），由解耦的 MemAgent 进行 query 感知的检索与证据驱动的信息抽取，用于个性化决策。", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>后训练 (Post-Training)</b> \u2014 基于合成多轮数据的拒绝采样 SFT 用于模型冷启动；采用 Rubric Reward 与 Deep Search Reward 的强化学习微调。以及大模型 Agent 主动推理方向的研究（T3、AREW）。", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>评测与基准</b> \u2014 构建 ShoppingBench（深度商品搜索）、APeB（个性化 Agent 行为）以及基于 rubric 的报告评测。", style_bullet))

    # --- ByteDance ---
    story.append(Spacer(1, 4))
    story.append(Indenter(left=INDENT))
    job_header2 = Table(
        [[Paragraph("<b>Senior Engineering Manager / Tech Lead</b>  |  字节跳动", style_job_title),
          Paragraph("2021 - 2024", style_job_period)]],
        colWidths=[(W - INDENT)*0.72, (W - INDENT)*0.28]
    )
    job_header2.setStyle(tbl_style)
    story.append(job_header2)
    story.append(Indenter(left=-INDENT))
    story.append(Paragraph(
        "带领 20+ 人工程团队，从 0 到 1 构建 <b>抖音商城</b> 的核心推荐与商品增长系统，"
        "奠定了个性化电商的基础，助力其成长为 <b>中国 GMV Top 3 的电商平台</b>。"
        "负责端到端推荐架构，日均服务约 1.7 亿活跃用户，覆盖商品、短视频、直播等场景，涵盖召回、排序与冷启动系统。",
        style_body_small
    ))

    story.append(Paragraph("Homepage Feed Recommendation", style_exp_label))
    story.append(Paragraph("构建并扩展抖音商城首页 feed 全链路推荐系统：", style_body_small))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>深度召回 (Deep Retrieval)</b> \u2014 超越双塔的召回（引入塔间特征交叉）、面向全链路一致性的多目标级联并结合 loss 优化，以及高阶 i2i 建模。", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>大排序模型 (Large Ranking Model)</b> \u2014 首创大排序模型，在稀疏与稠密侧同时进行参数规模扩展、长序列到图的建模，以及 scaling law 探索。", style_bullet))

    story.append(Paragraph("Product Cold-Start System", style_exp_label))
    story.append(Paragraph("主导设计面向新品大规模冷启动的专项系统：", style_body_small))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>流量策略</b> \u2014 构建与主流量解耦的分道（lane）服务架构，实现对新品的可控探索；研发 Uplift 建模进行个性化流量分配，平衡探索效率与转化收益。", style_bullet))
    story.append(Paragraph(u"<bullet>\u2022</bullet><b>效率优化</b> \u2014 通过多模态表征、相似商品知识迁移，以及稀疏反馈下的冷启感知训练策略，提升冷启动排序效果。", style_bullet))

    # --- Alibaba ---
    story.append(Spacer(1, 4))
    story.append(Indenter(left=INDENT))
    job_header3 = Table(
        [[Paragraph("<b>Tech Lead</b>  |  阿里巴巴集团", style_job_title),
          Paragraph("2017 - 2021", style_job_period)]],
        colWidths=[(W - INDENT)*0.72, (W - INDENT)*0.28]
    )
    job_header3.setStyle(tbl_style)
    story.append(job_header3)
    story.append(Indenter(left=-INDENT))
    story.append(Paragraph(
        "首创 <b>EdgeRec</b> —— 业界首个在十亿级电商 feed（手机淘宝）上落地的端上 AI 推荐系统。"
        "发明 <b>Generator-Evaluator</b> 两阶段重排框架（GRN、GE），现为 listwise 重排的标准范式。"
        "打造阿里巴巴端云协同 MLOps 平台 Edge-X-Platform，赋能集团 10+ 业务线。",
        style_body_small
    ))

    # === Selected Publications ===
    story.append(Paragraph("精选论文", style_section))
    story.append(Paragraph('总引用数：1,690  |  h-index：16  |  完整列表见 <a href="https://scholar.google.com/citations?user=QseahYcAAAAJ">Google Scholar</a>', style_body_small))

    # Helper: render one-line publication
    MUTED = TEXT_MUTED.hexval()
    def add_pub(title, venue, role=None):
        meta = f'<font color="#{MUTED[2:]}">, {venue}</font>'
        if role:
            meta += f'<font color="#{MUTED[2:]}">  |  {role}</font>'
        story.append(Paragraph(f"<b>{title}</b>{meta}", style_pub_oneline))

    # --- LLM Agents ---
    story.append(Paragraph("LLM Agents", style_pub_group))
    add_pub("On Information Self-Locking in RL for Active Reasoning of LLM Agents", "Submitted to ICML 2026", "项目负责人")
    add_pub("Reducing Belief Deviation in RL for Active Reasoning of LLM Agents", "ICLR 2026 | Oral", "项目负责人")
    add_pub("MemRerank: Preference Memory for Personalized Product Reranking", "arXiv 2026", "项目负责人")

    # --- Benchmarks ---
    story.append(Paragraph("Benchmarks", style_pub_group))
    add_pub("APeB: Benchmarking Personalization Ability of Large Language Model Agents", "Submitted to ICML 2026", "项目负责人")
    add_pub("ShoppingComp: Are LLMs Really Ready for Your Shopping Cart?", "Submitted to ICML 2026", "合作研究")

    # --- Recommender Systems ---
    story.append(Paragraph("Recommender Systems", style_pub_group))
    add_pub("EdgeRec: Recommender System on Edge in Mobile Taobao", "CIKM 2020", "第一作者")
    add_pub("Personalized Adaptive Meta Learning for Cold-start User Preference Prediction", "AAAI 2021", "项目负责人")
    add_pub("Exact-k Recommendation via Maximal Clique Optimization", "SIGKDD 2019", "第一作者")
    add_pub("GRN: Generative Rerank Network for Context-wise Recommendation", "arXiv 2021", "项目负责人")
    add_pub("Revisit Recommender System in the Permutation Prospective", "arXiv 2021", "项目负责人")
    add_pub("Query-based Interactive Recommendation by Meta-path and Adapted Attention-GRU", "CIKM 2019", "共同第一作者")
    add_pub("Gift: Graph-guided Feature Transfer for Cold-start Video Click-through Rate Prediction", "CIKM 2022")

    # --- Information Retrieval & Search ---
    story.append(Paragraph("Information Retrieval &amp; Search", style_pub_group))
    add_pub("IRGAN: A Minimax Game for Unifying Generative and Discriminative IR Models", "SIGIR 2017", "最佳论文荣誉提名 | 首位工业界作者")
    add_pub("Conceptualize and Infer User Needs in E-commerce", "CIKM 2019")
    add_pub("Query Tracking for E-commerce Conversational Search", "CIKM 2018")
    add_pub("A Minimax Game for Instance Based Selective Transfer Learning", "SIGKDD 2019")

    # --- NLP & Text Generation ---
    story.append(Paragraph("NLP &amp; Text Generation", style_pub_group))
    add_pub("Deep Cascade Multi-task Learning for Slot Filling in Online Shopping Assistant", "AAAI 2019", "第一作者")
    add_pub("Multi-Modal GAN for Short Product Title Generation in Mobile E-Commerce", "NAACL 2019")
    add_pub("Automatic Generation of Chinese Short Product Titles for Mobile Display", "AAAI 2019", "第一作者")
    add_pub("Representing Verbs as Argument Concepts", "AAAI 2016", "第一作者")

    # === Education ===
    story.append(Paragraph("教育背景", style_section))

    story.append(Indenter(left=INDENT))
    edu1 = Table(
        [[Paragraph("<b>计算机科学与技术硕士</b>  |  上海交通大学", style_subsection),
          Paragraph("2014 - 2017", style_job_period)]],
        colWidths=[(W - INDENT)*0.72, (W - INDENT)*0.28]
    )
    edu1.setStyle(tbl_style)
    story.append(edu1)
    story.append(Indenter(left=-INDENT))
    story.append(Paragraph("ADAPT 实验室研究助理。研究方向：信息检索、自然语言处理、机器学习。", style_edu_desc))

    story.append(Spacer(1, 3))
    story.append(Indenter(left=INDENT))
    edu2 = Table(
        [[Paragraph("<b>计算机软件工程学士</b>  |  西安交通大学", style_subsection),
          Paragraph("2010 - 2014", style_job_period)]],
        colWidths=[(W - INDENT)*0.72, (W - INDENT)*0.28]
    )
    edu2.setStyle(tbl_style)
    story.append(edu2)
    story.append(Indenter(left=-INDENT))
    story.append(Paragraph("获 Google 优秀学生奖学金（全国每年授予 100 名学生）。", style_edu_desc))

    # === Honors & Awards ===
    story.append(Paragraph("荣誉与奖项", style_section))
    story.append(Paragraph("ACM SIGIR 2017 最佳论文荣誉提名奖", style_body_small))
    story.append(Paragraph("Google 优秀学生奖学金 —— 全国每年授予 100 名学生（2013）", style_body_small))

    doc.build(story)
    print("Resume generated: Yu_Gong_Resume_CN.pdf")

build_resume()
