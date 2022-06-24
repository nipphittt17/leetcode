import java.util.ArrayList;
import java.util.List;

public class DivideString {
    public String[] divideString(String s, int k, char fill) {
        for(int i = 0 ; i < s.length()%k ; i++){
            s = s + fill;
        } 
        
        List<String> output = new ArrayList<String>();
        String temp = "";

        for(int i = 0 ; i< s.length() + s.length()%k ; i++){
            temp = temp + s.charAt(i);

            if((i+1)%k == 0) {
                output.add(temp);
                temp = "";
            }
        }


        return (String[]) output.toArray();
    }
}
