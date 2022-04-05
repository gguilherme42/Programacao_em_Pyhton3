import collections

User = collections.namedtuple("User", "username forename middlename surname id")
ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)
NAMEWIDTH = 17
USERNAMEWIDTH = 9


def generate_username(fields: list, usernames: set) -> str:
    new_username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] + fields[SURNAME]).replace("-", "").replace("'", ""))

    new_username = original_name = new_username[:8].lower()

    count = 1
    while new_username in usernames:
        new_username = f"{original_name}{count}"
        count += 1
    
    return new_username


def process_line(line: str, usernames: set) -> User:
    fields = line.split(":")
    username = generate_username(fields, usernames)
    
    usernames.add(username)

    user = User(username, fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])
    return user


def create_user_fullname(user: User) -> str:
    initial = ''
    if user.middlename:
        initial = f" {user.middlename[0]}"
    name = f"{user.surname}, {user.forename} {initial}"
    return f"{name:.{NAMEWIDTH}}"   

def print_column_header():
    column_title = f"{'Name':<{NAMEWIDTH}} {'ID':^6} {'Username':{USERNAMEWIDTH}}"
    column_title_underline = f"{'':-<{NAMEWIDTH}} {'':-<6} {'':-<{USERNAMEWIDTH}}"
    print(f"{column_title} {'':10} {column_title}")
    print(f"{column_title_underline} {'':10} {column_title_underline}")


def print_new_page(page_number: int):
    if page_number % 63 == 0:
        print('' if page_number == 0 else '\n')
        print_column_header()


def print_rl_users(r_user: User, l_user: User):
    l_name = create_user_fullname(l_user)
    r_name = create_user_fullname(r_user)

    left_user_to_print = f"{l_name:<{NAMEWIDTH}} {l_user.id:^6} {l_user.username:<{USERNAMEWIDTH}}"

    right_user_to_print = f"{r_name:.<{NAMEWIDTH}} {r_user.id:^6} {r_user.username:<{USERNAMEWIDTH}}"

    print(f'{left_user_to_print} {"":10} {right_user_to_print}')


def create_users_pair(users: dict[User]) -> enumerate[tuple[dict[User]]]:
    ordered_users = sorted(users)
    left_users, right_users =  ordered_users[::2], ordered_users[1::2] # odd and even
    users_pair = zip(left_users, right_users)

    return enumerate(users_pair)

def print_users(users: dict[User]):    
    for i, (left_user, rigth_user) in create_users_pair(users): 
        l_user, r_user = users[left_user], users[rigth_user]

        print_new_page(i)
        print_rl_users(r_user, l_user)


def main():
    import sys
    
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print(f"usage: {sys.argv[0]} file1 [file2 [...fileN]]")
        sys.exit()

    usernames: set[str] = set()
    users: dict[User] = {}

    for filename in sys.argv[1:]:
        for line in open(filename, encoding="utf8"):
            line = line.strip()
            if line:
                user = process_line(line, usernames)
                users[(user.surname.lower(), user.forename.lower(), user.id)] = user
    
    print_users(users)


main()