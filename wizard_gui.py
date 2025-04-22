
import tkinter as tk
from tkinter import filedialog, messagebox
import os

try:
    from gpt_engine import generate_intro, generate_cover_letter
except:
    from mock_gpt import generate_intro, generate_cover_letter

state = {
    "level": "nichts",
    "cloud_link": "",
    "resume_path": "",
    "freitext": "",
    "gehalt": "",
    "waehrung": "EUR",
    "cloud_sandbox": False,
    "api_sandbox": False,
    "api_key": ""
}

def mock_list_cloud_folder(link):
    return ["test1.pdf", "old_cv.docx", "notes.txt"]

def show_main_window():
    def update_state():
        state["cloud_link"] = cloud_entry.get().strip()
        state["resume_path"] = resume_entry.get().strip()
        state["freitext"] = freitext_entry.get("1.0", tk.END).strip()
        state["gehalt"] = gehalt_entry.get().strip()
        state["waehrung"] = waehrung_var.get()
        state["api_key"] = api_entry.get().strip()
        state["cloud_sandbox"] = cloud_sandbox_var.get()
        state["api_sandbox"] = api_sandbox_var.get()

    def go_action():
        update_state()
        if state["cloud_sandbox"]:
            files = mock_list_cloud_folder(state["cloud_link"])
            messagebox.showinfo("Cloud-Inhalt", "📂 Gefundene Dateien:\n" + "\n".join(files))
        elif state["api_sandbox"]:
            intro = generate_intro(state["freitext"])
            letter = generate_cover_letter(state["freitext"], state["resume_path"], style_level=state["waehrung"])
            messagebox.showinfo("Sandbox Test", f"Intro:\n{intro}\n\nAnschreiben:\n{letter}")
        else:
            messagebox.showinfo("Under Construction", "🚧 Diese Funktion wird aktuell gebaut – stay tuned!")

    def back_action():
        update_state()
        root.destroy()
        show_mode_selection()

    root = tk.Tk()
    root.title("WŒRK – Deine Angaben")

    tk.Label(root, text="Link zu deinem Cloudspeicher-Ordner:").pack(pady=(10, 0))
    cloud_entry = tk.Entry(root, width=50)
    cloud_entry.insert(0, state["cloud_link"])
    cloud_entry.pack()

    cloud_sandbox_var = tk.BooleanVar(value=state["cloud_sandbox"])
    tk.Checkbutton(root, text="Sandbox Mode", variable=cloud_sandbox_var).pack()

    if state["level"] in ["wenig", "moderat"]:
        tk.Label(root, text="Lebenslauf-Entwurf (optional, lokal oder Cloud-Link):").pack(pady=(10, 0))
        resume_entry = tk.Entry(root, width=50)
        resume_entry.insert(0, state["resume_path"])
        resume_entry.pack()
    else:
        resume_entry = tk.Entry()

    if state["level"] == "wenig":
        tk.Label(root, text="Was wünschst du dir beruflich? (Freitext):").pack(pady=(10, 0))
        freitext_entry = tk.Text(root, height=4, width=50)
        freitext_entry.insert("1.0", state["freitext"])
        freitext_entry.pack()
    else:
        freitext_entry = tk.Text()

    if state["level"] == "wenig":
        tk.Label(root, text="Gewünschtes Jahresgehalt (brutto):").pack(pady=(10, 0))
        gehalt_entry = tk.Entry(root, width=20)
        gehalt_entry.insert(0, state["gehalt"])
        gehalt_entry.pack()

        tk.Label(root, text="Währung:").pack()
        waehrung_var = tk.StringVar(value=state["waehrung"])
        tk.OptionMenu(root, waehrung_var, "EUR", "USD", "GBP", "CHF", "SEK").pack()
    else:
        gehalt_entry = tk.Entry()
        waehrung_var = tk.StringVar()

    tk.Label(root, text="OpenAI API Key:").pack(pady=(10, 0))
    api_entry = tk.Entry(root, width=50, show="*")
    api_entry.insert(0, state["api_key"])
    api_entry.config(state=tk.DISABLED if state["api_sandbox"] else tk.NORMAL)
    api_entry.pack()

    api_sandbox_var = tk.BooleanVar(value=state["api_sandbox"])
    def toggle_api_state():
        api_entry.config(state=tk.DISABLED if api_sandbox_var.get() else tk.NORMAL)
    tk.Checkbutton(root, text="Sandbox Mode", variable=api_sandbox_var, command=toggle_api_state).pack()

    tk.Button(root, text="Zurück", command=back_action).pack(side=tk.LEFT, padx=20, pady=20)
    tk.Button(root, text="Go!", command=go_action).pack(side=tk.RIGHT, padx=20, pady=20)

    root.mainloop()

def show_mode_selection():
    def proceed():
        state["level"] = var.get()
        sel.destroy()
        show_main_window()

    sel = tk.Tk()
    sel.title("WŒRK – Beitragsstufe wählen")

    tk.Label(sel, text="Wie viel möchtest du selbst beitragen?").pack(pady=10)
    var = tk.StringVar(value=state["level"])

    options = {
        "nichts": "Nur Cloud-Ordner – alles automatisch.",
        "wenig": "Zusätzlich Freitext, Gehalt und Lebenslaufentwurf.",
        "moderat": "Weitere Details (in Vorbereitung)."
    }

    for key, label in options.items():
        tk.Radiobutton(sel, text=f"{key.capitalize()} – {label}", variable=var, value=key).pack(anchor="w")

    tk.Button(sel, text="Weiter", command=proceed).pack(pady=10)
    sel.mainloop()

if __name__ == "__main__":
    show_mode_selection()
