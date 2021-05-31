#ESI
import random
import math
import time

def read_file_144():
    file = input("Podaj nazwe pliku: ")
    f = open(file, "r")
    file_144 = f.readlines()
    f.close()
    return file_144

def XD():
    global list_144
    list_144 = read_file_144()

def do_first():
    #ile_os_list.clear()
    global list_length, list_144

    list_length = int(list_144[3].split()[2])
    #print(list_length)
    for x in list_144[6:-1]:
        changed_144 = x.split()[1:]
        tup1 = (int(changed_144[0]), int(changed_144[1]))
        tup_144.append(tup1)
    for a in range(1,ile_os+1):
        os_144 = []
        for x in range(0, list_length):
            os_144.append(x)
        random.shuffle(os_144)
        ile_os_list.append(os_144)

def intersection():   #krzyzowanie
    #print(ile_os_list)
    intersection_list = []
    #r2 = 0
    p2 = []
    r2 = []
    for x in range(0,ile_os):
        intersection_list.append(x)
    random.shuffle(intersection_list)

    for z in range(0, ile_os,2):
        w_lb_psl = random.random()
        if w_lb_psl <= pr_krzyz:
            r1 = ile_os_list[intersection_list[z]][:list_length//2]
            for s in range(0, len(ile_os_list[intersection_list[z+1]])):
                r2.append(ile_os_list[intersection_list[z+1]][s])
            for v in range(0, len(r1)):
                for o in range(0,len(r2)):
                    if r1[v] == r2[o]:
                        r2[o] = -1
            for e in range(0, len(r2)):
                if r2[e] != -1:
                    p2.append(r2[e])
            intersection_list_results.append(r1+p2)
   # print("XDXDXDXDXDXDXDXDXD")
   # print(ile_os_list)
            #print(intersection_list_results)
            #print(r1)
           # print(p2)
            #print(intersection_list_results)
           # print(len(r1))
            #print(len(r2))
           # print(len(p2))
            #print(len(intersection_list_results))
    #intersection_list_results.clear()
   # intersection_list.clear()
    #print(r1)
    #print(r2)
    #print(p2)
   # print(intersection_list_results)
    #print(len(r1+p2)


def mutation():   #mutacja
    global ile_os_list
    mutation_list = ile_os_list + intersection_list_results

    for x in range(0, len(mutation_list)):
        #print(mutation_list[x])
        w_lb_psl2 = random.random()
        if w_lb_psl2 <= pr_mut:
            rd = random.randint(0,(list_length-1))
            rd2 = random.randint(0,(list_length-1))
            while True:
                if rd == rd2:
                    rd2 = random.randint(0, (list_length-1))
                else:
                    break
            #for a in len(mutation_list[x]):
            hej = mutation_list[x][rd]
            #print(mutation_list[x])
            mutation_list[x][rd] = mutation_list[x][rd2]
            mutation_list[x][rd2] = hej
    ile_os_list = mutation_list



def count_road(arrr):
    result_xy = 0.0
    for a in range(0, len(arrr)-1):
        result_xy += math.fabs(tup_144[arrr[a]][0] - tup_144[arrr[a+1]][0]) + math.fabs(tup_144[arrr[a]][1] - tup_144[arrr[a+1]][1])
    result_xy += math.fabs(tup_144[arrr[0]][0] - tup_144[arrr[-1]][0]) + math.fabs(tup_144[arrr[0]][1] - tup_144[arrr[-1]][1])
    return result_xy
def selection():   #selekcja

    global ile_os_list
    ile_os_list.sort(key=lambda x: count_road(x), reverse= True) # sortuje od najdluzszej trasy do najkrotszej
    wagi = [ i + 1 for i in range(len(ile_os_list))] # ustalam wagi, uzupelniam liste od 1 do 144, najdluzsza ma namniejsza wage a najktotsza najwieksza
    nowa_lista = random.sample(ile_os_list, k=len(ile_os_list), counts=wagi) #losuje k ellementów z ille os list z czego te elelmeenty maja prawdopodobnienstwo wypadnieecia z listy wagi
    ile_os_list = nowa_lista

def sortt():
    ile_os_list.sort(key=lambda x: count_road(x))
    xxx = int(count_road(ile_os_list[0]))
    xxx1 = ile_os_list[0]
    print(int(xxx))
    print(ile_os_list[0])
    with open("esi_db.txt", "a") as f:
        print(f"{xxx1} {xxx}", file=f)
        print("", file=f)
def start():
    czas = int(input("Podaj czas wykonywania programu w sekundach: "))
    startTime = time.time()
    XD()
    for x in range(0,10):
        ile_os_list.clear()
        do_first()
        while time.time() - startTime < czas:
            intersection()
            mutation()
            selection()
        sortt()
    with open("esi_db.txt", "a") as f:
        print("******************************", file=f)


ile_os = 200
pr_krzyz = 1
pr_mut = 0.5
tup_144 = []
tup_127 = []
list_127 = []
list_144 = []
list_length = 0
ile_os_list = []

intersection_list_results = []
mutation_list = []
list_144 = []
#do_144()
#do_127()
start()


