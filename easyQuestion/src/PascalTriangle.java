//118. Pascal's Triangle

import java.util.ArrayList;
import java.util.List;

public class PascalTriangle {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<List<Integer>>(numRows);

        List<Integer> sums = new ArrayList<Integer>();

        //loop for numRows round i.e. 5
        for(int i = 0 ; i < numRows ; i++){
            
            //create a list of size i+1
            List<Integer> rows = new ArrayList<Integer>();
            for(int r = 0 ; r < i+1 ; r ++){
                rows.add(0);
            }
            
            //-> first and last is 1
            rows.set(0,1);
            rows.set(rows.size()-1, 1);  

            //loop through each rows  -> another is  calculate from sum
            for(int j = 1 ; j < rows.size()-1 ; j++){
                rows.set(j, sums.get(j-1));
            }

            //array of sum w/ size = rows.size - 2 -> use for next round
            for(int k = 0 ; k < rows.size()-1 ; k++){
                sums.add(0);
                sums.set(k, rows.get(k)+rows.get(k+1));
            }
            
            result.add(rows);
                       
        }
        return result;
        
    }
}
