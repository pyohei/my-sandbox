//–â‘è10-5

public class Student {
	String name;		//name
	int[] tens;			//score of test
	public Student (String name, int x, int y, int z) {
		this.tens = new int[3];
		this.name = name;
		this.tens[0] = x;
		this.tens[1] = y;
		this.tens[2] = z;
	}
	public String toString() {
		String s = "[" + name;
		for (int i = 0; i < tens.length; i++) {
			s += "," + tens[i];
		}
		s += "]";
		return s;
	}
	
	public int total () {
		int sum = 0;
		for (int i= 0; i < tens.length; i++) {
			sum += tens[i];
		}
		return sum;
	}
}