---
title: "Document Q&A System 📄"
layout: single
classes: wide
share: false
related: false
read_time: true
show_date: true

gallery:
  - url: /assets/images/projects/2-docutalku_upload.png
    image_path: /assets/images/projects/2-docutalku_upload.png
    alt: "Document Upload Interface"
sidebar:
  - title: "Technologies"
    text: "Python, Claude AI, FAISS, Streamlit"
  - title: "When"
    text: "Apr 2025"
---

A powerful document question-answering system that uses Claude AI to answer questions about uploaded PDF documents with vector similarity search for accurate context retrieval.

[View Live App](https://docutalku-995326108656.europe-west2.run.app){: .btn .btn--primary}
[View on GitHub](https://github.com/riobanerjee/document-qa-system){: .btn .btn--primary}

## Features

- PDF document upload and processing
- Intelligent text chunking with overlap for context preservation
- Question answering powered by Claude AI (Anthropic)
- Clean and intuitive Streamlit interface
- Hosted on Google Cloud Platform (Cloud Run)
- Modular architecture for easy maintenance and scaling

## Technology Stack

- **Backend**: Python with modular architecture
- **AI**: Claude API (Anthropic)
- **Vector Search**: FAISS for efficient similarity search
- **Frontend**: Streamlit for interactive web interface
- **Document Processing**: PyPDF2 for PDF text extraction
- **Cloud**: Google Cloud Platform (Cloud Run)

## Architecture

The system follows a clean, modular design:
1. **Document Processing**: Extract and chunk text from PDFs
2. **Vector Storage**: Create embeddings and store in FAISS index
3. **Query Processing**: Find relevant passages using similarity search
4. **Answer Generation**: Use Claude AI to generate contextual answers

{% include gallery caption="Document Q&A System Interface and Functionality" %}