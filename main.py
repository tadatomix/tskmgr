import os.path
import os
import csv
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

print("Welcome to the Task Manager")

def task_creation ():
    qe = ""
    while (qe != "n"):
        taskName = input ("Write down the task name: ")
        taskState = input ("Write down importance level (Critical/Moderate/Light): ")
        taskDate = input ("Write down the date of reminder: ")
        taskCompletion = "False"
        qe = input("Do you want to add another task? (y/n) ")
        with open('task.csv', 'a') as file:
            file.write(taskName + ";" + taskState + ";" + taskDate + ";" + taskCompletion + '\n')
    print ("Finished writing task(s)")
    qr = input ("Do you want to write down current tasks? (y/n) ")
    if (qr == "y"):
        task_reading()

def task_reading ():
    colorama_init()
    with open("task.csv", 'r') as file:
        csvreader = csv.reader(file, delimiter=';')
        i = 0
        text = ""
        nonfText = ""
        rowLabels = ["Number", "Completion", "Name", "State", "Date"]
        print (rowLabels[0] + "|" + rowLabels[1] + "|" + rowLabels[2] + "|" + rowLabels[3] + "|" + rowLabels[4])
        for row in csvreader:
            i+=1
            l=0
            text += str(i) + "." + " | "
            nonfText += str(i) + "." + " | "
            if (row[3] == "True"):
                text += "\U00002705 " + " | "
                nonfText += "_ " + " | "
            if (row[3] == "False"):
                text += "\U0001F532 " + " | "
                nonfText += "_ " + " | "
            if (row[1] == "Critical"):
                text += f'{Fore.RED}' + row[0] + f'{Style.RESET_ALL}' + " | "
                text += f'{Fore.RED}' + row[1] + f'{Style.RESET_ALL}' + " | "
                nonfText += row[0] + " | "
                nonfText += row[1] + " | "
            if (row[1] == "Moderate"):
                text += f'{Fore.YELLOW}' + row[0] + f'{Style.RESET_ALL}' + " | "
                text += f'{Fore.YELLOW}' + row[1] + f'{Style.RESET_ALL}' + " | "
                nonfText += row[0] + " | "
                nonfText += row[1] + " | "
            if (row[1] == "Light"):
                text += f'{Fore.GREEN}' + row[0] + f'{Style.RESET_ALL}' + " | "
                text += f'{Fore.GREEN}' + row[1] + f'{Style.RESET_ALL}' + " | "
                nonfText += row[0] + " | "
                nonfText += row[1] + " | "
            text += row[2] + " | "
            nonfText += row[2] + " | "
            while (l < len(nonfText)):
                print('-', end='')
                l+=1
            print('')
            print(text)
            text = ""
            nonfText = ""

if (os.path.exists('task.csv')):
    if (os.stat('task.csv').st_size == 0):
        qt = input ("There's no tasks. Do you want to create one? (y/n) ")
        if (qt == "y"):
            task_creation()
        else:
            qr = input ("Do you want to write down current tasks? (y/n) ")
            if (qr == "y"):
                task_reading()
            else:
                quit()
    else:
        qr = input ("Do you want to write down current tasks? (y/n) ")
        if (qr == "y"):
            task_reading()
else:
    qc = input("File doesn't exist. Do you want to create one? (y/n) ")
    if (qc == "y"):
        open('task.csv', 'a').close()
        qt = input ("There's no tasks. Do you want to create one? (y/n) ")
        if (qt == "y"):
            task_creation()
        else:
            exit()
    else:
        exit()
