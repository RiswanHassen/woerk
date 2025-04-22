
import os
import json
import mimetypes

def collect_user_data(name, email, social_links, folder_path):
    files_info = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            mime_type, _ = mimetypes.guess_type(full_path)
            files_info.append({
                "filename": file,
                "path": full_path,
                "type": mime_type or "unknown"
            })
    profile = {
        "name": name,
        "email": email,
        "social_links": social_links,
        "documents": files_info
    }
    os.makedirs("data", exist_ok=True)
    with open("data/user_profile_raw.json", "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2, ensure_ascii=False)
    return profile

def dummy_llm_analysis(profile):
    # Hier käme die LLM-Analyse später rein
    return {
        "cv_summary": "Basierend auf deinen Dokumenten habe ich einen CV mit Fokus auf Cybersecurity erstellt.",
        "personality": "Analytisch, autodidaktisch, zielorientiert",
        "recommended_roles": [
            "Junior Red Team Operator",
            "Technical Content Creator (Cybersecurity)",
            "Security Researcher – Threat Intelligence"
        ]
    }

if __name__ == "__main__":
    # Test
    user = collect_user_data(
        name="Riswan Hassen",
        email="riswan@example.com",
        social_links={
            "GitHub": "https://github.com/RiswanHassen",
            "LinkedIn": "https://linkedin.com/in/deinprofil"
        },
        folder_path="testordner/"
    )
    result = dummy_llm_analysis(user)
    print(json.dumps(result, indent=2, ensure_ascii=False))
