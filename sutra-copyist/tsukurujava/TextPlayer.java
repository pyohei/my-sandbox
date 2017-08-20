//List 12-12

public class TextPlayer extends Player {
	String text;
	public TextPlayer(String text) {
		this.text = text;
	}
	public void play() {
		System.out.println(text);
	}
	public static void main (String[] args) {
		TextPlayer player = new TextPlayer("‚±‚ñ‚É‚¿‚í");
		player.loop(3);
	}
}

abstract class Player {
	public abstract void play();
	public void loop(int n) {
		for (int i = 0; i < n; i++){
			play();
		}
	}
}
