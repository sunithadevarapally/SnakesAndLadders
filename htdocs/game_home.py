#!C:\Users\sunit\AppData\Local\Programs\Python\Python37\python
import cgi;
import cgitb;
from Snakes_And_Ladders_Class import Player
from Snakes_And_Ladders_Class import Snake
from Snakes_And_Ladders_Class import Ladder
from Snakes_And_Ladders_Class import Board

cgitb.enable()
 
print("Content-type: text/html\r\n")
form = cgi.FieldStorage() 

print("""
<html>
<head>
<title>Snakes and Ladders</title>
</head>
<body>
<center>
<h1>Snakes and Ladders</h1>
</center>

""")

# Get number of players from input
player_count = form.getvalue('player_count')
player_names = []
if player_count == None or player_count == '0':
	print(
	"""
	Enter number of players:
	<form action="/game_home.py" method = "post">
	<select name="player_count">
	  <option value="2">2</option>
	  <option value="3">3</option>
	  <option value="4">4</option>
	  <option value="5">5</option>
	  <option value="6">6</option>
	</select>
	<input type="submit" value="Submit">
	</form>

	
	""")
else:
	player_count = int(player_count)
	for i in range(1, player_count+1):
		temp_name = form.getvalue('player_name_' + str(i))
		if temp_name != None:
			player_names.append(temp_name)
	if len(player_names) == 0:
		print("Number of players = {}". format(player_count))
		print("""<form action="/game_home.py" method = "post"><br>""")
		for i in range(1, player_count+1):
			print("Enter player {} name: ".format(str(i)))
			print("<input type='text' name='player_name_{}'><br>".format(i))
		print("""<input type='hidden' name='player_count' value = '{}'>
		<input type='submit' value='Submit'>
		</form>""".format(player_count))
		
	else:
		snakes_list = {25:Snake(25,5), 34:Snake(34, 1), 47:Snake(47,19), 65:Snake(65,52), 87:Snake(87,57), 91:Snake(91,61), 99:Snake(99,69)}
		ladders_list = {3:Ladder(3,51), 6:Ladder(6,27), 20:Ladder(20,70), 36:Ladder(36,55), 63:Ladder(63,95), 68:Ladder(68, 98)}
		players_list = []
		for i in range(1, player_count+1):
			player_position = form.getvalue('player_' +str(i)+ '_position')
			if player_position == None:
				player_position = 0
			player = Player(player_names[i-1], int(player_position))
			players_list.append(player)
		new_board = Board(players_list, snakes_list, ladders_list)
		if "RollDice" in form:
			print("<div><div style='float:right; left:600px; position:absolute;'>")
			winner_found = new_board.play_round()
			if winner_found:
				player_count = 0
				player_names = []
		print("</div><form action='/game_home.py' method = 'post'><br>")
		print("<div style = 'float:left'; align='middle'>")
		print("<img src='snakesladderspicture.jpg' alt='Snakes and Ladders' width='500' height='500'>")
		for i in range(1, player_count+1):
			p_pos = players_list[i-1].position
			if p_pos%10 != 0 or p_pos == 0:
				p_pos_x = (50*(p_pos%10))-25
			else:
				p_pos_x = (50*((p_pos-1)%10))+25
			if p_pos%10 != 0 or p_pos == 0:
				p_pos_y = 550-(45*(int(p_pos/10)))
			else:
				p_pos_y = 550-(45*(int((p_pos-1)/10)))
			print("<img src='dot-{}.png' style='position:absolute; top:{}px; left:{}px;' alt='Player-{}' width='20' height='20'>".format(i, p_pos_y, p_pos_x, i))

		print("<br/><input name='RollDice' type='submit' value='Roll Dice'></div>")
		for i in range(1, player_count+1):
			print("<input type='hidden' name='player_name_{}' value = '{}'>".format(i, players_list[i-1].name))
			print("<input type='hidden' name='player_{}_position' value = '{}'>".format(i, players_list[i-1].position))
		print("<input type='hidden' name='player_count' value = '{}'>".format(player_count))
		print("</form></div>")
		
		
print("""
</body>
</html>
""")	