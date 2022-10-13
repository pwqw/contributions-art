import os
from datetime import timedelta
from git import Repo


THE_EDIT_FILE = os.getcwd() + '/+arte♡.dat'


def valida_coherencia(cadena):
    assert len(cadena) % 7 == 0


def edit_a_file():
    try:
        with open(THE_EDIT_FILE, 'r') as f:
            line = f.readline()
            if '¿y el arte?' in line:
                write = '¿qué arte?'
            else:
                write = '¿y el arte?'
            f.close()
    except FileNotFoundError:
        write = '¿y el arte?'
    with open(THE_EDIT_FILE, 'w+') as f:
        f.write(write)
        f.close()
    return write


def do_the_commits(contributions, datetime):
    contributions = int(contributions)
    if contributions == 4:
        commits = 12
    elif contributions == 3:
        commits = 4
    elif contributions == 2:
        commits = 2
    elif contributions == 1:
        commits = 1
    else:
        commits = 0
    index = Repo(os.getcwd()).index
    for i in range(commits):
        m = edit_a_file()
        index.add(THE_EDIT_FILE)
        date = datetime + timedelta(seconds=i * 3)
        index.commit(m, commit_date=date, author_date=date)
