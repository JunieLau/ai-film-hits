// Update only the lanes actually scanned. The page computes last addition from the archive cards.
// Detailed verification: data/batches/2026-11-23-reddit-xhs.json.
const LANE_SCAN_STATUS = Object.freeze({
  reddit: {
    batch: "2026-11-23-reddit-xhs",
    scannedAt: "2026-11-23T01:15:00+08:00",
    labelZh: "已扫描 · 未核到达标新作",
    labelEn: "Scan completed · no new verified qualifying work",
    detailZh: "核对了 49 个 Reddit 原帖的发布日期、分数和评论，其中 34 条在 72 小时内。高热度作品《Spider-Man vs Doom》已跨栏收录；其余没有核实到同时达标的全新作品。",
    detailEn: "Checked date, score and comments for 49 original Reddit posts, 34 within 72 hours. The highly engaged Spider-Man vs Doom is already listed elsewhere on this board, and no other new clip met all criteria in this sample."
  },
  xhs: {
    batch: "2026-11-23-reddit-xhs",
    scannedAt: "2026-11-23T01:15:00+08:00",
    labelZh: "已扫描 · 原帖数据待核验",
    labelEn: "Scanned · original-post verification limited",
    detailZh: "逐一核查 9 个线索：能确认的万赞线索已超过 72 小时；其余未能从小红书原帖同时核实首发、点赞和封面。没有因此放宽门槛，也不判定站内没有爆款。",
    detailEn: "Nine leads were examined. The traceable 10K-plus leads fell outside 72 hours; for the others, Xiaohongshu did not expose enough source data to verify original date, likes and cover. This is not a confirmed zero."
  }
});
