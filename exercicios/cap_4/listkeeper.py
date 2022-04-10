import os


def filter_lst_files() -> dict:
    result = filter(lambda file: file.endswith(".lst"), os.listdir("."))
    return sorted(result)


def read_file_lst_content(filename: str) -> list:
    file_list = []
    fh = None
    try:
        fh = open(filename, encoding="utf8")
        
        file_list = [line.strip() for line in fh]
    except EnvironmentError as err:
        print(f"ERROR → {err}")
    finally:
        if fh:
            fh.close()
        if file_list:
            file_list.sort()
        return file_list


def get_integer(message: str, name="integer", default=None, minimum=0, maximum=100, allow_zero=True) -> int: 
	message += f"[{default}] " if default else ""

	while True:
		try:
			line = int(input(message))
			if line == 0 and not(allow_zero):
				if default is not None:
					return default
				return minimum
			
			if not(minimum <= line <= maximum):
				raise ValueError(f"{name} must be at least between {minimum} and {maximum} ")
			return line
		except ValueError as err:
			print(f"ERROR {err}")


def get_string(message: str, can_save: bool, has_content: bool) -> str: 
    valid_options = set(f'A{"D" if has_content else ""}{"S" if can_save else ""}Q')
    while True:
        try:
            line = input(message).strip().upper()
            if not line:
                raise ValueError("string may not be empty")
        
            if line not in valid_options:
                raise ValueError("string not valid")

            return line

        except ValueError as err:
            print(f"ERROR {err}")


def get_filename(lst_files: list[str]) -> str:
    result = ''
    if lst_files:
        file_number = get_integer("Choose a file: ", maximum=len(lst_files))
        if file_number == 0:
            result = input("Enter a filename: ").strip().lower()
        else:
            result = lst_files[file_number - 1]
    else:
        result = input("Enter a filename: ").strip().lower()
    
    result += '' if result.endswith('.lst') else '.lst'
    return result
    

def print_lst_files(lst_files: list):
    if lst_files:
        for i, value in enumerate(lst_files):
            print(f"{(i + 1):3} → {value}")
    else:
        print("No files were find. Create a new file")
    print()   
    

def user_options_input(can_be_saved: bool, has_content: bool) -> str:
    result = get_string(f"[A]dd {'[D]elete' if has_content else ''} {'[S]ave' if can_be_saved else ''} [Q]uit: ", can_be_saved, has_content)
    return result


def print_lst_content(list_to_print: list):
    print()
    if list_to_print:
        for i, value in enumerate(list_to_print):
            print(f"{(i+1)}: {value}")    
    else:
        print("-- no items are in the list --")
    print()

can_be_saved: bool = False

def main(): 
    import sys
    import os

    existing_lst_files = filter_lst_files()
    filename = None 

    print_lst_files(existing_lst_files)
    
    filename = get_filename(existing_lst_files)
    
    lst_content = read_file_lst_content(filename)

    def add_item():
        global can_be_saved
        item = input("Add item: ").strip()
        lst_content.append(item)
        lst_content.sort()
        can_be_saved = True

    def delete_item():
        global can_be_saved
        item_index = (get_integer("Remove item: ", minimum=1, maximum=len(lst_content), allow_zero=False) - 1)
        lst_content.pop(item_index)
        lst_content.sort()
        can_be_saved = True

    def save_file():
        global can_be_saved
        if can_be_saved:    
            fh = None
            try:
                fh = open(filename, 'a', encoding="utf8")
                content_to_write = ''
                for line in lst_content:
                    content_to_write = f"{line}\n"
                fh.write(content_to_write)
                can_be_saved = False

            except EnvironmentError as err:
                print(f"ERROR {err}")
            finally:
                if fh:
                    fh.close()

    def quit_program():
        global can_be_saved
        if can_be_saved:
            ask = input('Do you want to save beofre quit [s/n]? ').strip().lower()[0]
            if ask == 's':
                save_file()
        sys.exit()

    os.system('clear')

    while True:        
        print_lst_content(lst_content)

        user_options = {"A": add_item, "D": delete_item, "S": save_file, "Q": quit_program}

        user_answer = user_options_input(can_be_saved, len(lst_content) > 0)
        
        user_options[user_answer]()
        
        os.system('clear')
        
        

main()