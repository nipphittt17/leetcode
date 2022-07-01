class Solution {
    public String reverseStr(String s, int k) {
        
        // if(s.length() < k) return reverseK(s);
        
        StringBuilder out = new StringBuilder();
        
        String sub = "";
        boolean sw = true;
        
        for(int i = 0 ; i < s.length() ; i++){
            sub = sub + (s.charAt(i)); 
            
            if((i+1)%k == 0){
                if(sw == true){
                    out.append(reverseK(sub));
                    sw = false;
                }
                else {
                    out.append(sub);
                    sw = true;    
                }   
                
                sub = "";
            }
        }
        
        if(sub.length() < k && sw == true) out.append(reverseK(sub));
        else out.append(sub);

        
        return out.toString();
    }
    
    
    
    public String reverseK(String sub){
                
        int left = 0;
        int right = sub.length()-1;
        char[] c = sub.toCharArray();
        
        while(left<right){
            char temp = c[left];
            c[left] = c[right];
            c[right] = temp;
            left++;
            right--;
        }

        return String.valueOf(c);   
    }

}