import java.io.*;

public class MaxFactor {
    public static int MaxCalc(int m, int n) {
        if (m > n) {
            int a = m;
            m = n;
            n = a;
        }
        while (m % n != 0) {
            int r;
            r = n % m;
            n = m;
            m = r;
        }
        return n;
    }
    
    public static void main (String[] args) {
        BufferedReader reader = new BufferedReader ( new InputStreamReader(System.in));
//        BufferedReader reader2 = new BufferedReader ( new InputStreamReader(System.in));
        try {
            String line = reader.readLine();
            int m = Integer.parseInt(line);
            line = reader.readLine();
            int n = Integer.parseInt(line);
            System.out.println(MaxCalc(m, n));
        } catch (IOException e) {
            System.out.println(e);
        } catch (NumberFormatException e) {
            System.out.println("noooo");
        }
    }
}