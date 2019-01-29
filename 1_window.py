# ブロック崩し
from tkinter import *

# ウィンドウの作成
win = Tk()
win.title("window")
cv = Canvas(win, width = 600, height = 400)
cv.pack()

# ゲームループ
def game_loop():
    win.after(50, game_loop)

game_loop()
win.mainloop() # ゲームウィンドウを表示