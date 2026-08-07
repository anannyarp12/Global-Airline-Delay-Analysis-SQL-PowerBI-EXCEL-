#!/usr/bin/env python3
"""TCS entry-level / NextStep ATS-friendly resume for Ananya Rai Paul."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
import os

OUT = os.path.join(os.path.dirname(__file__), "Ananya_Rai_Paul_Resume_TCS.pdf")
INK = HexColor("#111111")
MUTED = HexColor("#333333")


def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(name="Name", fontName="Helvetica-Bold", fontSize=15, leading=18, textColor=INK, alignment=TA_CENTER, spaceAfter=2))
    s.add(ParagraphStyle(name="Contact", fontName="Helvetica", fontSize=9, leading=11, textColor=MUTED, alignment=TA_CENTER, spaceAfter=7))
    s.add(ParagraphStyle(name="Section", fontName="Helvetica-Bold", fontSize=10, leading=12, textColor=INK, spaceBefore=7, spaceAfter=2))
    s.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=9.5, leading=12, textColor=INK, spaceAfter=2))
    s.add(ParagraphStyle(name="RoleTitle", fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=INK, spaceBefore=2, spaceAfter=0))
    s.add(ParagraphStyle(name="OrgMeta", fontName="Helvetica", fontSize=9, leading=11, textColor=MUTED, spaceAfter=1))
    s.add(ParagraphStyle(name="ResumeBullet", fontName="Helvetica", fontSize=9.2, leading=11.5, textColor=INK, leftIndent=10, spaceAfter=1.2))
    s.add(ParagraphStyle(name="Line", fontName="Helvetica", fontSize=9.2, leading=11.5, textColor=INK, spaceAfter=1.2))
    return s


def rule():
    return HRFlowable(width="100%", thickness=0.7, color=HexColor("#888888"), spaceBefore=0, spaceAfter=3)


def bullet(text, st):
    return Paragraph(f"• {text}", st["ResumeBullet"])


def build():
    st = styles()
    doc = SimpleDocTemplate(
        OUT,
        pagesize=letter,
        leftMargin=0.58 * inch,
        rightMargin=0.58 * inch,
        topMargin=0.4 * inch,
        bottomMargin=0.4 * inch,
        title="Ananya Rai Paul — Resume",
        author="Ananya Rai Paul",
    )
    story = []

    story.append(Paragraph("ANANYA RAI PAUL", st["Name"]))
    story.append(
        Paragraph(
            "anannyaraipaul@gmail.com | +91 9933491546 | linkedin.com/in/annyarp | github.com/anannyarp12",
            st["Contact"],
        )
    )

    story.append(Paragraph("CAREER OBJECTIVE", st["Section"]))
    story.append(rule())
    story.append(
        Paragraph(
            "B.Sc. Statistics (Honours) fresher seeking an entry-level role at TCS. Skilled in SQL, "
            "Python (working knowledge), Excel, and Power BI, with strong statistical foundations, "
            "problem-solving ability, and clear English communication. Eager to contribute to data "
            "analysis, reporting, and technology-driven business solutions while learning in a "
            "structured corporate environment.",
            st["Body"],
        )
    )

    story.append(Paragraph("EDUCATION", st["Section"]))
    story.append(rule())
    story.append(
        Paragraph(
            "<b>B.Sc. Statistics (Honours)</b> — University of North Bengal (Siliguri College) | CGPA: <b>7.70 / 10</b>",
            st["Line"],
        )
    )
    story.append(
        Paragraph(
            "Coursework: Probability, Regression, Hypothesis Testing, Multivariate Analysis, Time Series, "
            "Design of Experiments, Statistical Quality Control, Exploratory Data Analysis",
            st["Line"],
        )
    )
    story.append(
        Paragraph(
            "<b>ISC Class XII</b> (2021) — English, Nepali, Mathematics, Physics, Chemistry | Percentage: <b>74%</b>",
            st["Line"],
        )
    )

    story.append(Paragraph("TECHNICAL SKILLS", st["Section"]))
    story.append(rule())
    for line in [
        "<b>Programming:</b> Python (working knowledge — scripting, data cleaning, basic analysis)",
        "<b>Database / Query:</b> SQL (Joins, Aggregations, Filtering, Grouping), DBMS concepts, data validation",
        "<b>Tools:</b> Microsoft Excel (Pivot Tables, VLOOKUP, Charts), Power BI (Dashboards, Data Modeling, DAX Basics)",
        "<b>Concepts:</b> Statistics, Data Cleaning, Data Wrangling, Exploratory Data Analysis, Reporting, Problem Solving",
        "<b>Soft Skills:</b> Communication, Documentation, Team Collaboration, Attention to Detail, Analytical Thinking",
    ]:
        story.append(Paragraph(f"• {line}", st["Line"]))

    story.append(Paragraph("ACADEMIC PROJECTS", st["Section"]))
    story.append(rule())

    story.append(Paragraph("Airline Delay Pattern Analysis | SQL, Excel, Power BI", st["RoleTitle"]))
    for b in [
        "Acquired and cleaned flight delay data; wrote SQL queries across routes, airports, and time periods",
        "Performed data wrangling and analysis to rank high-impact delay bottlenecks with clear rationales",
        "Built Power BI dashboard and written report to support data-driven operational decisions",
    ]:
        story.append(bullet(b, st))

    story.append(Paragraph("Revenue and Product Performance Analysis | SQL, Power BI", st["RoleTitle"]))
    for b in [
        "Queried and joined 2,000+ multi-region sales records using SQL to evaluate revenue performance",
        "Identified top product categories and regional gaps; prepared KPI dashboards for stakeholders",
        "Documented analysis and recommendations for prioritization and business reporting",
    ]:
        story.append(bullet(b, st))

    story.append(Paragraph("Retail Transaction and Seasonal Trend Analysis | Microsoft Excel", st["RoleTitle"]))
    for b in [
        "Cleaned and analyzed 5 lakh+ retail transaction records using Pivot Tables and charts",
        "Applied exploratory data analysis to uncover seasonal trends and customer purchase patterns",
        "Delivered clear insights for demand timing and reporting use cases",
    ]:
        story.append(bullet(b, st))

    story.append(Paragraph("Interactive Sales Performance Dashboard | Power BI", st["RoleTitle"]))
    story.append(
        bullet(
            "Designed multi-view Power BI dashboards with data modeling and DAX measures for faster KPI reporting",
            st,
        )
    )

    story.append(Paragraph("WORK EXPERIENCE", st["Section"]))
    story.append(rule())
    story.append(Paragraph("Guide, Translator and Operations Coordinator", st["RoleTitle"]))
    story.append(Paragraph("Neora Valley Jungle Camp, Kolakham, Kalimpong | 1 Year", st["OrgMeta"]))
    for b in [
        "Handled communication with international guests and coordinated day-to-day operations under pressure",
        "Improved planning, documentation, and problem-solving skills transferable to client and team environments",
    ]:
        story.append(bullet(b, st))

    story.append(Paragraph("CERTIFICATIONS", st["Section"]))
    story.append(rule())
    story.append(Paragraph("• IBM – Introduction to Data Analytics", st["Line"]))
    story.append(Paragraph("• Google – Fundamentals of Digital Marketing", st["Line"]))

    story.append(Paragraph("ACHIEVEMENTS", st["Section"]))
    story.append(rule())
    story.append(
        Paragraph(
            "• Represented school in the men's chess competition in Class 10, building focus and strategic thinking",
            st["Line"],
        )
    )

    doc.build(story)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
