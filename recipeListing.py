recipes = {
	"Gear":						[["Iron Ingot"],[1],1,1],
	"Magnetic Coil":						[["Magnet","Copper Ingot"],[2,1],1,2],
	"Prism":						[["Glass"],[3],2,2],
	"Plasma Exciter":						[["Magnetic Coil","Prism"],[4,2],2,1],
	"Hydrogen Fuel Rod":						[["Titanium Ingot","Hydrogen"],[1,10],6,2],
	" - Thruster":						[["Steel","Copper Ingot"],[2,3],4,1],
	"Reinforced Thruster":						[["Titanium Alloy","Electromagnetic Turbine"],[5,5],6,1],
	"Titanium Crystal":						[["Organic Crystal","Titanium Ingot"],[1,3],4,1],
	"Casimir Crystal":						[["Titanium Crystal","Graphene","Hydrogen"],[1,2,12],4,1],
	"Casimir Crystal (Advanced)":						[["Optical Grating Crystal","Graphene","Hydrogen"],[8,2,12],4,1],
	"Titanium Glass":						[["Glass","Titanium Ingot","Water"],[2,2,2],5,2],
	"Particle Broadband":						[["Carbon Nanotube","Crystal Silicon","Plastic"],[2,2,1],8,1],
	"Plane Filter":						[["Casimir Crystal","Titanium Glass"],[1,2],12,1],
	"Deuteron Fuel Rod":						[["Titanium Alloy","Deuterium","Super-Magnetic Ring"],[1,20,1],12,2],
	"Annihilation Constraint Sphere":						[["Particle Container","Processor"],[1,1],20,1],
	"Antimatter Fuel Rod":						[["Antimatter","Hydrogen","Annihilation Constraint Sphere","Titanium Alloy"],[12,12,1,1],24,2],
	"Circuit Board":						[["Iron Ingot","Copper Ingot"],[2,1],1,2],
	"Processor":						[["Circuit Board","Microcrystalline Component"],[2,2],3,1],
	"Quantum Chip":						[["Processor","Plane Filter"],[2,2],6,1],
	"Microcrystalline Component":						[["High-Purity Silicon","Copper Ingot"],[2,1],2,1],
	"Organic Crystal (Original)":						[["Log","Plant Fuel","Water"],[20,30,10],6,1],
	"Crystal Silicon (Advanced)":						[["Fractal Silicon"],[1],1.5,2],
	"Photon Combiner":						[["Prism","Circuit Board"],[2,1],3,1],
	"Photon Combiner (Advanced)":						[["Optical Grating Crystal","Circuit Board"],[1,1],3,1],
	"Solar Sail":						[["Graphene","Photon Combiner"],[1,1],4,2],
	"Space Warper":						[["Graviton Lens"],[1],10,1],
	"Space Warper (Advanced)":						[["Gravity Matrix"],[1],10,8],
	"Frame Material":						[["Carbon Nanotube","Titanium Alloy","High-Purity Silicon"],[4,1,1],6,1],
	"Dyson Sphere Component":						[["Frame Material","Solar Sail","Processor"],[3,3,3],8,1],
	"Small Carrier Rocket":						[["Dyson Sphere Component","Deuteron Fuel Rod","Quantum Chip"],[2,4,2],6,1],
	"Logistics Drone":						[["Iron Ingot","Processor","Thruster"],[5,2,2],4,1],
	"Logistics Vessel":						[["Titanium Alloy","Processor","Reinforced Thruster"],[10,10,2],6,1],
	"Electric Motor":						[["Iron Ingot","Gear","Magnetic Coil"],[2,1,1],2,1],
	"Electromagnetic Turbine":						[["Electric Motor","Magnetic Coil"],[2,2],2,1],
	"Particle Container":						[["Electromagnetic Turbine","Copper Ingot","Graphene"],[2,2,2],4,1],
	"Particle Container (Advanced)":						[["Unipolar Magnet","Copper Ingot"],[10,2],4,1],
	"Graviton Lens":						[["Diamond","Strange Matter"],[4,1],6,1],
	"Super-Magnetic Ring":						[["Electromagnetic Turbine","Magnet","Energetic Graphite"],[2,3,1],3,1],
	"Proliferator Mk.I":						[["Coal"],[1],.5,1],
	"Proliferator Mk.II":						[["Proliferator Mk.I","Diamond"],[2,1],1,1],
	"Proliferator Mk.III":						[["Proliferator Mk.II","Carbon Nanotube"],[2,1],2,1],
	"Foundation":						[["Stone Brick","Steel"],[3,1],1,1],
	"Logistics Bot":						[["Iron Ingot","Electromagnetic Turbine","Processor"],[2,1,1],2,1],
	"Plastic":						[["Refined Oil","Energetic Graphite"],[2,1],3,1],
	"Sulfuric Acid":						[["Refined Oil","Stone","Water"],[6,8,4],6,4],
	"Organic Crystal":						[["Plastic","Refined Oil","Water"],[2,1,1],6,1],
	"Graphene":						[["Energetic Graphite","Sulfuric Acid"],[3,1],3,2],
	"Carbon Nanotube":						[["Graphene","Titanium Ingot"],[3,1],4,2],
	"Carbon Nanotube (Advanced)":						[["Spiniform Stalagmite Crystal"],[6],4,2],
	"Deuterium":						[["Hydrogen"],[10],2.5,5],
	"Strange Matter":						[["Particle Container","Iron Ingot","Deuterium"],[2,2,10],8,1],
	"Reforming Refine":						[["Refined Oil","Hydrogen","Coal"],[2,1,1],4,3],
	"Electromagnetic Matrix":						[["Magnetic Coil","Circuit Board"],[1,1],3,1],
	"Energy Matrix":						[["Energetic Graphite","Hydrogen"],[2,2],6,1],
	"Structure Matrix":						[["Diamond","Titanium Crystal"],[1,1],8,1],
	"Information Matrix":						[["Processor","Particle Broadband"],[2,1],10,1],
	"Gravity Matrix":						[["Graviton Lens","Quantum Chip"],[1,1],24,2],
	"Universe Matrix":						[["Electromagnetic Matrix","Energy Matrix","Structure Matrix","Information Matrix","Gravity Matrix","Antimatter"],[1,1,1,1,1,1],15,1],
	"Iron Ingot":						[["Iron Ore"],[1],1,1],
	"Magnet":						[["Iron Ore"],[1],1.5,1],
	"Copper Ingot":						[["Copper Ore"],[1],1,1],
	"Stone Brick":						[["Stone"],[1],1,1],
	"Energetic Graphite":						[["Coal"],[2],2,1],
	"Silicon Ore":						[["Stone"],[10],10,1],
	"Crystal Silicon":						[["High-Purity Silicon"],[1],2,1],
	"Glass":						[["Stone"],[2],2,1],
	"High-Purity Silicon":						[["Silicon Ore"],[2],2,1],
	"Diamond":						[["Energetic Graphite"],[1],2,1],
	"Diamond (Advanced)":						[["Kimberlite Ore"],[1],1.5,2],
	"Steel":						[["Iron Ingot"],[3],3,1],
	"Titanium Ingot":						[["Titanium Ore"],[2],2,1],
	"Titanium Alloy":						[["Titanium Ingot","Steel","Sulfuric Acid"],[4,4,8],12,4],
	"Wind Turbine":						[["Iron Ingot","Gear","Magnetic Coil"],[6,1,3],4,1],
	"Tesla Tower":						[["Iron Ingot","Magnetic Coil"],[2,1],1,1],
	"Matrix Lab":						[["Iron Ingot","Glass","Circuit Board","Magnetic Coil"],[8,4,4,4],3,1],
	"Wireless Power Tower":						[["Tesla Tower","Plasma Exciter"],[1,3],3,1],
	"Oil Extractor":						[["Steel","Stone Brick","Circuit Board","Plasma Exciter"],[12,12,6,4],8,1],
	"Oil Refinery":						[["Steel","Stone Brick","Circuit Board","Plasma Exciter"],[10,10,6,6],6,1],
	"Chemical Plant":						[["Steel","Stone Brick","Glass","Circuit Board"],[8,8,8,2],5,1],
	"Miniature Particle Collider":						[["Titanium Alloy","Frame Material","Super-Magnetic Ring","Graphene","Processor"],[20,20,25,10,8],15,1],
	"Artificial Star":						[["Titanium Alloy","Frame Material","Annihilation Constraint Sphere","Quantum Chip"],[20,20,10,10],30,1],
	"Assembling Machine Mk.I":						[["Iron Ingot","Gear","Circuit Board"],[4,8,4],2,1],
	"Assembling Machine Mk.II":						[["Assembling Machine Mk.I","Graphene","Processor"],[1,8,4],3,1],
	"Assembling Machine Mk.III":						[["Assembling Machine Mk.II","Particle Broadband","Quantum Chip"],[1,8,2],4,1],
	"Mining Machine":						[["Iron Ingot","Circuit Board","Magnetic Coil","Gear"],[4,2,2,2],3,1],
	"Water Pump":						[["Iron Ingot","Stone Brick","Electric Motor","Circuit Board"],[8,4,4,2],4,1],
	"Arc Smelter":						[["Iron Ingot","Stone Brick","Circuit Board","Magnetic Coil"],[4,2,4,2],3,1],
	"Thermal Power Plant":						[["Iron Ingot","Stone Brick","Gear","Magnetic Coil"],[10,4,4,4],5,1],
	"Solar Panel":						[["Copper Ingot","High-Purity Silicon","Circuit Board"],[10,10,5],6,1],
	"EM-Rail Ejector":						[["Steel","Gear","Processor","Super-Magnetic Ring"],[20,20,5,10],6,1],
	"Ray Receiver":						[["Steel","High-Purity Silicon","Photon Combiner","Processor","Super-Magnetic Ring"],[20,20,10,5,20],8,1],
	"Satellite Substation":						[["Wireless Power Tower","Super-Magnetic Ring","Frame Material"],[1,10,2],5,1],
	"Accumulator":						[["Iron Ingot","Super-Magnetic Ring","Crystal Silicon"],[6,1,3],3,1],
	"Energy Exchanger":						[["Titanium Alloy","Steel","Processor","Particle Container"],[40,40,40,8],15,1],
	"Vertical Launching Silo":						[["Titanium Alloy","Frame Material","Graviton Lens","Quantum Chip"],[80,30,20,10],30,1],
	"Conveyor Belt MK.I":						[["Iron Ingot","Gear"],[2,1],1,3],
	"Conveyor Belt MK.II":						[["Conveyor Belt MK.I","Electromagnetic Turbine"],[3,1],1,3],
	"Conveyor Belt MK.III":						[["Conveyor Belt MK.II","Super-Magnetic Ring","Graphene"],[3,1,1],1,3],
	"Sorter MK.I":						[["Iron Ingot","Circuit Board"],[1,1],1,1],
	"Sorter MK.II":						[["Sorter MK.I","Electric Motor"],[2,1],1,2],
	"Sorter MK.III":						[["Sorter MK.II","Electromagnetic Turbine"],[2,1],1,2],
	"Storage MK.I":						[["Iron Ingot","Stone Brick"],[4,4],2,1],
	"Storage MK.II":						[["Steel","Stone Brick"],[8,8],4,1],
	"Splitter":						[["Iron Ingot","Gear","Circuit Board"],[3,2,1],2,1],
	"Planetary Logistics Station":						[["Steel","Titanium Ingot","Processor","Particle Container"],[40,40,40,20],20,1],
	"Interstellar Logistics Station":						[["Planetary Logistics Station","Titanium Alloy","Particle Container"],[1,40,20],30,1],
	"Spray Coater":						[["Steel","Plasma Exciter","Circuit Board","Microcrystalline Component"],[4,2,2,2],3,1],
	"Fractionator":						[["Steel","Stone Brick","Glass","Processor"],[8,4,4,1],3,1],
	"Orbital Collector":						[["Interstellar Logistics Station","Super-Magnetic Ring","Reinforced Thruster","Accumulator (Full)"],[1,50,20,20],30,1],
	"Mini Fusion Power Plant":						[["Titanium Alloy","Super-Magnetic Ring","Carbon Nanotube","Processor"],[12,10,8,4],10,1],
	"Storage Tank":						[["Iron Ingot","Stone Brick","Glass"],[8,4,4],2,1],
	"Plane Smelter":						[["Arc Smelter","Frame Material","Plane Filter","Unipolar Magnet"],[1,5,4,15],5,1],
	"Traffic Monitor":						[["Iron Ingot","Gear","Glass","Circuit Board"],[3,2,1,2],2,1],
	"Geothermal Power Station":						[["Steel","Copper Ingot","Photon Combiner","Super-Magnetic Ring"],[15,20,4,1],6,1],
	"Advanced Mining Machine":						[["Titanium Alloy","Frame Material","Super-Magnetic Ring","Quantum Chip","Optical Grating Crystal"],[20,10,10,4,40],20,1],
	"Automatic Piler":						[["Steel","Gear","Super-Magnetic Ring","Processor"],[3,4,1,2],4,1],
	"Logistics Distributor":						[["Iron Ingot","Plasma Exciter","Processor"],[8,4,4],8,1],
	"Quantum Chemical Plant":						[["Chemical Plant","Titanium Glass","Strange Matter","Quantum Chip"],[1,10,3,3],10,1],
	"Silicon Ore":	[],
    "Iron Ore":		[],
    "Copper Ore":	[],
    "Stone":		[],
    "Titanium Ore":	[]
}