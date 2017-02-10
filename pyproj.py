#this is a game that will be created largly upon whim. 

#imports
from random import *

#classes
class Hero ():
        def __init__(self,name):
                self.level = 1
                self.health = 100
                self.inventory =[]
                self.name = name
                self.position = (0,0)
                self.char = "t"
        def add_item(self,item):
                self.inventory += item

class Room():
        def __init__(self,area):
                self.items = []
                self.mobs = []
                self.area = []
                self.entities = {}
                for row in range(10):
                        self.area.append([])
                        for col in range(10):
                                self.area[row].append("x")
        def place_entity(self,entity):
                self.entities[entity] = entity.position
                self.area[entity.position[0]][entity.position[1]] = entity.char
        def show(self):
                for row in self.area:
                        print(row)
room_1 = []
room_1 = Room(room_1)
new_name = input("what is your name Hero?").capitalize()
player = Hero(new_name)
room_1.place_entity(player)
room_1.show()
print("Hello {}. You are level {}, you have {} health and you have {} in your inventory...welcome".format(player.name,player.level,player.health,player.inventory))
test_1 = input("would you like to grab the apple and add it to your inventory? yes/no ").lower().strip()
apple = ["apple"]
if test_1 == "yes":
        player.add_item(apple)
else:
        pass
print(player.inventory)
test_2 = input("would you like to grab the stick and add it to your inventory? yes/no").lower().strip()
stick = ["stick"]
if test_2 == "yes":
        player.add_item(stick)
else:
        pass
print(player.inventory)

