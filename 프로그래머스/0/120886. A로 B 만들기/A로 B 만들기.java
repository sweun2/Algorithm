class Solution {
    public int solution(String before, String after) {
        int[] alpha = new int[26];
        
        for(char c : before.toCharArray()) {
            alpha[c - 'a'] += 1;
        }
        for(char c : after.toCharArray()) {
            alpha[c - 'a'] -= 1;
        }
        
        for(int i : alpha) {
            if (i != 0) return 0;
        }
        return 1;
    }
}