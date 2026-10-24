# AI Film Hits Moodboard · 全球 AI 爆款视频雷达

在线站点：<https://junielau.github.io/ai-film-hits/>

![preview](preview.png)

## 这是什么

一份精选 moodboard，收录 Instagram、X、Reddit、YouTube 上的病毒式 AI 视频，以及一份 **顶尖 AI 电影人** 名单（最多 80 人，按粉丝数从高到低排序）。另有 **AI 教程** 标签（10 条），列表可按综合最佳 / 最新 / 最多观看排序。

## 如何查看

用浏览器直接打开 [`index.html`](index.html)。这是单个文件，图片已以 base64 内联，不需要服务器，也不需要登录。它同时可以作为 GitHub Pages 的入口页。

## 更新节奏

每 2 天更新一次（周日 / 周二 / 周四 / 周六，约 10:00 Asia/Shanghai）。**只追加、不删除**：已收录的条目永远保留。每一次更新都是一个新的 commit，因此 git 历史就是完整的版本历史。

## 数据规则

- 所有指标都是真实、可核对的。
- 拿不到的数据显示为 **N/A**。
- 计入爆款需要可计数的分享数 ≥ 100。Instagram 不公开分享数，因此 IG 条目标记为 **待验证 / unverified**。

## 目录

| 路径 | 说明 |
| --- | --- |
| `index.html` | 构建好的单文件站点（图片 base64 内联），用浏览器直接打开 |
| `src/index.html` | 可编辑源文件（引用 `src/img/*.jpg`） |
| `src/build.py` | 把 `src/img/*.jpg` 内联进仓库根目录的 `index.html` |
| `src/img/` | 压缩后的封面与头像 JPEG |
| `scripts/merge_append.py` | 只追加的合并脚本 |
| `data/posts_archive.json` | 所有曾加入条目的只追加档案（不删除行） |
| `data/batches/*.json` | 每次更新的批次记录 |
| `preview.png` | 截图 |

重新构建：

```bash
python3 src/build.py
```

---

Live site: <https://junielau.github.io/ai-film-hits/>

## What it is

A curated moodboard of viral AI videos across Instagram, X, Reddit, and YouTube, plus a **Top AI Filmmakers** list (up to 80, sorted by followers). There is also an **AI Tutorial** tab (10 tutorials); lists can be sorted by Best overall, Newest, or Most viewed.

## How to view

Open [`index.html`](index.html) in a browser. It is a single file with images inlined — no server, no login. It also works as the GitHub Pages entry point.

## Update cadence

Every 2 days (Sunday / Tuesday / Thursday / Saturday, around 10:00 Asia/Shanghai). Updates are **append-only**: prior entries are never removed. Every update is a new commit, so git history is the full version history.

## Data rules

- All metrics are real and verifiable.
- Unavailable data is shown as **N/A**.
- A hit requires ≥100 shares where shares are countable. Instagram hides shares, so IG items are marked **待验证 / unverified**.

## Repo layout

| Path | Role |
| --- | --- |
| `index.html` | Built, self-contained site (images inlined as base64). Open it directly in a browser. |
| `src/index.html` | Editable source (references `src/img/*.jpg`) |
| `src/build.py` | Inlines `src/img/*.jpg` into `index.html` at the repo root |
| `src/img/` | Compressed JPEG covers and avatars |
| `scripts/merge_append.py` | Append-only merge script |
| `data/posts_archive.json` | Append-only archive of every post ever added (never delete rows) |
| `data/batches/*.json` | Per-update batch records |
| `preview.png` | Screenshot |

Rebuild:

```bash
python3 src/build.py
```
