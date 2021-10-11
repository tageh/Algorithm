public class BinaryTree{
    Node root;
    
    public BinaryTree(int key){
        root = new Node(key);
    }

    public BinaryTree(){
        root = null;
    }

    public void insert(int value){
       root = insertNode(root, value); 
    }


    public Node insertNode(Node root, int value){
        if(root == null){
            root = new Node(value);
            return root;
        }
        
        if(value < root.data){
            root.left = insertNode(root.left, value);
        }else if(value > root.data){
            root.right = insertNode(root.right, value);
        }
        return root;
    }

    public void printLevels(Node root) {
        int height = treeHeight(root);

        for (int i = 1; i <= height; i++) {
            printSingleLevel(root, i);
            System.out.println();

        }
    }

    public int treeHeight(Node root) {
        if (root == null) {
            return 0;
        }

        int leftHeight = treeHeight(root.left);
        int rightHeight = treeHeight(root.right);

        return Math.max(leftHeight, rightHeight) + 1;
    }

    public void printSingleLevel(Node root, int level) {
        if (root == null)
            return;

        if (level == 1) {
            System.out.print(root.data + " ");
        } else if (level > 1) {
            printSingleLevel(root.left, level - 1);
            printSingleLevel(root.right, level - 1);
        }
    }

     public int smallestElement(Node temp){  
          if(root == null) {  
              System.out.println("Tree is empty");  
              return 0;  
          }  
          else {  
                int leftMin, rightMin;  
                int min = temp.data;  
                  
                if(temp.left != null){  
                  leftMin = smallestElement(temp.left);  
                  min = Math.min(min, leftMin);  
                }  
                  
                if(temp.right != null){  
                  rightMin = smallestElement(temp.right);  
                  min = Math.min(min, rightMin);  
                }  
                return min;  
          }  
      }  

      public int largestElement(Node temp){
          if(root == null) {
              System.out.println("Tree is empty");
              return 0;
          }
          else {
                int leftMax, rightMax;
                int max = temp.data;

                if(temp.right != null){
                  leftMax = largestElement(temp.left);
                  max = Math.max(max, leftMax);
                }

                if(temp.right != null){
                  rightMax = largestElement(temp.right);
                  max = Math.max(max, rightMax);
                }
                return max;
          }
      }
}
