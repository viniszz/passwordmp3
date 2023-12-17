from time import sleep
import pygame


def principal():
    while True:
        global wrong
        wrong = 1
        print('\033[0;49;97m[1] Register')
        print('[2] Login')
        print('[3] End')
        choice = int(input('Enter your choice: '))
        print()
        if choice == 1:
            print('Loading...')
            print()
            sleep(0.5)
            registerpass()
        elif choice == 2:
            print('Loading...')
            print()
            sleep(0.5)
            loginpass()
        else:
            print('Ending...')
            sleep(1)
            break


def registerpass():
    global register
    register = str(input('\033[0;49;97mType your new password: '))
    if register == 'reset':
        print()
        print("\033[0;49;91mYou can't use this password!")
        print()
        registerpass()
    elif len(register) <= 3:
        print()
        print('\033[0;49;91mYour password is too short!')
        print('\033[0;49;91mIt needs to have at least 4 characters!')
        print()
        registerpass()
    else:
        print()
        print(f'Your new password is: \033[4;49;32m{register}\033[0;49;97m!')
        print()
        principal()


def loginpass():
    if register == '':
        print('\033[0;49;91mPassword not defined!')
        print()
    else:
        global wrong
        login = str(input('\033[0;49;97mUse your password to login: '))
        if login == 'reset':
            print()
            registerpass()
        elif login != register:
            if wrong > 3:
                print()
                print('\033[0;49;91mWrong password!')
                print('\033[0;49;91mYou just forgot your password?')
                print('\033[0;49;91mType "reset" to register again!')
                print()
                loginpass()
            print()
            print('\033[0;49;91mWrong password!')
            wrong += 1
            print()
            loginpass()
        else:
            print()
            print('\033[0;49;32mLogin successfully!')
            print()

            print('\033[0;49;97m[1] Play ColdPlay - A Sky Full Of Stars.')
            print('[2] Play The Chainsmokers - Something just like this.')
            choice2 = int(input('Enter your choice: '))

            if choice2 == 1:
                pygame.init()
                pygame.mixer.music.load('coldplay.mp3')
                pygame.mixer.music.play()
                print()
                input('Press [ENTER] to reload the program.')
                print()
            elif choice2 == 2:
                pygame.init()
                pygame.mixer.music.load('chainsmokers.mp3')
                pygame.mixer.music.play()
                print()
                input('Press [ENTER] to reload the program.')
                print()
                principal()


# PROGRAMA PRINCIPAL
register = ''
wrong = 1

print()
principal()
