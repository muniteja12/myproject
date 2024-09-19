from tkinter import *
from random import *
from time import *
from math import *
def onKeyDown(event):
    global lastkey, appOn
    lastkey = event.keysym
    if lastkey == "Escape" : appOn = False
#--Allow for a graceful exit
def onShutdown():
    global appOn
    appOn = False
win = Tk()
win.title('Chaos Spinner')         
win.geometry("640x480")             
win.state('zoomed')                
win.config(bg="#000000")          
win.update()                        
winwid = win.winfo_width()         
winhei = win.winfo_height()
canv = Canvas(win, width = winwid, height = winhei, bg="black")  
canv.pack()                       
win.bind("<KeyPress>", onKeyDown) 
win.protocol("WM_DELETE_WINDOW",onShutdown)  
 
appOn = True                      
while appOn:                        
    lastkey = ""                   
    amount = randint(4,16)          
    total = 0                       
    angle = []                     
    dist = []
    rate = []
    x = []
    y = []
    angrng = randint(1,12) * 15     
    for i in range(0,amount):      
        angle.append(randint(-angrng,angrng)) 
        dist.append(randint(16,round((winhei/1.1)/amount)))  
        total = total + dist[i]     
        rate.append(randint(-10,10) * 2)  
    for i in range(0,amount):      
        rndpos = randint(0,amount-1) 
        dist[rndpos] = dist[rndpos] + (((winhei / 1.1) - total) // amount)
    x.append(winwid // 2)           
    y.append(winhei // 2)
    for i in range(1,amount):       
        x.append(round(x[i-1]+dist[i]*cos(radians(angle[i]))))
        y.append(round(y[i-1]+dist[i]*sin(radians(angle[i]))))
    x.append(x[amount-1])           
    y.append(y[amount-1])
 
    pen = []                        
    for i in range(0,amount): pen.append(None)  
    line = []                       
    while appOn and lastkey != "space" and (time_ns() // 100000000) % 150 != 0 :  
        for i in range(1,amount):   
            if pen[i] != None:      
                canv.delete(pen[i]) 
            angle[i] = angle[i]+rate[i]                                        
            x[i] = x[i-1]+dist[i]*cos(radians(angle[i]))
            y[i] = y[i-1]+dist[i]*sin(radians(angle[i]))
            pen[i] = canv.create_line(x[i-1],y[i-1],x[i],y[i],fill="green")    
         
     
        color = ["#"+''.join([choice('ABCDEF0123456789') for i in range(6)])]  
        line.append(canv.create_line(x[amount-1],y[amount-1],x[amount],y[amount], fill=color))  
        x[amount] = x[amount-1]                                                
        y[amount] = y[amount-1]
        line.append(canv.create_oval(x[amount-1]-3,y[amount-1]-3,x[amount-1]+3,y[amount-1]+3, outline=color)) 
        canv.update()                
        sleep(0.025)                
    for s in line: canv.delete(s)    
    for l in pen: canv.delete(l)     
win.destroy()