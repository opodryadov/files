from pprint import pprint

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_cook_book('recipes.txt')
    temp_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            temp_list[ingredient['ingredient name']] = \
                {'measure': ingredient['measure'],
                 'quantity': (int(ingredient['quantity']) * person_count)}
    return temp_list

def check_count():
    with open('recipes.txt', 'r', encoding='utf-8') as file_work:
        count = 1
        for line in file_work:
            if line == "\n":
                count += 1
        return count

def create_cook_book(output_name):
    with open(output_name, 'r', encoding='utf-8') as file_work:
        cook_book = {}
        for j in range(check_count()):
            dish_name = file_work.readline().strip()
            counter = file_work.readline()
            cook_book[dish_name] = []
            for i in range(int(counter)):
                ingredient = file_work.readline().strip().split(' | ')
                temp_dict = {'ingredient name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
                cook_book[dish_name].append(temp_dict)
            file_work.readline()
    return cook_book

pprint(create_cook_book('recipes.txt'))
print("\n__________\n")
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))