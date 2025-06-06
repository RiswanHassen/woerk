import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os
from gpt_engine import generate_intro
from cover_letter_gen import generate_cover_letter
from input_level_select import ask_contribution_level

CONFIG_PATH = 'config/config.json'

def save_config(api_key, cv_path):
    os.makedirs('config', exist_ok=True)
    with open(CONFIG_PATH, 'w') as f:
        json.dump({'api_key': api_key, 'cv_path': cv_path}, f)

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as f:
            return json.load(f)
    return {}

def browse_cv(entry):
    path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if path:
        entry.delete(0, tk.END)
        entry.insert(0, path)

def run_generation():
    job = job_entry.get("1.0", tk.END).strip()
    api_key = api_key_entry.get().strip()
    cv_path = cv_entry.get().strip()
    style_level = style_var.get()

    if not job or not api_key or not cv_path:
        messagebox.showerror("Fehler", "Bitte alle Felder ausfüllen.")
        return

    save_config(api_key, cv_path)
    intro = generate_intro(job, api_key)
    letter = generate_cover_letter(job, cv_path, api_key, style_level)
    messagebox.showinfo("Fertig", f"Intro:\n{intro}\n\nAnschreiben:\n{letter}")

# Start mit Beitragsstufe
user_input = ask_contribution_level()

root = tk.Tk()
root.title("WŒRK – dein Jobschmied")

tk.Label(root, text="Traumjob (Freitext):").pack()
job_entry = tk.Text(root, height=4, width=50)
job_entry.pack()

tk.Label(root, text="OpenAI API Key:").pack()
api_key_entry = tk.Entry(root, width=50, show="*")
api_key_entry.pack()

tk.Label(root, text="Lebenslauf (PDF):").pack()
cv_entry = tk.Entry(root, width=40)
cv_entry.pack(side=tk.LEFT, padx=(10, 0))
tk.Button(root, text="Durchsuchen", command=lambda: browse_cv(cv_entry)).pack(side=tk.LEFT)

# Sprachlicher Stil
style_var = tk.StringVar(value="7")
tk.Label(root, text="Sprachlicher Stil (1 = direkt / 10 = diplomatisch):").pack(pady=(10, 0))
style_menu = tk.OptionMenu(root, style_var, *[str(i) for i in range(1, 11)])
style_menu.pack()

tk.Button(root, text="Generieren", command=run_generation).pack(pady=10)

root.mainloop()
