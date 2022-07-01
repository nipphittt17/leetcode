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
    // int sum = 0;
    int sumK = 0;
    public int sumEvenGrandparent(TreeNode root) {
        
//         if(root == null) return sum;
//         if(root.left == null && root.right == null) return sum;
        
//         if(root.val%2 == 0){
//             sum = sum + sumGrandkids(root);
//         }
//         sumEvenGrandparent(root.left);
//         sumEvenGrandparent(root.right); 
        sumGrandkids(root,null);
        return sumK;
    }
    
    
    public int sumGrandkids(TreeNode root, TreeNode parents){
        
       
//         if(root.left != null){
//             if(root.left.right != null) sumK+=root.left.right.val;
//             if(root.left.left != null) sumK+=root.left.left.val;
//         }
        
//         if(root.right != null){
//             if(root.right.left != null) sumK+=root.right.left.val;
//             if(root.right.right != null) sumK+=root.right.right.val;
//         }
        
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