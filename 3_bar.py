# ブロック崩し
from tkinter import *

 # ボールを表す辞書型データ --- (*1)
ball = {
    "dirx": 15, # X方向のボールの速さ
    "diry": -15,  # Y方向のボールの速さ
    "x": 350, # ボールの位置
    "y": 300,
    "w": 10, # ボールの幅
}

# ウィンドウの作成 --- (*2)
win = Tk()
win.title("ball")
cw = 1000
ch = 600
cv = Canvas(win, width = cw, height = ch)
cv.pack()

# 画面を描画する --- (*3)
def draw_objects():
    cv.delete('all') # 既存の描画を破棄
    # ボールを描画
    cv.create_oval(
        ball["x"] - ball["w"], ball["y"] - ball["w"],
        ball["x"] + ball["w"], ball["y"] + ball["w"],
        fill="blue")

# ボールの移動 --- (*4)
def move_ball():
    # 仮の変数に移動後の値を記録
    bx = ball["x"] + ball["dirx"]
    by = ball["y"] + ball["diry"]
    # 上左右の壁に当たった？
    if bx < 0 or bx > cw: ball["dirx"] *= -1
    if by < 0 or by > ch: ball["diry"] *= -1
    # 移動内容を反映
    if 0 <= bx <= cw: ball["x"] = bx
    if 0 <= by <= ch: ball["y"] = by

# ゲームループ --- (*5)
def game_loop():
    draw_objects()
    move_ball()
    win.after(50, game_loop)

game_loop()
win.mainloop() # ゲームウィンドウを表示