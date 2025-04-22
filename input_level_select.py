
import tkinter as tk
from tkinter import messagebox

def ask_contribution_level():
    def proceed():
        level = var.get()
        freitext = freitext_entry.get("1.0", tk.END).strip()
        result['level'] = level
        result['freitext'] = freitext if level == "wenig" else None
        result['moderat_data'] = "Wird später abgefragt" if level == "moderat" else None
        win.destroy()

    win = tk.Tk()
    win.title("Beitragsstufe wählen")

    tk.Label(win, text="Wie viel möchtest du selbst beitragen?").pack(pady=10)
    var = tk.StringVar(value="nichts")
    result = {}

    levels = {
        "nichts": "Nur einen Cloud-Ordner angeben – WŒRK übernimmt alles.",
        "wenig": "Zusätzlich ein paar Sätze zur aktuellen Situation eingeben.",
        "moderat": "Eigene Unterlagen, Gehaltswunsch, Foto, Ort etc. bereitstellen."
    }

    for key, text in levels.items():
        tk.Radiobutton(win, text=f"{key.capitalize()} – {text}", variable=var, value=key).pack(anchor="w")

    tk.Label(win, text="(Optional) Freitext bei 'Wenig':").pack(pady=(10, 0))
    freitext_entry = tk.Text(win, height=3, width=50)
    freitext_entry.pack()

    tk.Button(win, text="Weiter", command=proceed).pack(pady=10)

    win.mainloop()
    return result

# Beispielnutzung
if __name__ == "__main__":
    data = ask_contribution_level()
    print(data)
