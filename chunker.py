
import os
import fitz  # PyMuPDF
import docx

def extract_text_from_pdf(filepath):
    try:
        doc = fitz.open(filepath)
        text = "".join(page.get_text() for page in doc)
        doc.close()
        return text
    except Exception as e:
        return f"[Fehler beim PDF-Parsing: {e}]"

def extract_text_from_docx(filepath):
    try:
        doc = docx.Document(filepath)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"[Fehler beim DOCX-Parsing: {e}]"

def extract_text_from_txt(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"[Fehler beim TXT-Lesen: {e}]"

def chunk_text(text, max_len=600):
    chunks = []
    current = ""
    for line in text.splitlines():
        if len(current) + len(line) < max_len:
            current += line.strip() + " "
        else:
            chunks.append(current.strip())
            current = line.strip() + " "
    if current:
        chunks.append(current.strip())
    return chunks

def process_folder(path):
    results = {}
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if not os.path.isfile(full_path):
            continue
        if file.lower().endswith(".pdf"):
            text = extract_text_from_pdf(full_path)
        elif file.lower().endswith(".docx"):
            text = extract_text_from_docx(full_path)
        elif file.lower().endswith(".txt"):
            text = extract_text_from_txt(full_path)
        else:
            continue
        results[file] = chunk_text(text)
    return results

if __name__ == "__main__":
    folder = input("Pfad zum Bewerbungsordner: ").strip()
    chunks_by_file = process_folder(folder)
    for filename, chunks in chunks_by_file.items():
        print(f"\n🗂 {filename} ({len(chunks)} Chunks)")
        for i, chunk in enumerate(chunks):
            print(f"--- Chunk {i+1} ---\n{chunk}\n")
