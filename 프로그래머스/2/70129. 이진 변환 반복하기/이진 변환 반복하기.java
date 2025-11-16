class Solution {
    public int[] solution(String s) {
        int[] answer = {0,0};
        int change = 0;
        int removed = 0;
        while (!s.equals("1")) {
            int before = s.length();
            s = s.replace("0","");
            int after = s.length();
            removed += before - after;
            
            s = Integer.toBinaryString(after);
            
            change +=1;
        }
        answer[0] = change;
        answer[1] = removed;
        return answer;
    }
}