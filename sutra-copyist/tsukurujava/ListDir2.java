import java.io.*;

public class ListDir2 {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.exit(0);
        }
        String dirname = args[0];
        File dir = new File(dirname);
        String[] dirlist = dir.list();
        for (int i = 0; i < dirlist.length; i++) {
            System.out.println(dirlist[i]);
        }
    }
}