import os
import sys





def return_lst_files_from_current_directory() -> list[str]:
    existing_files = os.listdir('.')
   

    filtered_files = filter(lambda file:  file.endswith('.lst'), existing_files)

    return [*filtered_files]


def print_files(files: list[str]) -> None:
    for file_number, file_name in enumerate(files, start=1):
        print(f'{file_number:3} - {file_name}')

user_options_dict = {'a': lambda : 'teste', 'd': lambda: 'DELETE', 's': lambda: "SAVE", 'q': sys.exit}


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



def main(): 
    create_lst_files_list()
    while True:
        current_directory_files = return_lst_files_from_current_directory()
        if current_directory_files:
            print_files(current_directory_files)
        else:
            print('-- No items are in the list --')
            file = input('Choose file name: ').strip()
        file += '.lst' if not(file.endswith('.lst')) else ''

        option = user_option()
        user_options_dict[option]()


main()


