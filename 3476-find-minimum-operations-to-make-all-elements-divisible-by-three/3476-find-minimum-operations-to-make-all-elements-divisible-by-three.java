class Solution {
    public int minimumOperations(int[] nums) {
        int sum = 0;
        for (int num : nums){
            sum += Math.min(1, num%3);
        }
        return sum;
    }
}