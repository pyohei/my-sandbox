//���3�|2
import java.io.*;

public class AverageAge {
	public static void main (String[] args) {
		BufferedReader reader = new BufferedReader (new InputStreamReader (System.in));
	
		try{
		String line;
		//1�l��
		System.out.println("A����̖��O�́H");
		String nameA = reader.readLine();
		System.out.println("A����̔N��́H");
		line = reader.readLine();
		int a = Integer.parseInt (line);
		//2�l��
		System.out.println("B����̖��O�́H");
		String nameB = reader.readLine();
		System.out.println("B����̔N��́H");
		line = reader.readLine();
		int b = Integer.parseInt (line);
		
		double c;
		c = ( a + b ) / 2.0;
		
		System.out.println(nameA +"����" + "��" + nameB +"����" +"��2�l�̔N��̕��ς�" + c + "�ł�");
		} catch (IOException e) {
			System.out.println(e);
		} catch (NumberFormatException e) {
			System.out.println(e);
		}
	}
}