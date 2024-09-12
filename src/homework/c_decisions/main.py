#
import decisions
def main():
    option=int(input ("Enter Option:"))
    total=int(input("Enter Total: "))

    result1=decisions.get_options_ratio(option, total)
    result2= decisions.get_faculty_rating(result1)
    print ("Ratio: ", )


