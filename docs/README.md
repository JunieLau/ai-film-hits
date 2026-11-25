# AI Film Hits（HIT VIDEO REPORTER）工作档案

本目录整理的是 HIT VIDEO REPORTER 自约 2026 年 10 月 21 日起，到 2026 年 11 月 22 日停止主动检索为止的日常工作、经验教训，以及各平台资料来源的准确度。站点是 Junie 的 [AI Film Hits / 全球 AI 爆款视频雷达](https://junielau.com/ai-film-hits/)，仓库为 [JunieLau/ai-film-hits](https://github.com/JunieLau/ai-film-hits)。

所有时间如无另注，均为 **Asia/Shanghai（UTC+8）**。

本稿只根据工作区既有记录写成：版本 SHIP 说明、`moodboard_history` 快照与 `posts_archive`、检查点与方法报告、工作记忆，以及已经对 Junie 说过的停工说明。本轮**没有**做新的站外检索或扫描，也**没有**改 GitHub 仓库。数字、提交哈希、栏次数只在记录里写得清楚时才写入；记录缺失处会标明缺口，不补造。

本目录不含密钥、token、cookie 或私人登录资料。

## 文件

| 文件 | 内容 |
| --- | --- |
| [WORK-LOG.md](WORK-LOG.md) | 按日工作日志：日期、做了什么、版本/提交、各栏新增数量、遇到的问题 |
| [LESSONS-LEARNED.md](LESSONS-LEARNED.md) | 训练下来的经验教训：全量更新口径、质量门槛、热度门槛、犯过的错、以后怎么做 |
| [SOURCES-GUIDE.md](SOURCES-GUIDE.md) | 资料来源准确度指南：各平台哪些来源可靠、哪些不可靠或已封锁、各自能证明什么、建议顺序 |

## 仓库关系

完整版本记录本来就在 GitHub 的提交历史里（`main` 分支；根目录 `index.html` 为线上页，`src/` 为源与封面，`data/posts_archive.json` 为追加档案）。本目录是给人和后续执行器看的说明，不是站点构建产物。

若要把这四份文件更新到 GitHub，请由父代理在 Junie 确认后提交（建议放在仓库 `docs/` 或同等说明目录），不要把本目录里的工作笔记误当成要覆盖线上 `index.html` 的发版包。

## 阅读时请先记住的几点

- **全量更新**指的是：在约定新窗口里发现、核验并加入最新爆款，而不是给旧卡改日期或批量刷新旧指标。
- 证据不齐或关键动作明显变形，应标 HOLD，宁缺毋滥。
- 某平台被墙后得到的 0，不是「已经确认没有新片」。
- 2026-11-21 20:30 至 2026-11-22 01:47 是空档，不能写成已工作。
- 2026-11-22 起因额度消耗过大已停止主动检索；定时任务的暂停操作曾被方案权限拒绝，未能保存暂停。在 Junie 亲自恢复之前，不应自行重启扫描。

## 编制说明

写成于 2026-11-25。主要依据包括：`moodboard_history/` 各版本快照与合并摘要、各 `SHIP.md` / `SHIP.txt`、`/workspace/v52` 与 `/workspace/v53/recovery-0148` 的检查点和方法报告、工作记忆 `/bot/workstream/ai-film-hits`。早期部分版本（尤其是 10 月 21–23 日的 v1–v18）没有完整 SHIP，只能依据当时的 `index.html` 快照计数；v38 / v38b 只有发版包，工作区未见独立 SHIP 正文，日志里已标明。
