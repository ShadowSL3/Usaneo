import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

app = tk.Tk()
app.title("OPIO SFX")
app.geometry(512+300)
def select_sfx():
    filetypes = (('Wav Files', '*.wav'), ('Mp3 Files', '*.mp3'))
    filename = filedialog.askopenfilename(title="Sfx Importer", initial_dir="/", filetypes=filetypes)
    if not filetypes == filename: 
       print("Ops Your file Not Wav or Mp3")
sfx_button = ttk.Button(app, text="Insert Sfx", command=select_sfx)
sfx_button.pack(expand=False)


app.mainloop()