def create_cook_book(file_name):
    cook_book = {}
    
    with open(file_name, 'r') as file:
        lines = file.readlines()
        
        i = 0
        while i < len(lines):
            dish_name = lines[i].strip()
            ingredient_count = int(lines[i + 1])
            i += 2
            
            ingredients = []
            for j in range(ingredient_count):
                ingredient_info = lines[i + j].strip().split('|')
                ingredient = {
                    'ingredient_name': ingredient_info[0].strip(),
                    'quantity': int(ingredient_info[1].strip()),
                    'measure': ingredient_info[2].strip()
                }
                ingredients.append(ingredient)
            
            cook_book[dish_name] = ingredients
            i += ingredient_count
            
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quanity'] * person_count
                measure = ingredient['measure']

                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity
    return shop_list

file_name = 'recipes.txt'
cook_book = create_cook_book(file_name)
print(cook_book)

dishes_to_cook = ['Омлет', 'Утка по-пекински']
person_count = 2
shopping_list = get_shop_list_by_dishes(dishes_to_cook, person_count, cook_book)
print(shopping_list)

def merge_files(file_list, result_filename):
    files_info = []
    
    for file in file_list:
        with open(file, 'r') as f:
            lines = f.readlines()
            num_lines = len(lines)

        files_info.append((file, num_lines, lines))
    
    files_info.sort(key=lambda x: x[1])
    
    with open(result_filename, 'w') as f:
        for file_info in files_info:
            file, num_lines, lines = file_info
            f.write(file + '\n')
            f.write(str(num_lines) + '\n')
            f.writelines(lines)
            f.write('\n')