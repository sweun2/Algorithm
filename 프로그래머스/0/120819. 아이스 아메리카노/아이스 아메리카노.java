class Solution {
    public int[] solution(int money) {
        int [] result = {money/5500,money-money/5500 * 5500};
        return result;
    }
}