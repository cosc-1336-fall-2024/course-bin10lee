#factorial function using a for range loop
def get_factorial(num1):
    TOTAL_X = 1
    for X in range(num1, 0, -1):
        TOTAL_X = TOTAL_X* X
    return TOTAL_X


def sum_odd_numbers(num2):
    Y = 1
    TOTAL_Y = 0

    while Y <= num2:
        if Y%2 == 1:
            TOTAL_Y = TOTAL_Y + Y
        Y = Y + 1
    return TOTAL_Y

def main_menu():
    print("Main Menu\option1-FACTORIAL\option2-SUM ODD NUMBERS\option3-EXIT")
    
def run_menu():
    OPTION = 0

    while OPTION != 3: 
        main_menu()
        OPTION = int(input("PLEASE ENTER YOUR SELECTION: "))
        run_the_option(OPTION)

    def run_the_option(OPTION):
        if OPTION == 1:
            NUM1 = int(input("PLEASE ENTER A NUMBER: "))
        if NUM1 > 0 and NUM1 < 10:
            RESULT1 = get_factorial(NUM1)
            print("RESULT: ", RESULT1)
        else:
            print("PLEASE ENTER A NUMBER AGAIN")

        elif OPTION == 2:
            NUM2 = int(input("ENTER A NUMBER: "))
        if NUM2 > 0 and NUM2 < 100:
            RESULT2 = sum_odd_numbers(NUM2)
            print("RESULT: ", RESULT2)
        else:
            print("PLEASE ENTER A NUMBER AGAIN")
        elif OPTION == 3:
        print("CONTINUE?\option1-yes\option2-no")
        OPTION2 = int(input("PLEASE ENTER YOUR SELECTION: "))

        if OPTION2 == 1:
            run_menu()

        elif OPTION2 == 2:
            ask_for_exit()
            
        else:
            print("INVALID OPTION")
            exit()

def ask_for_exit():
    CHOICE = input("EXIT?\ENTER Y OR N")

    if CHOICE == "Y" or CHOICE == "y":
        print("EXIT")
        exit()
    
    else:
        print("INVALID")
        exit()
    
    