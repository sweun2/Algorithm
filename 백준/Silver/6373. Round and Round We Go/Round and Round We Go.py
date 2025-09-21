import sys
while True:
    number = sys.stdin.readline().strip()
    if not number:
        break

    def is_cycle(number):
        ds = number * 2
        for i in range(1,len(number)+1):
            
            checked = str(int(number) * i)
            
            if len(number) > len(checked):
                checked = (len(number) - len(checked)) * "0" + checked
                
            if checked not in ds:
                return False
        return True

    
    if is_cycle(number):
        print(number + " is cyclic")
    else:
        print(number + " is not cyclic")