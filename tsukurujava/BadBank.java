// List16-3

public class BadBank {
	//credit balance
	private int value = 0;
	// deposit
	public void addMoney (int money) {
		// reserve present balance
		int currentValue = value;
		// curcumstance
		System.out.println (Thread.currentThread() + "‚ª addMoney ‚É“ü‚è‚Ü‚µ‚½B ");
		// change present balance
		value += money;
		//check the contradiction
		if ( currentValue + money != value) {
			System.out.println (Thread.currentThread() + " ‚Å–µ‚‚ª¶‚¶‚Ä‚¢‚Ü‚· ");
			System.exit(-1);
		}
		//represent curcumstance
		System.out.println(Thread.currentThread() + "‚ª addMoney ‚©‚ço‚Ü‚µ‚½B");
	}
}
