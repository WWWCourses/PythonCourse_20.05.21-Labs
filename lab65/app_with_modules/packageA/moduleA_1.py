class Game:
	def __init__(self, name, year ):
		# instance attributes
		self.name = name
		self.year = year

	# instance methods
	def play(self):
		print(f'{self.name} is playing')


# class attribute
Game.id = 1


if __name__ == '__main__':
	pass