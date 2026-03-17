import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int maxDistinct(String s) {
        Set<Character> uniqueChars = new HashSet<>();
        char[] chars = s.toCharArray();
        
        for (char character: chars){
            uniqueChars.add(character);
            
        }

        return uniqueChars.size();
    }
}