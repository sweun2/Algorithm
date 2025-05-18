import math

a = int(input())
b = int(input())
arr_a = [0] * 19
arr_b = [0] * 19

for i in range(1,18):
    arr_a[i] = (a/100)**(i) * math.comb(18,i) * (1-(a/100))**(18-i) 
    arr_b[i] = (b/100)**(i) * math.comb(18,i) * (1-(b/100))**(18-i)
    

resulta=(arr_a[2]+arr_a[3]+arr_a[5]+arr_a[7]+arr_a[11]+arr_a[13]+arr_a[17])    
resultb=(arr_b[2]+arr_b[3]+arr_b[5]+arr_b[7]+arr_b[11]+arr_b[13]+arr_b[17])    

print(1- ((1-resulta) * (1-resultb)))