public class GoodBank {
    private int value = 0;
    public synchronized void addMoney (int money) {
        int currentValue = value;
        System.out.println(Thread.currentThread() + " ‚ª addMoney ‚É“ü‚è‚Ü‚µ‚½");
        value += money;
        if (currentValue + money != value) {
            System.out.println(Thread.currentThread() + "‚Å–µ‚‚ª”­¶‚µ‚Ü‚µ‚½B");
            System.exit(-1);
        }
        System.out.println (Thread.currentThread() + "‚ª addMoney ‚©‚ço‚Ü‚µ‚½B");
    }
}