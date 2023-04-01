import java.io.IOException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> al = new ArrayList<Integer>();

        for(int i=1;i<29;i++){
            int n = sc.nextInt();
            al.add(n);
        }
        for(int i=1;i<31;i++){
            if(al.contains(i)){
                continue;
            }
            else {
                System.out.println(i);
            }
        }
    }
}
