#this code initialized the csv file with the right name and headers, which main.py then appended throughout the week.
import csv

#header names list
header = ['Time', 'Time_Formatted', 'Temp_External', 'Temp_Internal', 'Open', 'Close_Actuation']

#write initial row of headers
with open('data_final.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)