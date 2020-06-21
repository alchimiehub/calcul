#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
import arabic_reshaper
import menus 



class Language:
    def __init__(self):
        pass
    def Languages(self, *args):
        Lan, = args
        
        En={'title':'Hisseb Calculator','File':'File', 'Quit':'Quit', 'Edit':'Edit', 'Copy Result':'Copy Result', 'Setting':'Setting','View':'View','Language':'Language', 'Help':'Help', 'About':'About'}

        Ar={'title':'حاسبة حساب', 'File':'ملف', 'Quit':'خروج' , 'Edit':'تحرير', 'Copy Result':'نسخ النتيجة' , 'Setting':'إعدادات' ,'View':'عرض','Language':'اللغة', 'Help':'مساعدة', 'About':'حول'}
        
        Fr={'title':'Hisseb Calculatrice','File':'Fichier', 'Quit':'Quite', 'Edit':'Edition', 'Copy Result':'Copie résultat', 'Setting':'Réglage','View':'Affichage','Language':'Langue', 'Help':'Aide', 'About':'A propos'}
        
        return vars()[Lan]

class GuiCalc:
    def __init__(self, root):
        
        
        self.root = root
        s_l=open("S_L", "r")
        self.logha=s_l.read(); s_l.close()
        lanG=Language()
        self.lang=lanG.Languages(self.logha)
        self.root.title(self.lang['title'])
        if self.logha=='Ar':
            for wrd in self.lang.keys():
                self.lang[wrd]=(arabic_reshaper.reshape(self.lang[wrd]))[::-1]
                   
        ScrWidth=self.root.winfo_screenwidth()
        ScrHeight=self.root.winfo_screenheight()
        self.root.geometry("300x350+"+str(int(ScrWidth*0.35))+"+"+str(int(ScrHeight*0.1)))
        self.root.resizable(0,0)       

        self.fram1 = Frame(self.root,width=287, height=70,highlightbackground="#87919B", highlightthickness=0)
        self.fram1.place(x=10, y=30)
        
        self.fram2 = Frame(self.root,width=200, height=150,highlightbackground="#87919B", highlightthickness=0)
        self.fram2.place(x=10, y=120)
        self.CalcMenu()
        
    def rebooot(self):
        self.root.destroy()    
        
    def Langua(self, l):
        file = open('S_L', 'w')
        file.write(l); file.close()
        self.root.destroy()
        main()


        
    def CalcMenu(self):
        hlp = menus.Help()
        menubar = Menu(self.root)
        
        FileMenu = Menu(menubar, tearoff=0)
        FileMenu.add_command(label=self.lang['Quit'], command=self.root.destroy)
        menubar.add_cascade(label=self.lang['File'], menu=FileMenu)
        
        EditMenu = Menu(menubar, tearoff=0)
        EditMenu.add_command(label=self.lang['Copy Result'], command='')
        EditMenu.add_separator()
        EditMenu.add_command(label=self.lang['Setting'], command='')
        menubar.add_cascade(label=self.lang['Edit'], menu=EditMenu)
        
        ViewMenu = Menu(menubar, tearoff=0)
        LangMenu = Menu(ViewMenu)
        LangMenu.add_command(label='English' , command= lambda :self.Langua('En'))
        LangMenu.add_command(label=(arabic_reshaper.reshape('العربية'))[::-1], command= lambda :self.Langua('Ar'))
        LangMenu.add_command(label='Français', command= lambda :self.Langua('Fr'))
        ViewMenu.add_cascade(label=self.lang['Language'], menu=LangMenu)
        menubar.add_cascade(label=self.lang['View'], menu=ViewMenu)
        
        HelpMenu = Menu(menubar, tearoff=0)
        HelpMenu.add_command(label=self.lang['About'], command= lambda :hlp.About_S(self.lang['About'],self.logha))
        menubar.add_cascade(label=self.lang['Help'], menu=HelpMenu)
        
        self.root.config(menu=menubar)
        
        
    def Calculat(self):       
        self.Lst=[]
        def OnClear():
            self.Lst=[]; self.Entvar.set('')
            self.Text1.configure(state='normal'); self.Text1.delete('1.0','end'); self.Text1.configure(state='disabled')
            
        def OnCalc(k):           
            if (str(k).isdigit()) | (k==' .'):
                k=str(k).replace(' ','')
                self.Entvar.set(self.Entvar.get()+str(k))
            
            else:
                if float(self.Entvar.get()).is_integer(): Nbr = int(float(self.Entvar.get()))
                else: Nbr = float(self.Entvar.get())
                self.Lst.append(self.Entvar.get())                
                self.Text1.configure(state='normal'); self.Text1.insert('end',' '+ str(Nbr)+' '+str(k))
                self.Text1.configure(state='disabled')
                self.EntG.delete(0, 'end')
                if k=='=':
                    st=''
                    for l in self.Lst:
                        if l=='x': l='*'
                        st+=l
                    Result=str(eval(st))
                    self.Lst=[]
                    if float(Result).is_integer(): Result = int(float(Result))
                    
                    self.Entvar.set(Result)
                else: self.Lst.append(k)
                      

        self.Entvar=StringVar(self.fram1)

        self.Text1 = Text(self.fram1,state='disabled',font="Arial 8 bold", width=45, height =1)
        self.Text1.place(x=0, y=5)

        self.EntG = Entry(self.fram1, textvariable=self.Entvar, font="Arial 20 bold", width=18)
        self.EntG.place(x=0, y=25)
        bt=['1','2','3',' /','4','5','6','x','7','8','9',' -',' .','0','=','+']
        for i in range(16):            
            b=Button(self.fram2, text = str(bt[i]), font="Arial 10 bold", padx=20, pady=13,command = lambda d=bt[i]:OnCalc(d))
            b.grid(row=i//4, column =i%4)
            
        b=Button(self.fram2, text = 'C', font="Arial 10 bold", padx=20, pady=36,command = OnClear)
        b.grid(row=0, column =4, rowspan=2)
            
        

class main:
    def __init__(self):
        calc = Tk()
        Ob=GuiCalc(calc)
        Ob.Calculat()
        calc.mainloop()           

    
if __name__ == '__main__':
    main()


