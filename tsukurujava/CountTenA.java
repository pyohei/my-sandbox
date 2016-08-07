// List16-1

public class CountTenA extends Thread {
	public static void main(String[] args) {
		CountTenA ct = new CountTenA();
		ct.start();
		for (int i = 0; i < 100 ; i++) {
			System.out.println("main: i = " + i );
		}
	}
	
	public void run() {
		for (int i = 0; i < 100 ; i++) {
			System.out.println ("run:i = " + i);
		}
	}
}