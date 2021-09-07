from tabulate import tabulate
# import psutil
import random
import time


class Stack(object):
    def __init__(self):
        self.items = []
        self.maxsize = 0
        self.size = 0

    def push(self, value):
        self.items.append(value)

    def pop(self):
        try:
            val = self.items.pop()
            return val
        except(IndexError):
            print("Stack is empty.")

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Stack is empty.")

    def isEmpty(self):
        return not bool(self.items)

    def isFull(self):
        if self.getStackSize() == self.maxsize:
            return True
        else:
            return False

    def getStackSize(self):
        self.size = len(self.items)
        return self.size

    def printStack(self):
        if self.items:
            print(self.items)
        else:
            print("Stack is empty.")

    def getSizeOfChs(self):

        while True:
            try:
                n = int(input("Please input the chessboard size >>"))
                if not 4 <= n <= 9:
                    raise ValueError
                else:
                    self.maxsize = n
                    break
            except(ValueError):
                print("Input right value.")
                pass






def findPosition(stack):

    if stack.isEmpty():
        rdmidx = [random.randrange(1, stack.maxsize+1), random.randrange(1, stack.maxsize+1)]
        stack.push(rdmidx)
        # print("첫 퀸", rdmidx)
        notEmpty = True
    else:
        notEmpty = True

    # for i in range(stack.size, stack.max+1):

    while notEmpty:

        if stack.isFull():
            return True # return값 다시 설정 필요
            break

        # stack.printStack()
        if stack.peek()[0] >= stack.maxsize: raw = stack.peek()[0]-stack.maxsize +1
        else: raw = stack.peek()[0]+1


        for i in range(stack.maxsize): #한 행에서 4번 검사 -> 어떤 행인지 알려줄 필요 있음
            # print("현재 인덱스",raw, i+1)

            idx = [raw, i+1]

            bool = verify(stack, idx) #수정
            # print("검증 결과",bool)
            if bool:
                stack.push(idx)
                break  # for문 탈출

        if not bool:
            # print("There is no valid position. Start Backtracking.")
            stack = backTracking(stack)




def backTracking(stack):

    while True:
        pop = stack.pop()
        # stack.printStack()


        if stack.isEmpty():
            # print("실행되니?")
            idx = [pop[0], pop[1]+1]
            stack.push(idx)
            return stack
            break

        elif pop[1]!=stack.maxsize:
            idx = [pop[0], pop[1]]
            for i in range(pop[1],stack.maxsize):#pop한 좌표 다음 좌표부터 집어넣기, (2,3) pop -> (2,4)
                idx[1]+=1
                # print("인덱스 더함", idx)
                bool = verify(stack, idx)
                # print("검증결과", bool)
                if bool: #for문 탈출
                  stack.push(idx)
                  break

            if bool: #while문 탈출
                return stack
                break

        else:
            pass # 스택 하나 더 pop






def verify(stack, idx):
    # 인덱스 받아서 열 및 대각선에 여왕이 있는지 검사
    # 없으면 True 아니면 False
    flg = None
    for raw, col in stack.items:
        # print("스택 인덱스 열",raw, col)
        if idx[1] == col:
            flg = False
            break

        elif (col-idx[1])/(raw-idx[0]) == -1 or (col-idx[1])/(raw-idx[0]) == 1:
            # print("기울기",(col-idx[1])/(raw-idx[0]))
            flg = False
            break

        else:
            flg = True

    return flg


    # mat=[]
    # for i in range(stack.maxsize):
    #     rowList = []
    #     for j in range(stack.maxsize+1):
    #         rowList.append("|     |")
    #
    #     mat.append(rowList)

def printChessBoard(stack):

    mat = [["|     |"] * (stack.maxsize+1) for i in range(stack.maxsize)]

    for raw, col in stack.items:

        mat[raw-1][0] = "Row %d - Col %d" %(raw, col)
        # print(raw-1, col)
        mat[raw-1][col] = ("|  Q  |")

    print(tabulate(mat))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    timelist = []
    # memlist = []
    # mem = psutil.virtual_memory()
    for i in range(100000):


        ChsBrd = Stack()
        # ChsBrd.getSizeOfChs()
        ChsBrd.maxsize = 9
        start = time.time()
        findPosition(ChsBrd)
        # printChessBoard(ChsBrd)


        timelist.append(time.time() - start)
        # memlist.append(mem.percent)

    # print(sum(timelist), len(timelist))
    print(sum(timelist) / len(timelist))
    # print(sum(memlist)/len(memlist))


# start = time.time()
#
# ChsBrd = Stack()
# ChsBrd.maxsize = getSizeOfChs()
# findPosition(ChsBrd)
# # while True: #findPosition과 BackTracking을 함수 내에서 연결하는 것도 괜찮을듯ㄱ
# #     if not : #출력후 백트래킹 넘어가기
# #         backTracking(ChsBrd)
# printChessBoard(ChsBrd)
#
# print("time", time.time() - start)