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
    
    public boolean isSameTree(TreeNode p, TreeNode q) {
        ArrayList<String> root_1 = new ArrayList<String>();
		ArrayList<String> root_2 = new ArrayList<String>();
	
			allTree(p,root_1);
			allTree(q,root_2);
	
			System.out.println(root_1);
			System.out.println(root_2);
	
			return root_1.equals(root_2);
    }
    
public static void allTree(TreeNode root, ArrayList<String> leaves){
	  if(root == null) leaves.add("null");
	  else{
		  leaves.add(String.valueOf(root.val));
		  allTree(root.left,leaves);
		  allTree(root.right,leaves);
	  }
	}

}