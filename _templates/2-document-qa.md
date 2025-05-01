---
title: "Document Q&A System 📝"
layout: single
classes: wide
share: false
related: false
read_time: true
show_date: true                      # Show post date

sidebar:
  - title: "Technologies"
    text: "Python, FAISS, Claude AI"
  - title: "Role"
    text: "ML Engineer"
  - title: "Period"
    text: "Mar 2024 - Present"
gallery:
  - url: /assets/images/projects/docqa-1.jpg
    image_path: /assets/images/projects/docqa-1.jpg
    alt: "Document upload interface"
  - url: /assets/images/projects/docqa-2.jpg
    image_path: /assets/images/projects/docqa-2.jpg
    alt: "Q&A interface"
---

A lightweight document question-answering system that uses Claude AI to answer questions about uploaded PDF documents with vector similarity search.

[View Live App](https://docutalku-995326108656.europe-west2.run.app){: .btn .btn--primary}
[View on GitHub](https://github.com/riobanerjee/DocuTalku){: .btn .btn--primary}

## Features

- PDF document upload and processing
- Text chunking with overlap for context preservation
- Vector similarity search using FAISS
- Question answering powered by Claude AI
- Clean Streamlit interface
- Hosted using GCP Cloud Run

## Technology Stack

- **Backend**: Python, FAISS
- **AI**: Claude API (Anthropic)
- **Frontend**: Streamlit
- **Cloud**: Google Cloud Platform (Cloud Run)
- **PDF Processing**: PyPDF2

{% include gallery caption="Document Q&A System Screenshots" %}