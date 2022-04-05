import collections

User = collections.namedtuple("User", "username forename middlename surname id")
ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)


def generate_username(fields: list, usernames: set) -> str:
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] + fields[SURNAME]).replace("-", "").replace("'", ""))

    username = original_name = username[:8].lower()

    count = 1
    while username in usernames:
        username = f"{original_name}{count}"
        count += 1
    usernames.add(username)
    
    return username


def process_line(line: str, usernames: set) -> User:
    fields = line.split(":")
    username = generate_username(fields, usernames)
    
    user = User(username, fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])
    return user


def print_users(users: dict):
    namewidth = 32
    usernamewidth = 9

    print(f"{'Name':<{namewidth}} {'ID':^6} {'Username':{usernamewidth}}")
    print(f"{'':-<{namewidth}} {'':-<6} {'':-<{usernamewidth}}")

    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.middlename:
            initial = f" {user.middlename[0]}"
        name = f"{user.surname}, {user.forename} {initial}"
        print(f"{name:.<{namewidth}} {user.id:4} {user.username:{usernamewidth}}")


def main():
    import sys
    
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print(f"usage: {sys.argv[0]} file1 [file2 [...fileN]]")
        sys.exit()

    usernames = set()
    users = {}

    for filename in sys.argv[1:]:
        for line in open(filename, encoding="utf8"):
            line = line.strip()
            if line:
                user = process_line(line, usernames)
                users[(user.surname.lower(), user.forename.lower(), user.id)] = user
    
    print_users(users)


main()