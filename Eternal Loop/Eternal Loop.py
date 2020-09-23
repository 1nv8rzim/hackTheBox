from os import system, chdir, listdir

used = {'Eternal Loop.py', 'Eternal Loop.zip', '.DS_Store', 'temp.txt'}
try:
    chdir('Eternal Loop')
except:
    pass


def ls():
    return set(listdir())


def new_zip():
    temp = ls() - used
    return temp.pop()


def password():
    system('strings ' + new_zip() + ' > temp.txt')
    with open('temp.txt') as file:
        output = file.readline().strip()

    temp = output.split('.')[0]
    try:
        int(temp)
        return temp
    except:
        with open('temp.txt') as file:
            return file.readlines()[-1].strip().split('.')[0]


def unzip():
    temp = new_zip()
    # print('unzip -P ' + password() + ' ' + temp)
    system('unzip -P ' + password() + ' ' + temp)
    try:
        int(password())
        system('rm ' + temp)
    except:
        raise ValueError
    # used.add(temp)


while True:
    try:
        unzip()
    except:
        break
