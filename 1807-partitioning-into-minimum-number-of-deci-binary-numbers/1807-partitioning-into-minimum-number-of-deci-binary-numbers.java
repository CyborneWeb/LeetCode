class Solution {
    public int minPartitions(String n) {
        int max = 0;

        if (n.length() == 1){
            return Integer.valueOf(n);
        }


        for (int i = 0; i<n.length(); i++){
            int current = Integer.valueOf(String.valueOf(n.charAt(i)));
            if (current > max){
                max = current;
            }

        }

        return max;

    }
}