//List12-15

class Rectangle2 {
	int width;
	int height;
	
	Rectangle2() {
		setSize(0, 0);
	}
	
	Rectamgle2(int width, int height) {
		setSize(width, height);
	}
	
	void setSize(int width, int height) {
		this.width = width;
		this.height = height;
	}
	
	public String toString() {
		return "[" + width + ", " + height + "]";
	}
}