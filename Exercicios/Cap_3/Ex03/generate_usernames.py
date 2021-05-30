import sys
from collections import namedtuple

ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)

User_tuple = namedtuple("User_tuple", "username forename middlename surname id")

def validate_start() -> None:
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print(f"Usage: {sys.argv[0]} file1 [fil2 [...fileN]]")
        sys.exit()


def generate_username(fields: list, usernames: set) -> str:
    new_username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] + fields[SURNAME]).replace("-", "").replace("'", ""))
    new_username = original_username = new_username.lower()[:8] # limit of an username is 8
    count = 1

    while new_username in usernames:
        new_username = f'{original_username}{count}'
        count += 1
    
    usernames.add(new_username)
    return new_username


def process_line(line: str, usernames: set) -> User_tuple:
    fields = line.split(':')
    new_username = generate_username(fields, usernames)
    new_user = User_tuple(new_username, fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])    
    return new_user



def printable_header(name_width: int, username_width: int) -> str:
    return f"{'Name':<{name_width}} {'ID':^6} {'Username':{username_width}}"
    

def printable_divider(name_width: int, username_width: int) -> str:
    return f"{'':-<{name_width}} {'':-<6} {'':-<{username_width}}"


def fix_len_columns(column1_list: list, column2_list: list) -> None:
    # It needs to be fixed because we need pairs to zip()
    if len(column1_list) > len(column2_list):
        column2_list.append("")
    elif len(column1_list) < len(column2_list):
        column1_list.append("")


def two_users_per_line(column1_list: list, column2_list: list, users: dict, name_width: int, username_width: int) -> None:
    count = 0
    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        name = f"{user.surname}, {user.forename} {initial}"
        name_limit = name_width if len(name) >= name_width else len(name)
        name = name[:name_limit]
        
        printable_result = f"{name:.<{name_width}} ({user.id:4}) {user.username:{username_width}}"

        if count % 2 == 0:
            column1_list.append(printable_result)
        else:
            column2_list.append(printable_result)
        count += 1
    
    fix_len_columns(column1_list, column2_list)




def print_users(users: dict) -> None:
    name_width = 17
    username_width = 9
    

    column1_list = [printable_header(name_width, username_width), printable_divider(name_width, username_width)]
    column2_list = [printable_header(name_width, username_width), printable_divider(name_width, username_width)]

    two_users_per_line(column1_list, column2_list, users, name_width, username_width)

    for column1, column2 in zip(column1_list, column2_list):
        print(f"{column1}    {column2}")


def main() -> None:
    validate_start()

    usernames_set = set()
    users_dict = {}

    for filename in sys.argv[1:]:
        for line in open(filename, encoding="utf8"):
            line = line.rstrip()
            if line:
                user = process_line(line, usernames_set)
                users_dict[(user.surname.lower(), user.forename.lower(), user.id)] = user
    
    print_users(users_dict)


if __name__ == "__main__":
    main() 