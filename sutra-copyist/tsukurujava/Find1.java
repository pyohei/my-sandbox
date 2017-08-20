import java.io.*;

public class Find1 {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("�g�p�@�Fjava Find1 ���������� < �����Ώۃt�@�C��");
            System.out.println("��Fjava Find1 System < Find1.java");
            System.exit(0);
        }
        String findstring = args[0];
        System.out.println("����������́u" + findstring + "�v�ł��B");
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        try {
            String line;
            int linenum = 1;
            while ((line = reader.readLine()) != null) {
                int n = line.indexOf(findstring);
                if (n >= 0) {
                    System.out.println(linenum + ":" + line);
                }
                linenum++;
            }
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}

