class Solution {
    public String[] divideString(String s, int k, char fill) {
        
        for(int i = 0 ; i < s.length()%k ; i++){
            s = s + fill;
        }
        
        int len = s.length() + s.length()%k;
        
        String[] output = new String[s.length()/k];
        int out = 0;
        String temp = "";
        
        System.out.println(s);

        for(int i = 0 ; i< len; i++){
            temp = temp + s.charAt(i);

            if((i+1)%k == 0) {
                output[out] = temp;
                temp = "";
                out++;
            }
        }


        return output;
    }
}