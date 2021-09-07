# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import itertools
import time
import numpy as np


def cityMap():
    f = open("city.txt", 'r', encoding='UTF8')
    lines = f.readlines()
    cityMap = [[int(lines[i].split()[n]) for n in range(17)] for i in range(17)]

    return cityMap


def cityDist(strt, end):
    return cityMap()[strt - 1][end - 1]


def menu():
    while True:
        try:
            mn = int(input("Shortest path(1) or Tsp(2)? Please input the menu number."))
            if mn == int(1):
                return mn
                break
            elif mn == int(2):
                return mn
                break
            else:
                raise ValueError

        except:
            print("Please input the right value")


def shortestMenu():
    while True:
        try:
            # ans = list(map(int, input("Please input the start & end. ex) 7 11").split()))
            strt = int(input("Please input the start city"))
            end = int(input("Please input the end city"))
            if not 0<strt<18 or not 0<end<18:
                raise ValueError
            return strt, end
            break
        except ValueError:
            print("Please input the right value")


def TSPMenu():
    while True:
        try:
            num = int(input("Please input the TSP size(3~17)"))
            if num < 3 or num > 17:
                raise ValueError
            else:
                return num
                break
        except:
            print("Please input the right value")


def TSPMap(num):
    mparr = np.array(cityMap())
    mp = list(map(list, mparr[:num, :num]))
    return mp


def findShortestCase(start, end, distance):
    shortest = ["", 999]

    def searchCase(start, end, length,tmplist):
        start -= 1
        end -= 1
        # print("시작:", start, "끝:", end, "현재경로:", tmplist, "길이:", length)
        if tmplist == "":
            tmplist += "%d" % (start+1)
        # print("현재경로", tmplist, "길이", length)

        if distance[start][end] == -1 or distance[start][end] ==0:
            # print("경로가 없거나 자신일때", start, end)
            return

        if distance[start][end] != -1:
            cmprLength =  length + distance[start][end]
            cmprList = tmplist + ",%d" % (end+1)
            # print("도착지까지의 길이:", cmprLength, "도착지까지의 경로:", cmprList)
            if cmprLength < shortest[1]:
                # print("Shortest에 저장", "현재 길이:",cmprLength, "현재 Shortest 길이:",shortest[1])
                shortest[0] = cmprList
                shortest[1] = cmprLength

        for i in range(17):
            # print("현재 길이:", length, "현재 경로", tmplist, "현재 개수", i+1)
            if start != i and distance[start][i] != -1 and length+distance[start][i] < shortest[1] and distance[start][i] != 0:
                nlength = length + distance[start][i]
                nlist = tmplist+ ",%d" % (i+1)
                searchCase(i+1, end+1, nlength, nlist)
            else:
                continue
        return shortest

    return searchCase(start, end, 0, "")
# length > shortest[1]
# else:
# length += cityDist(start, end)
# tmplist += ",%d" % (start)

def permute(num):
    # n<=10 일 때만 사용가능
    inpList = [x + 1 for x in range(num)]
    permutation = list(itertools.permutations(inpList))
    # print(permutation)
    # permutation = list(map(lambda x: ''.join(x), permutation))
    return permutation


def distanceCalc(list, distance):
    shortest = [" ", 999999]
    for prmt in list:
        flg = True
        tmpdis = 0
        # print("reset",tmpdis)
        for idx, i in enumerate(prmt):
            # print("i", i)
            if i == prmt[-1]: #13254
                if distance[int(i)-1][int(prmt[0])-1] == -1:
                    flg = False
                else:
                    tmpdis += distance[int(i)-1][int(prmt[0])-1]
                break
            # print("distance",cityDist(int(i),int(prmt[idx+1])), i)
            if distance[int(i)-1][int(prmt[idx + 1])-1] == -1:
                flg = False
                break
            tmpdis += distance[int(i)-1][int(prmt[idx + 1])-1]

        # print("nowtmpdis", tmpdis, "shortest", shortest[1])
        if tmpdis < shortest[1] and flg:
            shortest[0] = prmt
            shortest[1] = tmpdis
            # print("nowshortest",shortest)

    return shortest


def TSP(distance):
    N = len(distance)
    VISITED_ALL = (1 << N) - 1  # if n이 5일때, 11111(전부 다녀간 경우) 만들어줌
    cache = [[None] * (1 << N) for _ in range(N)]
    INF = float('inf')

    def find_path(last, visited): #last: 중간(현재까지 방문한) 경로의 마지막도시, #visited: 방문한 도시의 집합
        if visited == VISITED_ALL:
            if distance[last][0] ==-1:
                return [], INF
            return [last+1], distance[last][0]

        if cache[last][visited] is not None: #cache에 있으면 그거 재사용
            return cache[last][visited]

        tmp = INF
        tmplist = []

        for city in range(N):
            # print("Come in for statement")
            if visited & (1 << city) == 0 and distance[last][city] != -1 : #visited & (1 << city) == 0 -> 아직 방문하지 않음 distance[last][city] != -1: 경로가 존재함
                ncity, ntmp = find_path(city, visited | (1 << city))
                ntmp += distance[last][city]
                ntmplist = [last+1] + ncity
                if ntmp < tmp:
                    tmplist = ntmplist
                    tmp = min(tmp, ntmp) #visited | (1 << city): city가 포함된 경로 갱신

        cache[last][visited] = tmplist, tmp
        return tmplist, tmp

    return find_path(0, 1 << 0) #0001


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Cmap = cityMap()
    mn = menu()
    if mn == 1:
        start, end = shortestMenu()
        st = time.time()
        print(findShortestCase(start, end, Cmap))
        print(time.time()-st)

    elif mn == 2:
        n = TSPMenu()
        mp = TSPMap(n)
        st = time.time()
        print("%d의 최단경로" % n, TSP(mp))
        # print(distanceCalc(permute(10), Cmap))
        print(time.time() - st)
