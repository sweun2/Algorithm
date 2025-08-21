import java.util.*;
import java.util.stream.IntStream;

class Solution {
    public double solution(int[] numbers) {
        return (double) IntStream.of(numbers).sum() / numbers.length;
    }
}