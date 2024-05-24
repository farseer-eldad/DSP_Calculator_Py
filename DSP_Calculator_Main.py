import recipeListing
import funktions

from dataclasses import dataclass

cmd_list = {1:["calc_to","Calculate the downstream of a Rescource"],
            2:["calc_from","Calculate the upstream from a Rescource"],
            3:["quit","Ends the Program"],
            4:["disall","displays all available Rescources"],
            5:["help","displays avialable commands"],
            6:["disres","displays a chosen Recipe"]}

run = True

while run:
    #Liste der Productionskette im Fomat: {<name>:[<amount_per_sec>,<number_basic_fabs>,<number_adv_fabs>]}
    product_list = {}
    user_in = input("What Operation?\n")
    if user_in == cmd_list[1][0]:
        user_in = input("What Rescource?\n")
        if user_in in recipeListing.recipes:   
            amount = input(user_in + " per Second?\n")
            try:
                a = float(amount)
                product_list = funktions.calculate_per_second(user_in,a,product_list)
                print("\n-------------------------------------------------------------\n")
                funktions.display_Product_List(product_list)
            except ValueError:
                print("Not a Number!")
    elif user_in == cmd_list[2][0]:
        user_in = input("What Rescource?\n")
        if user_in in recipeListing.recipes:   
            amount = input(user_in + " per Second?\n")
            try:
                a = float(amount)
                product_list = funktions.calculate_from_source(user_in,a,product_list)
                print("\n-------------------------------------------------------------\n")
                funktions.display_Product_List(product_list)
            except ValueError:
                print("Not a Number!\n")
    elif user_in == cmd_list[3][0]:
        print("Shutting down...")
        run = False
        continue
    elif user_in == cmd_list[4][0]:
        funktions.display_All_Items()
        continue
    elif user_in == cmd_list[5][0]:
        funktions.print_cmds(cmd_list)
        continue
    elif user_in == cmd_list[6][0]:
        user_in = input("What Rescource?\n")
        if user_in in recipeListing.recipes:   
            product_list = funktions.show_recipe(user_in)
        continue
    else:
        print("Material Exisitert nicht")

