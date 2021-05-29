#ESI
import random
import math
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
   # print(len(mutation_list)) # długość listy po krzyzowaniu
    for x in range(0, len(mutation_list)):
        #print(mutation_list[x])
        w_lb_psl2 = random.random()
        if w_lb_psl2 <= pr_mut:
            rd = random.randint(0,143)
            rd2 = random.randint(0,143)
            while True:
                if rd == rd2:
                    rd2 = random.randint(0, 143)
                else:
                    break
            #for a in len(mutation_list[x]):
            hej = mutation_list[x][rd]
            mutation_list[x][rd] = mutation_list[x][rd2]
            mutation_list[x][rd2] = hej



    #selekcja
    print(len(mutation_list))
    print(len(tup_144))
    for x in range(0, len(mutation_list)):
        print(mutation_list[x])
        first_x = 0
        first_y = 0
        second_x = 0
        second_y = 0
        result_xy = 0
        for z in range(0, len(mutation_list[x])):
            for a in range(0, len(tup_144)):
                if (mutation_list[x][z])-1 == a:
                    print(mutation_list[x][z])
                    print(tup_144[a])
                    first_x = tup_144[a][0]
                    first_y = tup_144[a][1]
                if z == 143:
                    print(mutation_list[x][0])
                    print(tup_144[a])
                    second_x = tup_144[a][0]
                    second_y = tup_144[a][1]
                else:
                    print(mutation_list[x][z+1])
                    print(tup_144[a])
                    second_x = tup_144[a][0]
                    second_y = tup_144[a][1]
            result_xy += math.fabs(first_x - second_x) + math.fabs(first_y - second_y)

            print(second_x, second_y)
            print(result_xy)
            print(mutation_list[x][0])
      #  for u in range(0, len(tup_144)):
            #if mutation_list[x][0] -1 == u:
              #  result_xy += math.fabs(tup_144[u][0]-second_x) + math.fabs(tup_144[u][1] - second_y)

              #  print(tup_144[u][0])
         #   print(result_xy)
        break
                #mutation_list[x][z] - mutation_list[x][z+1]


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
pr_mut = 0.5
tup_144 = []
tup_127 = []
list_127 = []
list_144 = []
do_144()



