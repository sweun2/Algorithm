class Solution {
    public int dfs(int depth, int sum, int[] numbers, int target) {
        if (depth == numbers.length) {
            if (sum == target) return 1;
            else return 0;
        }
        
        int plus = dfs(depth + 1, sum + numbers[depth], numbers, target);
        int minus = dfs(depth + 1, sum - numbers[depth], numbers, target);
        
        return plus + minus; 
    }
    
    public int solution(int[] numbers, int target) {
        return dfs(0, 0, numbers, target); 
    }
}
