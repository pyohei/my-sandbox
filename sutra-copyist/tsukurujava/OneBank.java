// Question 16-11

public class OneBank {
	private static int value = 0;
	public static synchronized void addMoney(int money) {
		int currentValue = value;
		System.out.println(Thread.currentThread() + " �� addMoney �ɓ���܂����B "	);
		value += money;
						try {
				Thread.sleep(4000);
			} catch (InterruptedException e) {
			}
		
		if (currentValue + money != value) {
			System.out.println(Thread.currentThread() + " �Ŗ����������Ă��܂��B");
			System.exit(-1);
		}
		System.out.println (Thread.currentThread() + "��addMoney����o�܂���");
					try {
				Thread.sleep(4000);
			} catch (InterruptedException e) {
			}
	}
}