#!/usr/local/bin/python3

#this is a game that will be created largly upon whim.

#imports
from random import *

EMPTY_POSITION = '-'
ROOM_HEIGHT = 5
ROOM_WIDTH = 5

#classes
class Game():
        def __init__(self, player):
                self.rooms = []
                self.characters = [player]
                self.player = player

        def show(self):
                room = self.player.room
                room.show()
                self.player.show()

        def turn_crank(self):
                for room in self.rooms:
                    room.reset_area(self.characters)
                self.show()

class Hero():
        def __init__(self, name, row, col):
                self.level = 1
                self.health = 100
                self.inventory = []
                self.name = name
                self.char = "+"

                self.room = None
                self.row = row
                self.col = col

                self.position = (0,0)

        def add_item(self,item):
                self.inventory += item

        def show(self):
                print("== {}'s Stats ==".format(self.name))
                print("Level: {}".format(self.level))
                print("Health: {}".format(self.health))
                print("Holding: {}".format(", ".join(self.inventory)))

class Room():
        def __init__(self, name):
                self.name = name
                self.items = []
                self.mobs = []
                self.entities = {}

                # # initialize field of play for this room
                # self.area = []

        def reset_area(self, characters):
                self.area = []
                for row in range(ROOM_HEIGHT):
                        self.area.append([])
                        for col in range(ROOM_WIDTH):
                                self.area[row].append(EMPTY_POSITION)
                for character in characters:
                        if character.room == self:
                                self.area[character.row][character.col] = character.char

        def show(self):
                for row in self.area:
                        print("".join(row))

new_name = input("what is your name Hero?").capitalize()
player = Hero(new_name, row=0, col=2)

game = Game(player=player)

room_1 = Room("Hall of the Mountain King")
game.rooms.append(room_1)

room_2 = Room("A maze of twisty little passages, all different")
game.rooms.append(room_2)

player.room = room_1

game.turn_crank()

test_1 = input("would you like to grab the apple and add it to your inventory? yes/no ").lower().strip()
apple = ["apple"]
if test_1 == "yes":
        player.add_item(apple)
else:
        pass
game.turn_crank()

test_2 = input("would you like to grab the stick and add it to your inventory? yes/no").lower().strip()
stick = ["stick"]
if test_2 == "yes":
        player.add_item(stick)
else:
        pass
game.turn_crank()
