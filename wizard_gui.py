
import tkinter as tk
from tkinter import filedialog, messagebox

state = {
    "level": "nichts",
    "cloud_link": "",
    "resume_path": "",
    "freitext": "",
    "gehalt": "",
    "waehrung": "EUR"
}

def show_main_window():
    def update_state():
        state["cloud_link"] = cloud_entry.get().strip()
        state["resume_path"] = resume_entry.get().strip()
        state["freitext"] = freitext_entry.get("1.0", tk.END).strip()
        state["gehalt"] = gehalt_entry.get().strip()
        state["waehrung"] = waehrung_var.get()

    def go_action():
        update_state()
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
