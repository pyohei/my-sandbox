// List 18-7
import java.io.*;

public class MakeDir1 {
	public static void main(String[] args) {
		if (args.length != 1) {
			System.out.println (" �g�p�@ : java MakeDir1 �f�B���N�g����");
			System.out.println (" �� : java MakeDir1 doc");
			System.exit(0);
		}
		String dirname = args[0];
		File dir = new File(dirname);
		if (dir.mkdirs()) {
			System.out.println (dirname + "���쐬���܂����B");
			System.out.println (" ��΃p�X��" + dir.getAbsolutePath() + "�ł��B");
		} else {
			System.out.println(dirname + "���쐬�ł��܂���ł����B");
		}
	}
}