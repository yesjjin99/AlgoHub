import java.io.*;
import java.util.*;

public class Main {

    static int n;
    static int[][] map;
    static int max = 0, min = Integer.MAX_VALUE;
    static int answer = 1;  // 아무 지역도 물에 안 잠길 수 있음

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        map = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                min = Math.min(min, map[i][j]);
                max = Math.max(max, map[i][j]);
            }
        }

        for (int i = min; i <= max; i++) {
            answer = Math.max(answer, bfs(i));
        }

        System.out.println(answer);
    }

    static int bfs(int h) {
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[n][n];
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] || map[i][j] <= h) continue;

                queue.add(new int[]{i, j});
                visited[i][j] = true;

                while (!queue.isEmpty()) {
                    int[] cur = queue.poll();

                    for (int d = 0; d < 4; d++) {
                        int nx = cur[0] + dx[d];
                        int ny = cur[1] + dy[d];

                        if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;

                        if (!visited[nx][ny] && map[nx][ny] > h) {
                            queue.add(new int[]{nx, ny});
                            visited[nx][ny] = true;
                        }
                    }
                }

                cnt++;
            }
        }

        return cnt;
    }
}