#!/usr/bin/env python3
"""Build PDF from ai-agent-book zh directory."""
import requests
import json
import sys
import time

BASE_RAW = "https://raw.githubusercontent.com/Kocoro-lab/ai-agent-book/main/"
BASE_API = "https://api.github.com/repos/Kocoro-lab/ai-agent-book/git/trees/main?recursive=1"

# Ordered file list (book order)
ORDER = [
    "zh/README.md",
    "zh/前言.md",
    "zh/TABLE_OF_CONTENTS.md",
    "zh/Part1-Agent基础/README.md",
    "zh/Part1-Agent基础/第01章：Agent的基础.md",
    "zh/Part1-Agent基础/第02章：ReAct循环.md",
    "zh/Part2-工具与扩展/README.md",
    "zh/Part2-工具与扩展/第03章：工具与用户交互.md",
    "zh/Part2-工具与扩展/第04章：MCP协议支持.md",
    "zh/Part2-工具与扩展/第05章：Skills技能系统.md",
    "zh/Part2-工具与扩展/第06章：Hooks事件系统.md",
    "zh/Part3-上下文与记忆/README.md",
    "zh/Part3-上下文与记忆/第07章：上下文的管理.md",
    "zh/Part3-上下文与记忆/第08章：记忆架构.md",
    "zh/Part3-上下文与记忆/第09章：跨对话记忆库.md",
    "zh/Part4-单Agent模式/README.md",
    "zh/Part4-单Agent模式/第10章：Planning模式.md",
    "zh/Part4-单Agent模式/第11章：Reflection模式.md",
    "zh/Part4-单Agent模式/第12章：Chain-of-Thought.md",
    "zh/Part5-多Agent编排/README.md",
    "zh/Part5-多Agent编排/第13章：并行优化.md",
    "zh/Part5-多Agent编排/第14章：DAG调度.md",
    "zh/Part5-多Agent编排/第15章：Swarm模式.md",
    "zh/Part5-多Agent编排/第16章：Handoff协议.md",
    "zh/Part6-高级推理/README.md",
    "zh/Part6-高级推理/第17章：Tree-of-Thoughts.md",
    "zh/Part6-高级推理/第18章：Debate模式.md",
    "zh/Part6-高级推理/第19章：Research-Synthesis.md",
    "zh/Part7-生产架构/README.md",
    "zh/Part7-生产架构/第20章：生产架构概览.md",
    "zh/Part7-生产架构/第21章：Temporal工作流.md",
    "zh/Part7-生产架构/第22章：可观察性.md",
    "zh/Part8-企业级特性/README.md",
    "zh/Part8-企业级特性/第23章：Token预算管理.md",
    "zh/Part8-企业级特性/第24章：权限与安全.md",
    "zh/Part8-企业级特性/第25章：安全执行.md",
    "zh/Part8-企业级特性/第26章：多租户架构.md",
    "zh/Part9-前沿实践/README.md",
    "zh/Part9-前沿实践/第27章：Deep-Research.md",
    "zh/Part9-前沿实践/第28章：Computer-Use.md",
    "zh/Part9-前沿实践/第29章：Agentic-Coding.md",
    "zh/Part9-前沿实践/第30章：Background-Agents.md",
    "zh/Part9-前沿实践/第31章：多模态操作.md",
    "zh/Part9-前沿实践/第32章：OpenClaw时代.md",
    "zh/Part9-前沿实践/第33章：Building-on-the-Harness-ShanClaw.md",
    "zh/Resources & Links/README.md",
    "zh/附录/README.md",
    "zh/附录/附录A：术语表.md",
    "zh/附录/附录B：模式选择指南.md",
    "zh/附录/附录C：常见问题FAQ.md",
]

def fetch_file(path):
    url = BASE_RAW + requests.utils.quote(path, safe='/')
    r = requests.get(url, timeout=30)
    if r.status_code == 200:
        return r.text
    print(f"  WARN: {r.status_code} for {path}", file=sys.stderr)
    return None

# First, get the actual file list from API to resolve encoding issues
print("Fetching file tree from GitHub API...", file=sys.stderr)
r = requests.get(BASE_API, timeout=30)
tree = r.json().get('tree', [])
actual_paths = {f['path'] for f in tree if f['type'] == 'blob' and f['path'].startswith('zh/')}

# Try to match ordered paths, fall back to sorted actual paths
matched = []
for path in ORDER:
    if path in actual_paths:
        matched.append(path)
    else:
        print(f"  MISS: {path}", file=sys.stderr)

# Add any zh/*.md files not in our order list
for p in sorted(actual_paths):
    if p.endswith('.md') and p not in matched and p not in ORDER:
        matched.append(p)
        print(f"  EXTRA: {p}", file=sys.stderr)

print(f"\nFetching {len(matched)} files...", file=sys.stderr)

combined_md = []
combined_md.append("""# From Concept to Production: Framework-Agnostic AI Agent Architecture Patterns

*AI Agent架构模式：从概念到生产*

---
""")

for i, path in enumerate(matched):
    print(f"  [{i+1}/{len(matched)}] {path}", file=sys.stderr)
    content = fetch_file(path)
    if content:
        # Add section separator
        combined_md.append(f"\n\n---\n\n")
        combined_md.append(content)
    time.sleep(0.1)  # be nice to GitHub

full_md = "\n".join(combined_md)

# Write combined markdown
with open("D:/workspace/ai/ai-agent-book-zh.md", "w", encoding="utf-8") as f:
    f.write(full_md)

print(f"\nMarkdown written: {len(full_md)} chars", file=sys.stderr)
print("DONE_MARKDOWN", flush=True)
