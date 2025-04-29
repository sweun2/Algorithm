class Solution {
    public int solution(int n) {
        int answer = 0;
        int k = n/2 ;
        for (int i = 1; i<=k; i++) {
            if (n%i==0) {
                answer += i;
            }
        }
        
        return answer + n;
    }
}