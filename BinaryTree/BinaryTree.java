import java.util.*;

public class BinaryTree{
    Node root;

    public BinaryTree(int key){
        root = new Node(key);
    }

    public BinaryTree(){
        root = null;
    }

    public void insert(int data){
        root = insertNode(root, data);
    }

    public Node insertNode(Node root, int data){
        if(root == null){
            root = new Node(data);
            return root;
        }

        if(data < root.key){
            root.left = insertNode(root.left, data);
        }else if(data > root.key){
            root.right = insertNode(root.right, data);
        }
        return root;
    }

    public int minVer(Node root){
        if(root.left == null){
            return root.key;
        }
        return minVer(root.left);
    }

    public int maxVer(Node root){
        if(root.right == null){
            return root.key;
        }
        return maxVer(root.right);
    }

    public void breathFistSearch(Node root){
        Queue<Node> que = new LinkedList<Node>();
        if(root == null){
            return;
        }
        que.offer(root);

        while(!que.isEmpty()){
            int level = que.size();
            for(int i = 0; i < level; i++){
                Node node = que.poll();
                System.out.print(node.key + " ");
                if(node.left != null){
                    que.offer(node.left);
                }
                if(node.right != null){
                    que.offer(node.right);
                }
            }
        System.out.println();
        } 
    }
}
