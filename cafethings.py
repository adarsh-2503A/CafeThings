from tkinter import *
from tkinter import filedialog,messagebox
from random import randint
from PIL import Image,ImageTk
import time
global u
import smtplib,ssl
u=1
a=Tk()
a.geometry("1440x750")
a.title("Cafe management")
a.resizable(0,0)
a.config(bg="#FFFFE4")
topframe=Frame(a,bd=10,relief=RIDGE,bg='#F0F0E6')
topframe.pack(side=TOP)#creates a box kind of frame at the centre of the top line
p=Label(topframe,text="THE GOTHIC CAFÉ",font=('Times New Roman',30,'bold'),bg='#F0F0FF',fg="black",bd=10,width=51)#in the first row and first column of topframe box
p.grid(row=0,column=0)
def Total():
    item11 = int(fishandchips.get()) * 170
    item12 = int(potatowedge.get()) * 140
    item13 = int(Applewoodsmokedpizza.get()) * 250
    item14 = int(NonVegAlfredoPenne.get()) * 160
    item15 = int(garlicbread.get()) * 70
    item16= int(Nonvegceasersalad.get()) * 120
    item17 = int(vegArrabiatapenne.get()) * 210
    item18 = int(NonVegManchowSoup.get()) * 140
    item19 = int(VegChilliBalls.get()) * 150
    o=item11+item12+item13+item14+item15+item16+item17+item18+item19
    costofStartersbox.delete(0, END)
    costofStartersbox.insert(0,str(o))
    item1 = int(Almondtea.get()) * 120
    item2 = int(Lemonandgingertea.get()) * 120
    item3 = int(Hotchocolate.get()) * 120
    item4 = int(Greentea.get()) * 120
    item5 = int(Expresso.get()) * 120
    item6 = int(Cappuccino.get()) * 120
    item7 = int(Cococola.get()) * 40
    item8 = int(Latte.get()) * 120
    item9 = int(Irishcoffee.get()) * 150
    l=item1 + item2 + item3 + item4 + item5 + item6 + item7 + item8 + item9
    costofdrinksbox.delete(0, END)
    costofdrinksbox.insert(0, str(l))
    item21 = int(Hotchocofudge.get()) * 145
    item22 = int(Deathbychocolate.get()) * 175
    item23 = int(NuttyDeathbychocolate.get()) * 195
    item24 = int(Candyland.get()) * 130
    item25 = int(cafefroppe.get()) *185
    item26 = int(Nutellabrownieblast.get()) * 185
    item27 = int(FerreroDelight.get()) * 210
    item28 = int(Blackcurrent.get()) * 75
    item29 = int(Kappi.get()) * 70
    p=item21+item22+item23+item24+item25+item26+item27+item28+item29
    costofDessertsbox.delete(0,END)
    costofDessertsbox.insert(0,str(p))
    t=l+p+o
    Subtotalbox.delete(0,END)
    Subtotalbox.insert(0, str(t))
    s=t*12/100
    Servicetaxbox.delete(0,END)
    Servicetaxbox.insert(0,str(s))
    f=t+s
    Totalcostbox.delete(0, END)
    Totalcostbox.insert(0,str(f))
def Receipt():
    global u
    Receiptframe.delete(1.0,END)
    l=randint(0,1000)
    billnumber='BILL'+str(' ')+str(l)
    date=time.strftime('%d-%m-%Y')
    Receiptframe.insert(END,f'Receipt ref: {billnumber}\t\t    {date}\n')
    Receiptframe.insert(END,"----------------------------------------------\n")
    Receiptframe.insert(END,f'Items\t\tcost of Items(RS)\n')
    Receiptframe.insert(END, "----------------------------------------------\n")
    Receiptframe.insert(END,f'Starters:\t\t{costofStartersbox.get()}\n')
    Receiptframe.insert(END,f'Drinks:\t\t{costofdrinksbox.get()}\n')
    Receiptframe.insert(END,f'Desserts:\t\t{costofDessertsbox.get()}\n')
    Receiptframe.insert(END,f'Sub Total:\t\t{Subtotalbox.get()}\n')
    Receiptframe.insert(END,f'Service tax:\t\t{Servicetaxbox.get()}\n')
    Receiptframe.insert(END,f'TOTAL:\t\t{Totalcostbox.get()}\n')
    Receiptframe.insert(END,f'\t\t TIME:{time.strftime("%I-%M-%p")}')
    u=Receiptframe.get("1.0",END)
def Save():
    p=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    bill=Receiptframe.get(1.0,END)
    p.write(bill)
    p.close()
    messagebox.showinfo('Information','Your Bill is saved Successfully')
def Send():
    global u
    def msg():
        number=o.get()
        auth='hw939XQ6FyRKLDEEptufOvuBMdPK6xyEznnLX7sWYKIrEEa63YNY4TCnWY8U'
        url='https://www.fast2sms.com/dev/bulk'
        parameters={
            'authorization':auth,
            'message':u,
            'numbers':number,
            'sender-id':'FSTSMS',
            'route':'p',
            'language':'english'
        }
        response=requests.get(url,params=parameters)
        dic=response.json()
        result=dic.get('return')
        if result==True:
            messagebox.showinfo('STATUS','Message sent successfully')
        else:
            messagebox.showinfo('STATUS','Something went wrong')
    def mailing():
        sender_add = 'adarshkanteti2503@gmail.com'  # storing the sender's mail id
        receiver_add = 'kantetiharibabu@gmail.com'  # storing the receiver's mail id
        password = 'hari@@@1003A'  # storing the password to log in
        # creating the SMTP server object by giving SMPT server address and port number
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.ehlo()  # setting the ESMTP protocol
        smtp_server.starttls()  # setting up to TLS connection
        smtp_server.ehlo()  # calling the ehlo() again as encryption happens on calling startttls()
        smtp_server.login(sender_add, password)  # logging into out email id
        msg_to_be_sent = '''
        Hello, receiver!
        Hope you are doing well.
        Welcome to PythonGeeks!
        '''
        # sending the mail by specifying the from and to address and the message
        smtp_server.sendmail(sender_add, receiver_add, msg_to_be_sent)
        print('Successfully the mail is sent')  # priting a message on sending the mail
        smtp_server.quit()
    j=Toplevel()
    j.title("Send BILL")
    topframe = Frame(j, bd=10, relief=RIDGE, bg='Light yellow')
    topframe.pack(side=TOP)
    p = Label(topframe, text="SEND BILL", font=('Times New Roman', 20, 'bold'), bg='orange', fg="black", bd=10,
              width=10)
    p.grid(row=0,column=0)
    photo = ImageTk.PhotoImage(Image.open('s6.jpeg').resize((170,130), Image.Resampling.LANCZOS))
    label = Label(j, image=photo,bg="lightpink")
    label.image = photo
    label.pack()
    k=Label(j,text="MOBILE NO",font=('Times New Roman', 18, 'bold'))
    k.pack()
    o=Entry(j,width=36,bg="lightblue")
    o.pack()
    r = Label(j, text='Bill', font=('Times New Roman', 18, 'bold underline'))
    r.pack()
    Bill=Text(j,font=('Times New Roman', 16, 'bold'),width=42,height=14,bg="lightblue")
    Bill.pack()
    send=Button(j,font=('Times New Roman', 18, 'bold'),text="SEND",bg="red",command=mailing)
    send.pack()
    Bill.insert(END,str(u))
    j.config(bg='Light pink')
    j.geometry('490x650+50+50')

def RESET():
    fishandchips.delete(0,END)
    fishandchips.insert(0, 0)
    potatowedge.delete(0,END)
    potatowedge.insert(0, 0)
    Applewoodsmokedpizza.delete(0,END)
    Applewoodsmokedpizza.insert(0, 0)
    NonVegAlfredoPenne.delete(0,END)
    NonVegAlfredoPenne.insert(0, 0)
    garlicbread.delete(0,END)
    garlicbread.insert(0, 0)
    Nonvegceasersalad.delete(0,END)
    Nonvegceasersalad.insert(0, 0)
    vegArrabiatapenne.delete(0,END)
    vegArrabiatapenne.insert(0, 0)
    NonVegManchowSoup.delete(0,END)
    NonVegManchowSoup.insert(0, 0)
    VegChilliBalls.delete(0,END)
    VegChilliBalls.insert(0, 0)
    Almondtea.delete(0,END)
    Almondtea.insert(0, 0)
    Lemonandgingertea.delete(0,END)
    Lemonandgingertea.insert(0, 0)
    Hotchocolate.delete(0,END)
    Hotchocolate.insert(0, 0)
    Greentea.delete(0,END)
    Greentea.insert(0, 0)
    Expresso.delete(0,END)
    Expresso.insert(0, 0)
    Cappuccino.delete(0,END)
    Cappuccino.insert(0, 0)
    Latte.delete(0,END)
    Latte.insert(0, 0)
    Irishcoffee.delete(0,END)
    Irishcoffee.insert(0, 0)
    Cococola.delete(0,END)
    Cococola.insert(0, 0)
    Hotchocofudge.delete(0,END)
    Hotchocofudge.insert(0, 0)
    Deathbychocolate.delete(0,END)
    Deathbychocolate.insert(0, 0)
    NuttyDeathbychocolate.delete(0,END)
    NuttyDeathbychocolate.insert(0, 0)
    Candyland.delete(0,END)
    Candyland.insert(0, 0)
    cafefroppe.delete(0,END)
    cafefroppe.insert(0, 0)
    Nutellabrownieblast.delete(0,END)
    Nutellabrownieblast.insert(0, 0)
    FerreroDelight.delete(0,END)
    FerreroDelight.insert(0, 0)
    Blackcurrent.delete(0,END)
    Blackcurrent.insert(0, 0)
    Kappi.delete(0,END)
    Kappi.insert(0, 0)
    costofStartersbox.delete(0,END)
    costofdrinksbox.delete(0, END)
    costofDessertsbox.delete(0, END)
    Subtotalbox.delete(0, END)
    Servicetaxbox.delete(0, END)
    Totalcostbox.delete(0, END)
    Receiptframe.delete(1.0, END)
#frames
menuframe=LabelFrame(a,bd=10,relief=RIDGE,text="MENU",font=('Times New Roman',19),labelanchor=N,width=750,height=690,bg="#FFFFE4")
menuframe.pack(side=LEFT)
startersframe=LabelFrame(menuframe,text="Starters",relief=RIDGE,bd=10,font=('Curlz MT',19),labelanchor=N)
startersframe.grid(row=0,column=0)
Drinksframe=LabelFrame(menuframe,text="Drinks",relief=RIDGE,bd=10,font=('Curlz MT',19),labelanchor=N)
Drinksframe.grid(row=0,column=1)
Dessertsframe=LabelFrame(menuframe,text="Sweet tooth",relief=RIDGE,bd=10,font=('Curlz MT',19),labelanchor=N)
Dessertsframe.grid(row=0,column=2)
Totalsframe=Frame(menuframe,bd=10,relief=RIDGE,pady=10)
Totalsframe.grid(row=1,column=0,columnspan=3)
Billingframe=Frame(a,bd=10,relief=RIDGE)
Billingframe.pack(side=RIGHT)
Calculator=LabelFrame(Billingframe,text="CALCULATOR",bd=10,font=('Times New Roman',19),relief=RIDGE,labelanchor=N,bg="#FFFFE4")
Calculator.grid(row=0,column=0)
Receiptframe=Text(Billingframe,bd=10,font=('Times New Roman',19),relief=RIDGE,width=31,height=8,bg="#FFFFE4")
Receiptframe.grid(row=1,column=0)
buttonframe=Frame(Billingframe,bd=10,relief=RIDGE)
buttonframe.grid(row=2,column=0)


#Lables( with Check buttuns)
Label(startersframe,text='Fish and chips',font=('Times New Roman',16)).grid(row=0,column=0,sticky=W)
Label(startersframe,text='Potato wedge',font=('Times New Roman',16)).grid(row=1,column=0,sticky=W)
Label(startersframe,text='Applewood smoked pizza',font=('Times New Roman',16)).grid(row=2,column=0,sticky=W)
Label(startersframe,text='Garlic bread',font=('Times New Roman',16)).grid(row=4,column=0,sticky=W)
Label(startersframe,text='Non Veg Alfredo Penne',font=('Times New Roman',16)).grid(row=3,column=0,sticky=W)
Label(startersframe,text='Veg Arrabiata Penne',font=('Times New Roman',16)).grid(row=6,column=0,sticky=W)
Label(startersframe,text='Non veg caesar salad',font=('Times New Roman',16)).grid(row=5,column=0,sticky=W)
Label(startersframe,text='Non Veg Manchow Soup',font=('Times New Roman',16)).grid(row=7,column=0,sticky=W)
Label(startersframe,text='Veg Chilli Balls',font=('Times New Roman',16)).grid(row=8,column=0,sticky=W)
Label(Drinksframe,text='Almond tea',font=('Times New Roman',16)).grid(row=0,column=0,sticky=W)
Label(Drinksframe,text='Lemon and ginger tea',font=('Times New Roman',16)).grid(row=1,column=0,sticky=W)
Label(Drinksframe,text='Hotchocolate',font=('Times New Roman',16)).grid(row=2,column=0,sticky=W)
Label(Drinksframe,text='Green tea',font=('Times New Roman',16)).grid(row=3,column=0,sticky=W)
Label(Drinksframe,text='Expresso',font=('Times New Roman',16)).grid(row=4,column=0,sticky=W)
Label(Drinksframe,text='Cappuccino',font=('Times New Roman',16)).grid(row=5,column=0,sticky=W)
Label(Drinksframe,text='Latte',font=('Times New Roman',16)).grid(row=6,column=0,sticky=W)
Label(Drinksframe,text='Irish coffee',font=('Times New Roman',16)).grid(row=7,column=0,sticky=W)
Label(Drinksframe,text='Coca-Cola',font=('Times New Roman',16)).grid(row=8,column=0,sticky=W)
Label(Dessertsframe,text='Hot choco fudge',font=('Times New Roman',16)).grid(row=0,column=0,sticky=W)
Label(Dessertsframe,text='Death by chocolate',font=('Times New Roman',16)).grid(row=1,column=0,sticky=W)
Label(Dessertsframe,text='Nutty Death by chocolate',font=('Times New Roman',16)).grid(row=2,column=0,sticky=W)
Label(Dessertsframe,text='Candy land',font=('Times New Roman',16)).grid(row=3,column=0,sticky=W)
Label(Dessertsframe,text='café Froppe',font=('Times New Roman',16)).grid(row=4,column=0,sticky=W)
Label(Dessertsframe,text='Nutella brownie blast',font=('Times New Roman',16)).grid(row=5,column=0,sticky=W)
Label(Dessertsframe,text='Ferrero Delight',font=('Times New Roman',16)).grid(row=6,column=0,sticky=W)
Label(Dessertsframe,text='Black current',font=('Times New Roman',16)).grid(row=7,column=0,sticky=W)
Label(Dessertsframe,text='Kappi',font=('Times New Roman',16)).grid(row=8,column=0,sticky=W)
#label and entries without check buttons for totals
costofStarters=Label(Totalsframe,text='cost of Starters',font=('Times New Roman',16))
costofStarters.grid(row=0,column=0,sticky=W)
costofStartersbox=Entry(Totalsframe,width=14)
costofStartersbox.grid(row=0,column=1,padx=70)
costofdrinks=Label(Totalsframe,text='cost of drinks',font=('Times New Roman',16))
costofdrinks.grid(row=1,column=0,sticky=W)
costofdrinksbox=Entry(Totalsframe,width=14)
costofdrinksbox.grid(row=1,column=1,padx=70)
costofDesserts=Label(Totalsframe,text='cost of Desserts',font=('Times New Roman',16))
costofDesserts.grid(row=2,column=0,sticky=W)
costofDessertsbox=Entry(Totalsframe,width=14)
costofDessertsbox.grid(row=2,column=1,padx=70)
Subtotal=Label(Totalsframe,text='Sub Total',font=('Times New Roman',16))
Subtotal.grid(row=0,column=2,sticky=W)
Subtotalbox=Entry(Totalsframe,width=14)
Subtotalbox.grid(row=0,column=3,padx=70)
Servicetax=Label(Totalsframe,text='Service Tax',font=('Times New Roman',16))
Servicetax.grid(row=1,column=2,sticky=W)
Servicetaxbox=Entry(Totalsframe,width=14)
Servicetaxbox.grid(row=1,column=3,padx=70)
Totalcost=Label(Totalsframe,text='Total cost',font=('Times New Roman',16))
Totalcost.grid(row=2,column=2,sticky=W)
Totalcostbox=Entry(Totalsframe,width=14)
Totalcostbox.grid(row=2,column=3,padx=70)
#Entries
fishandchips=Entry(startersframe,bd=7,width=6,font=('Times New Roman',16))
fishandchips.insert(0,0)
fishandchips.grid(row=0,column=1)
potatowedge=Entry(startersframe,bd=7,width=6,font=('Times New Roman',16))
potatowedge.insert(0,0)
potatowedge.grid(row=1,column=1)
Applewoodsmokedpizza=Entry(startersframe,bd=7,width=6,font=('Times New Roman',16))
Applewoodsmokedpizza.insert(0,0)
Applewoodsmokedpizza.grid(row=2,column=1)
garlicbread=Entry(startersframe,bd=7,width=6,font=('Times New Roman',16))
garlicbread.insert(0,0)
garlicbread.grid(row=4,column=1)
NonVegAlfredoPenne=Entry(startersframe,bd=7,width=6,font=('Times New Roman',16))
NonVegAlfredoPenne.insert(0,0)
NonVegAlfredoPenne.grid(row=3,column=1)
vegArrabiatapenne=Entry(startersframe,bd=7,width=6,font=('Times New Roman',16))
vegArrabiatapenne.insert(0,0)
vegArrabiatapenne.grid(row=6,column=1)
Nonvegceasersalad=Entry(startersframe,bd=7,width=6,font=('Times New Roman',16))
Nonvegceasersalad.insert(0,0)
Nonvegceasersalad.grid(row=5,column=1)
NonVegManchowSoup=Entry(startersframe,bd=7,width=6,font=('Times New Roman',16))
NonVegManchowSoup.insert(0,0)
NonVegManchowSoup.grid(row=7,column=1)
VegChilliBalls=Entry(startersframe,bd=7,width=6,font=('Times New Roman',16))
VegChilliBalls.insert(0,0)
VegChilliBalls.grid(row=8,column=1)
Almondtea=Entry(Drinksframe,bd=7,width=6,font=('Times New Roman',16))
Almondtea.insert(0,0)
Almondtea.grid(row=0,column=1)
Lemonandgingertea=Entry(Drinksframe,bd=7,width=6,font=('Times New Roman',16))
Lemonandgingertea.insert(0,0)
Lemonandgingertea.grid(row=1,column=1)
Hotchocolate=Entry(Drinksframe,bd=7,width=6,font=('Times New Roman',16))
Hotchocolate.insert(0,0)
Hotchocolate.grid(row=2,column=1)
Greentea=Entry(Drinksframe,bd=7,width=6,font=('Times New Roman',16))
Greentea.insert(0,0)
Greentea.grid(row=3,column=1)
Expresso=Entry(Drinksframe,bd=7,width=6,font=('Times New Roman',16))
Expresso.insert(0,0)
Expresso.grid(row=4,column=1)
Cappuccino=Entry(Drinksframe,bd=7,width=6,font=('Times New Roman',16))
Cappuccino.insert(0,0)
Cappuccino.grid(row=5,column=1)
Latte=Entry(Drinksframe,bd=7,width=6,font=('Times New Roman',16))
Latte.insert(0,0)
Latte.grid(row=6,column=1)
Irishcoffee=Entry(Drinksframe,bd=7,width=6,font=('Times New Roman',16))
Irishcoffee.insert(0,0)
Irishcoffee.grid(row=7,column=1)
Cococola=Entry(Drinksframe,font=('Times New Roman',16),bd=7,width=6)
Cococola.insert(0,0)
Cococola.grid(row=8,column=1)
Hotchocofudge=Entry(Dessertsframe,font=('Times New Roman',16),bd=7,width=6)
Hotchocofudge.insert(0,0)
Hotchocofudge.grid(row=0,column=1)
Deathbychocolate=Entry(Dessertsframe,font=('Times New Roman',16),bd=7,width=6)
Deathbychocolate.insert(0,0)
Deathbychocolate.grid(row=1,column=1)
NuttyDeathbychocolate=Entry(Dessertsframe,font=('Times New Roman',16),bd=7,width=6)
NuttyDeathbychocolate.insert(0,0)
NuttyDeathbychocolate.grid(row=2,column=1)
Candyland=Entry(Dessertsframe,font=('Times New Roman',16),bd=7,width=6)
Candyland.insert(0,0)
Candyland.grid(row=3,column=1)
cafefroppe=Entry(Dessertsframe,font=('Times New Roman',16),bd=7,width=6)
cafefroppe.insert(0,0)
cafefroppe.grid(row=4,column=1)
Nutellabrownieblast=Entry(Dessertsframe,font=('Times New Roman',16),bd=7,width=6)
Nutellabrownieblast.insert(0,0)
Nutellabrownieblast.grid(row=5,column=1)
FerreroDelight=Entry(Dessertsframe,font=('Times New Roman',16),bd=7,width=6)
FerreroDelight.insert(0,0)
FerreroDelight.grid(row=6,column=1)
Blackcurrent=Entry(Dessertsframe,font=('Times New Roman',16),bd=7,width=6)
Blackcurrent.insert(0,0)
Blackcurrent.grid(row=7,column=1)
Kappi=Entry(Dessertsframe,font=('Times New Roman',16),bd=7,width=6)
Kappi.insert(0,0)
Kappi.grid(row=8,column=1)
#calculator
p = Entry(Calculator, width=27, borderwidth=5,justify=RIGHT,font=(20))
p.grid(row=0, column=0, columnspan=4, padx=30)
def numbers(num):
    current = p.get()
    p.delete(0, END)
    p.insert(0, str(current) + str(num))
def delete():
    num = p.get()
    p.delete(0, END)
    num = num[0:-1]
    p.insert(0, str(num))
def add():
    num = p.get()
    p.delete(0, END)
    p.insert(0,str(num)+str("+"))
def sub():
    num = p.get()
    p.delete(0, END)
    p.insert(0,str(num)+str("-"))
def mul():
    num = p.get()
    p.delete(0, END)
    p.insert(0,str(num)+str("*"))
def div():
    num = p.get()
    p.delete(0, END)
    p.insert(0,str(num)+str("/"))
def dot():
    current = p.get()
    p.delete(0, END)
    p.insert(0, str(current) + str('.'))
def clr():
    p.delete(0,END)
def leftbrac():
    current = p.get()
    p.delete(0, END)
    p.insert(0, str(current) + str('('))
def rightbrac():
    current = p.get()
    p.delete(0, END)
    p.insert(0, str(current) + str(')'))
def equals():
    o = p.get()
    p.delete(0, END)
    fa = eval(o)
    p.insert(0, fa)
butt9= Button(Calculator, text=9,padx=40, pady=12,bg="white",fg="brown",command=lambda : numbers(9)).grid(row=1,column=0)
butt8= Button(Calculator,text=8,padx=40, pady=12,bg="white",fg="brown",command=lambda : numbers(8)).grid(row=1,column=1)
butt7= Button(Calculator,text=7,padx=40, pady=12,bg="white",fg="brown",command=lambda : numbers(7)).grid(row=1,column=2)
butt6= Button(Calculator,text=6,padx=40, pady=12,bg="white",fg="brown",command=lambda : numbers(6)).grid(row=2,column=0)
butt5= Button(Calculator,text=5,padx=40, pady=12,bg="white",fg="brown",command=lambda : numbers(5)).grid(row=2,column=1)
butt4= Button(Calculator,text=4,padx=40, pady=12,bg="white",fg="brown",command=lambda : numbers(4)).grid(row=2,column=2)
butt3= Button(Calculator,text=3,padx=40, pady=12,bg="white",fg="brown",command=lambda : numbers(3)).grid(row=3,column=0)
butt2= Button(Calculator,text=2,padx=40, pady=12,bg="white",fg="brown",command=lambda : numbers(2)).grid(row=3,column=1)
butt1= Button(Calculator,text=1,padx=40, pady=12,bg="white",fg="brown",command=lambda : numbers(1)).grid(row=3,column=2)
butt0= Button(Calculator,text=0,padx=40, pady=12,bg="white",fg="brown",command=lambda : numbers(0)).grid(row=4,column=1)
buttdel= Button(Calculator,text='DEL',padx=33, pady=12,bg="white",fg="brown",command=delete).grid(row=4,column=2)
buttadd= Button(Calculator, text="+",padx=36, pady=12,bg="white",fg="brown",command=add).grid(row=1,column=3)
buttsub= Button(Calculator, text="-",padx=39, pady=12,bg="white",fg="brown",command=sub).grid(row=2,column=3)
buttmul= Button(Calculator, text="*",padx=39, pady=12,bg="white",fg="brown",command=mul).grid(row=3,column=3)
buttdiv= Button(Calculator, text="/",padx=37, pady=12,bg="white",fg="brown",command=div).grid(row=4,column=3)
buttclear=Button(Calculator, text="Clear",padx=29, pady=12,bg="white",fg="brown",command=clr).grid(row=4,column=0)
buttdot=Button(Calculator, text=".",padx=41, pady=12,bg="white",fg="brown",command=dot).grid(row=5,column=0)
buttlefbrac=Button(Calculator, text="(",padx=41, pady=12,bg="white",fg="brown",command=leftbrac).grid(row=5,column=1)
buttrightbrac=Button(Calculator, text=")",padx=40, pady=12,bg="white",fg="brown",command=rightbrac).grid(row=5,column=2)
buttequals=Button(Calculator, text="=",padx=37, pady=12,bg="white",fg="brown",command=equals).grid(row=5,column=3)
butttotal=Button(buttonframe,text="Total",font=('Times New Roman',16),bd=3,command=Total)
butttotal.grid(row=0,column=0)
buttReciept=Button(buttonframe,text="Receipt",font=('Times New Roman',16),bd=3,command=Receipt)
buttReciept.grid(row=0,column=1)
buttSave=Button(buttonframe,text="Save",font=('Times New Roman',16),bd=3,command=Save)
buttSave.grid(row=0,column=2)
buttSend=Button(buttonframe,text="Send",font=('Times New Roman',16),bd=3,command=Send)
buttSend.grid(row=0,column=3)
buttReset=Button(buttonframe,text="Reset",font=('Times New Roman',16),bd=3,command=RESET)
buttReset.grid(row=0,column=4)
a.mainloop()

