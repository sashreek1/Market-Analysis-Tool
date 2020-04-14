from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkFont
import time
from cv.detect_colours import detect_colour
from sendmsg import send_data
from sendmsg import get_data
from graphing import get_plot
import cv.bought as bought

class app():
    def __init__(self, root):
        self.root = root
        self.height = self.root.winfo_screenheight() 
        self.width = self.root.winfo_screenwidth()
        self.app_width = int(0.5*self.width)
        self.app_length = int(0.5*self.height)
        self.root.geometry(str(self.app_width)+"x"+str(self.app_length))
        self.root.title("Market Analysis")
        self.colour_count = {}
        self.create()  

    def Analytics_page(self):
        
        analytics_page = Tk()
        analytics_page.geometry(str(int(0.5*self.width))+"x"+str(int(0.5*self.height)))
        analytics_page.title("Analytcis Page")

        canvas = Canvas(analytics_page)
        canvas.create_line(0, 0.20*self.app_length, self.app_width, 0.20*self.app_length)  
        canvas.pack(fill = BOTH, expand = True)
        
        a = Button(analytics_page,text="Start Shelf Cam", command=lambda: detect_colour(self.product_info_entry, self.colour_count))
        a.place(relx=0.5, rely=0.25, anchor=CENTER)
        
        button_desc_a = Label(analytics_page, text="Select this button to begin looking for specified objects on the shelf")
        button_desc_a.place(relx=0.5, rely=0.355, anchor=CENTER)

        canvas.create_line(0, 0.375*self.app_length, self.app_width, 0.375*self.app_length)  
        canvas.pack(fill = BOTH, expand = True)
        
        b = Button(analytics_page,text="Get Graphs", command= lambda: get_plot(get_data()))
        b.place(relx=0.5, rely=0.425, anchor=CENTER)

        button_desc_b = Label(analytics_page, text="Select this button to get a plot of the current sales of the objects in the shelf.")
        button_desc_b.place(relx=0.5, rely=0.520, anchor=CENTER)

        canvas.create_line(0, 0.540*self.app_length, self.app_width, 0.540*self.app_length)  
        canvas.pack(fill = BOTH, expand = True)

        analytics_page.mainloop()

    def product_info_entry(self):

        def false_alarm ():
            product_entry.destroy()
            detect_colour(self.product_info_entry, self.colour_count)

        def submit_json ():
            object_desc = {}
            object_desc["name"] = e1.get()
            object_desc["age"] = int(e2.get())
            object_desc["origin"] = e3.get()
            object_desc["sales"] = str(self.colour_count)
            object_desc["timestamp"] = time.time()
            object_desc["bought"] = str(bought.bought)
            print(object_desc)
            send_data(object_desc)
            
            product_entry.destroy()
            detect_colour(self.product_info_entry, self.colour_count)
            
            
        product_entry = Tk()
        product_entry.geometry(str(int(0.3*self.width))+"x"+str(int(0.3*self.height)))
        product_entry.title("Product Info Page")

        Label(product_entry, text="Product Name").place(relx=0.2, rely=0.2)
        Label(product_entry, text=" Age").place(relx=0.2,rely=0.3)
        Label(product_entry, text=" Origin").place(relx=0.2,rely=0.4)

        e1 = Entry(product_entry)
        e2 = Entry(product_entry)
        e3 = Entry(product_entry)

        e1.place(relx=0.5, rely=0.2)
        e2.place(relx=0.5,rely=0.3)
        e3.place(relx=0.5,rely=0.4)

        Sub = Button(product_entry, text="Submit", command=submit_json)
        Sub.place(relx=0.5,rely=0.7)

        fp = Button(product_entry, text="False Positive", command=false_alarm)
        fp.place(relx=0.5,rely=0.8)
        
        product_entry.mainloop()

    def customer_page(self):
        customer_page = Tk()
        customer_page.geometry(str(int(0.5*self.width))+"x"+str(int(0.5*self.height)))
        customer_page.title("Product Info Page")

        box_desc = Label(customer_page, text="Product Name :")
        box_desc.place(relx=0.5, rely=0.205, anchor=CENTER)

        product_name = Entry(customer_page)
        product_name.place(relx=0.5, rely=0.25, anchor=CENTER)

        self.disp_info = Text(customer_page, height=int(0.5*self.app_length), width=self.app_width, font=("Helvetica", 32))
        self.disp_info.place(relx=0,rely=0.5)

        submit_button = Button(customer_page, text="Submit", command=lambda:(self.Sub_func(product_name.get())))
        submit_button.place(relx=0.5, rely=0.320, anchor=CENTER)

        customer_page.mainloop()

    def Sub_func(self, name):
        self.disp_info.configure(state="normal")
        self.disp_info.delete('1.0', END)
        self.data = get_data()
        for i in self.data:
            if i[1] == name:
                self.disp_info.insert(END,"Name : "+i[1]+"\n")
                self.disp_info.insert(END,"Origin : "+i[3]+"\n")
        self.disp_info.configure(state="disabled")

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
