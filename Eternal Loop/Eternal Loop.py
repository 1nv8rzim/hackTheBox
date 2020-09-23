from os import system, chdir, listdir

used = {'Eternal Loop.py', 'Eternal Loop.zip', '.DS_Store'}
chdir('Eternal Loop')


def ls():
    return set(listdir())


def new_zip():
    temp = ls() - used
    return temp.pop()


def strings():
    system('strings ' + new_zip() + ' > temp.txt')
    with open('temp.txt') as file:
        output = file.readline().strip()
    return output
