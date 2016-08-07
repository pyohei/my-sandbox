import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

import twitter4j.Twitter;
import twitter4j.TwitterFactory;
import twitter4j.Status;
import twitter4j.TwitterException;

public class SimpleTweet {
    public static void main(String[] args) throws IOException, TwitterException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String tweet = "";
        while(tweet.isEmpty()) {
            System.out.print("�������Ă� ? : ");
            tweet = br.readLine();
            if(tweet.length() > 140) {
                System.out.println("���������𒴂��Ă��܂��B");
                tweet = "";
                continue;
            }
        }

        Twitter twitter = new TwitterFactory().getInstance();
        Status status = twitter.updateStatus(tweet);
        System.out.println(status.getUser().getScreenName() + " �Ƃ��ē��e���܂��� : " + status.getText());

        br.close();
    }
}