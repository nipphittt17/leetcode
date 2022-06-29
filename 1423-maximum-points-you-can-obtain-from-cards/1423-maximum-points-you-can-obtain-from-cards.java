class Solution {
    public int maxScore(int[] cardPoints, int k) {
        
        int[] cardLeft = new int[cardPoints.length];
        int[] cardRight = new int[cardPoints.length];
        
        cardLeft[0] = cardPoints[0];
        for(int i = 1 ; i < k ; i++){
            cardLeft[i] = cardPoints[i] + cardLeft[i-1];
        }
        
        cardRight[cardRight.length-1] = cardPoints[cardPoints.length-1];
        for(int i = cardPoints.length-2 ; i > cardPoints.length-1-k ; i--){
            cardRight[i] = cardPoints[i] + cardRight[i+1];
        }

        int max = 0; 
        int innerSum = 0;
        int start = -1;
        int end = cardRight.length-k;
        
        while(start < k){
            
            if(start == -1) innerSum = innerSum + 0;
            else innerSum = innerSum + cardLeft[start];
            
            if(end == cardPoints.length) innerSum = innerSum + 0;
            else innerSum = innerSum + cardRight[end];
            
            if(innerSum > max) max = innerSum;
            innerSum = 0;
            
            start++;
            end++;
        }
    
        return max;
    }
}