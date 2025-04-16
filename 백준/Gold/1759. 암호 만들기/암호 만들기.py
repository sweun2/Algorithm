l,c = map(int,input().split())
code = sorted(list(input().split()))

def back(result:str):
    if len(result) == l:
        mom = result.count("a")+result.count("e")+result.count("i")+result.count("o")+result.count("u")
        son = l - mom
        
        if mom>=1 and son >=2:
            print(result)
        return
    
    for i in code:
        if(is_valid(result,i)):
            back(result + i)
        


def is_valid(result:str,i):
    if result.count(i) !=0:
        return False
    
    for s in result:
        if s>i:
            return False 
    return True

back("")