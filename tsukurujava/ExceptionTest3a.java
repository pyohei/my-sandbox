// List 13-2

public class ExceptionTest3a {
	public static void main (String[] args) {
		int[] myarray = new int[3] ;
		myAssign (myarray, 5, 0);
		System.out.println("�I�����܂�");
	}
	
	static void myAssign (int[] arr, int index, int value) {
		System.out.println ("myAssign�ɗ��܂���");
		try {
			System.out.println("������܂�");
			arr [index] = value;
			System.out.println ("������܂���");
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println ("����ł��܂���ł����B");
			System.out.println ("��O��" + e + "�ł��B");
		}
		System.out.println ("myAssign����A��܂�");
	}
}