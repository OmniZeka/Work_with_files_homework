def read_cook_book():
    with open('Cook_book.txt', encoding='utf-8') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()]

        cook_book_dict = {}

        index = 0
        while index < len(lines):
            dish_name = lines[index]
            index += 1

            count_of_ingredients = int(lines[index])
            index += 1

            ingredients = []

            for _ in range(count_of_ingredients):
                ingredients_data = lines[index].split('|')
                ingredients_info = {
                    'ingredient_name': ingredients_data[0],
                    'quantity': int(ingredients_data[1]),
                    'measure': ingredients_data[2]
                }
                ingredients.append(ingredients_info)
                index += 1
                cook_book_dict[dish_name] = ingredients
    return cook_book_dict


cook_book = read_cook_book()
for dish, info in cook_book.items():
    print(dish, info)
print()
print('-----------------------------------------------------')
print()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish_info in dishes:
        if dish_info in cook_book:
            for ingredient in cook_book[dish_info]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {
                        'measure': measure,
                        'quantity': quantity
                    }

    return shop_list


shopping_list = get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)

for dish, info in shopping_list.items():
    print(dish, info)
