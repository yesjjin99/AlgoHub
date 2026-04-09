import java.io.*;
import java.util.*;

public class Main {

    static int answer = 0;
    static int n;  // 공간의 크기
    static int[][] board;
    static int x, y;  // 아기상어의 위치
    static int size = 2, cur = 0;  // 아기 상어 크기, 현재 먹은 물고기의 개수

    static int[] dx = {-1, 1, 0, 0},  dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());

        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 9) {
                    x = i; y = j;
                }
            }
        }

        /*
        (이동할 때마다 answer +1)
        2. 먹을 수 있는 물고기 == 1
        - 그 물고기로 이동 => 먹은 물고기 +1
        - 현재 물고기를 먹음으로써 - 현재 본인의 크기와 같은 수의 물고기를 먹은 것이라면 => 아기상어 크기 +1, 먹은 쿨고기 = 0
        3. 먹을 수 있는 물고기 > 1
        - 그 중 가장 거리가 가까운 물고기로 이동 => 먹은 물고기 +1
        - 만약 거리가 가까운 물고기가 여러개라면 -> 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기로 이동
            -> 최소 거리인 물고기 리스트 임시로 저장(좌표) - x좌표 오름차순, y좌표 오름차순으로 정렬하여 가장 첫번째 값으로 접근!
        - 현재 물고기를 먹음으로써 - 현재 본인의 크기와 같은 수의 물고기를 먹은 것이라면 => 아기상어 크기 +1, 먹은 쿨고기 = 0
        4. else (먹을 수 있는 물고기 없음)
        - return answer; 종료!
        */

        move();
        System.out.println(answer);
    }

    public static void move() {
        while (true) {
            ArrayList<Fish> fishes = bfs();
            if (fishes.isEmpty()) return;

            fishes.sort((o1, o2) -> {
                if (o1.dist == o2.dist) {
                    if (o1.point.x == o2.point.x) {
                        return o1.point.y - o2.point.y;
                    }
                    return o1.point.x - o2.point.x;
                }
                return o1.dist - o2.dist;
            });

            int i = fishes.get(0).point.x;
            int j = fishes.get(0).point.y;
            int time = fishes.get(0).dist;
            board[i][j] = 0; board[x][y] = 0;
            x = i; y = j;

            cur++;
            answer += time;
            if (size == cur) {
                size++;
                cur = 0;
            }
        }
    }

    // 현재 아기상어의 위치에서 먹을 수 있는 물고기 찾기
    public static ArrayList<Fish> bfs() {
        Queue<Point> queue = new ArrayDeque<>();
        int[][] visited = new int[n][n];  // 거리 계산
        ArrayList<Fish> result = new ArrayList<>();

        queue.offer(new Point(x, y));
        visited[x][y] = 0;

        /*
        1. 아기상어의 상하좌우를 확인한다.
        - 자신보다 큰 물고기가 있는 칸은 지날 수 없음 & 자신과 크기가 같은 물고기가 있는 칸은 지날 수 있음 (먹을 수 없음)
        - 먹을 수 있는 물고기의 '개수와 각 물고기까지 거리'를 구한다
        */
        while (!queue.isEmpty()) {
            Point p = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = p.x + dx[i], ny = p.y + dy[i];
                if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;

                if (visited[nx][ny] == 0 && board[nx][ny] <= size) {
                    Point newP = new Point(nx, ny);
                    queue.offer(newP);
                    visited[nx][ny] = visited[p.x][p.y] + 1;

                    if (board[nx][ny] > 0 && board[nx][ny] < size) {
                        result.add(new Fish(visited[nx][ny], newP));
                    }
                }
            }
        }

        return result;
    }

    public static class Point {
        int x, y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static class Fish {
        int dist;  // 거리
        Point point;  // 좌표

        public Fish(int dist, Point point) {
            this.dist = dist;
            this.point = point;
        }
    }
 }