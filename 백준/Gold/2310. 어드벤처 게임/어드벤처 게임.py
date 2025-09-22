from collections import deque
while True:
    n = int(input())
    if n == 0:
        break
    graph = [[] for i in range(n+1)]
    room = [('E',0)]*(n+1)
    for i in range(1,n+1):
        temp = input().split()
        room[i] = temp[0],int(temp[1])
        if len(temp) <= 3:
            continue
        
        graph[i] = list(map(int,temp[2:-1]))
    visited = [False] * (n+1)
    visited[1] = True
    global flag
    flag = False
    
    def dfs(x,cur_money,depth):
        global flag
        room_info = room[x]
        if depth == n and x!=n:
            return
        if x == n:
            if room_info[0] =='T' and room_info[1]>cur_money:
                return
            else:
                flag = True
                return
        
        for next_room in graph[x]:
            if not visited[next_room]:
                visited[next_room] = True
                
                if room_info[0] == 'E':
                    dfs(next_room,cur_money,depth+1)
                elif room_info[0]  == 'L':
                    dfs(next_room, max(cur_money,room_info[1]),depth+1)
                else:
                    if room_info[1] <= cur_money:
                        dfs(next_room, cur_money - room_info[1],depth+1)
                    else:
                        return
                visited[next_room] = False
        
    dfs(1,0,0)
    
    if flag:
        print("Yes")
    else:
        print("No")       