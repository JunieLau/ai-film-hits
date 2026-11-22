// Update only the lanes actually scanned. The page computes last addition from the archive cards.
// Detailed verification: data/batches/2026-11-23-reddit-xhs.json.
const LANE_SCAN_STATUS = Object.freeze({
  reddit: {
    "batch": "2026-11-23-reddit-weekly-backfill",
    "scannedAt": "2026-11-23T02:04:09+08:00",
    "labelZh": "已补录 · 社区周榜",
    "labelEn": "Backfill published · community showcase",
    "detailZh": "复核 r/aivideos 社区周榜前 10 条，补录第 6 名《澳洲鸸鹋战争》。保留 11 月 19 日原帖日期；不算作近 72 小时首发。",
    "detailEn": "Reviewed all 10 r/aivideos showcase posts and backfilled the No. 6 entry. Its November 19 post date is unchanged; it is not a 72-hour premiere."
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
