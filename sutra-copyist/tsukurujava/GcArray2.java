// List 15-3

import java.util.*;

public class GcArray2 {
	static ArrayList<int[]> list = new ArrayList<int[]>();
	public static void main(String[] args) {
		while (true) {
			int[] a = new int[1000];
			for (int i = 0; i < 1000; i++) {
				a[i] = i ;
			}
			
			System.out.println("Žc‚è‚Ìƒƒ‚ƒŠ = " + Runtime.getRuntime().maxMemory());
		}
	}
}