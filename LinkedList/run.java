import java.util.Random;

public class run{
    public static void main(String[] args) {
    
        LinkedList myList = new LinkedList();   
        Random random = new Random();


        for(int i = 0; i < 10; i++){
            myList.append(random.nextInt(100));
        }

        myList.sortList();
        myList.printList();

    }
}
