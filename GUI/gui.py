from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkFont
import time


def hello():  
    """Place holder function"""
    print("hello!")


class app():
    """docstring for app"""
    def __init__(self, root):
        self.root = root
        self.height = self.root.winfo_screenheight() 
        self.width = self.root.winfo_screenwidth()
        self.app_width = int(0.5*self.width)
        self.app_length = int(0.5*self.height)
        self.root.geometry(str(self.app_width)+"x"+str(self.app_length))
        self.root.title("Market Analysis")
        self.create()  

    def Analytics_page(self):
        analytics_page = Tk()
        analytics_page.geometry(str(int(0.5*self.width))+"x"+str(int(0.5*self.height)))
        analytics_page.title("Analytcis Page")

        canvas = Canvas(analytics_page)
        canvas.create_line(0, 0.20*self.app_length, self.app_width, 0.20*self.app_length)  
        canvas.pack(fill = BOTH, expand = True)
        
        a = Button(analytics_page,text="Start Shelf Cam", command=hello)
        a.place(relx=0.5, rely=0.25, anchor=CENTER)
        
        button_desc_a = Label(analytics_page, text="Select this button to begin looking for specified objects on the shelf")
        button_desc_a.place(relx=0.5, rely=0.355, anchor=CENTER)

        canvas.create_line(0, 0.375*self.app_length, self.app_width, 0.375*self.app_length)  
        canvas.pack(fill = BOTH, expand = True)
        
        b = Button(analytics_page,text="Get Graphs", command=hello)
        b.place(relx=0.5, rely=0.425, anchor=CENTER)

        button_desc_b = Label(analytics_page, text="Select this button to get a plot of the current sales of the objects in the shelf.")
        button_desc_b.place(relx=0.5, rely=0.520, anchor=CENTER)

        canvas.create_line(0, 0.540*self.app_length, self.app_width, 0.540*self.app_length)  
        canvas.pack(fill = BOTH, expand = True)

        analytics_page.mainloop()

    def customer_page(self):
        customer_page = Tk()
        customer_page.geometry(str(int(0.5*self.width))+"x"+str(int(0.5*self.height)))
        customer_page.title("Product Info Page")

        box_desc = Label(customer_page, text="Product Name :")
        box_desc.place(relx=0.5, rely=0.205, anchor=CENTER)

        product_name = Entry(customer_page)
        product_name.place(relx=0.5, rely=0.25, anchor=CENTER)

        submit_button = Button(customer_page, text="Submit", command=hello)
        submit_button.place(relx=0.5, rely=0.320, anchor=CENTER)

        disp_info = Text(customer_page, height=int(0.5*self.app_length), width=self.app_width)
        disp_info.place(relx=0,rely=0.5)

        disp_info.configure(state="disabled")

        customer_page.mainloop()

    def create(self):
        menubar = Menu(self.root)  
        menubar.add_command(label="Analytics", command=self.Analytics_page)
        menubar.add_command(label="Product info", command=self.customer_page)  
        self.root.config(menu=menubar)
        welcome_font = tkFont.Font(family="Lucida Grande", size=55)
        welcome_label = Label(self.root, text='         Welcome To \nThe Market Analysis App ',font=welcome_font)
        welcome_label.pack(fill='both', expand=True, anchor=CENTER)
        


if __name__ == "__main__": 

    root = Tk()
    analysis_app = app(root)
    root.mainloop()