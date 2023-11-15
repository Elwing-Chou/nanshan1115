import pandas as pd
import tkinter as tk
import tkinter.filedialog as dialog

def func():
    chosen = dialog.askopenfilenames()
    csvlist = []
    for c in chosen:
        csv = pd.read_csv(c, encoding="utf-8")
        csvlist.append(csv)
    combine = pd.concat(csvlist, axis=0)
    combine.to_csv("combine.csv", encoding="utf-8")
    # 第二時間的設置
    l["text"] = "合併完成"

window = tk.Tk()
window.geometry("500x500+250+100")
# 元件(父元件)
b = tk.Button(window, text="開始處理", command=func)
# 排版(pack)
b.pack()
# 第一時間的設置
l = tk.Label(window, text="?????")
l.pack()
window.mainloop()