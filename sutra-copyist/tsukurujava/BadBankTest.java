// List 16-4

public class BadBankTest extends Thread {
	BadBank bank;
	public BadBankTest (BadBank bank) {
		this.bank =bank;
	}
	public void run() {
		while (true) {
			//deposit 100 yen
			bank.addMoney(100);
			//take out 100 yen
			bank.addMoney(-100);
		}
	}
	
	public static void main(String[] args) {
		BadBank bank = new BadBank();
		new BadBankTest(bank).start();
		new BadBankTest(bank).start();
	}
}