//Question 16-6

public class Hyoji extends Thread {
	public static void main (String[] args) {
		Hyoji hj = new Hyoji();
		hj.start();
		
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