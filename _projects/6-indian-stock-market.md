---
title: "Indian Stock Market Pipeline 📈"
layout: single
classes: wide
share: false
related: false
read_time: true
show_date: true

gallery:
sidebar:
  - title: "Technologies"
    text: "GCP, BigQuery, Cloud Functions, Looker Studio"
  - title: "When"
    text: "May 2025"
---

A lightweight, serverless GCP pipeline that automatically fetches, analyzes, and visualizes Indian stock market data with technical indicators and anomaly detection.

[View on GitHub](https://github.com/riobanerjee/indian-stock-pipeline){: .btn .btn--primary}

## Features

- Daily automated data ingestion from Indian Stock Exchange API
- Technical indicators calculation (7-day moving averages)
- Interactive Looker Studio dashboard
- Serverless architecture for cost efficiency
- Automated scheduling with Cloud Scheduler

## Technology Stack

- **Cloud Platform**: Google Cloud Platform
- **Data Storage**: BigQuery for analytics and warehousing
- **Compute**: Cloud Functions for serverless data processing
- **Scheduling**: Cloud Scheduler for automated triggers
- **Visualization**: Looker Studio for interactive dashboards
- **API**: Indian Stock Exchange API (free tier)

## Architecture

The pipeline follows a serverless ETL pattern:
1. **Extract**: Cloud Functions fetch daily stock data
2. **Transform**: Calculate technical indicators and detect anomalies
3. **Load**: Store processed data in BigQuery
4. **Visualize**: Real-time dashboard updates in Looker Studio

{% include gallery caption="Stock Market Pipeline Dashboard and Analytics" %}