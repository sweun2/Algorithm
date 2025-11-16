class Solution {
    public String solution(String s) {
        Boolean flag = true;
        String answer = "";
        for(char c : s.toCharArray()) {
            if (" ".equals(String.valueOf(c))) {
                flag = true;
                answer += " ";
            } 
            else {
                if (flag && (('a'<=c && c<='z') || ('A'<=c && c<='Z') )) {
                    answer+= (String.valueOf(c).toUpperCase());
                } else {
                    answer += String.valueOf(c).toLowerCase();
                }
                flag = false;
            }
        }
        return answer;
    }
}