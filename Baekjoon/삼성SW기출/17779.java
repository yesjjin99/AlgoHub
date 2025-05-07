import java.util.*;
import java.io.*;

public class Main {

    static int n;
    static int answer = Integer.MAX_VALUE;
    static int[][] board;
    static int totalCount = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        board = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                totalCount += board[i][j];
            }
        }

        for (int x = 0; x < n; x++) {
            for (int y = 0; y < n; y++) {
                for (int d1 = 1; d1 < n; d1++) {
                    for (int d2 = 1; d2 < n; d2++) {
                        if (x + d1 + d2 >= n) continue;
                        if (y - d1 < 0 || y + d2 >= n) continue;

                        countRegions(x, y, d1, d2);
                    }
                }
            }
        }

        System.out.println(answer);
    }

    static void countRegions(int x, int y, int d1, int d2) {
        boolean[][] border = new boolean[n][n];
        int[] count = new int[5];

        // 경계선 표시
        for (int i = 0; i <= d1; i++) {
            border[x + i][y - i] = true;
            border[x + d2 + i][y + d2 - i] = true;
        }

        for (int i = 0; i <= d2; i++) {
            border[x + i][y + i] = true;
            border[x + d1 + i][y - d1 + i] = true;
        }

        // 1구역 인구수
        for (int i = 0; i < x + d1; i++) {
            for (int j = 0; j <= y; j++) {
                if (border[i][j]) break;
                count[0] += board[i][j];
            }
        }

        // 2구역 인구수
        for (int i = 0; i <= x + d2; i++) {
            for (int j = n - 1; j > y; j--) {
                if (border[i][j]) break;
                count[1] += board[i][j];
            }
        }

        // 3구역 인구수
        for (int i = x + d1; i < n; i++) {
            for (int j = 0; j < y - d1 + d2; j++) {
                if (border[i][j]) break;
                count[2] += board[i][j];
            }
        }

        // 4구역 인구수
        for (int i = x + d2 + 1; i < n; i++) {
            for (int j = n - 1; j >= y - d1 + d2; j--) {
                if (border[i][j]) break;
                count[3] += board[i][j];
            }
        }

        // 5구역 인구수
        count[4] = totalCount;
        for (int i = 0; i < 4; i++) {
            count[4] -= count[i];
        }

        Arrays.sort(count);
        answer = Math.min(answer, count[4] - count[0]);
    }
}