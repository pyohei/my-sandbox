public class GoodBank {
    private int value = 0;
    public synchronized void addMoney (int money) {
        int currentValue = value;
        System.out.println(Thread.currentThread() + " �� addMoney �ɓ���܂���");
        value += money;
        if (currentValue + money != value) {
            System.out.println(Thread.currentThread() + "�Ŗ������������܂����B");
            System.exit(-1);
        }
        System.out.println (Thread.currentThread() + "�� addMoney ����o�܂����B");
    }
}