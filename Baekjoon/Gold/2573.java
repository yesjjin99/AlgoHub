import java.io.*;
import java.util.*;

public class Main {

    static int n, m;
    static int[][] map;
    static int answer = 0;

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        while (true) {
            if (checkAllMelting()) {  // 만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면
                answer = 0;
                break;
            }

            melt();
            answer++;

            if (bfs()) break;
        }

        System.out.println(answer);
    }

    static void melt() {
        int[][] count = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 0) continue;

                for (int k = 0; k < 4; k++) {
                    int nx = i + dx[k], ny = j + dy[k];
                    if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;

                    if (map[nx][ny] == 0) {
                        count[i][j]++;
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                map[i][j] = Math.max(map[i][j] - count[i][j], 0);
            }
        }
    }

    static boolean bfs() {
        int cnt = 0;
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[n][m];

        for (int x = 0; x < n; x++) {
            for (int y = 0; y < m; y++) {
                if (map[x][y] == 0 || visited[x][y]) continue;

                queue.add(new int[]{x, y});
                visited[x][y] = true;

                while (!queue.isEmpty()) {
                    int[] cur = queue.poll();

                    for (int i = 0; i < 4; i++) {
                        int nx = cur[0] + dx[i], ny = cur[1] + dy[i];
                        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

                        if (!visited[nx][ny] && map[nx][ny] != 0) {
                            queue.add(new int[]{nx, ny});
                            visited[nx][ny] = true;
                        }
                    }
                }
                cnt++;
            }
        }

        return cnt >= 2;
    }

    static boolean checkAllMelting() {
        int cnt = Arrays.stream(map).flatMapToInt(Arrays::stream).sum();
        return cnt == 0;
    }
}