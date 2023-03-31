import java.io.IOException;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws IOException {
      Scanner sc = new Scanner(System.in);
      int n = sc.nextInt();
      int x = sc.nextInt();
      int[] small = new int[n];
      int[] num = new int[n];
      for(int i=0;i<n;i++){
          num[i] = sc.nextInt();
      }
      for(int i=0;i<n;i++){
          if (x > num[i]){
              small[i] = num[i];
          }
      }
        for(int i=0;i<n;i++){
            if (small[i] != 0) {
                System.out.print(small[i] + " ");
            }
        }
    }
}
