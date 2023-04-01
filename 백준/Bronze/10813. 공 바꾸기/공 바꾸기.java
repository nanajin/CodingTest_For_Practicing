import java.io.IOException;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] num = new int[n];
        for(int i=1;i<n+1;i++){
            num[i-1] = i;
        }
        for(int a=0;a<m;a++){
            int i = sc.nextInt();
            int j = sc.nextInt();
            int temp = num[i-1];
            num[i-1] = num[j-1];
            num[j-1] = temp;
        }

        for(int i=0;i<n;i++){
            System.out.print(num[i]+" ");
        }
    }
}
