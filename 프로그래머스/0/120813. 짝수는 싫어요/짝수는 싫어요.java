import java.util.*;
class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> result = new ArrayList<>();
        
        for(int i=1; i<=n; i++) {
            if (i%2==1) result.add(i);
        }
        return result.stream().mapToInt(i->i).toArray();
    }
}