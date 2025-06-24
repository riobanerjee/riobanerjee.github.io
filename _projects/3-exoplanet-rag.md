---
title: "Exoplanet RAG 🔍"
layout: single
classes: wide
share: false
related: false
read_time: true
show_date: true

gallery:
  - url: /assets/images/projects/3-exoplanet_rag.png
    image_path: /assets/images/projects/3-exoplanet_rag.png
    alt: "RAG Interface"
sidebar:
  - title: "Technologies"
    text: "Python, LangChain, Ollama, ChromaDB"
  - title: "When"
    text: "May 2025"
---

A Retrieval Augmented Generation (RAG) system for querying exoplanet research papers from ArXiv. This framework demonstrates how RAG can be applied to scientific literature, enabling natural language queries about exoplanet research.

[View on GitHub](https://github.com/riobanerjee/exoplanet-rag){: .btn .btn--primary}

## Features

- Fetch and process ArXiv papers about exoplanets automatically
- Create vector embeddings for efficient similarity search
- Answer questions using retrieved context and local LLM
- Web interface built with Streamlit
- Local deployment with Ollama for privacy
- Configurable models and parameters

## Technology Stack

- **Framework**: LangChain for RAG pipeline
- **LLM**: Ollama (Gemma3:1b) for local inference
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **Vector Store**: ChromaDB
- **Frontend**: Streamlit web interface
- **Data Source**: ArXiv API for research papers

## Example Queries

- "What are sub Neptunes?"
- "How are exoplanets detected?"  
- "What is the habitable zone?"
- "What is an atmospheric retrieval?"

{% include gallery caption="Exoplanet RAG System Interface" %}