from retrograde import *
from modules import *

import os
''' 
Ships and buildings are the actors in the game world. They are composed of a list of modules that support each other and add their own abilities.
They can also be used to store module lists, for instance to gift to the player in a certain scenario.

They are stored as lists of modules or as portable serialized files.

They are wrapped in an actor class when they are put into the game world. This is done later to improve portability of the ship object, with the hope that the player will enjoy a collection of custom ships or the ability to share them.

'''

def shipyard(shipType):
	# first, search through serialised files to find one matching the name.


	directoryString = "ships/"
	directory = os.fsencode(directoryString)

	for file in os.listdir(directory):
	     filename = os.fsdecode(file)
	     if filename == shipType:
	         print(filename)
	         return dill.load(open(directoryString+shipType, 'rb'))
	    
	# if there was no user definition of it, load it from the defaults.
	if shipType == 'rocket_1':
 		return [
			Module('generator',[0,0]),
			Module('engine 10',[0,15]),
			Module('RCS',[0,-10]) ]

	elif shipType == 'rocket_2':
		return [
			Module('generator',[0,0]),
			Module('engine 10',[-13,8],0.6/math.pi),
			Module('engine 10',[13,8],-0.6/math.pi),
			Module('RCS',[-13,-10]),
			Module('RCS',[13,-10]) ,
			Module('cannon 10',[0,-10]) ]

	elif shipType == 'building_1':
		return [
			Module('spar 10',[0,-100],(0.5* math.pi)),
			Module('box 10',[0,0])]

	elif shipType == 'space_station_1':
		return [
			Module('box 100',[0,0]),
			Module('spar 100',[1000,0],0.5 * math.pi),
			Module('box 100',[-1000,0]),
			Module('box 100',[2000,0]),
			Module('box 100',[-2000,0]),
			Module('box 100',[3000,0]),
			Module('docking port',[0,507.5]),
			Module('solar panel',[0,-550]),
			Module('solar panel',[200,-550]),
			Module('solar panel',[-200,-550])]

	elif shipType == 'derelict_hyperunit':
		return [
			Module('hyperdrive 10',[0,0])]

	elif shipType == 'ida_frigate':
		return [
			Module('generator',[0,50]),
			Module('engine 10',[-13,58],0.6/math.pi),
			Module('engine 10',[13,58],-0.6/math.pi),
			Module('RCS',[-13,40]),
			Module('RCS',[13,40]) ,
			Module('box 10',[0,10]),
			Module('box 10',[0,-40]),
			Module('hyperdrive 10',[0,-75]),
			Module('RCS',[-13,-70]),
			Module('RCS',[13,-70]) ]

	elif shipType == 'smallParts':
		return [
			Module('generator',[0,0]),
			Module('generator',[0,0]),
			Module('engine 10',[0,0]),
			Module('engine 10',[0,0]),
			Module('RCS',[0,0]),
			Module('hyperdrive 10',[0,-75]),
			Module('cannon 10',[0,-10]),
			Module('cannon 10',[0,-10]),
			Module('box 10',[0,10]),
			Module('spar 10',[0,-100],(0.5* math.pi)),
			Module('starbridge armor',[0,10]),
			Module('starbridge armor',[0,10]),
			Module('starbridge armor',[0,10]),
			Module('starbridge armor',[0,10]),
			Module('starbridge armor',[0,10]),
			Module('starbridge armor',[0,10]),
			Module('box 5',[0,10]),
			Module('turret 10',[0,-100],(0.5* math.pi)),
			Module('turret 10',[0,-100],(0.5* math.pi)),
			


			]

	elif shipType == 'bigParts':
		return [
			Module('spar 10',[0,-100],(0.5* math.pi)),
			Module('spar 10',[0,-100],(0.5* math.pi)),
			Module('spar 100',[0,-100],(0.5* math.pi)),
			Module('spar 100',[0,-100],(0.5* math.pi)),
			Module('engine 100',[0,-100],(0.5* math.pi)),
			Module('engine 100',[0,-100],(0.5* math.pi)),
			Module('RCS 100',[0,-100],(0.5* math.pi)),
			Module('RCS 100',[0,-100],(0.5* math.pi)),
			Module('dome 100',[0,-100],(0.5* math.pi)),
			
			Module('docking port',[0,507.5]),

			Module('docking port',[0,507.5]),
			Module('solar panel',[0,-550]),
			Module('solar panel',[200,-550]),
			Module('solar panel',[0,-550]),
			Module('solar panel',[200,-550]),


			]

	elif shipType == 'sport parts':
		return [
			Module('fighter RCS',[0,0]),
			Module('fighter RCS',[0,0]),
			Module('fighter RCS',[0,0]),
			Module('fighter RCS',[0,0]),
			]

	elif shipType == 'nano orbital section':
		return [
			Module('nano orbital',[0,0],(0))
			


			]

