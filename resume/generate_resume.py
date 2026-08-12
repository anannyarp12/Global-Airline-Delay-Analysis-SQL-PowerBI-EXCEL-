#!/usr/bin/env python3
"""Generate Ananya Rai Paul's Automattic-tailored one-page resume PDF."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
import os

OUTPUT = os.path.join(os.path.dirname(__file__), "Ananya_Rai_Paul_Resume_Automattic.pdf")

INK = HexColor("#1a1a1a")
MUTED = HexColor("#3d3d3d")
ACCENT = HexColor("#0d4f4f")
RULE = HexColor("#c8d4d4")


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="Name",
            fontName="Helvetica-Bold",
            fontSize=19,
            leading=22,
            textColor=INK,
            alignment=TA_CENTER,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Contact",
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            textColor=MUTED,
            alignment=TA_CENTER,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Section",
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=12,
            textColor=ACCENT,
            spaceBefore=9,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            fontName="Helvetica",
            fontSize=9.5,
            leading=12.5,
            textColor=INK,
            alignment=TA_JUSTIFY,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="RoleTitle",
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=13,
            textColor=INK,
            spaceBefore=2,
            spaceAfter=0,
        )
    )
    styles.add(
        ParagraphStyle(
            name="OrgMeta",
            fontName="Helvetica-Oblique",
            fontSize=9,
            leading=12,
            textColor=MUTED,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ResumeBullet",
            fontName="Helvetica",
            fontSize=9.5,
            leading=12.5,
            textColor=INK,
            leftIndent=11,
            spaceAfter=2.5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SkillLine",
            fontName="Helvetica",
            fontSize=9.5,
            leading=12.5,
            textColor=INK,
            spaceAfter=2.5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="EduLine",
            fontName="Helvetica",
            fontSize=9.5,
            leading=12.5,
            textColor=INK,
            spaceAfter=2,
        )
    )
    return styles


def section_rule():
    return HRFlowable(
        width="100%",
        thickness=0.9,
        color=RULE,
        spaceBefore=0,
        spaceAfter=5,
    )


def bullet(text, styles):
    return Paragraph(f"• {text}", styles["ResumeBullet"])


def build():
    styles = build_styles()
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=letter,
        leftMargin=0.62 * inch,
        rightMargin=0.62 * inch,
        topMargin=0.45 * inch,
        bottomMargin=0.45 * inch,
        title="Ananya Rai Paul — Resume",
        author="Ananya Rai Paul",
    )

    story = []

    story.append(Paragraph("ANANYA RAI PAUL", styles["Name"]))
    story.append(
        Paragraph(
            "anannyaraipaul@gmail.com &nbsp;|&nbsp; linkedin.com/in/annyarp "
            "&nbsp;|&nbsp; github.com/anannyarp12<br/>"
            "Kalimpong, India (APAC) &nbsp;·&nbsp; Fully remote-ready "
            "&nbsp;·&nbsp; Flexible / irregular hours OK",
            styles["Contact"],
        )
    )

    story.append(Paragraph("PROFESSIONAL SUMMARY", styles["Section"]))
    story.append(section_rule())
    story.append(
        Paragraph(
            "Independent, behind-the-scenes operator with one year managing foreign "
            "tourists, logistics, and day-to-day coordination at a remote jungle camp. "
            "Comfortable owning the unexpected, working under pressure, and adapting to "
            "flexible hours across time zones. Self-directed — no mandated task list "
            "needed — with clear communication, calm judgment, and a drive to keep "
            "operations running so others can focus.",
            styles["Body"],
        )
    )

    story.append(Paragraph("EXPERIENCE", styles["Section"]))
    story.append(section_rule())
    story.append(
        Paragraph(
            "Guide, Translator &amp; Operations Coordinator",
            styles["RoleTitle"],
        )
    )
    story.append(
        Paragraph(
            "Neora Valley Jungle Camp — Kolakham, Kalimpong &nbsp;|&nbsp; "
            "Hotel / Resort Line &nbsp;|&nbsp; 1 Year",
            styles["OrgMeta"],
        )
    )
    for b in [
        "Trusted on-ground operator for foreign tourists: guiding, translating, and "
        "coordinating end-to-end experiences so guests and camp staff stayed focused.",
        "Organized trek logistics, village lunch arrangements, and overall camp "
        "coordination — prioritizing requests, handling last-minute changes, and "
        "keeping schedules and communications clear.",
        "Interfaced daily with international guests across cultures with professionalism "
        "and discretion; resolved issues quickly and managed competing priorities "
        "under pressure.",
        "Anticipated needs, filled operational gaps before they became problems, and "
        "improved workflows by organizing information and improvising practical "
        "solutions when plans shifted.",
        "Worked flexible and often irregular hours to support guests and operations — "
        "comfortable with rapid context-switching and varied schedules.",
    ]:
        story.append(bullet(b, styles))

    story.append(Paragraph("CORE STRENGTHS", styles["Section"]))
    story.append(section_rule())
    for line in [
        "<b>Operations &amp; logistics:</b> Priority triage, travel/activity coordination, "
        "meeting &amp; project prep, dependable follow-through",
        "<b>Stakeholder communication:</b> Professional interface with international "
        "guests and partners; cross-cultural translation and clarity",
        "<b>Judgment under pressure:</b> Calm handling of urgent issues, last-minute "
        "changes, and competing demands",
        "<b>Remote &amp; flexible work:</b> High ownership from APAC; ready to support "
        "global / West Coast–aligned collaboration on flexible hours",
        "<b>Research &amp; systems:</b> Spot inefficiencies, organize information, and "
        "prepare stakeholder-ready briefings (Statistics, SQL, Excel, Power BI)",
    ]:
        story.append(Paragraph(f"• {line}", styles["SkillLine"]))

    story.append(Paragraph("SELECTED PROJECTS", styles["Section"]))
    story.append(section_rule())
    story.append(
        Paragraph(
            "<b>Revenue &amp; Product Performance Analysis</b> — SQL, Power BI: "
            "Synthesized 2,000+ multi-region records into clear stakeholder priorities "
            "and a KPI dashboard for fast review.",
            styles["SkillLine"],
        )
    )
    story.append(
        Paragraph(
            "<b>Airline Delay Pattern Analysis</b> — SQL, Excel, Power BI: "
            "Triaged operational bottleneck patterns and turned messy data into a "
            "clear visual briefing for faster decisions.",
            styles["SkillLine"],
        )
    )
    story.append(
        Paragraph(
            "<b>Interactive Sales Dashboard</b> — Power BI: "
            "Structured views that cut manual report compilation — closing process "
            "gaps before others felt the friction.",
            styles["SkillLine"],
        )
    )

    story.append(Paragraph("TOOLS &amp; WORKING STYLE", styles["Section"]))
    story.append(section_rule())
    story.append(
        Paragraph(
            "Excel (Pivot Tables, VLOOKUP, Charts) · SQL · Power BI · strong written / "
            "async communication · attention to detail · candor · reliable follow-through",
            styles["Body"],
        )
    )

    story.append(Paragraph("EDUCATION &amp; CERTIFICATIONS", styles["Section"]))
    story.append(section_rule())
    story.append(
        Paragraph(
            "<b>University of North Bengal</b> — B.Sc. Statistics (Honours)",
            styles["EduLine"],
        )
    )
    story.append(
        Paragraph(
            "IBM – Introduction to Data Analytics &nbsp;·&nbsp; "
            "Google – Fundamentals of Digital Marketing",
            styles["EduLine"],
        )
    )

    doc.build(story)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    build()
