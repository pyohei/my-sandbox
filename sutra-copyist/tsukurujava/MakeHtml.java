//ñ‚ëË7Å|3
import java.io.*;

public class MakeHtml {
	public static void main(String[] args) {
		
		BufferedReader reader = new BufferedReader (new InputStreamReader (System.in));
		
		try {
			String line;
			// rule 1
			System.out.println("<html><head><title>My page</title></head><body>");
	
			while ( (line = reader.readLine()) !=null) {
			if (line.startsWith("a")) {
				//rule 3
				System.out.println ("<h1>" + line.substring(1) + "</h1>");
			} else if (line.startsWith("b")) {
				//rule 4
				System.out.println ("<h2>" + line.substring(1) + "</h2>");
			} else if (line.startsWith("----")) {
				//rule 5
				System.out.println ("<hr>");
			} else if (line.startsWith("adress")) {
				//rule 6
				System.out.println ("< a href=mailto: mukashohei76@gmail.com >mukaishohei76@gmail.com</a>");
			} else {
				//rule7
				System.out.println (line);
			}
		}
				//rule2
				System.out.println("</body></html>");
			} catch (IOException e) {
				System.out.println (e);
			}
		}
	}