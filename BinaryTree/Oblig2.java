import java.util.*;

public class Oblig2{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        BinaryTree tree = new BinaryTree();

       
        while(true){
            System.out.println("Type a value to insert: ");
            int value = input.nextInt();
            if(value != 0){
                tree.insert(value);
            }else{
                break;
            }
        }    

        System.out.println("\n");
        tree.printLevels(tree.root);
        System.out.println("\nSmalest value is: "+ tree.smallestElement(tree.root));
        System.out.println("\nLargest value is: "+ tree.largestElement(tree.root));
    }
}
