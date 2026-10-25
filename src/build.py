#!/usr/bin/env python3
"""Embed local img/*.jpg as data URIs into a single HTML file (optional local build)."""
import re, base64, os
from pathlib import Path
ROOT = Path(__file__).resolve().parent
src = ROOT / 'index.html'
out = ROOT.parent / 'AI_Film_Hits_Moodboard.html'
s = src.read_text(encoding='utf-8')
used = set(re.findall(r'img/[A-Za-z0-9_.\-]+\.jpg', s))
missing = [u for u in used if not (ROOT / u).exists()]
print('used', len(used), 'missing', len(missing))
def rep(m):
    f = ROOT / m.group(0)
    if not f.exists():
        return m.group(0)
    return 'data:image/jpeg;base64,' + base64.b64encode(f.read_bytes()).decode()
s2 = re.sub(r'img/[A-Za-z0-9_.\-]+\.jpg', rep, s)
out.write_text(s2, encoding='utf-8')
print('wrote', out, 'size', out.stat().st_size)
