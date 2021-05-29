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
    ile_os_list = []
    list_144 = read_file_144()
    for x in list_144[6:-1]:
        changed_144 = x.split()[1:]
        tup1 = (int(changed_144[0]), int(changed_144[1]))
        tup_144.append(tup1)
    for a in range(1,ile_os+1):
        os_144 = []
        for x in range(1, 145):
            os_144.append(x)
        random.shuffle(os_144)
        ile_os_list.append(os_144)

    #krzyzowanie
    intersection_list = []
    intersection_list_results = []

    for x in range(0,ile_os):
        intersection_list.append(x)
    random.shuffle(intersection_list)

    for z in range(0, ile_os,2):
        w_lb_psl = random.random()
        if w_lb_psl <= pr_krzyz:
            p1 = ile_os_list[intersection_list[z]][:72]
            osobnik2 = ile_os_list[intersection_list[z+1]]
            p2 = []
            for v in range(0, len(p1)):
                for o in range(0,len(osobnik2)):
                    if p1[v] == osobnik2[o]:
                        osobnik2[o] = 0
            for e in range(0, len(osobnik2)):
                if osobnik2[e] != 0:
                    p2.append(osobnik2[e])

            intersection_list_results.append(p1+p2)
            #print(intersection_list_results)

    #mutacja
    mutation_list = []
    mutation_list = ile_os_list + intersection_list_results
    print(len(mutation_list)) # długość listy po krzyzowaniu
   #print(mutation_list)



def do_127():
    ile_os_list = []
    list_127 = read_file_127()
    for x in list_127[6:-1]:
        changed_127 = x.split()[1:]
        tup1 = (int(changed_127[0]),int(changed_127[1]))
        tup_127.append(tup1)
    for a in range(1, ile_os + 1):
        os_127 = []
        for x in range(1, 145):
            os_127.append(x)
        random.shuffle(os_127)
        ile_os_list.append(os_127)
    print(tup_127)


ile_os = 200
pr_krzyz = 0.5
tup_144 = []
tup_127 = []
list_127 = []
list_144 = []
do_144()



