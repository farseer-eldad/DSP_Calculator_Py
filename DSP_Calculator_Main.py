import recipeListing
import funktions

from dataclasses import dataclass


run = True

while run:
    #Liste der Productionskette im Fomat: {<name>:[<amount_per_sec>,<number_basic_fabs>,<number_adv_fabs>]}
    product_list = {}
    user_in = input("Which Material?\n")
    

    if user_in in recipeListing.recipes:   
        amount = input(user_in + " per Second?\n")
        try:
            a = float(amount)
            product_list = funktions.calculate_per_second(user_in,a,product_list)
        except ValueError:
            print("Not a Number!")
    elif user_in == "quit":
        print("Shutting down...")
        run = False
        continue
    elif user_in == "disall":
        funktions.display_All_Items()
        continue
    else:
        print("Material Exisitert nicht")

    print("\n-------------------------------------------------------------\n")

    funktions.display_Product_List(product_list)

