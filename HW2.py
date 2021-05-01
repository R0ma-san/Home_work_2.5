import random

names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt', 
	'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt', 
	'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt', 
	'fhjhafhdfa.txt']
a = random.choice(names)
f = open(a, 'w')

def func(names):
    for i in names:
        try:
            f = open(a, 'w')
            f.write("Ramazan")
        except:
            print(f'Файла {i} не существует!')
func(names)
