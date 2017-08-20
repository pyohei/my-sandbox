import java.util.*;

public class LinkedListTest1 {
	public static void main(String[] args) {
		LinkedList<String> list = new LinkedList<String>();
		
		list.add("mukai");
		list.add("shohei");
		list.add("chisako");
		list.add("mosakuso");
		
		System.out.println(list);
		
		list.addFirst("hiyoko");
		
		System.out.println(list);
	}
}
