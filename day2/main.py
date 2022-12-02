import os

class RockPaperScissors:
    def __init__(self):
        self.player_score = 0
        self.opponent_score = 0

    def play_turn(self, player_input:str, opponent_input:str):
        if player_input.lower() == "rock":
            self.player_score += 1
            if opponent_input.lower() == "scissors":
                self.player_score += 6
            elif opponent_input.lower() == "paper":
                self.opponent_score += 1
            elif opponent_input.lower() == "rock":
                self.player_score += 3
        elif player_input.lower() == "paper":
            self.player_score += 2
            if opponent_input.lower() == "scissors":
                self.opponent_score += 1
            elif opponent_input.lower() == "paper":
                self.player_score += 3
            elif opponent_input.lower() == "rock":
                self.player_score += 6
        elif player_input.lower() == "scissors":
            self.player_score += 3
            if opponent_input.lower() == "scissors":
                self.player_score += 3
            elif opponent_input.lower() == "paper":
                self.player_score += 6 
            elif opponent_input.lower() == "rock":
                self.opponent_score += 1
                
    def translate_challenge_one_input(self, input_string:str):
        if input_string == "A X":
            opponent_input = "rock"
            player_input = "rock"
        elif input_string == "B X":
            opponent_input = "paper"
            player_input = "rock"
        elif input_string == "C X":
            opponent_input = "scissors"
            player_input = "rock"
        elif input_string == "A Y":
            opponent_input = "rock"
            player_input = "paper"
        elif input_string == "B Y":
            opponent_input = "paper"
            player_input = "paper"
        elif input_string == "C Y":
            opponent_input = "scissors"
            player_input = "paper"
        elif input_string == "A Z":
            opponent_input = "rock"
            player_input = "scissors"
        elif input_string == "B Z":
            opponent_input = "paper"
            player_input = "scissors"
        elif input_string == "C Z":
            opponent_input = "scissors"
            player_input = "scissors"
        self.play_turn(player_input=player_input, opponent_input=opponent_input)

    def translate_challenge_two_input(self, input_string:str):
        if input_string == "A X":
            opponent_input = "rock"
            player_input = "scissors"
        elif input_string == "B X":
            opponent_input = "paper"
            player_input = "rock"
        elif input_string == "C X":
            opponent_input = "scissors"
            player_input = "paper"
        elif input_string == "A Y":
            opponent_input = "rock"
            player_input = "rock"
        elif input_string == "B Y":
            opponent_input = "paper"
            player_input = "paper"
        elif input_string == "C Y":
            opponent_input = "scissors"
            player_input = "scissors"
        elif input_string == "A Z":
            opponent_input = "rock"
            player_input = "paper"
        elif input_string == "B Z":
            opponent_input = "paper"
            player_input = "scissors"
        elif input_string == "C Z":
            opponent_input = "scissors"
            player_input = "rock"
        self.play_turn(player_input=player_input, opponent_input=opponent_input)


    def get_player_score(self):
        print(self.player_score)

    def get_opponent_score(self):        
        print(self.opponent_score)





game = RockPaperScissors()

with open("input.txt", "r") as input_file:
    turns_string = input_file.read()
    turns_list = turns_string.split("\n")
    for turn in turns_list:
        game.translate_challenge_two_input(input_string=turn)
    game.get_player_score()
