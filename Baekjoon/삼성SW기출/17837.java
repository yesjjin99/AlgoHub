import java.util.*;
import java.io.*;

public class Main {

    static int n, k;  // 체스판의 크기, 말의 개수
    static int[][] board;  // 체스판의 정보 - 0은 흰색, 1은 빨간색, 2는 파란색
    static int[][] pieces;  // 말의 정보 - 순서대로 행, 열의 번호, 이동 방향
    static List<Integer>[][] game;

    static int[] dx = {0, 0, -1, 1};  // 순서대로 →, ←, ↑, ↓
    static int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        game = new ArrayList[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                game[i][j] = new ArrayList<>();
            }
        }

        pieces = new int[k][3];
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            pieces[i][0] = Integer.parseInt(st.nextToken()) - 1;
            pieces[i][1] = Integer.parseInt(st.nextToken()) - 1;
            pieces[i][2] = Integer.parseInt(st.nextToken()) - 1;

            game[pieces[i][0]][pieces[i][1]].add(i);
        }

        int round = 1;
        boolean check = false;
        while (round++ < 1000) {
            for (int i = 0; i < k; i++) {
                movePiece(i);

                if (game[pieces[i][0]][pieces[i][1]].size() >= 4) {
                    check = true;
                    break;
                }
            }

            if (check) break;
        }

        System.out.println(round >= 1000 ? -1 : round - 1);
    }

    static void movePiece(int i) {
        int x = pieces[i][0], y = pieces[i][1], d = pieces[i][2];
        int idx = game[x][y].indexOf(i);
        List<Integer> move = new ArrayList<>(game[x][y].subList(idx, game[x][y].size()));  // i번 말과 위에 있는 모든 말

        int nx = x + dx[d], ny = y + dy[d];

        if (nx < 0 || nx >= n || ny < 0 || ny >= n) {  // 체스판을 벗어나는 경우
            d = (d % 2 == 0) ? d + 1 : d - 1;  // 이동 방향을 반대로
            pieces[i][2] = d;
            nx = x + dx[d]; ny = y + dy[d];

            if (board[nx][ny] != 2) {
                movePiece(i);
            }
        } else if (board[nx][ny] == 0) {  // 이동하려는 칸이 흰색인 경우
            for (int m : move) {
                pieces[m][0] = nx; pieces[m][1] = ny;
            }
            game[x][y].subList(idx, game[x][y].size()).clear();  // A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동
            game[nx][ny].addAll(move);  // 기존 말들의 위로 이동
        } else if (board[nx][ny] == 1) {  // 이동하려는 칸이 빨간색인 경우
            for (int m : move) {
                pieces[m][0] = nx; pieces[m][1] = ny;
            }
            game[x][y].subList(idx, game[x][y].size()).clear();
            Collections.reverse(move);  // i번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로
            game[nx][ny].addAll(move);
        } else if (board[nx][ny] == 2) {
            d = (d % 2 == 0) ? d + 1 : d - 1;
            pieces[i][2] = d;
            nx = x + dx[d]; ny = y + dy[d];

            if ((0 <= nx && nx < n && 0 <= ny && ny < n) && board[nx][ny] != 2) {    // 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히
                movePiece(i);
            }
        }
    }
}