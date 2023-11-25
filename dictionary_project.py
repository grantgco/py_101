# Scrabble Project
# November 25, 2023
# PGG

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]

letters_to_points = dict(zip(letters,points))

print(letters_to_points.get("A"))

def score_word(word):
	point_total = 0 
	for letter in word:
    	point_total += letters_to_points.get(letter)
  	return point_total

print(score_word("BROWNIE"))

player1 = ["BLUE", "TENNIS", "EXIT"]
word_nerd = ["EARTH", "EYES", "MACHINE"]
lexiCon = ["ERASER", "BELLY", "HUSKY"]
ProfReader = ["ZAP", "COMA", "PERIOD"]

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "word_nerd": word_nerd, "lexicon": lexiCon, "ProfReader": ProfReader}

#print(player_to_words)

player_to_points = dict()

for player, words in player_to_words.items():
  player_points=0
  for word in words:
     player_points += score_word(word)
  player_to_points[player] = player_points
