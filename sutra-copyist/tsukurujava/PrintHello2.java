class LabelPrinter2 extends Thread {
    String label;												//�t�B�[���h�Ƃ��Ē�`
    LabelPrinter2(String label) {
        this.label = label;									//1�ڂ�label�̓t�B�[���h
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
        LabelPrinter2 th = new LabelPrinter2("����ɂ���");
        th.start();
    }
}