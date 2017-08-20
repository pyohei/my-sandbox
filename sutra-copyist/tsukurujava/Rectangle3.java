public class Rectangle3 {
	final int INITIAL_WIDTH = 10;
	final int INITIAL_HEIGHT =20;
	int width;
	int height;
	int x;
	int y;
	Rectangle3() {
		width = INITIAL_WIDTH;
		height = INITIAL_HEIGHT;
		x = 0;
		y = 0;
	}
	Rectangle3(int width, int height) {
		this.width = INITIAL_WIDTH;
		this.height = INITIAL_HEIGHT;
		this.x = 0;
		this.y = 0;
	}
		Rectangle3(int x, int y, int width, int height) {
		this.width = INITIAL_WIDTH;
		this.height = INITIAL_HEIGHT;
		this.x = x;
		this.y = y;
	}
	void setLocation (int x, int y) {
		this.x = x;
		this.y = y;
	}
	void setSize (int width, int height) {
		this.width = width;
		this.height = height;
	}
	public String toString() {
		return "[ width = " + width +", height = " + height + ", x = " + x + ", y = " + y  + "]";
	}
	Rectangle3 intersect(Rectangle3 r) {
		int sx = Math.max(this.x, r.x);
		int sy = Math.max(this.y, r.y);
		int ex = Math.max(this.x + this.width, r.x + r.width);
		int ey = Math.max(this.x + this.height, r.x + r.height);
		int newwidth = ex - sx;
		int newheight = ey - sy;
		if (newwidth > 0 && newheight > 0) {
			return new Rectangle3 (sx, sy, newwidth, newheight);
		} else {
			return null;
		}
	}
	public static void main(String[] args) {
		Rectangle3 a, b, c, d, e;
		a = new Rectangle3 (0, 0, 20, 10);
		b = new Rectangle3 (5, 5, 20, 10);
		c = new Rectangle3 (20, 10, 20, 10);
		d = new Rectangle3 (-10, -20, 100, 200);
		e = new Rectangle3 (21, 11, 20, 10);
		System.out.println("a = " +a);
		System.out.println("b = " +b);
		System.out.println("c = " +c);
		System.out.println("d = " +d);
		System.out.println("e = " +e);
		System.out.println("a �� a �̏d�Ȃ� = " + a.intersect(a));
		System.out.println("a �� b �̏d�Ȃ� = " + a.intersect(b));
		System.out.println("a �� c �̏d�Ȃ� = " + a.intersect(c));
		System.out.println("a �� d �̏d�Ȃ� = " + a.intersect(d));
		System.out.println("a �� e �̏d�Ȃ� = " + a.intersect(e));
	}
}