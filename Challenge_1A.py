
import numpy as np
import tkinter as tk
from tkinter import ttk

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import(
	FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
#import matplotlib.animation as animation
from matplotlib import style
from matplotlib.patches import FancyArrowPatch

from itertools import combinations, product
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.proj3d import proj_transform

LARGE_FONT= ("Verdana", 12)

class Vector_transform(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

       # tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Vector transformation app")
        
        
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
        

        button1 = tk.Button(container, text= "Translate in x")
        button1.grid(column=1,row=1,pady=3, sticky=tk.W)
        entry1 = tk.Entry(container, width=20)
        entry1.grid(column=2,row=1,padx=4,pady=0,sticky=tk.W)

        button2 = tk.Button(container, text= "Translate in y")
        button2.grid(column=1,row=2,pady=3, sticky=tk.W)
        entry2 = tk.Entry(container, width=20)
        entry2.grid(column=2,row=2,padx=4,pady=0,sticky=tk.W)

        button3 = tk.Button(container, text= "Translate in z")
        button3.grid(column=1,row=3,pady=6, sticky=tk.W)
        entry3 = tk.Entry(container, width=20)
        entry3.grid(column=2,row=3,padx=4,pady=0,sticky=tk.W)

        button4 = tk.Button(container, text= "Rotate in x")
        button4.grid(column=1,row=4,pady=6, sticky=tk.W)
        entry4 = tk.Entry(container, width=20)
        entry4.grid(column=2,row=4,padx=4,pady=0,sticky=tk.W)
        
        button5 = tk.Button(container, text="Rotate in y")
        button5.grid(column=1,row=5,pady=3, sticky=tk.W)
        entry5 = tk.Entry(container, width=20)
        entry5.grid(column=2,row=5,padx=4,pady=0,sticky=tk.W)
        
        button6 = tk.Button(container, text="Rotate in z")
        button6.grid(column=1,row=6,pady=6, sticky=tk.W)
        entry6 = tk.Entry(container, width=20)
        entry6.grid(column=2,row=6,padx=4,pady=0,sticky=tk.W)

        button7 = tk.Button(container, text="Stretch")
        button7.grid(column=1,row=7,pady=6, sticky=tk.W)
        entry7 = tk.Entry(container, width=20)
        entry7.grid(column=2,row=7,padx=4,pady=0,sticky=tk.W)
                         
        button8 = tk.Button(container, text="Reflect")
        button8.grid(column=1,row=8,pady=6, sticky=tk.W)
        entry8 = tk.Entry(container, width=20)
        entry8.grid(column=2,row=8,padx=4,pady=0,sticky=tk.W)
        self.show_frame(graphImbedded)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        

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
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

##        button1 = ttk.Button(self, text="translate", command = lambda: controller.show_frame(graphImbedded))
##        button1.place(relx=1,rely=1)
##        
##        button2 = ttk.Button(self, text="rotate", command = lambda: controller.show_frame(graphImbedded))
##        button2.place(x=550,y=200)
##        
##        button3 = ttk.Button(self, text="reflect", command = lambda: controller.show_frame(graphImbedded))
##        button3.pack(side=tk.RIGHT)
##        
##        button4 = ttk.Button(self, text = "stretch", command = lambda: controller.show_frame(graphImbedded))
##        button4.pack(side=tk.RIGHT)
##        
       
        fig = Figure(figsize=(5,5), dpi=100)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        ax = fig.add_subplot(111, projection="3d")


        r = [-1, 1]
        for s, e in combinations(np.array(list(product(r,r,r))), 2):
            if np.sum(np.abs(s-e)) == r[1]-r[0]:
                ax.plot3D(*zip(s,e), color="b")
        ax.scatter([0],[0],[0],color="g",s=100)
        
        
        vector = Arrow3D([1,1],[0.5,1],[0.3,1], mutation_scale=20, lw=1, arrowstyle="-|>", color="m")
        vector_1 = Arrow3D([1,0],[0.5,0],[0.3,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="g")
        vector_2= Arrow3D([0,1],[0,1],[0,1], mutation_scale=20, lw=1, arrowstyle="-|>", color="c")

        a = Arrow3D([0,0],[0,1],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
        b = Arrow3D([0,-1],[0,0],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
        c = Arrow3D([0,0],[0,0],[0,1], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
        d = Arrow3D([0,0],[0,0],[0,-1], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
        e = Arrow3D([0,1],[0,0],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
        f = Arrow3D([0,0],[0,-1],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")

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
        
        


        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


app = Vector_transform()
app.mainloop()
