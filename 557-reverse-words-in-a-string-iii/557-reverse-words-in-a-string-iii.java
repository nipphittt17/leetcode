class Solution {
    public String reverseWords(String s) {
        
        s = s + " ";

        String each = "";
        String out = "";
        
        for(char c : s.toCharArray()) {
             if(c == ' '){
                each = reverseEach(each);
                out = out + each;
                each = "";
            }
            
            else each = each + c;
            
        }
        
        return out.substring(0,out.length()-1);
    }
     
    
    public String reverseEach(String s){
        
        char[] e = s.toCharArray();
        int i = 0;
        int j = s.length()-1;
        
        while(i<j){
            char temp = e[i];
            e[i] = e[j];
            e[j] = temp;
            
            i++;
            j--;
        } 
        
        s = String.valueOf(e);
        
        s = s + " ";
        return s;
    }
}