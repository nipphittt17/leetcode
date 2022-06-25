/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    
    List<Integer> post = new ArrayList<Integer>();
    
    public List<Integer> postorder(Node root) {
        
        //base case
        if(root == null) return new ArrayList<Integer>();
        
        for(int i = 0 ; i < root.children.size() ; i++){
            postorder(root.children.get(i));
        }
        post.add(root.val);
        
        return post;
    }
}