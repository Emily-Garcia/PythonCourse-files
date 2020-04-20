import os

def validate_user_selection(selection):
    return True if isinstance(selection, int) and selection > 0 and selection < 3 else False

def validate_user_wants_exist(selection):
    return selection == 3

def format_dict_to_string(dictionary):
    # PARA COMENTAR EN PYTHON NOMÁS PONES UN HASHTAG
    # name:Sabritas|price:15.0|color:Amarillo
    # attributes = []
    # for key,value in dictionary.items():
    #     attributes.append(f'{key}:{value}')
    # ['name:Sabritas', 'price:15.0', 'color:Amarillo']
    # return '|'.join(attributes)
    #                       [Las list comprenhesion retornan una lista]
    return '|'.join([f'{key}:{value}' for key, value in dictionary.items()])

def format_string_to_dict(string):
    pairs = string.split('|')
    papita = {}
    for pair in pairs:
        [key, value] = pair.split(':')
        papita[key] = value
    return papita

def write_in_file(dictionary):
    file = open('papitas.txt', 'a')
    file.write(format_dict_to_string(dictionary)+'\n')
    print('\nPapita registrada con éxito\n')
    file.close()

def read_file():
    papitas = []
    if os.path.exists('papitas.txt'):
        file = open('papitas.txt', 'r')
        papitas_lines = file.readlines()
        for line in papitas_lines:
            papitas.append(format_string_to_dict(line))
    return papitas

def add_papita():
    # Atributos: Name, Price, Color
    name = input('¿Cuál es el nombre de las papita?: ')
    price = float(input('¿Cuánto cuesta?: '))
    color = input('¿Cuál es el color de la envoluta?: ')
    papita = {
        'name': name,
        'price': price,
        'color': color
    }
    write_in_file(papita)

def get_papitas():
    papitas = read_file()
    print("----------------------------")
    print('Nombre\t\tPrecio\t\tColor\t\t')
    print()
    if len(papitas) > 0:
        for papita in papitas:
            print(f'{papita["name"]}\t\t{papita["price"]}\t\t{papita["color"]}')
        print("----------------------------")
    else:
        print('Aun no tiene papitas registradas')


def handle_user_selection(selection):
    if selection == 1:
        add_papita()
    else:
        get_papitas()
        pass

def main():
    opt_exit = 'N'
    while opt_exit != 'S':
        papitas = read_file()
        print('Papitas app')
        print('Te presentamos nuestro menú de opciones')
        print('1. Agregar o registrar nueva papita')
        print('2. Ver las papitas registradas')
        print('3. Salir del programa')
        opt = int(input('¿Qué opción deseas hacer?: '))
        if validate_user_selection(opt):
            handle_user_selection(opt)
        elif validate_user_wants_exist(opt):
            opt_exit = 'S'
        else:
            print('OPCIÓN INVÁLIDA')
    print('Ejecución finalizada')

main()