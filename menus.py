#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
import arabic_reshaper

class Menu_S:
    def __init__(self):
        pass
        
    def Setting_S(self):
        pass
        
    def Help_S(self):
        pass

class Help:  
    def __init__(self):
        pass
              
    def About_S(self,*args):
        title1, lang1, =args
        about=Toplevel()
        if lang1=='Ar':
            title1=arabic_reshaper.reshape(title1)[::-1]
        about.title(title1)
        ScrWidth=about.winfo_screenwidth()
        ScrHeight=about.winfo_screenheight()
        about.geometry("350x200+"+str(int(ScrWidth*0.4))+"+"+str(int(ScrHeight*0.15)))
        about.resizable(0,0)  
        
        Lab_Dict={'En':"Hisseb v0.0.1 \n\nThis application is developped by 'alchimie',\n You are free to edit it and using \nfor personal or business. \n\n For more info:\n alchimierel@gmail.com \n"}
        try:
            text1=Lab_Dict[lang1]
        except Exception:
            text1= '0.0.1'+ arabic_reshaper.reshape(' حساب نسخة ')[::-1] +'\n alchimie '+arabic_reshaper.reshape('هذا التطبيق تم تطويره بواسطة' )[::-1] +'\n'+ arabic_reshaper.reshape('يمكنك استعماله أو تعديل لغرض شخصي أو تجاري')[::-1] + '\n\n' + arabic_reshaper.reshape('لمزيد من المعلومات التواصل على:')[::-1] + '\n alchimierel@gmail.com \n'
       
        Lab=Label(about, text=text1).pack()
        
        Bt=Button(about, text='Ok', command=about.destroy).pack()  
        
        about.mainloop()
        
