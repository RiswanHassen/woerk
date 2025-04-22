# 📘 WŒRK – Projekt-Dokumentation

## ✅ Stand: 22.04.2025 19:19

---

## 📋 Was wir heute gemacht haben

- Fokus: **Beitragsstufe „nichts“**
- Lokale GUI komplett überarbeitet für intuitive UX:
  - Minimale Ansicht bei „nichts“
  - Erweiterte Ansicht bei „wenig“ (Lebenslauf, Freitext, Gehalt)
- Drag & Drop für Lebenslauf integriert + fallback-sicher
- Fortschrittsanzeige (Widget mit % + Popup) eingebaut
- Lokales **Chunking-Modul** erstellt für PDFs, DOCX und TXT
  - Inhalte werden automatisch in GPT-verdauliche Blöcke zerlegt
- Dateiparser vollständig lokalisiert – keine Cloud-Anbindung nötig

---

## 🔜 Nächste Schritte (voraussichtlich)

1. Integration des Chunkers in die GUI (`Go!`)
2. Fortschrittsanzeige mit echtem Verarbeitungstakt verknüpfen
3. Verarbeitungsergebnisse speichern (z. B. als Markdown / JSON / TXT)
4. GPT-Verbindung vorbereiten (später aktivierbar)
5. LLM-Module:
   - Profilanalyse
   - Skill-Extraktion
   - Jobtitel-Vorschläge
6. Exportoption für Lebenslauf + Anschreiben (Markdown, PDF, ggf. DOCX)
7. Vorbereitung der Web-/Mobile-Version (**WOERK2go**)

---

## 🔖 Hinweise

- Das Projekt läuft lokal, ohne Internetzugriff.
- Die Dateien im Ordner werden **nicht verändert**, sondern nur gelesen.
- GPT-Anbindung erfolgt **erst, wenn die lokale Verarbeitung reibungslos läuft.**

---

## 🛠 Struktur

- `wizard_gui.py` – Haupt-GUI
- `widget_window.py` – Fortschrittsanzeige
- `chunker.py` – Lokaler Dokumenten-Parser & Chunker
- `mock_gpt.py` – Platzhalter für GPT-Funktionen
- `dropbox_parser.py` – veraltet (aktuell nicht aktiv)
- `/config/` – gespeicherte API Keys & Pfade (optional)

---

## 📁 Projektziel (lokal)

> Der Nutzer muss **nur einen Ordner auswählen.**  
> WŒRK übernimmt: Analyse, Strukturierung, Generierung.  
> Alles lokal, sicher und verständlich.

