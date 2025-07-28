import os
import json
import datetime
from app.extractor import extract_relevant_sections

input_dir = "/app/input"
output_dir = "/app/output"
persona = "Undergraduate Chemistry Student"
job = "Identify key concepts and mechanisms for exam preparation on reaction kinetics"

def main():
    files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]
    results = extract_relevant_sections(files, persona, job, input_dir)

    output_json = {
        "metadata": {
            "input_documents": files,
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": datetime.datetime.now().isoformat()
        },
        "extracted_sections": results["sections"],
        "subsection_analysis": results["subsections"]
    }

    with open(os.path.join(output_dir, "output.json"), "w") as f:
        json.dump(output_json, f, indent=2)

if __name__ == "__main__":
    main()
