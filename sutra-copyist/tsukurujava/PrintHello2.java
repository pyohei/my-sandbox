class LabelPrinter2 extends Thread {
    String label;												//フィールドとして定義
    LabelPrinter2(String label) {
        this.label = label;									//1つ目のlabelはフィールド
    }
    public void run() {
        while (true) {
            try {
                System.out.println(label);
                Thread.sleep(1000);
            } catch (InterruptedException e) {
            }
        }
    }
}

public class PrintHello2 {
    public static void main (String[] args){
        LabelPrinter2 th = new LabelPrinter2("こんにちわ");
        th.start();
    }
}