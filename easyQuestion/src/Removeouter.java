package easyQuestion.src;

//1021. Remove Outermost Parentheses


public class Removeouter {
    public String removeOuterParentheses(String s) {
        
        //loop through s
        int cl = 0;
        int cr = 0;
        int flag = 0;
        int start = 0;
        String out = "";
        
        for(int i = 0 ; i < s.length() ; i++){
                   
            // count "(" && count ")"
            if(s.charAt(i) == '(') {
                if(flag == 0) {
                    start = i;
                }
                cl++;
            }
            else cr++;
            
            flag = 1;
            
            if(cl == cr){
            //if #"(" == #")" -> 1 decomposition
            //remove start&end
                out = out + s.substring(start+1, i);
                flag = 0;
            }
            
        }

        return out;    
            
    }
}
