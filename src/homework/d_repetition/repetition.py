#factorial function using a for range loop
def get_factorial(num1):
    total_x=1
    for x in range(num1, 0, -1):
        total_x=tptal_x*x
    return total_x

def sum_odd_numbers(num2):
    y=1
    total_y=0
    while y<=num2:
        if y%2==1:
            total_y=total_y+y
        y=y+1
    return total_y
    
    