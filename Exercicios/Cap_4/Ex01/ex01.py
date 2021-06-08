import os
import sys


print(os.listdir('./'))

def user_option() -> str:
    option = input('[A]dd [D]elete [S]ave [Q]uit [a]: ').lower().strip()[0]
    return option

