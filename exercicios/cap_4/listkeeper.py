import os

def filter_lst_files() -> dict:
    result = filter(lambda file: file.endswith(".lst"), os.listdir("."))
    return sorted(result)

def process_file(filename: str):
    fh = None
    try:
        fh = open(filename, "wr", enconding="utf8")
    except EnvironmentError as err:
        print(f"ERROR → {err}")
    finally:
        fh.close()

def print_lst_files(lst_files: list):
    for i, value in enumerate(lst_files):
        print(f"{i:3} {value}")
        

def main(): 
    existing_lst_files = filter_lst_files()
    filename = None 

    if existing_lst_files:
        print_lst_files(existing_lst_files)
        filename = input("Choose a filename: ")
    else:
        print("No files were find. Create a new file")
        filename = input("Enter a filename: ")
    
    process_file(filename)
        

main()