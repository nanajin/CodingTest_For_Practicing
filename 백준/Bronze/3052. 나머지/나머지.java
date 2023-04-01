import java.io.IOException;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        HashSet<Integer> s = new HashSet<Integer>();
        for(int i=0;i<10;i++){
            int n = sc.nextInt();
            int mod = n % 42;
            s.add(mod);
        }
        System.out.println(s.size());
    }
}
