import java.util.*;

public class ArrayListTest2 {
	public static void main(String[] args) {
		ArrayList<Integer> list = new ArrayList<Integer>();
		list.add(2);
		list.add(4);
		list.add(7);
		System.out.println(list);
		list.add(5);
		list.remove(list.get(2));
//		for (int i = 0; i <= 1; i++) {
//			System.out.println(list);
//		}
		for (Iterator<Integer> it = list.iterator(); it.hasNext(); ) {
			int name = it.next();
			System.out.println(name);
		}
	}
}
