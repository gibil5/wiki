"""
    Pythonic Programming
    
    Pythonic
    ---------
    Item 2 - Follow the PEP-8 style guide (pylint)
    Item 4 - Use the fstring. 
    Item 6 - Multiple assignment unpacking, over indexing
    Item 7 - Prefer enumerate over range
    Item 8 - Use zip to process Iterators in parallel
    Item 10 - Prevent repetition with assignment expressions

    Lists and dics
    ----------------
    item 11 - Know how to slice sequences
    item 12 - avoid striding and slicing in a single expression
    item 13 - prefer catch all unpacking over slicing

    Functions
    ----------
    item 19 - Never unpack more than tree variables
    item 20 - Prefer raising exceptions than returning None
"""

# Multiple assignment unpacking, over indexing
snacks_cal = {
    'chips': 140,
    'popcorn': 80,
    'nuts': 190,
}
sc = snacks_cal.items()
print(sc)

#snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
#for rank, (name, calories) in enumerate(snacks, 1):
#for rank, (name, calories) in enumerate(snacks_cal.items(), 1):
print('\nItem 6 - Multiple assignment unpacking, over indexing')
for rank, (name, calories) in enumerate(sc, 1):
    print(f'{rank}, {name}, {calories}')


# Item 7 - Prefer enumerate over range
print('\nItem 7 - Prefer enumerate over range')
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for i, flavor in enumerate(flavor_list, 1):
    print(f'{i}: {flavor}')


#Item 8 - Use zip to process Iterators in parallel
item = 'Item 8 - Use zip to process Iterators in parallel'
print(f'\n{item}')
names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]

for name, count in zip(names, counts):
    print(f'{name}: {count}')

import itertools
for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')


# Item 10 - Prevent repetition with assignment expressions
item = 'Item 10 - Prevent repetition with assignment expressions'
print(f'\n{item}')
fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}
print(fresh_fruit)
if (count := fresh_fruit.get('apple', 0)) >= 4:
    #make_cider(count)
    print('make_cider')
else:
    #out_of_stock()
    print('out of stock')


# item 13 - prefer catch all unpacking over slicing
item = 'item 13 - prefer catch all unpacking over slicing'
print(f'\n{item}')

car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)



# item 19 - Never unpack more than tree variables
item = 'item 19 - Never unpack more than tree variables'
print(f'\n{item}')

def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

longest, *middle, shortest = get_avg_ratio(lengths)
print(f'\n{longest:1.2f}, {shortest:1.2f}')
print(f'\n{middle}')




# item 20 - Prefer raising exceptions than returning None
item = 'item 20 - Prefer raising exceptions than returning None'
print(f'\n{item}')

def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')

x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)


