'''
A undirected, unweighted graph with N vertices and M edges is given on standard input.
The vertices are numbered from 1 to N. The first input line contains the number N ≤ 100, and the second input line contains M.
After that, M lines follow, each of which describes a single edge of the graph.
An edge is specified by the numbers of two distinct vertices that it connects.

Write a program that determines the connected components of the given graph. 
On each output line, write a list of vertices that form a single connnected component.
Use spaces to separate the numbers on each line.
Each of the numbers 1 through N will appear exactly once in the output, since each vertex will lie in exactly one connected component. 
You may write the connected components in any order, and you may likewise list the vertices in each connected component in any order.

Example of input:

10
7
1 2
5 9
4 6
1 8
8 2
7 6
2 10
One possible correct output:

1 2 8 10
3
7 4 6
5 9

'''


N = int(input())
M = int(input())

adjecent = [[] for x in range(N+1)]
visited = [False for i in range(N+1)]

for i in range(M):
    edge = list(map(int, input().split()))
    adjecent[edge[0]].append(edge[1])
    adjecent[edge[1]].append(edge[0])
    

def find_components(peak,component):
    visited[peak] = True
    for i in adjecent[peak]:
        if visited[i] == False:
            component.append(i)
            find_components(i, component)
    return component
        
        
for i in range(1,N+1):
    if visited[i] == False:
        new_component = []
        new_component.append(i)
        new_component = find_components(i, new_component)
        print(*new_component)