/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    int sumK = 0;
    public int sumEvenGrandparent(TreeNode root) {
        
        sumGrandkids(root,null);
        return sumK;
    }
    
    
    public int sumGrandkids(TreeNode root, TreeNode parents){
        
        if(root == null) return 0;
        if(parents != null && parents.val%2 == 0){
            if(root.right != null) {
                sumK += root.right.val;
            }
            if(root.left != null) {
                sumK += root.left.val;
            }   
        }
        
        sumGrandkids(root.left,root);
        sumGrandkids(root.right,root);
        
        
        return sumK;
    }
}