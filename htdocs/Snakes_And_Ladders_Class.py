#This file contains the basic classes.

import random
class Player:
	def __init__(self, name, position = 0):
		self.name = name
		self.position = position
	def __repr__(self):
		return "Player {} is at position {}.<br/>".format(self.name, self.position)
			
class Snake:
	def __init__(self, from_position, to_position):
		self.from_position = from_position
		self.to_position = to_position
	def is_valid(self):
		if self.from_position < self.to_position:
			print("Invalid snake positions. Change the positions.<br/>")
			return False
		return True
		
class Ladder:
	def __init__(self, from_position, to_position):
		self.from_position = from_position
		self.to_position = to_position
		
	def is_valid(self):
		if self.from_position > self.to_position:
			print("Invalid ladder positions. Change the positions.<br/>")
			return False
		return True
		
class Board:
	def __init__(self, players, snakes, ladders):
		self.players = players
		self.snakes = snakes
		self.ladders = ladders
	def play_round(self):
		for i in range(0, len(self.players)):
			print(self.players[i])
			dice_count = random.randint(1,6)
			print("Dice rolled value is {}.<br/>".format(dice_count))
			#prev_position = players[i].position
			self.players[i].position += dice_count
			temp_position = self.players[i].position
			if temp_position in self.snakes.keys():
				print("Found in snakes list and will move from {} to {}.<br/>".format(temp_position, self.snakes[temp_position].to_position))
				temp_position = self.snakes[temp_position].to_position
				self.players[i].position = temp_position
				print("Player {} is now at position {}.<br/>".format(self.players[i].name, self.players[i].position))
			elif temp_position in self.ladders.keys():
				print("Found in ladders list and will move from {} to {}.<br/>".format(temp_position, self.ladders[temp_position].to_position))
				temp_position = self.ladders[temp_position].to_position 
				self.players[i].position = temp_position
				print("Player {} is now at position {}.<br/>".format(self.players[i].name, self.players[i].position))
			elif temp_position > 100:
				temp_position = temp_position - dice_count
				self.players[i].position = temp_position
				print("Player will move to more than 100 which is invalid so moving the player back to {}.<br/>".format(temp_position))
				print("Player {} is now at position {}.<br/>".format(self.players[i].name, self.players[i].position))
			else:
				print("Player {} is now at position {}.<br/>".format(self.players[i].name, self.players[i].position))

			if temp_position == 100:
				print("<br/>")
				print("Winner is {}.<br/>".format(self.players[i].name))
				return True
			print("<br/>")
		return False
		
	
	
	
