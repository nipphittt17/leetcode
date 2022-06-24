class Solution {
    public boolean checkIfPangram(String sentence) {
        
        int[] countAlpha = new int[26];
        
        for(int i = 0 ; i < sentence.length() ; i++){
            int index = (int)sentence.charAt(i);
            countAlpha[index-97]++;
        }

        for(int i = 0 ; i < countAlpha.length ; i++){
            if(countAlpha[i] == 0) return false;
        }

        return true;
    }
}