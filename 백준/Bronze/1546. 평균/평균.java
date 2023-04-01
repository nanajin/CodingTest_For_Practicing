import java.io.IOException;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] scoreArr = new int[n];
        int max = scoreArr[0];
        double avg = 0;
        for(int i=0;i<n;i++){
            int score = sc.nextInt();
            scoreArr[i] = score;
            max = Math.max(score,max);
        }
        for(int i=0;i<n;i++){
            avg += (double)scoreArr[i]/max*100;
        }
        System.out.println(avg/n);
    }
}
