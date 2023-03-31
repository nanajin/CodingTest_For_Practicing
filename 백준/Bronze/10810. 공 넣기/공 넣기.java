import java.io.IOException;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] num = new int[n];
        for(int a=0;a<m;a++){
            int i = sc.nextInt();
            int j = sc.nextInt();
            int k = sc.nextInt();
            for(int b=i;b<j+1;b++){
                num[b-1] = k;
            }
        }

        for(int i=0;i<n;i++){
            System.out.print(num[i]+" ");
        }
    }
}
