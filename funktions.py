import recipeListing
import math

from dataclasses import dataclass


basic_fabricator_factor = 0.75
advanced_fabricator_factor = 1
basic_furnace_factor = 4/3

belt_1, belt_2, belt_3 = 6, 12, 30


#material as String and wanted in 1/second
def calculate_per_second(res,wanted,product_list):
    material = recipeListing.recipes[res]


    if material:
        base_production = material[2]*advanced_fabricator_factor                    #Productiontime for 1 Advanced Fabricator or the Player
        base_production_speed = material[3]/base_production                         #Productionspeed in n/s per Advanced Fabricator
        slowed_production_speed = base_production_speed*basic_fabricator_factor     #Productionspeed in n/s per Basic Fabricator

        basic_fabricators = wanted/slowed_production_speed              #Amount of Basic Fabricators needed
        advanced_fabricators = wanted/base_production_speed             #Amount of Advanced Fabricators needed

        belts = [math.ceil(wanted/belt_1),math.ceil(wanted/belt_2),math.ceil(wanted/belt_3)]

        for v in range(len(material[0])):
            per_sec = (material[1][v]/base_production)*advanced_fabricators
            product_list = calculate_per_second(material[0][v],per_sec,product_list)
        if res in product_list:
            product_list[res] = [product_list[res][0]+wanted,product_list[res][1]+basic_fabricators,product_list[res][2]+advanced_fabricators,[product_list[res][3][0]+belts[0],product_list[res][3][1]+belts[1],product_list[res][3][2]+belts[2]]]
        else:
            product_list[res] = [wanted,basic_fabricators,advanced_fabricators,belts]
        return product_list
    else:
        if res in product_list:
            product_list[res] = [product_list[res][0]+wanted,0,0,[0,0,0]]
        else:
            product_list[res] = [wanted,0,0,[0,0,0]]
        return product_list
    
def display_Product_List(product_list):
    for n,a in product_list.items():
        print(n + "\nAmount per Second:\t" + str(a[0]) + "\nNumber of Fabricators:\t" + str(a[1]) +" (" + str(a[2]) 
              + ")\nBelts Mk1 (Mk2) [Mk3]\t" + str(a[3][0]) + " (" + str(a[3][1]) + ") [" + str(a[3][2]) + "]\n")
        
def display_All_Items():
    line, line_max = 0,4
    print("\n")
    for n in recipeListing.recipes:
        if line < line_max:    
            print(n)
            line += 1
        else:
            print(n + "\n")
            line = 0
    print("\n")