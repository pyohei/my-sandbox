// Question 16-11

public class OneBank {
	private static int value = 0;
	public static synchronized void addMoney(int money) {
		int currentValue = value;
		System.out.println(Thread.currentThread() + " ‚ª addMoney ‚É“ü‚è‚Ü‚µ‚½B "	);
		value += money;
						try {
				Thread.sleep(4000);
			} catch (InterruptedException e) {
			}
		
		if (currentValue + money != value) {
			System.out.println(Thread.currentThread() + " ‚Å–µ‚‚ª¶‚¶‚Ä‚¢‚Ü‚·B");
			System.exit(-1);
		}
		System.out.println (Thread.currentThread() + "‚ªaddMoney‚©‚ço‚Ü‚µ‚½");
					try {
				Thread.sleep(4000);
			} catch (InterruptedException e) {
			}
	}
}