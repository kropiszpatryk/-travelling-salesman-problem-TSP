#ESI
import random

def read_file_127():
    f = open("bier127.tsp", "r")
    file_127 = f.readlines()
    f.close()
    return file_127

def read_file_144():
    f = open("pr144.tsp", "r")
    file_144 = f.readlines()
    f.close()
    return file_144

def do_144():
    list_144 = read_file_144()
    for x in list_144[6:-1]:
        changed_144 = x.split()[1:]
        tup1 = (int(changed_144[0]), int(changed_144[1]))
        tup_144.append(tup1)
    print(tup_144)

def do_127():
    list_127 = read_file_127()
    for x in list_127[6:-1]:
        changed_127 = x.split()[1:]
        tup1 = (int(changed_127[0]),int(changed_127[1]))
        tup_127.append(tup1)
    print(tup_127)

tup_144 = []
tup_127 = []
list_127 = []
list_144 = []
do_144()



