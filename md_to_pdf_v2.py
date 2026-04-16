#!/usr/bin/env python3
"""Convert markdown to PDF using xhtml2pdf with Chinese font support."""
import sys
import os
import markdown

# Read combined markdown
with open("D:/workspace/ai/ai-agent-book-zh.md", encoding="utf-8") as f:
    md_text = f.read()

md = markdown.Markdown(extensions=[
    'markdown.extensions.tables',
    'markdown.extensions.fenced_code',
    'markdown.extensions.toc',
])
body_html = md.convert(md_text)

# Find a CJK font on the system
import glob

def find_font(names):
    paths = [
        "C:/Windows/Fonts/",
        "C:/Users/dingy/AppData/Local/Microsoft/Windows/Fonts/",
    ]
    for name in names:
        for p in paths:
            matches = glob.glob(p + name, recursive=False)
            if matches:
                return matches[0].replace("\\", "/")
    return None

cjk_font = find_font(["msyh.ttc", "msyh.ttf", "simhei.ttf", "simsun.ttc", "arial.ttf"])
print(f"Using font: {cjk_font}", file=sys.stderr)

# Build @font-face if found
font_face = ""
font_family = "Arial, sans-serif"
if cjk_font:
    font_name = os.path.splitext(os.path.basename(cjk_font))[0]
    font_face = f"""
@font-face {{
    font-family: '{font_name}';
    src: url('file:///{cjk_font}');
}}
"""
    font_family = f"'{font_name}', Arial, sans-serif"

css = f"""
{font_face}

body {{
    font-family: {font_family};
    font-size: 11pt;
    line-height: 1.8;
    color: #1a1a1a;
}}

h1 {{
    font-size: 20pt;
    font-weight: bold;
    color: #1a1a2e;
    margin-top: 30pt;
    margin-bottom: 8pt;
    border-bottom: 2pt solid #4a90d9;
    padding-bottom: 4pt;
    page-break-before: always;
}}

h1:first-child {{ page-break-before: avoid; }}

h2 {{
    font-size: 15pt;
    font-weight: bold;
    color: #16213e;
    margin-top: 20pt;
    margin-bottom: 6pt;
}}

h3 {{
    font-size: 12pt;
    font-weight: bold;
    color: #0f3460;
    margin-top: 14pt;
    margin-bottom: 4pt;
}}

h4 {{
    font-size: 11pt;
    font-weight: bold;
    margin-top: 10pt;
}}

p {{ margin: 5pt 0; }}

pre {{
    background: #f0f4f8;
    padding: 8pt;
    font-size: 9pt;
    border-left: 3pt solid #4a90d9;
    margin: 8pt 0;
    overflow: hidden;
    white-space: pre-wrap;
    word-wrap: break-word;
}}

code {{
    font-size: 9pt;
    background: #f0f4f8;
    padding: 1pt 3pt;
}}

pre code {{
    background: transparent;
    padding: 0;
}}

blockquote {{
    border-left: 4pt solid #4a90d9;
    background: #f0f7ff;
    margin: 8pt 0;
    padding: 6pt 10pt;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin: 8pt 0;
    font-size: 10pt;
}}

th {{
    background: #2c3e50;
    color: white;
    padding: 4pt 8pt;
    text-align: left;
    font-weight: bold;
}}

td {{
    padding: 4pt 8pt;
    border-bottom: 0.5pt solid #ddd;
}}

tr:nth-child(even) td {{ background: #f8f9fa; }}

ul, ol {{ margin: 5pt 0; padding-left: 20pt; }}
li {{ margin: 2pt 0; }}

hr {{
    border: none;
    border-top: 0.5pt solid #ddd;
    margin: 12pt 0;
}}

@page {{
    size: A4;
    margin: 2.5cm 2cm 2.5cm 2cm;
    @frame footer {{
        -pdf-frame-content: footer;
        bottom: 1cm;
        margin-left: 2cm;
        margin-right: 2cm;
        height: 1cm;
    }}
}}
"""

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{css}</style>
</head>
<body>
{body_html}
</body>
</html>"""

with open("D:/workspace/ai/ai-agent-book-zh.html", "w", encoding="utf-8") as f:
    f.write(html)
print("HTML written.", file=sys.stderr)

# Generate PDF
print("Generating PDF with xhtml2pdf...", file=sys.stderr)
from xhtml2pdf import pisa

with open("D:/workspace/ai/ai-agent-book-zh.pdf", "wb") as out:
    result = pisa.CreatePDF(
        html.encode("utf-8"),
        dest=out,
        encoding="utf-8",
        path="D:/workspace/ai/",
    )

if result.err:
    print(f"PDF errors: {result.err}", file=sys.stderr)
else:
    size = os.path.getsize("D:/workspace/ai/ai-agent-book-zh.pdf")
    print(f"PDF generated: {size/1024/1024:.1f} MB")
    print("Saved to: D:/workspace/ai/ai-agent-book-zh.pdf")
