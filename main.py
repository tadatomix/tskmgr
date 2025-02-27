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
        menu()

def task_reading ():
    colorama_init()
    with open("task.csv", 'r') as file:
        csvreader = csv.reader(file, delimiter=';')
        i = 0
        text = ""
        nonfText = ""
        rowLabels = ["Number", "Completion", "Name", "State", "Date"]
        counter_label = rowLabels[0]
        name_label = rowLabels[2]
        state_label = rowLabels[3]
        for row in csvreader:
            i+=1
            counter = str(i) + "."
            if len(counter) > len(rowLabels[0]):
                while (len(rowLabels[0]) != len(counter)):
                    counter_label+=" "
            else:
                while (len(counter) != len(rowLabels[0])):
                    counter+=" "
            text += counter + "|"
            nonfText += counter + "|"
            if (row[3] == "True"):
                check = "\U00002705"
                while (len(check) != len(rowLabels[1] - 1)):
                    check+=" "
                text += check + "|"
                nonfText += check + "|"
            if (row[3] == "False"):
                check = "\U0001F532"
                while (len(check) != (len(rowLabels[1]) - 1)):
                    check+=" "
                text += check + "|"
                nonfText += check + "|"
            name = row[0]
            state = row[1]
            if len(name) > len(name_label):
                while (len(name_label) < len(name)):
                    name_label+=" "
            else:
                while (len(name) < len(name_label)):
                    name+=" "
            if len(state) > len(state_label):
                while (len(state_label) < len(state)):
                    state_label+=" "
            else:
                while (len(state) < len(state_label)):
                    state+=" "
            if (row[1] == "Critical"):
                text += f'{Fore.RED}' + name + f'{Style.RESET_ALL}' + "|"
                text += f'{Fore.RED}' + state + f'{Style.RESET_ALL}' + "|"
                nonfText += name + "|"
                nonfText += state + "|"
            if (row[1] == "Moderate"):
                text += f'{Fore.YELLOW}' + name + f'{Style.RESET_ALL}' + "|"
                text += f'{Fore.YELLOW}' + state + f'{Style.RESET_ALL}' + "|"
                nonfText += name + "|"
                nonfText += state + "|"
            if (row[1] == "Light"):
                text += f'{Fore.GREEN}' + name + f'{Style.RESET_ALL}' + "|"
                text += f'{Fore.GREEN}' + state + f'{Style.RESET_ALL}' + "|"
                nonfText += name + "|"
                nonfText += state + "|"
            date = row[2]
            date_label = rowLabels[4]
            if len(date) > len(date_label):
                while (len(date_label) != len(date)):
                    date_label+=" "
            else:
                while (len(date) != len(date_label)):
                    date+=" "
            text += date + "|"
            nonfText += date + "|"
            text+="\n"
        print(counter_label + "|" + rowLabels[1] + "|" + name_label + "|" + state_label + "|" + date_label + "|")
        print(text)
        text = ""
        nonfText = ""

def task_deletion(task_num):
    with open("task.csv",'r') as F:
        file_list = F.read().split('\n')
    with open('task.csv', 'w', encoding='utf-8') as s1:
        del file_list[task_num-1]
        s1.write('\n'.join(file_list))
    menu()

def menu():
    task_reading()
    print("1. Write down new tasks"+ "\n" + "2. Delete existing task" + "\n" + "3. Set existing task as done" + "\n" + "4. Quit")
    menu = int(input("Pick an item (1-4): "))
    if(menu == 1):
        task_creation()
    if(menu == 2):
        del_num = int(input("Pick a line to delete"))
        task_deletion(del_num)
    if(menu == 3):
        print("Not implemented yet")
    if(menu == 4):
        exit()
if (os.path.exists('task.csv')):
    if (os.stat('task.csv').st_size == 0):
        qt = input ("There's no tasks. Do you want to create one? (y/n) ")
        if (qt == "y"):
            task_creation()
        else:
            exit()
    else:
        menu()
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
