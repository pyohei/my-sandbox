// List 18-3

import java.io.*;

public class DeleteFile1 {
	public static void main (String[] args) {
		if (args.length != 1) {
			System.out.println("使用法: java DeleteFile1 削除ファイル");
			System.out.println("例: java DeleteFile1 trash.txt");
			System.exit(0);
		}
		String filename = args[0];
		File file = new File (filename);
		if (file.delete()) {
			System.out.println (filename + " is cmpletely deleted!!");
		} else {
			System.out.println (filename + " isn't deleted");
		}
	}
}