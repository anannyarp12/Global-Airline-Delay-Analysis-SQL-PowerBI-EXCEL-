#!/usr/bin/env python3
"""Generate a short Automattic-tailored cover letter for Ananya Rai Paul."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
import os

OUT_DIR = os.path.dirname(__file__)
PDF_PATH = os.path.join(OUT_DIR, "Ananya_Rai_Paul_Cover_Letter_Automattic.pdf")

INK = HexColor("#1a1a1a")
MUTED = HexColor("#555555")
ACCENT = HexColor("#0d4f4f")


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="Name",
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=17,
            textColor=INK,
            alignment=TA_LEFT,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Contact",
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            textColor=MUTED,
            alignment=TA_LEFT,
            spaceAfter=14,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Meta",
            fontName="Helvetica",
            fontSize=9.5,
            leading=12,
            textColor=INK,
            alignment=TA_LEFT,
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="LetterBody",
            fontName="Helvetica",
            fontSize=10.5,
            leading=15,
            textColor=INK,
            alignment=TA_LEFT,
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SignOff",
            fontName="Helvetica",
            fontSize=10.5,
            leading=14,
            textColor=INK,
            alignment=TA_LEFT,
            spaceBefore=4,
            spaceAfter=2,
        )
    )
    return styles


def build():
    styles = build_styles()
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=0.85 * inch,
        rightMargin=0.85 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
        title="Cover Letter — Ananya Rai Paul",
        author="Ananya Rai Paul",
    )

    story = []
    story.append(Paragraph("Ananya Rai Paul", styles["Name"]))
    story.append(
        Paragraph(
            "+91 9933491546 &nbsp;·&nbsp; anannyaraipaul@gmail.com &nbsp;·&nbsp; "
            "Kalimpong, India (APAC) &nbsp;·&nbsp; Remote-ready",
            styles["Contact"],
        )
    )
    story.append(
        Paragraph(
            "Hiring Team<br/>Automattic",
            styles["Meta"],
        )
    )
    story.append(Paragraph("Dear Hiring Team,", styles["LetterBody"]))

    paragraphs = [
        "I’m writing to apply for the assistant role supporting Matt and the Wranglers "
        "team. I’m drawn to Automattic’s remote-first, high-trust way of working — "
        "independent people who create net positive impact without a rigid task list — "
        "and I’m ready to work flexibly across time zones from APAC.",
        "For one year at Neora Valley Jungle Camp in Kolakham, Kalimpong, I worked as a "
        "guide, translator, and on-ground coordinator for foreign tourists. That meant "
        "organizing treks and village lunches, managing last-minute changes, and keeping "
        "communications clear under pressure so guests and the team could focus. I learned "
        "to anticipate needs, exercise judgment when priorities competed, and stay calm "
        "when plans shifted.",
        "I bring that same behind-the-scenes ownership to this role: protecting focus, "
        "handling the unexpected, and communicating with professionalism and discretion. "
        "I learn quickly, take responsibility seriously, and would welcome the chance to "
        "support the team with reliability, candor, and care.",
        "Thank you for your time and consideration. I’d be glad to discuss how I can help.",
    ]
    for p in paragraphs:
        story.append(Paragraph(p, styles["LetterBody"]))

    story.append(Spacer(1, 8))
    story.append(Paragraph("Warm regards,", styles["SignOff"]))
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Ananya Rai Paul</b>", styles["SignOff"]))

    doc.build(story)
    print(f"Wrote {PDF_PATH}")


if __name__ == "__main__":
    build()
