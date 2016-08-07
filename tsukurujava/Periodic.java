// List16-8

public class Periodic {
	public static void main (String[] args) {
		for (int i = 0; i < 10; i++) {
			int  time = i * i * i * 100;
			System.out.println ("Start sleep : time = " + time);
			
			try {
				Thread.sleep(time);
			} catch ( InterruptedException e ) {
			}
		}
	}
}
