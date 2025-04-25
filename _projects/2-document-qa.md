---
title: "Document Q&A System"
excerpt: "AI-powered document question-answering system using Claude AI and vector similarity search"
header:
  image: /assets/images/projects/document-qa-cover.jpg
  teaser: /assets/images/projects/document-qa-thumb.jpg
tags:
  - NLP
  - Claude AI
  - FAISS
  - Streamlit
  - GCP
date: 2024-03-15
---

A powerful document question-answering system that uses Claude AI to answer questions about uploaded PDF documents with vector similarity search.

[View Live App](https://docutalku-995326108656.europe-west2.run.app){: .btn .btn--primary}
[View on GitHub](https://github.com/riobanerjee/document-qa-system){: .btn .btn--primary}

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