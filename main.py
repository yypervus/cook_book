with open('recipes.txt', encoding='utf-8') as file:
    lines = file.readlines()
    cook_book = {}
    list_ = [[]]
    for string in lines:
        if string != '\n':
            if '|' in string:
                list_[-1].append(string.strip().split('|'))
            else:
                list_[-1].append(string.strip())
        else:
            list_.append([])

    for dish in list_:
        value = []
        for ingredient in dish:
            if type(ingredient) == list:
                dict_ingredient = dict(ingredient_name=ingredient[0], quantity=ingredient[1], measure=ingredient[2])
                value.append(dict_ingredient)
        cook_book[dish[0]] = value

print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    finish_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for dict_ingred in cook_book[dish]:
                if dict_ingred['ingredient_name'] not in finish_dict:
                    finish_dict[dict_ingred['ingredient_name']] = dict(measure=dict_ingred['measure'], quantity=int(
                        dict_ingred['quantity']) * person_count)
                else:
                    finish_dict[dict_ingred['ingredient_name']] = dict(measure=dict_ingred['measure'], quantity=int(
                        dict_ingred['quantity']) * person_count + finish_dict[dict_ingred['ingredient_name']].pop(
                        'quantity'))

        else:
            return f'Неверно введено название блюда'
    return finish_dict


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
