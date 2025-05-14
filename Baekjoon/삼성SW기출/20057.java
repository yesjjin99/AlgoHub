import java.util.*;
import java.io.*;

public class Main {

    static int n;
    static int[][] board;
    static int answer = 0;

    static int[] dx = {0, 1, 0, -1};  // 왼쪽 - 아래쪽 - 오른쪽 - 위쪽
    static int[] dy = {-1, 0, 1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int x = n / 2, y = n / 2;

        for (int i = 1; i < n; i += 2) {
            // i만큼 왼쪽 -> 아래쪽으로 이동
            for (int j = 0; j < i; j++) {
                x += dx[0];
                y += dy[0];
                moveLeft(x, y);
            }
            for (int j = 0; j < i; j++) {
                x += dx[1];
                y += dy[1];
                moveDown(x, y);
            }

            // i + 1만큼 오른쪽 -> 위쪽으로 이동
            for (int j = 0; j < i + 1; j++) {
                x += dx[2];
                y += dy[2];
                moveRight(x, y);
            }

            for (int j = 0; j < i + 1; j++) {
                x += dx[3];
                y += dy[3];
                moveUp(x, y);
            }
        }

        // 마지막으로 n - 1만큼 왼쪽으로 이동
        for (int i = 0; i < n - 1; i++) {
            x += dx[0];
            y += dy[0];
            moveLeft(x, y);
        }

        System.out.println(answer);
    }

    static void moveLeft(int i, int j) {  // 왼쪽으로 이동하여 (i, j)에 도착
        int[][] moves = {
            {-1, -1, 10}, {1, -1, 10},
            {-1, 0, 7}, {1, 0, 7},
            {0, -2, 5},
            {-2, 0, 2}, {2, 0, 2},
            {-1, 1, 1}, {1, 1, 1},
            {0, -1, -1}
        };
        int amount = board[i][j];

        for (int[] move : moves) {
            int k = 0;
            if (move[2] == -1) {  // 마지막 α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양
                k = board[i][j];
            } else {
                k = amount * move[2] / 100;
            }
            board[i][j] -= k;

            if (i + move[0] < 0 || i + move[0] >= n || j + move[1] < 0 || j + move[1] >= n) {
                answer += k;  // 격자 밖으로 나간 경우
                continue;
            }
            board[i + move[0]][j + move[1]] += k;
        }
    }

    static void moveDown(int i, int j) {
        int[][] moves = {
            {1, -1, 10}, {1, 1, 10},
            {0, -1, 7}, {0, 1, 7},
            {2, 0, 5},
            {0, -2, 2}, {0, 2, 2},
            {-1, -1, 1}, {-1, 1, 1},
            {1, 0, -1}
        };
        int amount = board[i][j];

        for (int[] move : moves) {
            int k = 0;
            if (move[2] == -1) {  // 마지막 α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양
                k = board[i][j];
            } else {
                k = amount * move[2] / 100;
            }
            board[i][j] -= k;

            if (i + move[0] < 0 || i + move[0] >= n || j + move[1] < 0 || j + move[1] >= n) {
                answer += k;  // 격자 밖으로 나간 경우
                continue;
            }
            board[i + move[0]][j + move[1]] += k;
        }
    }

    static void moveRight(int i, int j) {
        int[][] moves = {
            {-1, 1, 10}, {1, 1, 10},
            {-1, 0, 7}, {1, 0, 7},
            {0, 2, 5},
            {-2, 0, 2}, {2, 0, 2},
            {-1, -1, 1}, {1, -1, 1},
            {0, 1, -1}
        };
        int amount = board[i][j];

        for (int[] move : moves) {
            int k = 0;
            if (move[2] == -1) {  // 마지막 α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양
                k = board[i][j];
            } else {
                k = amount * move[2] / 100;
            }
            board[i][j] -= k;

            if (i + move[0] < 0 || i + move[0] >= n || j + move[1] < 0 || j + move[1] >= n) {
                answer += k;  // 격자 밖으로 나간 경우
                continue;
            }
            board[i + move[0]][j + move[1]] += k;
        }
    }

    static void moveUp(int i, int j) {
        int[][] moves = {
            {-1, -1, 10}, {-1, 1, 10},
            {0, -1, 7}, {0, 1, 7},
            {-2, 0, 5},
            {0, -2, 2}, {0, 2, 2},
            {1, -1, 1}, {1, 1, 1},
            {-1, 0, -1}
        };
        int amount = board[i][j];

        for (int[] move : moves) {
            int k = 0;
            if (move[2] == -1) {  // 마지막 α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양
                k = board[i][j];
            } else {
                k = amount * move[2] / 100;
            }
            board[i][j] -= k;

            if (i + move[0] < 0 || i + move[0] >= n || j + move[1] < 0 || j + move[1] >= n) {
                answer += k;  // 격자 밖으로 나간 경우
                continue;
            }
            board[i + move[0]][j + move[1]] += k;
        }
    }
}