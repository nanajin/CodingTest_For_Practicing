import java.io.IOException;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws IOException {
      Scanner sc = new Scanner(System.in);
      int n = sc.nextInt();
      int cnt = 0;
      int[] num = new int[100];
      for(int i=0;i<n;i++){
          num[i] = sc.nextInt();
      }
      int v = sc.nextInt();
      for(int i=0;i<n;i++){
          if (v == num[i]){
              cnt++;
          }
      }
        System.out.println(cnt);
    }
}
