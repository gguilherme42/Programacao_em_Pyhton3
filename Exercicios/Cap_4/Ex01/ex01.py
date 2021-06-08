import os
import sys


def return_lst_files() -> list[str]:
    existing_files = os.listdir('.')
   

    filtered_files = filter(lambda file: file.endswith('.lst'), existing_files)

    return [*filtered_files]


def user_option() -> str:
    option = input('[A]dd [D]elete [S]ave [Q]uit [a]: ').lower().strip()[0]
    return option


def open_file(file_name: str) -> None:
    fh = None
    try:
        fh = open(file_name, encoding='utf8')
    except EnvironmentError as err:
        print(f'ERROR: {err}')
    





def main(): 
    # file = input('Choose file name: ').strip()
    print(return_lst_files())


main()


