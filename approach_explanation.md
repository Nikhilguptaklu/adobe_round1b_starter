# Approach Explanation

## Problem Understanding
The goal is to extract the most relevant sections from a set of PDFs for a specific persona and their job-to-be-done.

## Methodology
1. **Text Extraction**: We use PyMuPDF to extract text from every page of each PDF.
2. **Semantic Matching**: We convert both the user's need (persona + job) and each text block into embeddings using `sentence-transformers`.
3. **Relevance Scoring**: We use cosine similarity to match each section's embedding to the task query.
4. **Filtering & Ranking**: Sections with a similarity above a certain threshold (e.g., 0.5) are kept and ranked by score.
5. **Subsection Extraction**: Matched blocks are also stored in detail as refined sub-sections.

## Why This Generalizes
This approach doesn't depend on specific PDF formatting or keywords — it semantically understands what the user needs, making it robust for any persona, task, or document type.

