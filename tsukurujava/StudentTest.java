//���10�|5

public class StudentTest {
	public static void main (String[] args) {
		Student[] data = {
			new Student ("����_", 65, 90, 100),
			new Student ("�����a�n", 82, 73, 64),
			new Student ("��������", 74, 31, 42),
			new Student ("�������Y", 100, 95, 99),
		};
		for (int i = 0; i < data.length; i++) {
			System.out.println ( data[i] + "\t^> " + data[i].total());
		}
	}
}