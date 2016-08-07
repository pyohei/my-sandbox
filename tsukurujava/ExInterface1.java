import java.text.*;
import java.util.*;

public class ExInterface1 implements Greeting, ShowingDate{
    public void greet() {
        System.out.println("‚±‚ñ‚É‚¿‚Í");
    }
    
    public void ShowDate() {
        SimpleDateFormat dateformatter = new SimpleDateFormat("yyyy/MM/dd");
        String dateString = dateformatter.format(new Date());
        System.out.println(dateString);
    }
    
    public static void main(String[] args) {
        ExInterface1 object1 = new ExInterface1();
        object1.greet();
        object1.ShowDate();
    }
}