import random

class Bot():

    def __init__(self, letter):
        self.letter = letter

    def update_map(self, mapa):
        rows = mapa.split('\n')
        map = []
        for index, row in enumerate(rows):
            map.append(row.split(","))

        pos = mapa.index(self.letter) / 2
        self.y = pos / len(rows)
        self.x = pos % len(rows)

    def move(self):
        mov = random.randrange(0, 8)
        print("mov %s" % mov)

	if mov == 0:
        	return "N"	
	elif mov == 1:
                return "E"
        elif mov == 2:
                return "S"
        elif mov == 3:
                return "O"
	elif mov == 4:
                return "BN"
        elif mov == 5:
                return "BE"
        elif mov == 6:
                return "BS"
        elif mov == 7:
                return "BO"

        return "P"