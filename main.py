
import tkinter as tk

def count_items():
    raw = entry.get().strip()
    if not raw:
        result.set("0")
        return

    items = [i.strip() for i in raw.split(",") if i.strip()]
    result.set(str(len(items)))

root = tk.Tk()
root.title("Item Counter")

tk.Label(root, text="Items (comma separated):").pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(padx=10)

tk.Button(root, text="Count", command=count_items).pack(pady=5)

result = tk.StringVar(value="0")
tk.Label(root, textvariable=result, font=("Arial", 16)).pack(pady=10)

root.mainloop()