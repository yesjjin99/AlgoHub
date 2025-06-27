import java.io.*;
import java.util.*;

class Main {
    static char[][] map;
    static int R;
    static int C;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        Queue<Move> moveQueue = new ArrayDeque<>();
        Queue<Move> fireQueue = new ArrayDeque<>();
        map = new char[R][C];
        boolean[][] visit = new boolean[R][C];

        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                char c = line.charAt(j);
                map[i][j] = c;
                if (c == 'J') {
                    moveQueue.add(new Move(i, j, 0));
                    visit[i][j] = true;
                }
                if (c == 'F') {
                    fireQueue.add(new Move(i, j, 0));
                    visit[i][j] = true;
                }
            }

        }

        int idx = 0;
        while (!moveQueue.isEmpty()) {
            //불 먼저 옮기기
            while (!fireQueue.isEmpty() && fireQueue.peek().count == idx) {
                Move cur = fireQueue.poll();
                for (int i = 0; i < 4; i++) {
                    int newFireX = cur.x + dx[i];
                    int newFireY = cur.y + dy[i];

                    if (newFireY >= R || newFireX >= C || newFireX < 0 || newFireY < 0 || map[newFireY][newFireX] == '#' || visit[newFireY][newFireX]) {
                        continue;
                    }

                    visit[newFireY][newFireX] = true;
                    fireQueue.add(new Move(newFireY, newFireX, cur.count + 1));
                }
            }

            while (!moveQueue.isEmpty() && moveQueue.peek().count == idx) {
                Move cur = moveQueue.poll();

                for (int i = 0; i < 4; i++) {
                    int newMoveX = cur.x + dx[i];
                    int newMoveY = cur.y + dy[i];
                    if (newMoveY >= R || newMoveX >= C || newMoveX < 0 || newMoveY < 0) {
                        System.out.println(cur.count + 1);
                        return;
                    } else if (map[newMoveY][newMoveX] == '#' || visit[newMoveY][newMoveX]) {
                        continue;
                    }
                    visit[newMoveY][newMoveX] = true;
                    moveQueue.add(new Move(newMoveY, newMoveX, cur.count + 1));
                }
            }
            idx++;
        }
        System.out.println("IMPOSSIBLE");


    }
}

class Move {
    int x, y, count;

    public Move(int y, int x, int count) {
        this.x = x;
        this.y = y;
        this.count = count;
    }
}