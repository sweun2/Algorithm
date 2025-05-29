def solution(genres, plays):
    pl = dict()
    for i in range(len(plays)):
        if not pl.get(genres[i]):
            pl[genres[i]] = list()
        pl[genres[i]].append((plays[i],i))

    pc = list()
    for gen in pl:
        pl[gen].sort(key = lambda x:(-x[0],x[1]))
        pc.append((sum([x[0] for x in pl[gen]]), gen))
    pc.sort(reverse = True)
    
    result = list()
    for sumv,gen in pc:
        for j in range(0,min(2,len(pl[gen]))):
            result.append(pl[gen][j][1])
    return result
        
        