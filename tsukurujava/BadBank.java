// List16-3

public class BadBank {
	//credit balance
	private int value = 0;
	// deposit
	public void addMoney (int money) {
		// reserve present balance
		int currentValue = value;
		// curcumstance
		System.out.println (Thread.currentThread() + "�� addMoney �ɓ���܂����B ");
		// change present balance
		value += money;
		//check the contradiction
		if ( currentValue + money != value) {
			System.out.println (Thread.currentThread() + " �Ŗ����������Ă��܂� ");
			System.exit(-1);
		}
		//represent curcumstance
		System.out.println(Thread.currentThread() + "�� addMoney ����o�܂����B");
	}
}
