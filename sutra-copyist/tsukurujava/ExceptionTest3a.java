// List 13-2

public class ExceptionTest3a {
	public static void main (String[] args) {
		int[] myarray = new int[3] ;
		myAssign (myarray, 5, 0);
		System.out.println("終了します");
	}
	
	static void myAssign (int[] arr, int index, int value) {
		System.out.println ("myAssignに来ました");
		try {
			System.out.println("代入します");
			arr [index] = value;
			System.out.println ("代入しました");
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println ("代入できませんでした。");
			System.out.println ("例外は" + e + "です。");
		}
		System.out.println ("myAssignから帰ります");
	}
}