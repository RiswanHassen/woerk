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
