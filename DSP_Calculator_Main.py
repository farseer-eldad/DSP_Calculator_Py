import Recipes

basic_fabricator_factor = 0.75
advanced_fabricator_factor = 1

basic_furnace_factor = 4/3



#material as String and wanted in 1/second
def calculate_per_second(res,wanted):
    material = Recipes.recipes[res]


    if material:
        base_production = material[2]*advanced_fabricator_factor                    #Productiontime for 1 Advanced Fabricator or the Player
        base_production_speed = material[3]/base_production                         #Productionspeed in n/s per Advanced Fabricator
        slowed_production_speed = base_production_speed*basic_fabricator_factor     #Productionspeed in n/s per Basic Fabricator

        basic_fabricators = wanted/slowed_production_speed              #Amount of Basic Fabricators needed
        advanced_fabricators = wanted/base_production_speed             #Amount of Advanced Fabricators needed

        print(res + "\nAmount per Second: " + str(wanted) + 
              "\nFabricators needed: " + str(basic_fabricators) + 
              " (" + str(advanced_fabricators) + ")\n\n")

        for v in range(len(material[0])):
            per_sec = material[1][v]*advanced_fabricators
            calculate_per_second(material[0][v],per_sec)
    else:
        print(res + "\nAmount per Second: " + str(wanted) + "\nFabricators needed: Rescource Extractor\n\n")
    
material = input("Which Material?\n")
amount = float(input(material + " per Second?\n"))

product_list = []

calculate_per_second(material,amount)