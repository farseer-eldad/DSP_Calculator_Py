import recipeListing
import funktions

run = True

while run:
    #Liste der Productionskette im Fomat: {<name>:[<amount_per_sec>,<number_basic_fabs>,<number_adv_fabs>]}
    product_list = {}
    material = input("Which Material?\n")
    

    if material in recipeListing.recipes:   
        amount = input(material + " per Second?\n")
        try:
            a = float(amount)
            product_list = funktions.calculate_per_second(material,a,product_list)
        except ValueError:
            print("Not a Number!")
    elif material == "quit":
        print("Shutting down...")
        run = False
        continue
    else:
        print("Material Exisitert nicht")

    print("\n-------------------------------------------------------------\n")

    funktions.display_Product_List(product_list)

