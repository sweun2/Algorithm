import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        Arrays.sort(targets, ((x,y)->x[0]-y[0]));
        int a =targets[0][0];
        int b =targets[0][1];
        int cnt =1;
        for(int[] target: targets){
            if(a == target[0]) {
                b= target[1];
            }  
            else {
                if(b>a) {
                    a=target[0];
                    b=target[1];
                }
                else {
                    cnt+=1;
                    a=target[0];
                    b=target[1];
                }
            }
        }
        return cnt;
    }
}