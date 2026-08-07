#!/usr/bin/env python3
"""ATS-friendly Turing Delivery Data Analyst resume for Ananya Rai Paul."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os

OUT = os.path.join(os.path.dirname(__file__), "Ananya_Rai_Paul_Resume_Turing.pdf")
INK = HexColor("#111111")
MUTED = HexColor("#333333")


def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=16, leading=19, textColor=INK, alignment=TA_CENTER, spaceAfter=3))
    s.add(ParagraphStyle(name="Contact", fontName="Helvetica", fontSize=9, leading=11, textColor=MUTED, alignment=TA_CENTER, spaceAfter=8))
    s.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=10, leading=12, textColor=INK, spaceBefore=8, spaceAfter=2))
    s.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=9.5, leading=12, textColor=INK, spaceAfter=3))
    s.add(ParagraphStyle(name="RoleTitle", fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=INK, spaceBefore=3, spaceAfter=0))
    s.add(ParagraphStyle(name="OrgMeta", fontName="Helvetica", fontSize=9, leading=11, textColor=MUTED, spaceAfter=2))
    s.add(ParagraphStyle(name="ResumeBullet", fontName="Helvetica", fontSize=9.5, leading=12, textColor=INK, leftIndent=10, spaceAfter=1.5))
    s.add(ParagraphStyle(name="Line", fontName="Helvetica", fontSize=9.5, leading=12, textColor=INK, spaceAfter=1.5))
    return s


def rule():
    return HRFlowable(width="100%", thickness=0.8, color=HexColor("#999999"), spaceBefore=0, spaceAfter=4)


def bullet(text, st):
    return Paragraph(f"• {text}", st["ResumeBullet"])


def build():
    st = styles()
    doc = SimpleDocTemplate(
        OUT,
        pagesize=letter,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
        topMargin=0.45 * inch,
        bottomMargin=0.45 * inch,
        title="Ananya Rai Paul — Resume",
        author="Ananya Rai Paul",
    )
    story = []

    story.append(Paragraph("ANANYA RAI PAUL", st["Name"]))
    story.append(
        Paragraph(
            "anannyaraipaul@gmail.com | linkedin.com/in/annyarp",
            st["Contact"],
        )
    )

    story.append(Paragraph("PROFESSIONAL SUMMARY", st["Section"]))
    story.append(rule())
    story.append(
        Paragraph(
            "B.Sc. Statistics (Honours) graduate and fresher seeking a Delivery Data Analyst role. "
            "Strong critical thinking, problem-solving, and English communication skills, with hands-on "
            "experience cleaning data, writing SQL, building analyses, and documenting clear technical "
            "explanations. Working knowledge of Python for data tasks. Comfortable evaluating outputs, "
            "comparing options with detailed rationales, and collaborating remotely in a full-time setup.",
            st["Body"],
        )
    )

    story.append(Paragraph("TECHNICAL SKILLS", st["Section"]))
    story.append(rule())
    for line in [
        "<b>Programming:</b> Python (beginner / working knowledge — scripting, data cleaning, basic analysis)",
        "<b>Query &amp; Data Handling:</b> SQL (joins, aggregations, filtering, grouping), data cleaning, data validation",
        "<b>Analysis &amp; Visualization:</b> Microsoft Excel (Pivot Tables, VLOOKUP, charts), Power BI (dashboards, data modeling)",
        "<b>Statistical Reasoning:</b> Hypothesis testing, probability, regression, exploratory data analysis",
        "<b>Core Strengths:</b> Critical thinking, problem-solving, technical writing/explanations, attention to detail, peer collaboration",
    ]:
        story.append(Paragraph(f"• {line}", st["Line"]))

    story.append(Paragraph("PROJECTS", st["Section"]))
    story.append(rule())

    story.append(Paragraph("Airline Delay Pattern Analysis — SQL, Excel, Power BI", st["RoleTitle"]))
    for b in [
        "Wrote SQL queries to extract and evaluate flight delay data across routes, airports, and time periods",
        "Compared delay patterns, ranked high-impact bottlenecks, and documented clear rationales for findings",
        "Built a dashboard and written summary explaining trends to support data-driven decisions",
    ]:
        story.append(bullet(b, st))

    story.append(Paragraph("Revenue &amp; Product Performance Analysis — SQL, Power BI", st["RoleTitle"]))
    for b in [
        "Queried and joined 2,000+ multi-region sales records using SQL to evaluate revenue and product performance",
        "Ranked top-performing categories and regional gaps, with structured explanations of the prioritization logic",
        "Delivered stakeholder-ready KPIs and a concise written analysis of recommended focus areas",
    ]:
        story.append(bullet(b, st))

    story.append(Paragraph("Retail Transaction &amp; Seasonal Trend Analysis — Microsoft Excel", st["RoleTitle"]))
    for b in [
        "Cleaned and analyzed 500,000+ retail transaction records; validated data quality before analysis",
        "Used exploratory data analysis to uncover seasonal spikes and recurring customer patterns",
        "Documented insights in clear written form to support campaign timing and decision-making",
    ]:
        story.append(bullet(b, st))

    story.append(Paragraph("Interactive Sales Performance Dashboard — Power BI", st["RoleTitle"]))
    story.append(
        bullet(
            "Designed multi-view dashboards with data modeling and DAX measures; structured outputs for quick review "
            "and reduced manual reporting effort",
            st,
        )
    )

    story.append(Paragraph("EXPERIENCE", st["Section"]))
    story.append(rule())
    story.append(Paragraph("Guide, Translator &amp; Operations Coordinator", st["RoleTitle"]))
    story.append(
        Paragraph(
            "Neora Valley Jungle Camp, Kolakham, Kalimpong | 1 Year",
            st["OrgMeta"],
        )
    )
    for b in [
        "Communicated clearly with international guests; explained options and decisions with professionalism",
        "Solved day-to-day problems under pressure, documented plans, and coordinated logistics end to end",
    ]:
        story.append(bullet(b, st))

    story.append(Paragraph("EDUCATION", st["Section"]))
    story.append(rule())
    story.append(
        Paragraph(
            "<b>University of North Bengal</b> — B.Sc. Statistics (Honours)",
            st["Line"],
        )
    )
    story.append(
        Paragraph(
            "Coursework emphasis: statistical reasoning, probability, regression, and analytical problem-solving",
            st["Line"],
        )
    )

    story.append(Paragraph("CERTIFICATIONS &amp; LEARNING", st["Section"]))
    story.append(rule())
    story.append(Paragraph("• IBM – Introduction to Data Analytics", st["Line"]))
    story.append(Paragraph("• Google – Fundamentals of Digital Marketing", st["Line"]))
    story.append(
        Paragraph(
            "• Building Python working knowledge for data analysis and scripting (ongoing)",
            st["Line"],
        )
    )

    doc.build(story)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
