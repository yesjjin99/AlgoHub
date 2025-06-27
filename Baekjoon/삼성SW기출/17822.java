import java.io.*;
import java.util.*;

public class Main {

    static int n, m, t;  // 원판의 개수, 각 원판에 적힌 정수의 개수, 회전 수
    static int x, d, k;
    static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());

        board = new int[n + 1][m];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        while (t-- > 0) {
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());

            rotate();
            changeNumber();
        }

        System.out.println(getTotal());
    }

    static void rotate() {
        for (int i = x; i <= n; i += x) {
            for (int j = 0; j < k; j++) {
                if (d == 0) {  // 시계 방향
                    int tmp = board[i][m - 1];
                    for (int p = m - 2; p >= 0; p--) {
                        board[i][p + 1] = board[i][p];
                    }
                    board[i][0] = tmp;
                } else if (d == 1) {  // 반시계 방향
                    int tmp = board[i][0];
                    for (int p = 1; p < m; p++) {
                        board[i][p - 1] = board[i][p];
                    }
                    board[i][m - 1] = tmp;
                }
            }
        }
    }

    static void changeNumber() {
        boolean[][] visited = new boolean[n + 1][m];  // 삭제할 좌표를 모두 모아두었다가, 한 번에 0으로 바꿔야 함
        boolean hasAdjacent = false;

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 0) continue;
                int cur = board[i][j];

                // 상하좌우(원판이므로 좌우는 원형 연결)
                int[] dx = {0, 0, 1, -1};
                int[] dy = {1, -1, 0, 0};

                for (int d = 0; d < 4; d++) {
                    int ni = i + dx[d];
                    int nj = (j + dy[d] + m) % m; // 원형 연결

                    if (ni < 1 || ni > n) continue;

                    if (board[ni][nj] == cur) {
                        visited[i][j] = true;
                        visited[ni][nj] = true;
                        hasAdjacent = true;
                    }
                }
            }
        }

        if (hasAdjacent) {
            for (int i = 1; i <= n; i++) {
                for (int j = 0; j < m; j++) {
                    if (visited[i][j]) board[i][j] = 0;
                }
            }
        } else {
            double avg = (double) getTotal() / countNumber();
            for (int i = 1; i <= n; i++) {
                for (int j = 0; j < m; j++) {
                    if (board[i][j] == 0) continue;

                    if (board[i][j] > avg) board[i][j]--;
                    else if (board[i][j] < avg) board[i][j]++;
                }
            }
        }
    }


    static int getTotal() {  // 원판에 적힌 수의 합
        return Arrays.stream(board)
            .flatMapToInt(Arrays::stream)
            .sum();
    }

    static int countNumber() {
        int cnt = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] != 0) cnt++;
            }
        }
        return cnt;
    }
}