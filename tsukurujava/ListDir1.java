// List18-6

import java.io.*;

public class ListDir1 {
	public static void main (String[] args) {
		if (args.length != 1) {
			System.out.println(" �g�p�@ : java ListDir1 �f�B���N�g����");
			System.out.println(" �� : java ListDir1 doc");
			System.out.println(0);
		}
		String dirname = args[0];
		File dir = new File(dirname);
		String[] dirlist = dir.list();
		for (int i = 0; i < dirlist.length; i++) {
			System.out.println(dirlist[i]);
		}
	}
}