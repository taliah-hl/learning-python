#this is to try build a user database using dictionary

from tkinter import *
win = Tk()
win.title('User Data Bank')
win.geometry('400x300')
win.resizable(0,0)


userdata = {}

userdata[1] = ( (0, 'name', 'Example'), (1, 'username', 'example_user1'), \
                (2, 'password', 'abc123'), (3, 'tel', '91234567'))

#試下打中文字
def getentry():
      u_id = str(id_en.get())
      u_name = str(name_en.get())
      u_username = str(username_en.get())
      u_pw = str(pw_en.get())
      u_tel = str(tel_en.get())
      info_tuple = (u_id, u_name, u_username, u_pw, u_tel)
      print(info_tuple)
      return store_entry(*info_tuple)

def store_entry(u_id, u_name, u_username, u_pw, u_tel):
      if u_id == '':
            raise ValueError('user id missing!')
      elif u_id in userdata:
            raise ValueError('user id duplicated!')
      else:
            userdata[u_id] = ( (0, 'name', u_name), \
                               (1, 'username', u_username), \
                               (2, 'password', u_pw), (3, 'tel', u_tel))
            print(userdata)

def print_msg(b):
      ''' b is boolean, 0 = fail, 1 = sucess  '''
      ''' need to think how to do!!! '''
      


      
topfram = Frame(win)
topfram.pack(side = TOP)

leftfr = Frame(topfram, width=80) #left frame
leftfr.pack(side = LEFT)
id_label = Label(leftfr, text = 'User ID' ,font=('Apercu light', 14), justify = LEFT)
id_label.pack(side = TOP)
name_label = Label(leftfr, text = 'Name'  ,font=('Apercu light', 14), justify = LEFT)
name_label.pack(side = TOP)
username_label = Label(leftfr, text = 'User name' ,font=('Apercu light', 14), justify = LEFT)
username_label.pack(side = TOP)
pw_label = Label(leftfr, text = 'Password' ,font=('Apercu light', 14), justify = LEFT)
pw_label.pack(side = TOP)
tel_label = Label(leftfr, text = 'Tel' ,font=('Apercu light', 14), justify = LEFT)
tel_label.pack(side = TOP)


rifr = Frame(topfram) #right frame
rifr.pack(side = LEFT)
id_en = Entry(rifr ,font=('Apercu light', 14))
id_en.pack(side = TOP)
name_en = Entry(rifr ,font=('Apercu light', 14))
name_en.pack(side = TOP)
username_en = Entry(rifr ,font=('Apercu light', 14))
username_en.pack(side = TOP)
pw_en = Entry(rifr, show='*' ,font=('Apercu light', 14))
pw_en.pack(side = TOP)
tel_en = Entry(rifr ,font=('Apercu light', 14))
tel_en.pack(side = TOP)

bot_fram = Frame(win)
bot_fram.pack(side = TOP)
store_btn = Button(bot_fram, text = 'Store', command = getentry)
store_btn.pack(side = TOP)






win.mainloop()



