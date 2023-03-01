import re
import sys
import threading
import numpy

def compute_height(n, parents):
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            adj_list[parents[i]].append(i)

    def height(v):
        if not adj_list[v]:
            return 1
        else:
            heights = [height(u) for u in adj_list[v]]
            return 1 + max(heights)

    return height(root)

def main():
    # read input from stdin
    Select = input()
    if (Select[0] == "I"):
        n = int(input())
        parents = list(map(int, input().split()))

        # compute height of tree
        height = compute_height(n, parents)

        # output result
        print(height)
    else :
        filename = input()
        fstr = str(filename)
        print("THIS IS THE INPUT" + filename + "THIS IS THE INPUT")
        if (bool(re.search('a', fstr[-2:]))):
            return
        else:
            with open(filename) as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
        # compute height of tree
        height = compute_height(n, parents)
        print("THIS IS THE INPUT" + filename + "THIS IS THE INPUT")
        # print(height)


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
# print(numpy.array([1,2,3]))
