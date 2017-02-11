#!/usr/local/bin/python3

#this is a game that will be created largly upon whim.

#imports
from random import *

EMPTY_POSITION = '.'
ROOM_HEIGHT = 5
ROOM_WIDTH = 5

#classes
class Game():
        def __init__(self):
                self.rooms = []
                self.characters = []

class Hero():
        def __init__(self, name, room, row, col):
                self.level = 1
                self.health = 100
                self.inventory = []
                self.name = name
                self.char = "t"

                self.room = room
                self.row = row
                self.col = col

                self.position = (0,0)

        def add_item(self,item):
                self.inventory += item

class Room():
        def __init__(self, name):
                self.name = name
                self.items = []
                self.mobs = []
                self.entities = {}

                # setup field of play for this room
                self.area = []

        def reset_area(self, game):
                for row in range(ROOM_HEIGHT):
                        self.area.append([])
                        for col in range(ROOM_WIDTH):
                                self.area[row].append(EMPTY_POSITION)
                for character in game.characters:
                        if character.room == self:
                                self.area[character.row][character.col] = character.char

        # def place_entity(self, entity):
        #         entity.row =
        #         self.entities[entity] = entity.position
        #         self.reset_area()

        def show(self, g):
                print("======= {} =======".format(self.name))
                self.reset_area(g)
                for row in self.area:
                        print("".join(row))

game = Game()
room_1 = Room("Hall of the Mountain King")
game.rooms.append(room_1)

room_2 = Room("A maze of twisty little passages, all different")
game.rooms.append(room_2)

new_name = input("what is your name Hero?").capitalize()
player = Hero(new_name, room=room_1, row=0, col=2)

game.characters.append(player)

# room_1.place_entity(player)
room_1.show(game)
room_2.show(game)
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
