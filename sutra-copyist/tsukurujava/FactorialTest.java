// –â‘è13-4

public class FactorialTest {
	public static void main (String[] args) {
		System.out.println (keisann (10));
	}
	
	public static int keisann (int n) {
		int a = 1;
		for ( int j =1 ; j < n + 1 ; j++) {
			a = a * j;
		}
			n = a;
			return n;
	}
}