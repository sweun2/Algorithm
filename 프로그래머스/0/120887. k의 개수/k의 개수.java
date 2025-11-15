class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        for(int a = i; a <= j; a++) {
            for(char c : Integer.toString(a).toCharArray()) {
                if (Integer.toString(k).equals(String.valueOf(c))) answer += 1;
            }
        }
        
        return answer;
    }
}