import sys
import optparse
import os
import time


USAGE_MESSAGE = "Usage: ls.py [options] [path1 [path2 [... pathN]]]"

def terminal_options() -> tuple:
    parser = optparse.OptionParser(usage=USAGE_MESSAGE)
    parser.add_option("-m", "--modified", action="store_true",dest="modified",
        help="show last modified date/time [default: off]")
    parser.add_option("-H", "--hidden", action="store_true",dest="hidden",
        help="show last modified date/time [default: off]")
    parser.add_option("-o", "--ordered", action="store", choices=["name", "n", "modified", "m", "size", "s"], dest="ordered", default="name",
        help="order by ('name', 'n', 'modified', 'm', 'size', 's')")
    parser.add_option("-r", "--recursive", action="store_true",dest="recursive",
        help="recurse into subdirectories [default: off]")
    parser.add_option("-s", "--size", action="store_true",dest="size",
        help="show sizes [default: off]")
    
    return parser.parse_args()


def process_lists(opts, filenames, dirnames):
    import datetime

    keys_lines = []
    for name in filenames:
        modified = ""
        if opts.modified:
            try:
                modified = (datetime.datetime.fromtimestamp(
                                os.path.getmtime(name))
                                    .isoformat(" ")[:19] + " ")
            except EnvironmentError:
                modified = "{0:>19} ".format("unknown")
        size = ""
        if opts.size:
            try:
                size = "{0:>15n} ".format(os.path.getsize(name))
            except EnvironmentError:
                size = "{0:>15} ".format("unknown")
        if os.path.islink(name):
            name += " -> " + os.path.realpath(name)
        if opts.ordered in {"m", "modified"}:
            orderkey = modified
        elif opts.ordered in {"s", "size"}:
            orderkey = size
        else:
            orderkey = name
        keys_lines.append((orderkey, "{modified}{size}{name}".format(
                                     **locals())))
    size = "" if not opts.size else " " * 15
    modified = "" if not opts.modified else " " * 20
    for name in sorted(dirnames):
        keys_lines.append((name, modified + size + name + "/"))
    for key, line in sorted(keys_lines):
        print(line)



def main():   
    options, paths = terminal_options()

    paths = paths if paths else ['.']
    count = [0, 0]

    if not(options.recursive):
        filenames = []
        dirnames = []

        for path in paths:
            if os.path.isfile(path):
                filenames.append(path)
                continue
            for name in os.listdir(path):
                if not options.hidden and name.startswith('.'):
                    continue
                fullname = os.path.join(path, name)
                if fullname.startswith('./'):
                    fullname = fullname[2:]
                if os.path.isfile(fullname):
                    filenames.append(fullname)
                else:
                    filenames.append(fullname)
        count[0] = len(filenames)
        count[1] = len(dirnames)
        process_lists(options, filenames, dirnames)       
                
    else: 
        for path in paths:
            for root, dirs, files in os.walk(path):
                if not options.hidden:
                    dirs[:] = [dir for dir in dirs if not dir.startswith('.')]
                filenames = []
                for name in files:
                    if not options.hidden and name.startswith("."):
                        continue
                    fullname = os.path.join(root, name)
                    if fullname.startswith("./"):
                        fullname = fullname[2:]
                    filenames.append(fullname)

            count[0] = len(filenames)
            count[1] = len(dirs)
            process_lists(options, filenames, [])
    
    files_n = f"{count[0]:n}" if count[0] else "no"
    directories_n = f"{count[1]:n}" if count[1] else "no"

    print(f"{files_n} file{'s' if count[0] != 1 else ''}, {directories_n} director{'ies' if count[1] != 1 else 'y'}")

        
       
if __name__ == "__main__":
    main()