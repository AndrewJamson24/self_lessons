import secrets
while True : #this wile loop keeps playing the game until player choose quit optin at the end 
	choices = ["Rock","Paper","Scissors"]

	player_input = None

	while player_input not in choices : #while the input will not be one from the choices list it will not procced forward , it will keep asking and you will be able to keep trying until you put the correct one 
		player_input = input("Choose rock,paper or scissors: ").replace(" ", "").capitalize() #first we use replace to get rid of the empty spaces then we use capitalize to make the first letter uppercase

	CPU = secrets.choice(choices)

	if player_input == CPU :
		print ("So your choice is " + player_input )
		print("CPU choice is " + CPU)
		print("Its a tie")
	elif player_input == "Scissors" and CPU == "Rock":
		print("So your choice is " + player_input )
		print("CPU choice is " + CPU)
		print("CPU wins")
	elif player_input == "Paper" and CPU == "Rock":
		print("So your choice is " + player_input )
		print("CPU choice is " + CPU)
		print("You won")
	elif player_input == "Rock" and CPU == "Paper":
		print("So your choice is " + player_input )
		print("CPU choice is " + CPU)
		print ("CPU wins")
	elif player_input == "Scissors" and CPU == "Paper":
		print("So your choice is " + player_input )
		print("CPU choice is " + CPU)
		print("You won")
	elif player_input == "Paper" and CPU =="Scissors" :
		print("So your choice is " + player_input )
		print("CPU choice is " + CPU)
		print("CPU wins")
	elif player_input == "Rock" and CPU == "Scissors" :
		print("So your choice is " + player_input )
		print("CPU choice is " + CPU)
		print("You won")

	play_again= input("Play again? (yes/no) : "  ).lower()

	if play_again != "yes" :
		break
print ("Bye!")

















