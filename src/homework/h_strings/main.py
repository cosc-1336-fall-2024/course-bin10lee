#
import strings
def main():
    print("MENU|1.Hamming Distance|2.Dna Complement|3.Exit")

    option=int(input("Please enter your selection: "))

    if option==1:
            dna1=input("Please enter DNA1: ")
            dna2=input("Please enter DNA2: ")
            result=strings.get_hamming_distance(dna1, dna2)
            print("Result: ", result)

    elif option==2:
            dna=input("Please enter DNA:")
            result1=strings.get_dna_complement(dna)
            print("Result: ", result1)
        
    elif option==3:
            print("Exit")
            exit()

main()


