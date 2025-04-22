def generate_cover_letter(job_description, cv_path, api_key, style_level):
    # GPT-Prompt mit Stilskala
    prompt = f"""
Der folgende Text ist eine ehrliche, spontane Beschreibung eines Berufswunsches. 
Bitte formuliere daraus ein professionelles Bewerbungsanschreiben in höflichem, authentischem Ton. 
Verwandle direkte Aussagen wie 'viel Geld' oder 'wenig Arbeit' in diplomatische Sprache, 
die dennoch den Kernwunsch wiedergibt.

Der Nutzer wünscht sich einen sprachlichen Stil der Stufe {style_level} auf einer Skala von 1 (direkt, umgangssprachlich, teils vulgär) bis 10 (diplomatisch, global zitierfähig, absolut professionell).

Freitext:
{job_description}

Lebenslauf:
[Dateipfad: {cv_path}]
"""

    # Dummy-Ausgabe
    return f"""
Sehr geehrte Damen und Herren,

bezüglich Ihrer Stelle: {job_description}

Anbei mein Lebenslauf:
{cv_path}

Mit freundlichen Grüßen,  
[Dein Name]
"""
