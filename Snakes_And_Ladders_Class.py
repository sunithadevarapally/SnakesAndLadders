import random
class Player:
	def __init__(self, name, position = 0):
		self.name = name
		self.position = position
	def __repr__(self):
		return "Player {} is at position {}".format(self.name, self.position)
			
class Snake:
	def __init__(self, from_position, to_position):
		self.from_position = from_position
		self.to_position = to_position
	def is_valid(self):
		if self.from_position < self.to_position:
			print("Invalid snake positions. Change the positions")
			return False
		return True
		
class Ladder:
	def __init__(self, from_position, to_position):
		self.from_position = from_position
		self.to_position = to_position
		
	def is_valid(self):
		if self.from_position > self.to_position:
			print("Invalid ladder positions. Change the positions")
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
			print("Dice rolled value is {}".format(dice_count))
			#prev_position = players[i].position
			self.players[i].position += dice_count
			temp_position = self.players[i].position
			if temp_position in self.snakes.keys():
				print("found in snakes list and will move from {} to {}\n".format(temp_position, self.snakes[temp_position].to_position))
				temp_position = self.snakes[temp_position].to_position
				self.players[i].position = temp_position
			elif temp_position in self.ladders.keys():
				print("found in ladders list and will move from {} to {}\n".format(temp_position, self.ladders[temp_position].to_position))
				temp_position = self.ladders[temp_position].to_position 
				self.players[i].position = temp_position
			elif temp_position > 100:
				temp_position = temp_position - dice_count
				self.players[i].position = temp_position
				print("player will move to more than 100 which is invalid so moving the player back to {}\n".format(temp_position))
			else:
				print("{}\n".format(self.players[i]))

			if temp_position == 100:
				print("Winner is player {}".format(self.players[i]))
				return True
		return False
		
	
	
	
