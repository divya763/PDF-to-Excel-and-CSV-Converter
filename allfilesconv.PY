from tkinter import *
from tkinter import filedialog as fd
# to open multiple files

import tabula # for pdf file conversion
#from tabula.io import read_pdf
# Create Object
root = Tk() 
# set Geometry
root.geometry('400x200')

def select_file():
    global source_file
    source_file = fd.askopenfilename(initialdir = "/",title = "Select File")
    

# PDF TO EXCEL
def pdf_to_excel():
    if source_file.endswith('.pdf'):
        # Read PDF File
        # this contain a list
        try:
            
            df = tabula.read_pdf(source_file, pages = 1)[0]
            files = [('Excel Files', '*.xlsx')]
            dest_file =fd.asksaveasfile(mode='w',filetypes=files,defaultextension ="*")
            # Convert into Excel File
            df.to_excel('Excel.xlsx')
        except Exception as e:
            print(e)
            

# PDF TO CSV
def pdf_to_csv():
    if source_file.endswith('.pdf'):
        # Read PDF File
        # this contain a list
        try:
            df = tabula.read_pdf(source_file, pages = 1)[0]
            files = [('CSV Files', '*.csv')]
            dest_file =fd.asksaveasfile(mode='w',filetypes=files,defaultextension ="*")
            # Convert into CSV File
           
            df.to_csv(dest_file)
        except Exception as e:
            print(e)


# Add Labels and Buttons
Label(root, text="PDF CONVERSION", font="italic 15 bold").pack(pady=10)

Button(root,text="Select PDF File",command=select_file,font=14).pack(pady=10)

frame = Frame()
frame.pack(pady=20)

excel_btn = Button(frame,text="PDF to Excel",command=pdf_to_excel,relief="solid",
                   bg="white",font=15)
excel_btn.pack(side=LEFT,padx=10)

csv_btn = Button(frame,text="PDF to CSV",command=pdf_to_csv,relief="solid",
                 bg="white",font=15)
csv_btn.pack()

# Execute Tkinter
root.mainloop()
