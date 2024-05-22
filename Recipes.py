recipes = {

#Base Rescources
'Iron Ore':[],
'Copper Ore':[],


#Smelter Recipes  <name>: [[<material_1>,....,material_n>],[amount_1,....,amount_n],<base_production_time>,<yield>]
#production_time is in seconds
"Iron Ingot":       [["Iron Ore"],[1],1,1],
"Magnet":           [["Iron Ore"],[1],1.5,1],
"Copper Ingot":     [["Copper Ore"],[1],1,1],

#Assembler Recipes <name>: ([<material_1>,....,material_n>],[amount_1,....,amount_n],<base_production_time>,<yield>)
#production_time is in seconds
"Gear":             [["Iron Ingot"],[1],1,1],
"Steel":            [["Iron Ingot"],[1],3,1],
"Circuit Board":    [["Iron Ingot","Copper Ingot"],[2,1],1,2],
"Magnetic Coil":    [["Magnet","Copper Ingot"],[2,1],1,2],
"Electric Motor":   [["Iron Ingot","Gear","Magnetic Coil"],[2,1,1],2,1]
}