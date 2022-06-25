class Solution {
    public String greatestLetter(String s) {
        
        int[] alphaU = new int[26];
        int[] alphaL = new int[26];
        
        for(char i : s.toCharArray()){
            if((int)i < 97) alphaU[i-65]++; //Upper case
            else alphaL[i-97]++; //Lower case
        }
        
        //if have both the element must be odd number that greater than 1
        String result = "";
        for(int i = 0 ; i < alphaU.length ; i++){
            if(alphaU[i] != 0 && alphaL[i] != 0) {
                result = String.valueOf((char)(i+65));
            }   
        }
        
        return result;
        
    }
}