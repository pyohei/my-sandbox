// –â‘è8-2
import java.io.*;

public class paraboraString {
	public static void main (String[] args) {
	BufferedReader reader = new BufferedReader (new InputStreamReader(System.in));
		try{
			String line = reader.readLine();
			int k = Integer.parseInt(line);
			printGraph(k);
			} catch (IOException e) {
			System.out.println(e);
			} catch (NumberFormatException e) {
			System.out.println("”Žš“ü‚ê‚Ä‚Ë");
			}	
		}
	
	public static void printGraph(int n) {
		for (int j = n; j > -n-1 ; j--) {
			for ( int i = 0; i <  j*j ; i++) {
				System.out.print("*");
				}
				System.out.println("");
			}
		}
	}