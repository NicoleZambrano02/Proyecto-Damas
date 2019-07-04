from tkinter import*
from tkinter import messagebox
tk=Tk()
canvas=Canvas(tk, width=800, height=645)
canvas.pack()
canvas.create_rectangle(5,5,80,640)
canvas.create_rectangle(160,5,80,640)
canvas.create_rectangle(240,5,80,640)
canvas.create_rectangle(320,5,80,640)
canvas.create_rectangle(400,5,80,640)
canvas.create_rectangle(480,5,80,640)
canvas.create_rectangle(560,5,80,640)
canvas.create_rectangle(640,5,80,640)

canvas.create_rectangle(5,5,640,80)
canvas.create_rectangle(5,160,640,80)
canvas.create_rectangle(5,240,640,80)
canvas.create_rectangle(5,320,640,80)
canvas.create_rectangle(5,400,640,80)
canvas.create_rectangle(5,480,640,80)
canvas.create_rectangle(5,560,640,80)
canvas.create_rectangle(5,640,640,80)

        #crear fichas de jugador 1
        #columna 1
n1=canvas.create_oval(10, 10, 75, 75, fill="black", tag="ficha")
n2=canvas.pack=canvas.create_oval(10, 235,75,165, fill="black", tag="ficha")
n3=canvas.pack=canvas.create_oval(10, 395,75,325, fill="black", tag="ficha")
n4=canvas.pack=canvas.create_oval(10, 555,75,485, fill="black", tag="ficha")

        #columna 2
n5=canvas.pack=canvas.create_oval(155, 155, 85, 85, fill="black", tag="ficha")
n6=canvas.pack=canvas.create_oval(155, 315, 85, 245, fill="black", tag="ficha")
n7=canvas.pack=canvas.create_oval(155, 475, 85, 405, fill="black", tag="ficha")
n8=canvas.pack=canvas.create_oval(155, 635, 85, 565, fill="black", tag="ficha")

        #columna 3
n9=canvas.pack=canvas.create_oval(235, 10, 165, 75, fill="black", tag="ficha")
n10=canvas.pack=canvas.create_oval(235, 235, 165, 165, fill="black", tag="ficha")
n11=canvas.pack=canvas.create_oval(235, 395, 165, 325, fill="black", tag="ficha")
n12=canvas.pack=canvas.create_oval(235, 555, 165, 485, fill="black", tag="ficha")
        
        #crear fichas de jugador 2

        #columna 1
canvas.pack=canvas.create_oval(635, 155, 565, 85, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(635, 315, 565, 245, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(635, 475, 565, 405, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(635, 635, 565, 565, fill="brown", tag="ficha")


            #columna 2
canvas.pack=canvas.create_oval(485, 10, 555, 75, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(485, 235,555, 165, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(485, 395,555,325, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(485, 555,555,485, fill="brown", tag="ficha")

      #columna 3
canvas.pack=canvas.create_oval(405, 155, 475, 85, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(405, 315, 475, 245, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(405, 475, 475, 405, fill="brown", tag="ficha")
canvas.pack=canvas.create_oval(405, 635, 475, 565, fill="brown", tag="ficha")

print('considere que para seleccionar una ficha a mover se debe contar desde el inicio del tablero hacia el lado del otro jugador de arriba hacia abajo')
print("mas claramente se muestran las pocisiones a continuacion: ")
print('el lado izquierdo corresponde al jugador 1 y el lado derecho al jugador 2')
print('[1,0,9,0,0 ,0,5,0]')
print('[0,5,0,0,0 ,9,0,1]')
print('[2,0,10,0,0,0,6,0]')
print('[0,6,0,0,0,10,0,2]')
print('[3,0,11,0,0,0,7,0]')
print('[0,7,0,0,0,11,0,3]')
print('[4,0,12,0,0,0,8,0]')
print('[0,8,0,0,0,12,0,4]')





x,y=25,15;
def jugador():
    turno=int(input("Ingrese el turno del jugador (1 o 2): "))
    if(turno==1):
        l = int(input("Ingrese el numero de pieza que desea mover (n): "))
        if (l>0 and l<13):
            l=16+l
            def move(event):
                global x,y
                if(x<585):
                    if event.keysym=="Up":
                        canvas.move(l,80,-80)
                        y=y-105
                        x=x+115
                        
                    
                    elif event.keysym=="Down":
                        canvas.move(l,80,80)
                        y=y+105
                        x=x+115
        else:
            print("ingrese una ficha correcta")
    

        
    else:
        r =int(input("Ingrese el numero de pieza que desea mover (r): "))
        if (r>0 and r<13):
            r=28+r   
            def move(event):
                global x,y
                if(x<585):
                    if event.keysym=="Up":
                        canvas.move(r,-80,-80)
                        y=y-105
                        x=x+115                
                    
                    elif event.keysym=="Down":
                        canvas.move(r,-80,80)
                        y=y+105
                        x=x+115
        else:
            print("ingrese una ficha correcta")
                  
    canvas.bind_all('<KeyPress-Up>', move)
    canvas.bind_all('<KeyPress-Down>', move)


btn=Button(text="pasar turno", width=15, height=3, command=jugador).place(x=660,y=10)



jugador()
    











tk.mainloop()
