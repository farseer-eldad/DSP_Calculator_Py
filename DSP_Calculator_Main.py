import recipeListing

basic_fabricator_factor = 0.75
advanced_fabricator_factor = 1

basic_furnace_factor = 4/3

#Liste der Productionskette im Fomat: {<name>:[<amount_per_sec>,<number_basic_fabs>,<number_adv_fabs>]}
product_list = {}

#material as String and wanted in 1/second
def calculate_per_second(res,wanted):
    material = recipeListing.recipes[res]


    if material:
        base_production = material[2]*advanced_fabricator_factor                    #Productiontime for 1 Advanced Fabricator or the Player
        base_production_speed = material[3]/base_production                         #Productionspeed in n/s per Advanced Fabricator
        slowed_production_speed = base_production_speed*basic_fabricator_factor     #Productionspeed in n/s per Basic Fabricator

        basic_fabricators = wanted/slowed_production_speed              #Amount of Basic Fabricators needed
        advanced_fabricators = wanted/base_production_speed             #Amount of Advanced Fabricators needed

        for v in range(len(material[0])):
            per_sec = material[1][v]*advanced_fabricators
            calculate_per_second(material[0][v],per_sec)
        if res in product_list:
            product_list[res] = [product_list[res][0]+wanted,product_list[res][1]+basic_fabricators,product_list[res][2]+advanced_fabricators]
        else:
            product_list[res] = [wanted,basic_fabricators,advanced_fabricators]
        return 1
    else:
        if res in product_list:
            product_list[res] = [product_list[res][0]+wanted,0,0]
        else:
            product_list[res] = [wanted,0,0]
        return 0
    
def display_Product_List():
    for n,a in product_list.items():
        print(n + "\nAmount per Second: " + str(a[0]) + "\nNumber of Fabricators: " + str(a[1]) +" (" + str(a[2]) + ")\n")

material = input("Which Material?\n")
amount = float(input(material + " per Second?\n"))

calculate_per_second(material,amount)

print("\n-------------------------------------------------------------\n")

display_Product_List()

