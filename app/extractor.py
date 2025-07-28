import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def extract_relevant_sections(files, persona, job, input_dir):
    query = f"{persona} needs to {job}"
    query_embedding = model.encode(query, convert_to_tensor=True)

    sections = []
    subsections = []
    rank = 1

    for filename in files:
        doc = fitz.open(os.path.join(input_dir, filename))
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text_blocks = page.get_text("blocks")

            for block in text_blocks:
                if block[4].strip():
                    text = block[4].strip()
                    section_embedding = model.encode(text, convert_to_tensor=True)
                    score = util.pytorch_cos_sim(query_embedding, section_embedding).item()

                    if score > 0.5:  # Threshold for relevance
                        sections.append({
                            "document": filename,
                            "page_number": page_num + 1,
                            "section_title": text[:50],
                            "importance_rank": rank
                        })
                        subsections.append({
                            "document": filename,
                            "refined_text": text,
                            "page_number": page_num + 1
                        })
                        rank += 1
    return {"sections": sections, "subsections": subsections}
