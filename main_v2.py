import os

def validate_user_selection(selection):
    return True if isinstance(selection, int) and selection > 0 and selection < 3 else False

def user_wants_exit(selection):
    return selection == 3

def handle_user_selection(selection):
    if selection == 1:
        add_papita()
    elif selection == 2:
        get_papitas()

def clean_screen():
    clear = lambda: os.system('clear') #on Linux System
    clear()

def format_dict_to_string(dictionary):
    return '|'.join([f'{key}: {value}' for key, value in dictionary.items()])

def format_line_to_object(line):
    pairs = line.split('|')
    papita = {}
    for pair in pairs:
        [key, value] = pair.replace(' ', '').replace('\n', '').split(':')
        papita[key] = value
    return papita

def write_in_file(dictionary):
    f = open('papitas.txt', 'a')
    f.write(format_dict_to_string(dictionary)+'\n')
    print("\nPapita registrada en el archivo\n")
    f.close()


def read_file():
    papitas = []
    if os.path.exists('papitas.txt'):
        file = open('papitas.txt', 'r')
        papitas_lines = file.readlines()
        for line in papitas_lines:
            papitas.append(format_line_to_object(line))
    return papitas


def add_papita():
    name = input('Cuál es el nombre de las papitas?: ')
    price = float(input('Cuánto cuesta?: '))
    color = input('Color de la bolsa: ')
    papita = {
        'name': name,
        'price': price,
        'color': color
    }
    write_in_file(papita)

def get_papitas():
    print("-----------------------------------------------------")
    print('Nombre\t\tPrecio\t\tColor\t\t')
    print()
    papitas = read_file()
    if len(papitas) > 0:
        for papita in papitas:
            print(f'{papita["name"]}\t\t{papita["price"]}\t\t{papita["color"]}\t\t')
        print("-----------------------------------------------------")
    print('Aun no tienes papitas registradas. VE Y REGISTRA UNA\n')


def main():
    opt_user = 'N'
    while opt_user != 'S':
        papitas = read_file()
        clean_screen()
        print('Papitas app')
        print('Te presentamos nuestro menú')
        print('1. Registrar nueva papita')
        print('2. Ver papitas registradas')
        print('3. Salir')
        opt = int(input('Qué opción deseas hacer? '))
        print()
        if validate_user_selection(opt):
            handle_user_selection(opt)
            input('Presiona una tecla para continuar: ')
        elif user_wants_exit(opt):
            opt_user = 'S'
        else:
            print('OPCIÓN INVÁLIDA')
            input('Presiona una tecla para continuar: ')
    print('Adios')
main()