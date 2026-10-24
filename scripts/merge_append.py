#!/usr/bin/env python3
"""APPEND-ONLY merge helper for AI Film Hits moodboard.
Usage (future refresh): load posts_archive.json, merge new posts by id, rewrite index.html arrays.
NEVER replace REELS/X_POSTS/REDDIT_POSTS/YT_POSTS wholesale — merge by id and keep history.
Every refresh: rewrite IG/X/REDDIT/YT_TREND_* blurbs; keep whyZh/whyEn on every video card.
"""
import json
from pathlib import Path
ARCHIVE = Path('/workspace/moodboard_history/posts_archive.json')

def merge_by_id(existing, incoming, id_key='id'):
    by = {p[id_key]: dict(p) for p in existing if id_key in p}
    for p in incoming:
        i = p[id_key]
        if i in by:
            by[i] = {**by[i], **p}  # refresh metrics, keep first addedAt if absent
            if 'addedAt' in existing_match(by, i) and 'addedAt' not in p:
                pass
        else:
            by[i] = dict(p)
    return list(by.values())

def existing_match(by, i):
    return by.get(i, {})

if __name__ == '__main__':
    print('Archive:', ARCHIVE, 'exists=', ARCHIVE.exists())
    if ARCHIVE.exists():
        a=json.loads(ARCHIVE.read_text())
        for k in ['instagram','x','reddit','youtube','filmmakers','tutorials','removed_tutorials']:
            print(k, len(a.get(k,[])))
        print('blocklist.tutorials', a.get('blocklist',{}).get('tutorials',[]))
