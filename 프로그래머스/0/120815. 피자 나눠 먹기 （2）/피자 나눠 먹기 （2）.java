class Solution {
    public static Integer gcd(Integer a, Integer b) {
        if (b == 0) return a;
        else return gcd (b, a%b);
    } 
    public int solution(int n) {
        int g = gcd(n, 6);
        int l = 6 * n / g;
        
        return l / 6;
    }
}