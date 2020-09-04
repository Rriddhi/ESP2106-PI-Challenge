
'''
Created on Thu Aug 20 13:66:13 2020

@author: smridhi
'''


import numpy as np
import tkinter as tk
from tkinter import ttk
from math import sin,cos,pi
import json
import os
import matplotlib.animation as animation

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import(
	FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib.patches import FancyArrowPatch
import matplotlib.animation as animation
from matplotlib import pyplot as plt

from itertools import combinations, product
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.proj3d import proj_transform

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 16:55:15 2020

@author: irwin
"""

from math import sqrt
from numpy import dot

# ax + by + cz = d  -- > (a,b,c,d)

def dotproduct(vector1, vector2):
    result = 0
    if len(vector1) == len(vector2):
        result = dot(vector1,vector2)
        return result

def planeunitnormvect(a,b,c,d):
  normvect = [a,b,c]
  unitnorm = []
  distance = d
  unitfactor = sqrt(a**2 + b**2 + c**2)
  for i in range(len(normvect)):
    unitnorm.append(normvect[i]/unitfactor)
    
  return unitnorm,d

def inputvect(x,y,z):
    return [x,y,z]

#reflectionvect(inputvect(1,2,3), planeunitnormvect(0,0,1,0))
  
def reflectionvect(inputvect, plane): 
    vector = inputvect
    unitnorm = plane[0]
    distance = plane[1]
    factor = 0
    refl = []
    if len(vector)==len(unitnorm):
        newvect = [0] * len(vector)
        factor = 2*(dot(vector,unitnorm)-distance)
        for i in range(len(unitnorm)):
            refl.append(unitnorm[i]*factor)
        for j in range(len(unitnorm)):
            newvect[j] = vector[j] - refl[j]
    return newvect



LARGE_FONT= ("Verdana", 12)

#starting arrays for the vectors
#arr_1 contains the vectors for translation
#arr_2 contains the input vectors

initial_arr1= [[0,0,0]]
initial_arr2= [[0,0,0]]
count = 0
fig = Figure(figsize=(5,5), dpi=100)
ax = fig.add_subplot(111, projection="3d")
ax.mouse_init()

##a = Axes3D(fig)
##a.set_xlim3d(-20, 20)
##a.set_ylim3d(-20,20)
##a.set_zlim3d(-20,20)

def animate(i):
    with open('test.txt','r+')as f:
            filesize = os.path.getsize('test.txt')
            if filesize!=0:        
                a = json.loads(f.read())
                f.truncate(0)
                print(a) 
            else:
                a = [[[0,0,0]],[[0,0,0]]]
               
            if len(a[0])> 1:
                V_1 = a[0][len(a[0])-1]
            else:
                V_1 = a[0][0]
            if len(a[1])>1:
                V_2 =a[1][len(a[1])-1]
            else:
                V_2 = a[1][0]
            
            x = [V_1[0],V_2[0]]
            y = [V_1[1],V_2[1]]
            z = [V_1[2],V_2[2]]
    
    
    ax.clear()
    
    vector = Arrow3D(x,y,z, mutation_scale=20, lw=1, arrowstyle="-|>", color="m")
    vector_1 = Arrow3D([x[0],0],[y[0],0],[z[0],0], mutation_scale=20, lw=1, arrowstyle="-|>", color="g")
    vector_2= Arrow3D([0,x[1]],[0,y[1]],[0,z[1]], mutation_scale=20, lw=1, arrowstyle="-|>", color="c")
    
    a = Arrow3D([0,0],[0,1],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
    b = Arrow3D([0,-1],[0,0],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
    c = Arrow3D([0,0],[0,0],[0,1], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
    d = Arrow3D([0,0],[0,0],[0,-1], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
    e = Arrow3D([0,1],[0,0],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
    f = Arrow3D([0,0],[0,-1],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")

##    r = [-1, 1]
##    for s, e in combinations(np.array(list(product(r,r,r))), 2):
##            if np.sum(np.abs(s-e)) == r[1]-r[0]:
##                ax.plot3D(*zip(s,e), color="b")
##    ax.scatter([0],[0],[0],color="g",s=100)
    
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')
               
    ax.add_artist(vector_1)
    ax.add_artist(vector_2)
    ax.add_artist(vector)
    ax.add_artist(a)
    ax.add_artist(b)
    ax.add_artist(c)
    ax.add_artist(d)
    ax.add_artist(e)
    ax.add_artist(f)

    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')


        
class Vector_transform(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

       # tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Vector transformation app")
       
        #Creates a 3D array 

        def retrieve_input(textBox):
            

            global arr_1 
            global arr_2
            global count 
            if count == 0:
                arr_1 = [[0,0,0]]
                arr_2 = [[0,0,0]]
                count +=1
            if  textBox == undo_transVector and len(arr_1)>0:
                arr_1.pop()
            elif textBox == undo_inputVector and len(arr_1)>0:
                arr_2.pop()
           
            else:
                inputValue= textBox.get()
                
            ls=[]
            #To perfom mathematical manupulations here to abtain vector.
            #V_1 refers to the translation vector(i.e green vector on the diagram),
            #V_2 refers to the input vector(ie cyan vector on the diagram)
            if textBox == get_transVector_input:
                a= get_transVector_input.get() #gets the tkinter object value 
                for i in a.split(","):
                    ls.append(round(float(i),2))
                    V_1 = ls
                arr_1.append(V_1)
                textBox.delete(0, 'end')
            if textBox == get_vector_input:
                a = get_vector_input.get()
                for i in a.split(","):
                    ls.append(round(float(i),2))
                    V_2 = ls
                arr_2.append(V_2)
                textBox.delete(0, 'end')
            if textBox == entry1:
                #to insert in the translation in x direction calculation
                if len(arr_1)>1:
                    a = arr_1[len(arr_1)-1]
                else:
                    a = arr_1[0]
                V_1 = [a[0] + round(float(entry1.get()),2),a[1], a[2]]
                arr_1.append(V_1)
                textBox.delete(0, 'end')
            if textBox == entry2:
                #to insert in the translation in y direcrion calculation
                if len(arr_1)>1:
                    a = arr_1[len(arr_1)-1]
                else:
                    a = arr_1[0]
                V_1 = [a[0],a[1] + round(float(entry2.get(),2)),0, a[2]]
                arr_1.append(V_1)
                textBox.delete(0, 'end')
            if textBox == entry3:
                #to insert in the translation in z direcrion calculation
                if len(arr_1)>1:
                    a = arr_1[len(arr_1)-1]
                else:
                    a = arr_1[0]
                V_1 = [a[0],a[1], a[2] + round(float(entry3.get(),2))]
                arr_1.append(V_1)
                textBox.delete(0, 'end')
            if textBox == entry4:
                # rotation in x calculation
                ang_rad = (round(float(entry4.get(),2))/180)*pi
                matrix_x = [[1,0,0],[0,cos(ang_rad),-sin(ang_rad)],[0,sin(ang_rad),cos(ang_rad)]]
                n=[]
                if len(arr_2)>1:
                    a = arr_2[len(arr_2)-1]
                else:
                    a = arr_2[0]
                for i in matrix_x:
                        value = round(np.dot(i,a),2)
                        n.append(value)
                V_2=n
                arr_2.append(V_2)      
                textBox.delete(0, 'end')    
            if textBox == entry5:
                #rotation in y calculation
                ang_rad = (round(float(entry5.get(),2))/180)*pi
                matrix_y = [[cos(ang_rad), 0,sin(ang_rad)],[0,1,0],[-sin(ang_rad),0,cos(ang_rad)]]
                n=[]
                if len(arr_2)>1:
                    a = arr_2[len(arr_2)-1]
                else:
                    a = arr_2[0]
                for i in matrix_y:
                        value = round(np.dot(i,a),2)
                        n.append(value)
                V_2=n
                arr_2.append(V_2)
                textBox.delete(0, 'end')
            if textBox == entry6:
                #rotation in z calculation
                ang_rad = (round(float(entry6.get(),2))/180)*pi
                matrix_z = [[cos(ang_rad), -sin(ang_rad), 0],[sin(ang_rad), cos(ang_rad), 0],[0,0,1]]
                n=[]
                if len(arr_2)>1:
                    a = arr_2[len(arr_2)-1]
                else:
                    a = arr_2[0]
                for i in matrix_z:
                        value = round(np.dot(i,a),2)
                        n.append(value)
                V_2=n
                arr_2.append(V_2)
                textBox.delete(0, 'end')
                
            if textBox == entry7:
                #stretch calculation
                if len(arr_2)>1:
                    a = arr_2[len(arr_2)-1]
                else:
                    a = arr_2[0]
                n = round(float(entry7.get()),2)
                V_2 = [a[0]*n,a[1]*n, a[2]*n]
                arr_2.append(V_2)
                textBox.delete(0, 'end')
                
            if textBox == entry8:
                #Reflect calculation
                n = entry8.get()
                for i in n.split(","):
                    ls.append(round(float(i),2))
                    pn = ls
                if len(arr_2)>1:
                    a = arr_2[len(arr_2)-1]
                else:
                    a = arr_2[0]
                
                V_2 = reflectionvect(inputvect(a[0],a[1],a[2]), planeunitnormvect(pn[0],pn[1],pn[2],pn[3]))
                arr_2.append(V_2)
                textBox.delete(0, 'end')
              
                
            print(arr_1)
            print(arr_2)
            array = [arr_1,arr_2]
            with open('test.txt','w+') as f:
                f.truncate(0)
                f.write(json.dumps(array))
           
        
        container = tk.Frame(self)
        
        container.pack(side=tk.RIGHT, fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(5, pad=7)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(3, pad=7)
        
      
        self.frames = {}

       
        frame = graphImbedded(container, self)
        self.frames[graphImbedded] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        
        get_vector_input= tk.Entry(container, width=20)
        get_vector_input.grid(column=0,row=1,pady=3, padx=3, sticky=tk.W)
        vector_button= tk.Button(container, text= "Input Vector", command = lambda: retrieve_input(get_vector_input))
        vector_button.grid(column=0, row=2,pady=6, padx=3, sticky=tk.W)

        get_transVector_input= tk.Entry(container, width=20)
        get_transVector_input.grid(column=0,row=3,pady=3, padx=3, sticky=tk.W)
        vector_button= tk.Button(container, text= "Translation Vector", command = lambda: retrieve_input(get_transVector_input))
        vector_button.grid(column=0, row=4,pady=0, padx=3, sticky=tk.W)

        undo_inputVector = ttk.Button(container,text="Undo Input", command = lambda:retrieve_input(undo_inputVector))
        undo_inputVector.grid(column =0, row = 6, pady=5, padx=3, sticky=tk.W)
        
        undo_transVector = ttk.Button(container,text="Undo Translation", command = lambda:retrieve_input(undo_transVector))
        undo_transVector.grid(column = 0, row=5, pady= 0, padx=3,sticky=tk.W)
        
        
        button1 = tk.Button(container, text= "Translate in x", command=lambda:retrieve_input(entry1))
        button1.grid(column=1,row=1,pady=3, sticky=tk.W)
        entry1 = tk.Entry(container, width=20)
        entry1.grid(column=2,row=1,padx=4,pady=0,sticky=tk.W)

        button2 = tk.Button(container, text= "Translate in y", command = lambda: retrieve_input(entry2))
        button2.grid(column=1,row=2,pady=3, sticky=tk.W)
        entry2 = tk.Entry(container, width=20)
        entry2.grid(column=2,row=2,padx=4,pady=0,sticky=tk.W)

        button3 = tk.Button(container, text= "Translate in z",command = lambda: retrieve_input(entry3))
        button3.grid(column=1,row=3,pady=6, sticky=tk.W)
        entry3 = tk.Entry(container, width=20)
        entry3.grid(column=2,row=3,padx=4,pady=0,sticky=tk.W)

        button4 = tk.Button(container, text= "Rotate in x", command = lambda: retrieve_input(entry4))
        button4.grid(column=1,row=4,pady=6, sticky=tk.W)
        entry4 = tk.Entry(container, width=20)
        entry4.grid(column=2,row=4,padx=4,pady=0,sticky=tk.W)
        
        button5 = tk.Button(container, text="Rotate in y", command = lambda: retrieve_input(entry5))
        button5.grid(column=1,row=5,pady=3, sticky=tk.W)
        entry5 = tk.Entry(container, width=20)
        entry5.grid(column=2,row=5,padx=4,pady=0,sticky=tk.W)
        
        button6 = tk.Button(container, text="Rotate in z",command = lambda: retrieve_input(entry6))
        button6.grid(column=1,row=6,pady=6, sticky=tk.W)
        entry6 = tk.Entry(container, width=20)
        entry6.grid(column=2,row=6,padx=4,pady=0,sticky=tk.W)

        button7 = tk.Button(container, text="Stretch", command = lambda: retrieve_input(entry7))
        button7.grid(column=1,row=7,pady=6, sticky=tk.W)
        entry7 = tk.Entry(container, width=20)
        entry7.grid(column=2,row=7,padx=4,pady=0,sticky=tk.W)
                         
        button8 = tk.Button(container, text="Reflect", command = lambda: retrieve_input(entry8))
        button8.grid(column=1,row=8,pady=6, sticky=tk.W)
        entry8 = tk.Entry(container, width=20)
        entry8.grid(column=2,row=8,padx=4,pady=0,sticky=tk.W)
        self.show_frame(graphImbedded)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
#Class generates the arrows to be drawn in the graph 
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

class graphImbedded(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
       
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        ax.mouse_init()
 

        #For the Blue container 
##        r = [-1, 1]
##        for s, e in combinations(np.array(list(product(r,r,r))), 2):
##            if np.sum(np.abs(s-e)) == r[1]-r[0]:
##                ax.plot3D(*zip(s,e), color="b")
##        ax.scatter([0],[0],[0],color="g",s=100)

       # print("new array 1", Vector_transform.new_arr1)
    
        
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


            
app = Vector_transform()
ani = animation.FuncAnimation(fig,animate, interval=3000)
app.mainloop()
