import java.io.*;
import java.util.*;

public class Main {

    static int answer = 4;
    static int n, m, h;
    static int[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        graph = new int[h + 1][n + 1];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a][b] = b + 1;  // 점선 a 위치(가로선)에서 b번 세로선과 b+1번 세로선 연결
            graph[a][b + 1] = b;
        }

        dfs(0, 1);
        System.out.println((answer > 3) ? -1 : answer);
    }

    // DFS, 백트래킹..?
    public static void dfs(int cnt, int x) {
        if (cnt >= answer) return;
        if (check()) {
            answer = cnt;
            return;
        }
        if (cnt == 3) return;

        for (int i = x; i <= h; i++) {
            for (int j = 1; j < n; j++) {
                if (graph[i][j] == 0 && graph[i][j + 1] == 0) {
                    graph[i][j] = j + 1; graph[i][j + 1] = j;
                    dfs(cnt + 1, i);
                    graph[i][j] = 0; graph[i][j + 1] = 0;
                }
            }
        }
    }

    public static boolean check() {  // 모든 i번 세로선의 결과가 i번이 나오는지
        int result = 0;

        for (int k = 1; k <= n; k++) {
            int i = 1; int j = k;
            while (i <= h) {
                if (graph[i][j] != 0) {
                    j = graph[i][j];
                }
                i++;
            }

            if (j == k) result++;
        }

        return result == n;
    }
}