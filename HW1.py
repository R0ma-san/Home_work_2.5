example = {
	   'iceberg': ['cold', 15, {'a', 'b'}, 33.98, 15/2, False],
	   'fire': ['hot', 46, ['cha', 'ching'], 81.13],
	   'earth': ['solid', 100, (13, 31, 1), 90.01, {'b':'c'}]
	   }
elements = ['fire', 'storm', 'cloud', 'iceberg', 'volcano', 'earth']

def func(example, elements):
    for i in elements:
        try:
            example[i]
        except KeyError:
            print(f'Ключа {i} не сущечтвует')
        else:
            x = 0
            for j in example[i]:
                try:
                    x+=j
                except:
                    continue
            print(i, '-', x)


func(example, elements)
  

