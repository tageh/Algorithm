public class LinkedList{
    Node head;

    public void append(int data){
        if(head == null){
            head = new Node(data);
            return;
        }

        Node current = head;
        while(current.next != null){
            current = current.next;
        }
        current.next = new Node(data);
    } 

    public void prepend(int data){
        Node newHead = new Node(data);
        newHead.next = head;
        head = newHead;
    }

    public void delete(int data){
        if(head == null){
            return;
        }
        if(head.data == data){
            head = head.next;
            return;
        }
        
        Node current = head;
        while(current.next != null){
            if(current.next.data == data){
                current.next = current.next.next;
                return;
            }
            current = current.next;
        }
    }

    public void printList(){
        if(head == null){
            System.out.println("List is empty");
        }

        Node current = head;

        while(current != null){
            System.out.println(current.data);
            current = current.next;
        }
    }

    public void sortList(){ //Bubble sort O(n²)
        int temp;
        Node current = head, index = null;
        if(head == null){
            System.out.println("Nothing to sort");
        }
        
        while(current.next != null){
            index = current.next;
    
            while(index != null){
                if(current.data > index.data){
                    temp = current.data;
                    current.data = index.data;
                    index.data = temp;
                }
                index = index.next;
            }
            current = current.next;
        }

    }

    public void revSortList(){ //Bubble sort reversed
        int temp;
        Node current = head, index = null;
        if(head == null){
            System.out.println("Nothing to sort");
        }
        
        while(current.next != null){
            index = current.next;
    
            while(index != null){
                if(current.data < index.data){
                    temp = current.data;
                    current.data = index.data;
                    index.data = temp;
                }
                index = index.next;
            }
            current = current.next;
        }
    }

    public int size(){
        int count = 0;
        Node current = head;
        
        if(head == null){
            return 0;
        }

        while(current != null){
            count += 1;
            current = current.next;
        }
        return count;
    }
}

class Node{
    Node next;
    int data;
    
    public Node(int data){
        this.data = data;
    }    
}
