# from packageA.moduleA_1 import Game,x
from packageA import moduleA_1 as m1




my_game = m1.Game(year=1990,name='Quake')
# print(my_game.name)
# print(my_game.year)

# res = my_game.play()
# print(res)


l = [1,2,3,1,2,3]
s = {1,2,3,1,2,3}

l_new = list(set(l))
print(l)
print(s)
print(l_new)

