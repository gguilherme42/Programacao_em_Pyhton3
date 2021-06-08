import os
import sys



def return_lst_files_from_current_directory() -> list[str]:
    existing_files = os.listdir('.')
   

    filtered_files = filter(lambda file: file.endswith('.lst'), existing_files)

    return [*filtered_files]


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
    






def main(): 
    while True:
        # file = input('Choose file name: ').strip()
        option = user_option()
        user_options_dict[option]()
        print(return_lst_files_from_current_directory())


main()


