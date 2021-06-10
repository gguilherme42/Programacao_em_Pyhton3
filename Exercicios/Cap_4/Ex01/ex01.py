import os
import sys




def return_lst_files_from_current_directory() -> list[str]:
    existing_files = os.listdir('.')
   

    filtered_files = filter(lambda file:  file.endswith('.lst'), existing_files)

    return [*filtered_files]


def print_files(files: list[str]) -> None:
    print('----- FILES -----')
    for file_number, file_name in enumerate(files, start=1):
        print(f'{file_number:3} - {file_name}')
    print('------------')


def print_lines(lines_list: list[str]) -> None:
    for line_number, line_name in enumerate(lines_list, start=1):
        print(f'{line_number:3} - {line_name}')
    print()


def user_option() -> str:
    while True:
        try:
            option = input('[A]dd [D]elete [S]ave [Q]uit [a]: ').lower().strip()[0]
        
        except IndexError as err:
            print('ERROR: invalid choice--enter one of "AaDdSsQq"')
        
        except KeyboardInterrupt:
            user_options_dict['q']()
        else:
            if option in 'adsq':
                return option
            print('ERROR: invalid choice--enter one of "AaDdSsQq"')
            


def open_file(file_name: str) -> None:
    fh = None
    try:
        fh = open(file_name, encoding='utf8')
    except EnvironmentError as err:
        print(f'ERROR: {err}')
    


def create_lst_files_list() -> None:
    if not(return_lst_files_from_current_directory()):
        for number in range(0, 10):
            new_file = open(f'file{number}.lst', 'w', encoding='utf8')
            new_file.close()


def valid_number_to_choose(msg: str, limit: int, stop_program_with_zero: bool) -> int:
    while True:
        try:
            file_number = int(input(msg))
        
        except ValueError:
            print('ERROR: invalid file number.')
        
        except KeyboardInterrupt:
            if stop_program_with_zero:
                sys.exit()

        else:
            if 0 <= file_number < limit:
                return file_number
            print('ERROR: invalid file number.')


def find_file_by_number(file_number: int, file_list: list[str]) -> int:
    return file_list[file_number - 1]


def input_file_name(msg: str) -> str:
    while True:
        try:
            file = input(msg).strip()
        
        except KeyboardInterrupt:
            user_options_dict['q']()
        else:
            file += '.lst' if not(file.endswith('.lst')) else ''
            return file


def read_file(file_name: str) -> list[str]:
    try:
        opened_file = open(file_name, 'r', encoding='utf8')
    except EnvironmentError as err:
        print(f'ERROR: {err}')
    else:
        file_lines = [line  for line in opened_file.read()]
        return file_lines
    finally:
        opened_file.close()


def user_option_when_file_is_empty() -> str:
    while True:
        try:
            option = input('[A]dd [Q]uit [a]: ').lower().strip()[0]
        
        except IndexError as err:
            print('ERROR: invalid choice--enter one of "AaQq"')
        
        except KeyboardInterrupt:
            user_options_dict['q']()
        else:
            if option in 'aq':
                return option
            print('ERROR: invalid choice--enter one of "AaQq"')



def add_line(line_list: list[str]) -> None:
    while True:
        try:
            new_line = input('Add item: ').strip()
        except IndexError:
            print('ERROR: Invalid line')
        
        except KeyboardInterrupt:
            sys.exit()

        else:
            if not(new_line == ''):
                line_list.append(new_line)
            print('ERROR: Invalid line')
            


def delete_line(line_list: list[str]) -> None:
    line_number = valid_number_to_choose('Delete item number (or 0 to cancel): ', len(line_list), False)
    if line_list > 0:
        line_list.pop(line_number - 1)


user_options_dict = {'a': add_line, 'd': delete_line, 's': lambda: "SAVE", 'q': sys.exit}

            


def main(): 
    create_lst_files_list()
    file = ''
    current_directory_files = return_lst_files_from_current_directory()

    if current_directory_files:
        print_files(current_directory_files)

        file_number = valid_number_to_choose('Choose a file by its number (0 to create a new file): ', len(current_directory_files), True)

        if file_number == 0:
            file = input_file_name('Choose file name: ')
            
        else: 
            file = find_file_by_number(file_number, current_directory_files)
        
    else:
        file = input_file_name('Choose file name: ')
        

    while True:
        file_lines = read_file(file)
        if not(file_lines):
            print('\n-- no items are in the list --\n')
            user_options_dict[user_option_when_file_is_empty()]()

        print_lines(file_lines)
        option = user_option()
        # Need to fix TypeErro when  the dict function is called
        if option == 'q':
            user_options_dict[option]()
        else:
            user_options_dict[option](file_lines)
            


main()


