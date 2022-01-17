#necessary modules
from time import sleep, time, strftime
import csv
import subprocess

#functions from other scripts
from weather import get_weather
from temp import get_temp
from switch import get_switch
from message import send_message

#to prevent infinite loop in case of bug
try:
    #while loop keeps this running while the script is kept running in the screen terminal
    while True:
        #all variables to be filled with data collected form the other scripts
        epoch_time = time()
        format_time = strftime("%m/%d/%Y, %H:%M:%S")
        weather = get_weather()
        temp = get_temp()
        open_switch = get_switch()
        close = 0

        #determine whether to send message or not based off conditions
        if weather < 4 and temp < 15:
            close = 1
        elif weather >= 4 and temp < 17:
            close = 1

        #send message if conditions are met
        if close == 1:
            send_message()

        #make a list with all the data collected to be appended to the csv
        data = [epoch_time, format_time, weather, temp, open_switch, close]

        #write new row of data with the new list
        with open('data_final.csv', 'a', encoding='UTF8', newline='') as file:
            #csv module enables easy writing to the file
            writer = csv.writer(file)
            #write the new row
            writer.writerow(data)

        #update the file on onedrive using the od_sync.sh script with runs rclose
        process = subprocess.run('od_sync.sh', shell=True, check=True) 

        #wait 5 minutes until the next data collection instance
        sleep(300)

#in case of bugs
except:
    KeyboardInterrupt




