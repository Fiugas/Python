import os

while(True):
    try:
        os.system("cls")

        option = int(input("==========================================\
            \n    Chose the option you want to run\
            \n 1.  Modeling the fishing pound population\
            \n 2.  2D data visualization\
            \n 3.  3D data visualization\
            \n 4.  Graph theory\
            \n 5.  Data and Statistisc whith Python\
            \n   Exercise: "))
    except:
        os.system("cls")
        option = 99

    if option == 1:
        os.system("cls")
        print()

    elif option == 2:
        os.system("cls")

    elif option == 3:
        os.system("cls")
    
    elif option == 4:
        os.system("cls")

    elif option == 5:
        os.system("cls")
    
    else:
        print("Please select a valid option")
        input("Press enter to continue.....")