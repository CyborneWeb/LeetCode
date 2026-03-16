class Solution {
    public int minPartitions(String n) {
        int max = 0;
        for (int i = 0; i<n.length(); i++){
            int current = Integer.parseInt(String.valueOf(n.charAt(i)));
            if (current > max){
                max = current;
            }

        }

        return max;

    }
}