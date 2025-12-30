from datetime import datetime 
from tkinter import Tk, messagebox

def writeFile(n,filename="need To Re-solve"):
    with open(filename,"a",encoding="utf-8") as f:
        now=str(datetime.now()).split(" ")[0]
        f.write(f'{n}번 다시풀기, 작성 날짜:{now}')


def pop(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    root = Tk()
    root.withdraw()  # 메인 창 숨기기
    messagebox.showinfo("다시 풀 문제", content)
    root.destroy()


def main():
    print("다시 풀 문제 넘버 입력>>",end="")
    while True:
        userinput=input()
        if userinput.isdigit():
            writeFile(userinput)
        else:
            if userinput=="pop":
                pop("need to Re-solve")
                

main()