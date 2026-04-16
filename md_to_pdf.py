#!/usr/bin/env python3
"""Convert combined markdown to PDF with Chinese font support."""
import sys
import re

# Read markdown
with open("D:/workspace/ai/ai-agent-book-zh.md", encoding="utf-8") as f:
    md_text = f.read()

# Convert markdown to HTML
import markdown
md = markdown.Markdown(extensions=[
    'markdown.extensions.tables',
    'markdown.extensions.fenced_code',
    'markdown.extensions.toc',
    'markdown.extensions.nl2br',
])
body_html = md.convert(md_text)

# CSS with Chinese font stack (uses system fonts available on Windows)
css = """
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700&display=swap');

* { box-sizing: border-box; }

body {
    font-family: 'Noto Sans SC', 'Microsoft YaHei', 'SimHei', 'WenQuanYi Micro Hei', sans-serif;
    font-size: 11pt;
    line-height: 1.8;
    color: #1a1a1a;
    margin: 0;
    padding: 0;
}

@page {
    size: A4;
    margin: 2.5cm 2.2cm 2.5cm 2.2cm;
    @bottom-right {
        content: counter(page);
        font-size: 9pt;
        color: #888;
    }
}

h1 {
    font-size: 24pt;
    font-weight: 700;
    color: #1a1a2e;
    margin-top: 2em;
    margin-bottom: 0.5em;
    page-break-before: always;
    border-bottom: 3px solid #4a90d9;
    padding-bottom: 0.3em;
}

h1:first-child {
    page-break-before: avoid;
}

h2 {
    font-size: 16pt;
    font-weight: 700;
    color: #16213e;
    margin-top: 1.8em;
    margin-bottom: 0.4em;
    border-left: 4px solid #4a90d9;
    padding-left: 0.6em;
}

h3 {
    font-size: 13pt;
    font-weight: 700;
    color: #0f3460;
    margin-top: 1.4em;
    margin-bottom: 0.3em;
}

h4 {
    font-size: 11pt;
    font-weight: 700;
    color: #333;
    margin-top: 1.2em;
}

p {
    margin: 0.6em 0;
    text-align: justify;
}

code {
    font-family: 'Cascadia Code', 'Consolas', 'Courier New', monospace;
    font-size: 9.5pt;
    background: #f0f4f8;
    padding: 1px 5px;
    border-radius: 3px;
    color: #c0392b;
}

pre {
    background: #1e2a3a;
    color: #e8e8e8;
    padding: 1em 1.2em;
    border-radius: 6px;
    overflow-x: auto;
    margin: 1em 0;
    page-break-inside: avoid;
}

pre code {
    background: transparent;
    color: #e8e8e8;
    padding: 0;
    font-size: 9pt;
    line-height: 1.5;
}

blockquote {
    border-left: 4px solid #4a90d9;
    background: #f0f7ff;
    margin: 1em 0;
    padding: 0.6em 1em;
    border-radius: 0 4px 4px 0;
}

blockquote p { margin: 0.2em 0; }

table {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
    font-size: 10pt;
    page-break-inside: avoid;
}

th {
    background: #2c3e50;
    color: #fff;
    padding: 0.5em 0.8em;
    text-align: left;
    font-weight: 700;
}

td {
    padding: 0.4em 0.8em;
    border-bottom: 1px solid #ddd;
}

tr:nth-child(even) td { background: #f8f9fa; }

ul, ol {
    margin: 0.6em 0;
    padding-left: 1.8em;
}

li { margin: 0.25em 0; }

hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 1.5em 0;
}

strong { color: #1a1a2e; }

a { color: #4a90d9; text-decoration: none; }
"""

# Full HTML document
html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI Agent架构模式：从概念到生产</title>
<style>
{css}
</style>
</head>
<body>
{body_html}
</body>
</html>"""

# Write HTML for inspection
with open("D:/workspace/ai/ai-agent-book-zh.html", "w", encoding="utf-8") as f:
    f.write(html)
print("HTML written.", file=sys.stderr)

# Generate PDF with WeasyPrint
print("Generating PDF (this may take a minute)...", file=sys.stderr)
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

font_config = FontConfiguration()

doc = HTML(
    string=html,
    base_url="D:/workspace/ai/"
)

doc.write_pdf(
    "D:/workspace/ai/ai-agent-book-zh.pdf",
    font_config=font_config,
    optimize_images=True,
)

import os
size = os.path.getsize("D:/workspace/ai/ai-agent-book-zh.pdf")
print(f"PDF generated: {size/1024/1024:.1f} MB", file=sys.stderr)
print(f"Saved to: D:/workspace/ai/ai-agent-book-zh.pdf")
