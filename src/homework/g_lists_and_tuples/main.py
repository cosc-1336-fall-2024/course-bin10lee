#
from lists import get_highest_list_value,get_lowest_list_value

def main():
    while True:
        print("1-Show the list low /high values//2-Exit")

        choice=input("Choose an option: ")

        if choice=="2":
            print("Exit")
            break
        elif choice=="1":
            numbers=[]
            while True:
                value=input("Enter a list value: ")
                if value.lower()=='stop':
                    break
                try:
                    numbers.append(int(value))
                except ValueError:
                    print("Please enter a valid integer")
                if len(numbers)>=3:
                    another=input("Do you want to enter another value? (Yes or No): ")
                    if another=="Yes":
                        break
                lowest=get_lowest_list_value
                highest=get_highest_list_value

                print(get_lowest_list_value)
                print(get_highest_list_value)

main()



