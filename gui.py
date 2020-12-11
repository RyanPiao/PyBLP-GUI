import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import pyblp
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from scipy import stats

# Create window object
app = Tk()
app.title('Pyblp_GUI')
app.geometry('1024x768')

# Define commands
def import_product_data():
    global s1_text_product
    csv_file_path_product = askopenfilename()
    print(csv_file_path_product)
    s1_text_product.set(csv_file_path_product)
    product_data = pd.read_csv(csv_file_path_product)

def import_agent_data():
    global s1_text_agent
    csv_file_path_agent = askopenfilename()
    print(csv_file_path_agent)
    s1_text_agent.set(csv_file_path_agent)
    agent_data = pd.read_csv(csv_file_path_agent)

# Section One: Loading Data
s1_lable = Label(app,text='Step 1: Loading the Data',font=('bold')).grid(row=0, column=0,columnspan=2, sticky=W+E+N+S , ipady=10)

# Product Data
s1_text_product = StringVar()
s1_prodcut_data = Label(app,text='Prodcut_data').grid(row=1, column=0, ipadx=20)
s1_productdata_entry = Entry(app, textvariable=s1_text_product).grid(row=1, column=1)
s1_productdata_btn = Button(app, text='Load',command=import_product_data).grid(row=1, column=2)

# Agent Data
s1_text_agent = StringVar()
s1_agent_data = Label(app,text='Agent_data').grid(row=1, column=3, ipadx=20)
s1_agentdata_entry = Entry(app, textvariable=s1_text_agent).grid(row=1, column=4)
s1_agentdata_btn = Button(app, text='Load',command=import_agent_data).grid(row=1, column=5)

# Start program
close = Button(app, text='Close',command=app.destroy).grid(row=10, column=10, sticky=E)
app.mainloop()

