#!/usr/bin/env python3
import datetime, os

tz_cn = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
today = tz_cn.strftime("%Y-%m-%d")
title = f"6G+卫星通信动态简报（{today}）"
slug = f"{today}-6g-satellite-brief"

draft_dir = "source/_drafts"
os.makedirs(draft_dir, exist_ok=True)
path = f"{draft_dir}/{slug}.md"

if os.path.exists(path):
    print("今日草稿已存在，跳过")
    exit(0)

content = f"""---
title: "{title}"
date: {today} 08:00:00
categories: [简报]
tags: [6G, 卫星通信, NTN, 空天地一体化]
brief_date: {today}
draft: true
---

## 今日摘要

> ⚠️ 此为自动生成草稿，待人工审核后发布。

- （待填充：过去24小时6G/卫星通信关键事件）
- （待填充：标准/研发/政策/活动动态）

## 分类详情

### 科技突破
- 暂无自动抓取结果

### 成果转化
- 暂无自动抓取结果

### 标准/研发进展
- 暂无自动抓取结果

### 展会/活动
- 暂无自动抓取结果

### 政策/规划
- 暂无自动抓取结果

## 趋势与观察

- 对中国6G产业：待每日数据积累后自动总结。
- 对北京6G及经开区布局：关注星地融合、低轨组网、通感算智原型落地。
"""

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("已生成草稿:", path)
