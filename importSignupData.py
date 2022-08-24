import pandas as pd
import tkinter as tk
from tkinter import filedialog
import time


# class Runner:
#     def __init__(self, first_name, last_name, school, gender, time_to_run):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.school = school
#         self.gender = gender
#         if gender == 'M':
#             self.distance = '8000m'
#         if gender == 'F':
#             self.distance = '6000m'
#         self.time_to_run = time_to_run
#
#     def set_time(self, time_string):  # Enter time in MM:SS.xx, will be stored as struct_time
#         self.time_to_run = time.strptime(time_string, '%M:%S')
#
#     def get_time(self):  # Returns time as string
#         return time.strftime('%M:%S', self.time_to_run)


def choose_files():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


def create_school_database():
    return pd.DataFrame(columns=['School', 'Primary Contact', 'Email', 'Phone Number'])


def create_individual_database():
    return pd.DataFrame(columns=['School', 'First Name', 'Last Name', 'Gender (M/F)'])


def read_school(file_path, df):
    xlsx = pd.ExcelFile(file_path)
    school_information = pd.read_excel(xlsx, 'Start Here!')
    school = school_information.iloc[3, 1]
    primary_contact = school_information.iloc[4, 1]
    email = school_information.iloc[5, 1]
    phone_number = school_information.iloc[6, 1]
    df.loc[len(df.index)] = [school, primary_contact, email, phone_number]
    return df


def read_individual(file_path, df):
    xlsx = pd.ExcelFile(file_path)
    individual_information = pd.read_excel(xlsx, 'Individual Events')
    individual_information = individual_information.dropna(axis=0)
    df = pd.concat([df, individual_information])
    return df


school_database = create_school_database()
individual_database = create_individual_database()
file = choose_files()
school_database = read_school(file, school_database)
individual_database = read_individual(file, individual_database)

