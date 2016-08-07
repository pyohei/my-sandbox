public class astPrint {
    public synchronized void ast() {
        for (int i = 0; i < 10; i ++) {
//            System.out.println ("***");
            try {
                System.out.println ("***");
                Thread.sleep(3000);
            } catch (InterruptedException e) {
            }
        }
    }
}