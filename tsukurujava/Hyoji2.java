//Question 16-6

public class Hyoji2 implements Runnable {
	public static void main (String[] args) {
		Hyoji2 hj = new Hyoji2();
		Thread th = new Thread(hj);
		th.start();
		
		for ( int i = 0 ; i < 10; i++) {
			System.out.println ("***");
			try {
				Thread.sleep(3000);
			} catch (InterruptedException e) {
			}
		}
	}
	
	public void run() {
		for (int n = 0; n < 10; n++) {
			System.out.println("=====");
			try {
				Thread.sleep(5000);
			} catch (InterruptedException e) {
			}
		}
	}
}