import java.io.IOException;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] basket = new int[n];
        for(int i=1;i<n+1;i++){
            basket[i-1] = i;
        }
        for(int i=0;i<m;i++){
            int a = sc.nextInt()-1;
            int b = sc.nextInt()-1;
            while(a<b){
                int temp = basket[a];
                basket[a] = basket[b];
                basket[b] = temp;
                a++;
                b--;
            }
        }
        for(int i=0;i<n;i++){
            System.out.print(basket[i]+" ");
        }
    }
}
