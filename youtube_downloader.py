import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    if url:
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download()
            messagebox.showinfo("Sukces", "Film został pobrany pomyślnie!")
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił błąd: {e}")
    else:
        messagebox.showwarning("Uwaga", "Proszę podać link do filmu.")

app = tk.Tk()
app.title("YouTube Downloader")

tk.Label(app, text="Wklej link do YouTube:").pack(pady=10)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(app, text="Pobierz", command=download_video)
download_button.pack(pady=20)

app.mainloop()
