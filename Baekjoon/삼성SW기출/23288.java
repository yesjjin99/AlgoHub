import java.util.*;
import java.io.*;

public class Main {

    static int[] dice = new int[]{0, 6, 5, 4, 3, 2, 1};  // 주사위 면 1의 반대편은 6
    static int[][] dir = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};  // 시계방향은 +1, 반시계방향은 -1

    static int n, m, k;
    static int[][] board;
    static int score = 0;
    static int x = 0, y = 0;
    static int up = 1, right = 3, front = 5;  // 주사위의 현재 윗면, 오른쪽 면, 앞을 바라보는 면
    static int dirIdx = 0;  // 가장 처음에 주사위의 이동 방향은 동쪽

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        while (k-- > 0) {
            moveDice();
            getScore();
            changeDir();
        }

        System.out.println(score);
    }

    // 주사위 굴리기
    static void moveDice() {
        int nx = x + dir[dirIdx][0];
        int ny = y + dir[dirIdx][1];

        if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
            dirIdx = (dirIdx + 2) % 4;  // 이동 방향에 칸이 없다면, 이동 방향을 반대로
        }

        switch (dirIdx) {
            case 0:
                int tmp = up;
                up = dice[right];
                right = tmp;
                break;
            case 1:
                tmp = up;
                up = dice[front];
                front = tmp;
                break;
            case 2:
                tmp = up;
                up = right;
                right = dice[tmp];
                break;
            case 3:
                tmp = up;
                up = front;
                front = dice[tmp];
                break;
        }

        x += dir[dirIdx][0];
        y += dir[dirIdx][1];
    }

    // 현재 칸에 대한 점수 구하기
    static void getScore() {
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[n][m];

        queue.add(new int[]{x, y});
        visited[x][y] = true;
        int cnt = 1;

        while (!queue.isEmpty()) {
            int[] v = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = v[0] + dir[i][0];
                int ny = v[1] + dir[i][1];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
                    continue;
                }

                if (!visited[nx][ny] && board[nx][ny] == board[x][y]) {
                    queue.add(new int[]{nx, ny});
                    visited[nx][ny] = true;
                    cnt++;
                }
            }
        }

        score += board[x][y] * cnt;
    }

    static void changeDir() {
        int down = dice[up], num = board[x][y];

        if (down > num) {
            dirIdx = (dirIdx + 1) % 4;  // 시계방향으로 회전
        } else if (down < num) {
            dirIdx = (dirIdx - 1 + 4) % 4;  // 반시계방향으로 회전
        }
    }
}