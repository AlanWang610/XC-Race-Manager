import pandas as pd
import tkinter as tk
from tkinter import filedialog
import time

class runner:
    def __init__(self, first_name, last_name, school, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.school = school
        self.gender = gender
        if gender == 'M':
            self.distance = '8000m'
        if gender == 'F':
            self.distance = '6000m'
    def set_time(self, time_string): # Enter time in MM:SS.xx, will be stored as struct_time
        self.time = time.strptime(time_string, '%M:%S')
    def get_time(self): # Returns time as string
        return time.strftime('%M:%S', self.time)

def chooseFiles():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def readFiles(file_path):
    xlsx = pd.ExcelFile(file_path)
    school_information = pd.read_excel(xlsx, 'Start Here!')
    individual_information = pd.read_excel(xlsx, 'Individual Events')
    print(school_information)
    print(individual_information)
    school = school_information[3][1]
    primary_contact = school_information[4][1]
    email = school_information[5][1]
    phone_number = school_information[6][1]


file_path = chooseFiles()
readFiles(file_path)


