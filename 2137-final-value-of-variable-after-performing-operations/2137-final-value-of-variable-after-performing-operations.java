class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int vsota = 0;
        for (String operation : operations){
            switch (operation) {
                case "X++":
                case "++X":
                    vsota++;
                    break;
                
                case "X--":
                case "--X":
                    vsota--;
                    break;

            }

        } return vsota;
        

    }
}