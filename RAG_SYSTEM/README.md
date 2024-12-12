# RAG System

## Objectives
- Set up a RAG (Retrieval-Augmented Generation) system.
- Explore the distribution of embeddings with user queries.
- Implement query augmentation.
- Perform result re-ranking.
- Utilize Embedding Adapters.

## Overview
This notebook demonstrates the implementation of a RAG system using Google Cloud's AI Platform, UMAP for dimensionality reduction, and various Python libraries for handling embeddings and queries. The system is designed to process and analyze text data, specifically focusing on the Gracie Jiu-Jitsu book.

## Steps
1. **Setup and Installation**:
   - Install necessary packages including `google-cloud-aiplatform`, `umap-learn`, `tqdm`, `pypdf`, `langchain`, `sentence-transformers`, `chromadb`, and `google-generativeai`.

2. **Data Preparation**:
   - Copy files from Google Cloud Storage.
   - Convert PDF to text using `PyPDF2`.
   - Split the PDF text into chunks to create embeddings due to token limits.

3. **Embedding Creation**:
   - Use `SentenceTransformers` to generate embeddings for the text chunks.
   - Store the embeddings in a ChromaDB database.

4. **Query Processing**:
   - Perform embedding searches on the ChromaDB database.
   - Use a RAG model to answer questions based on the retrieved information.

5. **Embedding Visualization**:
   - Visualize the distribution of embeddings in a 2D space using UMAP.
   - Analyze how queries map to the embedding space to gain insight into answer relevance.

6. **Query Augmentation**:
   - Improve query results by expanding the search with similar queries or providing expected answers.
   - Use LLMs to automatically generate enhanced queries.

7. **Result Re-ranking**:
   - Re-rank results to select the most relevant responses for processing.
   - Use a cross-encoder model for improved accuracy in ranking.

8. **Embedding Adapters**:
   - Fine-tune the embedding model on the dataset using user queries.
   - Adapt the embedding model to better understand domain-specific nuances.

## Usage
- Run the notebook cells sequentially to set up the RAG system and process the text data.
- Modify the queries and data sources as needed to fit your specific use case.
- Use the visualization and augmentation techniques to analyze and improve the query results.

## Author
Rod Morrison
