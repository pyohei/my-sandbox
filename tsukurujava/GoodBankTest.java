/**
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
**/

public class GoodBankTest extends Thread {
    public GoodBank bank;
    public GoodBankTest(GoodBank bank) {
        this.bank = bank;
    }
    public void run() {
        while (true) {
            bank.addMoney(100);
            bank.addMoney(-100);
        }
    }
    public static void main (String[] args) {
        GoodBank bank = new GoodBank();
        GoodBankTest Gbank = new GoodBankTest(bank);
        Gbank.start();
        new GoodBankTest(bank).start();
    }
}