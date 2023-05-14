import csv
import matplotlib.pyplot as plt
import tkinter as tk
import datetime as dt
import tkinter.colorchooser

filename = 'database.csv'

def main():
    
    #ファイルをリスト化
    array = readfile(filename)
    #処理の内容
    process = mainMenu(array)
    
    

def readfile(filename):    
	print('読込中')
	with open(filename, 'r', newline='', encoding='shift-jis') as csvfile:
		#CSVを読み込む
		csvreader = csv.reader(csvfile)
		#SBVをリスト化
		array = list(csvreader)
		
		print('読込完了')
		return array


def writefile(filename, array):
    with open(filename, 'w', newline='', encoding='shift-jis') as csvfile:
        csvwriter = csv.writer(csvfile)
        try:
            print('書き込み中')
            csvwriter.writerows(array)
        finally:
            print('書き込み終了')

def mainMenu(array):
    print('書き込み画面')
    mainroot = tk.Tk()
    mainroot.geometry('750x500')
    mainroot.title('メインメニュー')
    def breakPane():
        exit()
    def createPane():
        mainroot.destroy()
    break_btn = tk.Button(mainroot, text='ソフトを終了', command=breakPane)
    break_btn.place(x=380, y=450)

    write_btn = tk.Button(mainroot, text='データを入力', command=createPane)
    write_btn.place(x=280, y=450)

    
    mainroot.mainloop()
    inputfile(array)
    



def inputfile(array):
    root = tk.Tk()
    root.geometry('580x200')
    root.title('予定追加画面')

    def ok():
        root.planTitle = title.get()
        root.planPriority =priority.get()

        root.startYear = sYear.get()
        root.startMonth = sMonth.get()
        root.startDay = sDay.get()
        root.startTime = sTime.get()
        root.startMin = sMin.get()

        root.endYear = eYear.get()
        root.endMonth = eMonth.get()
        root.endDay = eDay.get()
        root.endTime = eTime.get()
        root.endMin = eMin.get()

        root.destroy()

    titlelabel = tk.Label(text='予定の名前')
    titlelabel.place(x=10, y=40)

    plabel = tk.Label(text='優先度')
    plabel.place(x=210, y=40)

    startlabel = tk.Label(text='開始')
    startlabel.place(x=10, y=70)

    endlabel = tk.Label(text='終了')
    endlabel.place(x=10, y=100)

    yearlabel = tk.Label(text='年')
    yearlabel.place(x=115, y=70)

    monthlabel = tk.Label(text='月')
    monthlabel.place(x=210, y=70)

    daylabel = tk.Label(text='日')
    daylabel.place(x=305, y=70)

    timelabel = tk.Label(text='時')
    timelabel.place(x=400, y=70)

    minlabel = tk.Label(text='分')
    minlabel.place(x=495, y=70)

    yearlabel2 = tk.Label(text='年')
    yearlabel2.place(x=115, y=100)

    monthlabel2 = tk.Label(text='月')
    monthlabel2.place(x=210, y=100)

    daylabel2 = tk.Label(text='日')
    daylabel2.place(x=305, y=100)

    timelabel2 = tk.Label(text='時')
    timelabel2.place(x=400, y=100)

    minlabel2 = tk.Label(text='分')
    minlabel2.place(x=495, y=100)

    # 年月日時分テキストボックス
    title = tk.Entry(width=20)
    title.place(x=80, y=40)

    priority = tk.Entry(width=20)
    priority.place(x=260, y=40)

    sYear = tk.Entry(width=10)
    sYear.place(x=45, y=70)

    sMonth = tk.Entry(width=10)
    sMonth.place(x=140, y=70)

    sDay = tk.Entry(width=10)
    sDay.place(x=235, y=70)

    sTime = tk.Entry(width=10)
    sTime.place(x=330, y=70)

    sMin = tk.Entry(width=10)
    sMin.place(x=425, y=70)

    eYear = tk.Entry(width=10)
    eYear.place(x=45, y=100)

    eMonth = tk.Entry(width=10)
    eMonth.place(x=140, y=100)

    eDay = tk.Entry(width=10)
    eDay.place(x=235, y=100)

    eTime = tk.Entry(width=10)
    eTime.place(x=330, y=100)
    
    eMin = tk.Entry(width=10)
    eMin.place(x=425, y=100)

    # OKボタン
    ok_btn = tk.Button(root, text='入力完了', command=ok)
    ok_btn.place(x=200, y=150)
    def breakPane():
        quit()
    break_btn = tk.Button(root, text='ソフトを閉じる', command=breakPane)
    break_btn.place(x=280, y=150)

    # カラーピッカー

    root.mainloop()

    # 入力された数値を日時に変換
    try:
        sumStartTime = str(dt.datetime(int(root.startYear),int(root.startMonth),int(root.startDay),int(root.startTime),int(root.startMin)))
        sumEndTime = str(dt.datetime(int(root.endYear),int(root.endMonth),int(root.endDay),int(root.endTime),int(root.endMin)))
        sumArray = [root.planTitle,sumStartTime,sumEndTime,int(root.planPriority)]
        array.append(sumArray)
    except:
        main()

    #ファイルを書き込み
    writefile(filename, array)
    
main()
print('終了')