import tkinter as tk
import os
#Root
root = tk.Tk()
root.title("Compendium")
root.geometry('240x240')
#Label
label = tk.Label(root, text="Start", fg="grey", font=("Arial", 16,))
label.pack()
#Text
text = tk.Text(root, width=100, height=20, fg="lightgreen")
text.pack()
text.config(bg="grey")
#Content
content = text.get("1.0", tk.END)
#Save
save_file = "text.txt"
if os.path.exists(save_file):
    with open(save_file, "r", encoding="utf-8") as f:
        text.insert("1.0", f.read())
def close():
    with open(save_file, "w", encoding="utf-8") as f:
        f.write(text.get("1.0", "end-1c"))
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close)
#End
root.mainloop()
