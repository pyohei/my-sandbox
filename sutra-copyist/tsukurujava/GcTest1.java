public class GcTest1 {
	public static void main (String[] args) {
		while (true) {
			String s = new String ("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
			System.out.println ("�c�胁���� = " + Runtime.getRuntime().freeMemory());
			System.gc();
		}
	}
}