import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());

        int[] nums = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int start = 0, end = 0;  // 투 포인터
        int sum = 0, answer = Integer.MAX_VALUE;

        while (start <= end && end <= n) {  // 마지막 인덱스까지 탐색할 수 있도록 종료조건 설정
            if (sum < s) {
                sum += nums[end++];
            } else {
                answer = Math.min(answer, end - start);
                sum -= nums[start++];
            }
        }

        System.out.println(answer == Integer.MAX_VALUE ? 0 : answer);
    }
}