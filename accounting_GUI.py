import tkinter as tk
from turtle import width

#balance= 1000

class Record:
    
    
    def __init__(self, num, date, cat, des, amount):
        self._date=date
        self._cat=cat
        self._des=str(des)
        self._amt=int(amount)
        self._item_num = int(num)
        

    @property
    def cat(self):
        return self._cat
    @property
    def des(self):
        return self._des
    @property
    def amt(self):
        return self._amt
    @property
    def date(self):
        return self._date
    @property
    def item_num(self):
        return self._item_num
    

class Records:
    _records=[]
    _balance = 10
    
    def __init__(self):
        
        try:
            with open('records.txt', 'r') as fin:
                content=fin.readlines()
                self._initial_money=int(content[0])

                for i in range(1, len(content)):
                    content[i]=content[i].split(' ')
                    self._records.append(Record(i, content[i][0], content[i][1],
                     content[i][2], content[i][3]))
                    
                print("Welcome back!")
                
        except:
            #mode=0
            self._initial_money = 1000
        self._balance=self._initial_money
    def add(self, item):
        self._records.append(item)

    def delete(self, name):
        for i in self.records:
            if i.des == name:
                self._records.remove(i)
    @property
    def total_item(self):
        return len(self._records)

    def balance(self):
        self._balance=self._initial_money
        for i in self._records:
            self._balance += i.amt
        return self._balance
    @property
    def records(self):
        return self._records;
    def save(self):
        with open('records.txt','w') as fin:
            fin.write(f"{self._initial_money}\n")
            for i in self._records:
                fin.write(f"{i.date} {i.cat} {i.des} {i.amt}\n")

txn = Records()

def add_record():
    '''get record and get'''
    en_date = str(date_box.get())
    try:
        assert en_date[2]==en_date[5]=='/'
        assert len(en_date) == 10
    except:
        print("Wrong Date Format!")
    else:
        print(cat_box.curselection())
        en_cat = cat_list[cat_box.curselection()[0]]
        en_des = str(des_box.get())
        en_amt = str(amt_box.get())
        txn.add(Record(txn.total_item +1, en_date, en_cat, en_des, en_amt))
        update_balance()

def update_balance():
    balance_var.set(f"You now have {txn.balance()} dollar.")

def search():
    while sres_box.size() >0:
        sres_box.delete(0)

    tofind =to_search_list[search_box.curselection()[0]]
    if tofind=='all':
        for i in txn.records:
            sres_box.insert(tk.END, 
            f"{i.item_num:2d}. {i.date:12s}{i.cat:15s}{i.des:15s}{i.amt}")
    else:
        for i in txn.records:
            if i.cat == tofind:
                sres_box.insert(tk.END, 
                f"{i.item_num:2d}. {i.date:12s}{i.cat:15s}{i.des:15s}{i.amt}")
def del_rec():
    todel  =sres_box.get(sres_box.curselection()[0])
    sres_box.delete(sres_box.curselection()[0])
    todel_num=int(todel[0]+todel[1])
    for i in txn.records:
        if todel_num == i.item_num:
            txn.delete(i.des)
    update_balance()

def save():
    txn.save()

     

win = tk.Tk()
win.title('XYZ Brokerage Client search')
win.geometry('800x600')
win.resizable(0,0)
win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=1)
leftframe = tk.Frame(win, width=800)
rightframe = tk.Frame(win, width=800)

leftframe.grid(row=0, column=0, rowspan=2, sticky="NSEW")
rightframe.grid(row=0, column=1, rowspan=2, sticky="NSEW")

initMoney = f"If no file, Initial Money default as: $1000"
initMoney_label = tk.Label(leftframe, text=initMoney)
date_label = tk.Label(leftframe, text='Date (MM/DD/YYYY)')
date_box = tk.Entry(leftframe)
cat_label = tk.Label(leftframe, text='Category')
cat_box = tk.Listbox(leftframe)
des_label = tk.Label(leftframe, text='Description')
des_box = tk.Entry(leftframe)
amt_label = tk.Label(leftframe, text='Amount')
amt_box = tk.Entry(leftframe)

cat_list=['salary', 'meal', 'transportation', 'other expense']
for i in cat_list:  
    cat_box.insert(tk.END, i)


initMoney_label.pack()
date_label.pack()
date_box.pack()
cat_label.pack()
cat_box.pack()
des_label.pack()
des_box.pack()
amt_label.pack()
amt_box.pack()

add_btn = tk.Button(leftframe, text='Add a record',
command = add_record)

add_btn.pack()


to_search_list=['salary', 'meal', 'transportation', 'other expense', 'all']
search_label = tk.Label(rightframe, text='Search by Category')
search_box=tk.Listbox(rightframe)
for i in to_search_list:
    search_box.insert(tk.END, i)

search_btn = tk.Button(rightframe, command= search, text='Search')
search_res_label=tk.Label(rightframe, text='Search Result')
sres_box=tk.Listbox(rightframe)


balance_var = tk.StringVar(rightframe)
balance_var.set(f"You now have {txn.balance()} dollar.")
balance_label = tk.Label(rightframe, textvariable= balance_var)
del_btn = tk.Button(rightframe, text= 'Delete', command=del_rec)
save_btn = tk.Button(rightframe, text='Save', command= save)

search_label.pack()
search_box.pack()
search_btn.pack()
search_res_label.pack()
sres_box.pack(fill='x',expand=1)
del_btn.pack()
balance_label.pack()
save_btn.pack()
win.mainloop()
