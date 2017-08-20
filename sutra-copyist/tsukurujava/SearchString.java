//Question 18-2

import java.io.*;

public class SearchString {
	public static void main(String[] args) {
		if (args.length != 2) {
			System.out.println ("�g�p�@�Fjava SearchString �������� �����Ώۃt�@�C��");
			System.out.println ("��Fjava SearchString System SearcjString.java");
			System.exit(0);
		}
		
		String String1 = args[0];
		String String2 = args[1];
		
		try {
			BufferedReader reader = new BufferedReader (new FileReader( String2));
			String line;
			int lineNum = 1;
			while ( (line = reader.readLine()) != null) {
				int n = line.indexOf (String1);
				if ( n >= 0) {
					System.out.println ( lineNum + " : " + line );
				}
				lineNum++;
			}
			reader.close();
		} catch (FileNotFoundException e) {
			System.out.println (String2 + "��������܂���");
		} catch (IOException e) {
			System.out.println (e);
		}
	}
}