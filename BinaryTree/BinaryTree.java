public class BinaryTree{
    Node root;
    
    public BinaryTree(int key){
        root = new Node(key);
    }

    public BinaryTree(){
        root = null;
    }

    public void insert(int value){
        if(value <= root.data){
            if(root.left == null){
                root.left = new Node(value);
            }else{
                root.left.insert(value);
            }
        }
    }


    public Node insertNode(Node root, int value){
        if(root == null){
            root = new Node(value);
            return root;
        }
        
        if(value < root.data){
            root.left = insertNode(root.left, value);
        }else if()
    }
}
