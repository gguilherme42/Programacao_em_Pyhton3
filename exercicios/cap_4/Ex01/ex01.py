import os
import sys




def return_lst_files_from_current_directory() -> list[str]:
    existing_files = os.listdir('.')
   

    filtered_files = filter(lambda file:  file.endswith('.lst'), existing_files)

    return [*filtered_files]


def create_lst_files_list() -> None:
    if not(return_lst_files_from_current_directory()):
        for number in range(0, 10):
            new_file = open(f'file{number}.lst', 'w', encoding='utf8')
            new_file.close()


# printing
def print_files(files: list[str]) -> None:
    print('----- FILES -----')
    for file_number, file_name in enumerate(files, start=1):
        print(f'{file_number:3} - {file_name}')
    print('------------')


def print_lines(lines_list: list[str]) -> None:
    for line_number, line_name in enumerate(lines_list, start=1):
        print(f'{line_number:3} - {line_name}')
    print()

# ------

            
# file

def open_file(file_name: str) -> None:
    fh = None
    try:
        fh = open(file_name, encoding='utf8')
    except EnvironmentError as err:
        print(f'ERROR: {err}')
    


def read_file(file_name: str) -> list[str]:
    file_lines = []
    try:
    
        opened_file = open(file_name, 'r')
    
    except EnvironmentError as err:
        print(err)
        return []
       
    else:
        for line in opened_file:
            file_lines.append(line.strip())
        opened_file.close()
        return file_lines

        


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

# ---

# validaition
def valid_number_to_choose(msg: str, limit: int, stop_program_with_zero: bool) -> int:
    while True:
        try:
            file_number = int(input(msg))
        
        except ValueError:
            print('ERROR: invalid file number.')
        
        except KeyboardInterrupt:
            sys.exit()

        else:
            
            if 0 <= file_number <= limit:
                if file_number == 0 and stop_program_with_zero:
                    sys.exit()
                return file_number
            print('ERROR: invalid file number.')


# --

# User options 

def user_option(has_unsaved_changes: bool, line_list_length: int) -> str:
    while True:
        try:
            option = input(f'[A]dd {"[D]elete" if line_list_length > 0 else ""} {"[S]ave" if has_unsaved_changes else ""} [Q]uit [a]: ').lower().strip()[0]
        
        except IndexError as err:
            print('ERROR: invalid choice--enter one of "AaDdSsQq"')
        
        except KeyboardInterrupt:
            sys.exit()
        else:
            valid_options = 'aq'
            valid_options += 's' if has_unsaved_changes else ''
            valid_options += 'd' if line_list_length > 0 else ''
            if option in valid_options:
                return option
            print('ERROR: invalid choice--enter one of "AaDdSsQq"')


def user_option_when_file_is_empty() -> str:
    while True:
        try:
            option = input('[A]dd [Q]uit [a]: ').lower().strip()[0]
        
        except IndexError as err:
            print('ERROR: invalid choice--enter one of "AaQq"')
        
        except KeyboardInterrupt:
            user_options_dict['q']()
        else:
            if option == 'a':
                return option
            elif option == 'q':
                sys.exit()
            print('ERROR: invalid choice--enter one of "AaQq"')


def add_line(line_list: list[str]) -> None:
   
    while True:
        try:
            new_line = input('Add item: ').strip()
        except IndexError:
            print('ERROR: Invalid name')
        
        except KeyboardInterrupt:
            sys.exit()

        else:
            if new_line:
                line_list.append(new_line)
                line_list.sort(key=lambda word: word.lower())
                return
            print('ERROR: Invalid name')
            

def delete_line(line_list: list[str]) -> None:
    line_number = valid_number_to_choose('Delete item number (or 0 to cancel): ', len(line_list), False)
    if line_number > 0:
        line_list.pop(line_number - 1)


def save(line_list_unsaved: list[str], file_name: str) -> None:
    try:
        opened_file = open(file_name, 'w')
    except EnvironmentError as err:
        print(f'ERROR: {err}')
    else:
        for line in line_list_unsaved:
            opened_file.write(f'{line}\n')
        print(f'Saved {len(line_list_unsaved)} items to {file_name}')
    finally:
        opened_file.close()    



def quit(has_unsaved_changes: bool, file_lines_unsaved: list[str], file: str) -> None:
    if has_unsaved_changes:
        while True:
            try:
                answer = input('Save unsaved changes (y/n) [y]: ').strip().lower()

            except KeyboardInterrupt:
                sys.exit()    
            else:
                if answer == 'y':
                    save(file_lines_unsaved, file)
                    sys.exit()
                elif answer == 'n':
                    sys.exit()
                print('ERROR: Invalid answer.')
    else:
        sys.exit()    



user_options_dict = {'a': add_line, 'd': delete_line, 's': save, 'q': quit}


            
def initial_config(current_directory_files: list[str]) -> str:
    file_name = ''
    if current_directory_files:
        print_files(current_directory_files)

        file_number = valid_number_to_choose('Choose a file by its number (0 to create a new file): ', len(current_directory_files), True)

        if file_number == 0:
            file_name = input_file_name('Choose file name: ')
            
        else: 
            file_name = find_file_by_number(file_number, current_directory_files)
    else:
        file_name = input_file_name('Choose file name: ')

    return file_name


def main(): 
    create_lst_files_list()
    file = ''
    current_directory_files = return_lst_files_from_current_directory()
    
    file = initial_config(current_directory_files)
  
    file_lines_saved = read_file(file)
    file_lines_unsaved = file_lines_saved[:]
    
    if not(file_lines_unsaved):
        print('\n-- no items are in the list --\n')
        user_options_dict[user_option_when_file_is_empty()](file_lines_unsaved)
    
    while True:
     
        print_lines(file_lines_unsaved)
        option = user_option(file_lines_saved != file_lines_unsaved, len(file_lines_unsaved))
        if option == 'q':
            user_options_dict[option](file_lines_saved != file_lines_unsaved, file_lines_unsaved, file)
        
        elif option == 's':
            user_options_dict[option](file_lines_unsaved, file)
            file_lines_saved = file_lines_unsaved[:]
        else:
            user_options_dict[option](file_lines_unsaved)
        
            


main()


