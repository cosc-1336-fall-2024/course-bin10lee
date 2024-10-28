#
import dictionary
def menu():
    print("1-Get p distance matrix / 2-Exit")
def display_result(result):
    for row in result:
        for item in row:
            print(str(item).rjust(3, " "), end=" ")
        print(" ")

def get_total_list():
    num=int(input("How many list?"))
    index=0
    total_list=[]
    while (index<num):
        input_list=input("Please enter a comma-separated list: ")
        s_list=input_list.split(",")
        s_list=[value.strip() for value in s_list]
        total-list.append(s_list)
        index +=1

    return total_list

def run_menu():
    option=0
    while option !=2:
        menu()
        option=int(input("Select 1 or 2: "))
    if option ==1:
        result1=get_total_list()
    elif option==2:
        exit()
    else:
        run_menu

run_menu()
