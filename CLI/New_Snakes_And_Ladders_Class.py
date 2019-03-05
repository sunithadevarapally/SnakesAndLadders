#This is the driver code

import random
from Snakes_And_Ladders_Class import Player
from Snakes_And_Ladders_Class import Snake
from Snakes_And_Ladders_Class import Ladder
from Snakes_And_Ladders_Class import Board
class SnakesAndLadders:
	def take_player_input(self):
		no_of_players = int(input("Enter number of players : "))
		players_list = []
		for i in range(1, no_of_players+1):
			player_name = input("Enter name of player" +  str(i) + ": ")
			player = Player(player_name)
			players_list.append(player)
		return players_list
	
	snakes_list = {}
	ladders_list = {}
	snakes_list = {25:Snake(25,5), 34:Snake(34, 1), 47:Snake(47,19), 65:Snake(65,52), 87:Snake(87,57), 91:Snake(91,61), 99:Snake(99,69)}
	ladders_list = {3:Ladder(3,51), 6:Ladder(6,27), 20:Ladder(20,70), 36:Ladder(36,55), 63:Ladder(63,95), 68:Ladder(68, 98)}
	#no_of_players = 2#int(input("Enter number of players : "))
	
	def take_snake_input(self):
		snakes_list = {}
		no_of_snakes = int(input("Enter number of snakes : "))
		for i in range(1, no_of_snakes+1):
			start_position = int(input("Snake" + str(i) + " from : "))
			end_position = int(input("Snake" + str(i) + " to : "))
			snake = Snake(start_position, end_position)
			while not snake.is_valid():
				start_position = int(input("Snake" + str(i) + " from : "))
				end_position = int(input("Snake" + str(i) + " to : "))
				snake = Snake(start_position, end_position)
			snakes_list[start_position] = snake
		return snakes_list
		
	def take_ladder_input(self):
		ladders_list = {}
		no_of_ladders = int(input("Enter number of ladders : "))
		for i in range(1, no_of_ladders+1):
			start_position = int(input("Ladder" + str(i) + " from : "))
			end_position = int(input("Ladder" + str(i) + " to : "))
			ladder = Ladder(start_position, end_position)
			while not ladder.is_valid():
				start_position = int(input("Ladder" + str(i) + " from : "))
				end_position = int(input("Ladder" + str(i) + " to : "))
				ladder = Ladder(start_position, end_position)
			ladders_list[start_position] = ladder
		return ladders_list

new_game = SnakesAndLadders()
players_list = new_game.take_player_input()
snakes_list = new_game.take_snake_input()
ladders_list = new_game.take_ladder_input()
new_board = Board(players_list, snakes_list, ladders_list)
while True:
	winner_found = new_board.play_round()
	if winner_found:
		break
	