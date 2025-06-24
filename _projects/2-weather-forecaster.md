---
title: "Weather Dashboard 🌤️"
layout: single
classes: wide
share: false
related: false
read_time: true
show_date: true                      # Show post date

gallery:
  - url: /assets/images/projects/1-nimbus_predict.png
    image_path: /assets/images/projects/1-nimbus_predict.png
    alt: "Dashboard view"
sidebar:
  - title: "Technologies"
    text: "Python, PySpark, Streamlit, GCP"
  - title: "When"
    text: "Apr 2025"
---

A simple weather dashboard that fetches real-time weather data, processes it into a manageable form, trains a prediction model, and displays the results on an interactive dashboard.

[View Live App](https://nimbus-predict-645776801901.europe-west2.run.app){: .btn .btn--primary}
[View on GitHub](https://github.com/riobanerjee/nimbus-predict){: .btn .btn--primary}

## Features

- Real-time weather data collection from OpenWeatherMap API
- Data processing pipeline using PySpark
- Containerized using Docker
- Interactive Streamlit dashboard
- Air pollution data visualization on maps
- CI/CD with GitHub Actions
- Hosted on Google Cloud Platform

## Technology Stack

- **Backend**: Python, PySpark
- **Frontend**: Streamlit
- **ML**: scikit-learn
- **Cloud**: Google Cloud Platform (Cloud Run)
- **CI/CD**: GitHub Actions
- **APIs**: OpenWeatherMap

{% include gallery caption="Weather Dashboard Application Screenshot" %}