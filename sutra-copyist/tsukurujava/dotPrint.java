public class dotPrint extends Thread{
    astPrint as;
    equPrint eq;
    public dotPrint(astPrint as) {
        this.as = as;
    }
    public dotPrint(equPrint eq) {
        this.eq = eq;
    }    
    public void run() {
        while (true) {
            as.ast();
            eq.equ();
        }
    }
    public static void main(String[] args) {
        astPrint as = new astPrint();
        equPrint eq = new equPrint();
        new dotPrint(as).start();
        new dotPrint(eq).start();
    }
}
/**
public class astPrint {
    public void ast() {
        for (int i = 0; i < 10; i ++) {
            System.out.println ("***");
            try {
                Thread.sleep(3000);
            } catch (InterruptedException e) {
            }
        }
    }
}
public class equPrint {
    public void equ() {
        for (int i = 0; i < 10; i ++) {
            System.out.println ("====");
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
            }
        }
    }
}
*/