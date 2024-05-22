import Recipes

basic_fabricator_factor = 4/3
advanced_fabricator_factor = 1

basic_furnace_factor = 4/3



#material as String and wanted in 1/second
def calculate_per_second(material,wanted):
    material = Recipes.recipes[material]


    if material[material]:
        base_production = material[3]*advanced_fabricator_factor                    #Productiontime for 1 Advanced Fabricator or the Player
        base_production_speed = 1/(base_production*material[4])                     #Productionspeed in n/s per Advanced Fabricator
        slowed_production_speed = base_production_speed*basic_fabricator_factor     #Productionspeed in n/s per Basic Fabricator

        basic_fabricators = wanted/slowed_production_speed              #Amount of Basic Fabricators needed
        advanced_fabricators = wanted/base_production_speed             #Amount of Advanced Fabricators needed

        print('Amount per Second: ' + wanted + '\nFabricators needed: ' + basic_fabricators + ' (' + advanced_fabricators + ')')

        for v in range(material[0]):
            calculate_per_second(material[0][v],material[1][v])
    else:
        print('Amount per Second: ' + wanted + '\nFabricators needed: Rescource Extractor')
    
material = input("Which Material?\n")
amount = input(material + " per Second?\n")

calculate_per_second(material,amount)