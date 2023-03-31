import java.io.IOException;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] num = new int[n];
        for(int i=0;i<n;i++){
            num[i] = sc.nextInt();
        }
        int max = num[0];
        int min = num[0];
        for(int i=0;i<n;i++){
            max = Math.max(num[i], max);
            min = Math.min(num[i], min);
        }
        System.out.println(min+" "+max);
    }
}
