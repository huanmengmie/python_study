# -*- coding:UTF-8 -*-
"""模拟登陆注册功能"""

db = {}
def newUser():
    prompt = 'enter your name: '
    while True:
        name = input(prompt)
        if name in db:
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = input('password: ')
    db[name] = pwd


def login():
    name = input("name: ")
    pwd = input("pwd: ")
    passwd = db.get(name)
    if pwd == passwd:
        print('welcome',name)
    else:
        print('login incorrect')


def showMenu():
    prompt = """
        [N]ew
        [L]ogin
        [Q]uit
        Enter choice:
    """
    done = False
    while not done:
        chose = False
        while not chose:
            choice = input(prompt).strip()[0].lower()
            print('\n you picker [%s]' % choice)
            if choice not in 'nlq':
                print('invalid option, try again')
            else:
                chose = True
        if choice == 'n':
            newUser()
        if choice == 'l':
            login()
        if choice == 'q':
            done = True

if __name__ == '__main__':
    showMenu()
