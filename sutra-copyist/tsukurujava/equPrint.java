public class equPrint {
    
    public synchronized void equ() {
        for (int n = 0; n < 10; n ++) {
//            System.out.println ("====");
            try {
                System.out.println ("====");
                Thread.sleep(5000);
            } catch (InterruptedException e) {
            }
        }
    }
}