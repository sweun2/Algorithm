import java.util.*;
class Solution {
    public int solution(int[] array) {
        Map<Integer,Integer> d = new HashMap<>();
        int max = 0;
        for (int num: array) {
            d.put(num,d.getOrDefault(num,0)+1);
            max = Math.max(max, d.get(num));
        }
        int cnt = 0;
        int m = -1;
        for (Map.Entry<Integer,Integer> e : d.entrySet()) {
            if(e.getValue()== max) {
                cnt +=1;
                m = e.getKey();
            }
            if (cnt >1) return -1;
        }
        return m;
    }
}