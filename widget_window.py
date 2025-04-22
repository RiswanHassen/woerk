
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time

def simulate_processing(callback=None):
    def run():
        for i in range(101):
            progress_var.set(i)
            percent_label.config(text=f"{i}%")
            time.sleep(0.05)
        if callback:
            callback()
        root.destroy()

    root = tk.Toplevel()
    root.title("WŒRK arbeitet...")
    root.geometry("200x100")
    root.attributes("-topmost", True)
    root.resizable(False, False)

    def close_widget():
        root.destroy()

    tk.Label(root, text="Verarbeitung läuft...", font=("Segoe UI", 10)).pack(pady=5)
    percent_label = tk.Label(root, text="0%", font=("Segoe UI", 12, "bold"))
    percent_label.pack()

    progress_var = tk.IntVar()
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=150, mode="determinate", variable=progress_var)
    progress_bar.pack(pady=5)

    close_button = tk.Button(root, text="❌", command=close_widget)
    close_button.place(relx=1.0, x=-5, y=5, anchor="ne")

    threading.Thread(target=run, daemon=True).start()
    root.mainloop()

def show_done_popup():
    popup = tk.Tk()
    popup.withdraw()
    popup.after(100, lambda: messagebox.showinfo("WŒRK", "📁 Verarbeitung abgeschlossen."))
    popup.mainloop()

if __name__ == "__main__":
    simulate_processing(callback=show_done_popup)
