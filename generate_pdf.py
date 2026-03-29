"""Generate PDF from AI-Terms-v1.0.md"""
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, HRFlowable

INPUT = "AI-Terms-v1.0.md"
OUTPUT = "AI-Terms-v1.0.pdf"

def md_to_story(md_text):
    styles = getSampleStyleSheet()

    # Custom styles
    styles.add(ParagraphStyle('DocTitle', parent=styles['Title'], fontSize=22, spaceAfter=20, textColor=HexColor('#000000')))
    styles.add(ParagraphStyle('H1', parent=styles['Heading1'], fontSize=18, spaceBefore=30, spaceAfter=12, textColor=HexColor('#1a1a1a')))
    styles.add(ParagraphStyle('H2', parent=styles['Heading2'], fontSize=14, spaceBefore=24, spaceAfter=10, textColor=HexColor('#2a2a2a')))
    styles.add(ParagraphStyle('H3', parent=styles['Heading3'], fontSize=12, spaceBefore=18, spaceAfter=8, textColor=HexColor('#3a3a3a')))
    styles.add(ParagraphStyle('Body', parent=styles['Normal'], fontSize=10, leading=15, spaceAfter=6, textColor=HexColor('#333333')))
    styles.add(ParagraphStyle('Italic', parent=styles['Normal'], fontSize=10, leading=15, spaceAfter=6, textColor=HexColor('#555555')))
    styles.add(ParagraphStyle('BulletItem', parent=styles['Normal'], fontSize=10, leading=15, spaceAfter=4, leftIndent=20, bulletIndent=10, textColor=HexColor('#333333')))
    styles.add(ParagraphStyle('NumberItem', parent=styles['Normal'], fontSize=10, leading=15, spaceAfter=4, leftIndent=20, bulletIndent=10, textColor=HexColor('#333333')))
    styles.add(ParagraphStyle('Bold', parent=styles['Normal'], fontSize=10, leading=15, spaceAfter=8, textColor=HexColor('#000000')))
    styles.add(ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, textColor=HexColor('#999999'), alignment=1))

    story = []
    lines = md_text.split('\n')
    i = 0
    in_table = False

    while i < len(lines):
        line = lines[i].rstrip()

        # Skip empty lines
        if not line:
            i += 1
            continue

        # Skip horizontal rules
        if line.strip() == '---':
            story.append(Spacer(1, 6))
            story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor('#cccccc')))
            story.append(Spacer(1, 6))
            i += 1
            continue

        # Skip code blocks
        if line.strip().startswith('```'):
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            if code_lines:
                code_text = '<br/>'.join(l.replace(' ', '&nbsp;') for l in code_lines)
                story.append(Paragraph(f'<font face="Courier" size="9" color="#666666">{code_text}</font>', styles['Body']))
            i += 1
            continue

        # Tables - simplified
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
            # Skip separator rows
            if re.match(r'^\|[\s\-|]+\|$', line.strip()):
                i += 1
                continue
            cells = [c.strip() for c in line.split('|')[1:-1]]
            row_text = ' | '.join(cells)
            row_text = format_inline(row_text)
            story.append(Paragraph(row_text, styles['Body']))
            i += 1
            continue
        else:
            in_table = False

        # Headers
        if line.startswith('# '):
            text = format_inline(line[2:])
            story.append(Paragraph(text, styles['DocTitle']))
            i += 1
            continue
        if line.startswith('## '):
            text = format_inline(line[3:])
            story.append(Paragraph(text, styles['H2']))
            i += 1
            continue
        if line.startswith('### '):
            text = format_inline(line[4:])
            story.append(Paragraph(text, styles['H3']))
            i += 1
            continue

        # Numbered list
        m = re.match(r'^(\d+)\.\s+(.*)', line)
        if m:
            text = format_inline(m.group(2))
            story.append(Paragraph(f'{m.group(1)}. {text}', styles['NumberItem']))
            i += 1
            continue

        # Bullet points
        if line.startswith('- '):
            text = format_inline(line[2:])
            story.append(Paragraph(f'&bull; {text}', styles['BulletItem']))
            i += 1
            continue

        # Regular paragraph
        text = format_inline(line)
        story.append(Paragraph(text, styles['Body']))
        i += 1

    # Footer
    story.append(Spacer(1, 30))
    story.append(Paragraph('AI Terms v1.0 — onyourterms.ai', styles['Footer']))

    return story

def format_inline(text):
    """Convert markdown inline formatting to reportlab XML"""
    # Escape XML special chars first (but not our formatting)
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')

    # Bold+italic
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<b><i>\1</i></b>', text)
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    # Italic (single *)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<font face="Courier" size="9">\1</font>', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<link href="\2">\1</link>', text)

    return text

# Read markdown
with open(INPUT, 'r', encoding='utf-8') as f:
    md_text = f.read()

# Build PDF
doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=2.5*cm,
    rightMargin=2.5*cm,
    topMargin=2*cm,
    bottomMargin=2*cm
)

story = md_to_story(md_text)
doc.build(story)
print(f"PDF generated: {OUTPUT}")
