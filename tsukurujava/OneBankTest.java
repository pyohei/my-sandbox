public class OneBankTest extends Thread {
	public void run() {
		while(true) {
			OneBank.addMoney(100);
			OneBank.addMoney(-100);
		}
	}
	
	public static void main(String[] args) {
		new OneBankTest().start();
		new OneBankTest().start();
	}
}
