import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); //후보자 몇 명인지
//        ArrayList<String> name = new ArrayList<String>();
        String v; //투표입력
        Queue<Integer>[] vote_arr = new LinkedList[1001];
        int voting_person = 0; //몇명이 투표했는지?
        //후보 이름 입력
        String[] name = new String[n];

        for(int i=0; i<n; i++){
            name[i] = br.readLine();
        }
        //투표값 저장
        int[] vote = new int[1001];
        while ((v = br.readLine()) != null && !v.isEmpty()) { //eof 처리
            String[] arr = v.split(" "); // [1,2,3]
            vote_arr[voting_person] = new LinkedList();
            for (int i = 0; i < n; i++) {
                vote_arr[voting_person].add(Integer.parseInt(arr[i]) - 1);
            }
            voting_person++;
        }

        while (true) {
            //집계
            for (int i = 0; i < voting_person; i++) {
                while (vote[vote_arr[i].peek()] == -1) {
                    vote_arr[i].poll();
                }
                vote[vote_arr[i].peek()]++;
            }

            int max = 0, min = 10000;
            for(int i=0; i<n; i++){
                max = Math.max(max,vote[i]);
                if(vote[i] != -1){
                    min = Math.min(min,vote[i]);
                }
            }
            //절반 이상 또는 동률일 때
            if (max*2 > voting_person || max == min) {
                for (int i = 0; i < n; i++) {
                    if (vote[i] == max) {
                        System.out.println(name[i]);
                    }
                }
                return;
            }
            for(int i=0; i<n; i++){
                if(vote[i] == min){
                    vote[i] = -1;
                }
                else if(vote[i] != -1){
                    vote[i] = 0;
                }
            }
        }
    }
}