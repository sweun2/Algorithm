import java.util.*;
class Solution
{
    public int minv = 1000000000;
    
    public int solution(int []A, int []B)
    {
        int n = A.length;
        Arrays.sort(A);
        Arrays.sort(B);
        int sumv = 0;
        for(int i=0; i<n; i++) {
            sumv += A[i] * B[n-i-1];
        }
        return sumv;
    }
}