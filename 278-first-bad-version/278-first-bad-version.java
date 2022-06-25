/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int first = 0;
        int last = n - 1;
        int mid = 0;
            
        while(first <= last){
            mid = first + (last-first)/2;
            
            if(isBadVersion(mid) == true) {
                if(isBadVersion(mid-1) == false) return mid;
                last = mid-1;
            } 
            else{
                if(isBadVersion(mid+1) == true) return mid + 1;
                first = mid+1;
            }        
        }
        
        return mid;
    } 
    
}