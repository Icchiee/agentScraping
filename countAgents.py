#!/usr/bin/env python
# coding: utf-8

# ## GUI設計

# In[65]:


import pandas as pd
import tabula
import PyPDF2
import csv
import tkinter as tk
from tkinter import messagebox
#画面全体
main_win = tk.Tk()
main_win.title("認定支援機関カウントツール")
main_win.geometry("500x200")

#フレーム
frame = tk.Frame(main_win)
frame.grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=10)

#ウィジェットの作成
label = tk.Label(frame, text='PDF名：')
entry = tk.Entry(frame)
button_execute=tk.Button(text='実行' , command = lambda:click())

# 各種ウィジェットの設置
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button_execute.grid(row=1, column=1)

#実行
def click():
    #値の取得＆データフレームとしての読み込み
    pdfName = entry.get()
    pdf_file = r"C:\Users\to0sh\Documents\jigyosaikoutiku\saitaku"+"\\"+entry.get()+".pdf"
    dfs = tabula.read_pdf(pdf_file, encoding='cp932', pages="all", multiple_tables=True)
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    #データフレームの用意＆格納
    dfAll_list=[]
    dfAll=pd.DataFrame(dfAll_list)
    for i in range(len(dfs)):
        if i%2 == 1:
           dfAll=pd.concat([dfAll, dfs[i]])
    
    #認定支援機関の数え上げ
    agent_num = dfAll['認定支援機関名'].value_counts(dropna=False)
    with open("re_agent_num.csv", mode="w", encoding="shift-jis", errors="ignore") as f:
    # ここでデータフレームを開いたファイルにcsvで書き込む
        agent_num.to_csv(f)
    
    entry.delete(0, tk.END) #テキストボックス内の文字を消し去る
    
    #完了後のコメント
    label = tk.Label(text="csv化できました！")
    label.place(x=20, y=50)
    
     

main_win.mainloop()



get_ipython().system('jupyter nbconvert --to python countAgents.ipynb')


# In[ ]:




