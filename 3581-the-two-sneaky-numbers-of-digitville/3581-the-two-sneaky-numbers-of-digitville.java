class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        int[] sneaky = new int[2];
        Set<Integer> seen = new HashSet<>();
        int i = 0;
        for (int num : nums) {
            if (!seen.add(num)) {  // .add() returns false if already present
                sneaky[i++] = num;
            }
        }
        return sneaky;
    }
}