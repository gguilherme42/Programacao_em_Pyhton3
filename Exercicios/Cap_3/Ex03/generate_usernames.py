import sys
from collections import namedtuple

ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)

User_tuple = namedtuple("User_tuple", "username forename middlename surname id")

def validate_start() -> None:
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print(f"Usage: {sys.argv[0]} file1 [fil2 [...fileN]]")
        sys.exit()


def generate_username(fields: list(), usernames: set) -> str:
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



def print_header(name_width: int, username_width: int) -> None:
    print(f"{'Name':<{name_width}} {'ID':^6} {'Username':{username_width}}")
    print(f"{'':-<{name_width}} {'':-<6} {'':-<{username_width}}")



def print_users(users: dict) -> None:
    name_width = 32
    username_width = 9
    print_header(name_width, username_width)

    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        name = f"{user.surname}, {user.forename} {initial}"
        
        print(f"{name:.<{name_width}} ({user.id:4}) {user.username:{username_width}}")



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