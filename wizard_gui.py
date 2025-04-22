
import tkinter as tk
from tkinter import filedialog, messagebox
import os

try:
    from gpt_engine import generate_intro, generate_cover_letter
except:
    from mock_gpt import generate_intro, generate_cover_letter

state = {
    "level": "wenig",
    "folder_path": "",
    "resume_path": "",
    "freitext": "",
    "gehalt": "",
    "waehrung": "EUR",
    "api_sandbox": False,
    "api_key": ""
}

def list_files_in_folder(path):
    try:
        return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    except Exception as e:
        return [f"[Fehler beim Lesen des Ordners] {e}"]

def show_main_window():
    def update_state():
        state["folder_path"] = folder_label.cget("text")
        state["resume_path"] = resume_entry.get().strip()
        state["freitext"] = freitext_entry.get("1.0", tk.END).strip()
        state["gehalt"] = gehalt_entry.get().strip()
        state["waehrung"] = waehrung_var.get()
        state["api_key"] = api_entry.get().strip()
        state["api_sandbox"] = api_sandbox_var.get()

    def select_folder():
        path = filedialog.askdirectory()
        if path:
            folder_label.config(text=path)

    def select_resume_file():
        path = filedialog.askopenfilename(filetypes=[("Documents", "*.pdf *.docx *.txt")])
        if path:
            resume_entry.delete(0, tk.END)
            resume_entry.insert(0, path)

    def go_action():
        update_state()
        files = list_files_in_folder(state["folder_path"])
        messagebox.showinfo("Verarbeite lokal", "📂 Enthaltene Dateien:\n" + "\n".join(files))

    def back_action():
        update_state()
        root.destroy()
        show_mode_selection()

    root = tk.Tk()
    root.title("WŒRK – Lokale Version (Fallback Drag & Drop)")

    tk.Label(root, text="Wähle einen Ordner mit deinen Bewerbungsunterlagen:").pack(pady=(10, 0))
    tk.Button(root, text="Ordner auswählen", command=select_folder).pack()
    folder_label = tk.Label(root, text=state["folder_path"] or "[Noch kein Ordner ausgewählt]")
    folder_label.pack(pady=(5, 10))

    tk.Label(root, text="Lebenslauf (optional):").pack()
    resume_entry = tk.Entry(root, width=60)
    resume_entry.insert(0, state["resume_path"])
    resume_entry.pack(pady=(5, 0))
    tk.Button(root, text="Datei auswählen", command=select_resume_file).pack(pady=(0, 5))

    try:
        import tkinterdnd2 as tkdnd
        from tkinterdnd2 import TkinterDnD
        resume_entry.drop_target_register(tkdnd.DND_FILES)
        resume_entry.dnd_bind('<<Drop>>', lambda event: resume_entry.delete(0, tk.END) or resume_entry.insert(0, event.data.strip('{}')))
    except ImportError:
        tk.Label(root, text="(Drag & Drop nicht verfügbar – Modul tkinterdnd2 fehlt)", fg="gray").pack()

    tk.Label(root, text="Was wünschst du dir beruflich? (Freitext):").pack()
    freitext_entry = tk.Text(root, height=4, width=50)
    freitext_entry.insert("1.0", state["freitext"])
    freitext_entry.pack()

    tk.Label(root, text="Gewünschtes Jahresgehalt (brutto):").pack()
    gehalt_entry = tk.Entry(root, width=20)
    gehalt_entry.insert(0, state["gehalt"])
    gehalt_entry.pack()

    tk.Label(root, text="Währung:").pack()
    waehrung_var = tk.StringVar(value=state["waehrung"])
    tk.OptionMenu(root, waehrung_var, "EUR", "USD", "GBP", "CHF", "SEK").pack()

    tk.Label(root, text="OpenAI API Key:").pack()
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
        "nichts": "Nur Ordner auswählen – alles automatisch.",
        "wenig": "Zusätzlich Freitext, Gehalt und Lebenslaufentwurf.",
        "moderat": "Weitere Details (in Vorbereitung)."
    }

    for key, label in options.items():
        tk.Radiobutton(sel, text=f"{key.capitalize()} – {label}", variable=var, value=key).pack(anchor="w")

    tk.Button(sel, text="Weiter", command=proceed).pack(pady=10)
    sel.mainloop()

if __name__ == "__main__":
    show_mode_selection()
