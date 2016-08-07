// Prime2
import java.io.*;

public class Prime2 {
	static final int MAX_PRIME = 1000;
	public static void main(String[] args) {
		String filename = args[0];
			try {
				PrintWriter writer = new PrintWriter(new BufferedWriter(new FileWriter(filename)));
				writePrime(writer);
				writer.close();
		} catch (FileNotFoundException e) {
			System.out.println ("nofile");
		} catch (IOException e) {
			System.out.println (e);
		}
	}
	public static void writePrime(PrintWriter writer) {
	//	int MAX_PRIME = 1000;
		boolean[] prime = new boolean[MAX_PRIME];
		for (int n = 0; n < MAX_PRIME; n++) {
			//prime[]‚Ì‰Šú‰»
			prime[n] = true;
		}
		prime[0] = false;//
		prime[1] = false;//‚±‚±2‚Â‚ªd—vBn=0,1‚ð‚µ‚È‚¢‚Æ‚·‚×‚Ä’Ê‚Á‚Ä‚µ‚Ü‚¤
		for  (int n = 0; n < MAX_PRIME; n++) {
			if (prime[n]) {
				writer.println(n);
				for (int i = 2; i * n < MAX_PRIME; i++) {
					prime[i * n] = false;
				}
			}
		}
	}
}