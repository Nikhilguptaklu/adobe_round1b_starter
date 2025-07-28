# Adobe Hackathon - Round 1B

## Objective
Extract relevant sections from multiple PDFs based on a specific persona and their job-to-be-done.

## How it works
We use sentence embeddings (`all-MiniLM-L6-v2`) to match PDF content to a natural language query composed of the persona and their task.

## Running the Code
Build and run the Docker container:

```bash
docker build --platform linux/amd64 -t adobe-round1b .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none adobe-round1b
```
