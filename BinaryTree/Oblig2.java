/Documents/Projects/Automatic-Doorbell/local/lyd.mp3')import java.util.*;

public class Oblig2{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        BinaryTree tree = new BinaryTree();

       
       /* while(true){
            System.out.println("Type a value to insert: ");
            int value = input.nextInt();
            if(value != 0){
                tree.insert(value);
            }else{
                break;
            }
        }    
        */
        tree.insert(100);
        tree.insert(35);
        tree.insert(120);
        tree.insert(10);
        tree.insert(40);
        tree.insert(110);
        tree.insert(140);

        
        System.out.println("Min: " + tree.minVer(tree.root));
        System.out.println("Min: " + tree.maxVer(tree.root));
        System.out.println("\n");
        tree.breathFistSearch(tree.root);
    }
}
