import java.io.*;
import java.util.*;

public class Main {

    private static int p1, p2;
    private static List<Integer>[] graph;
    private static boolean[] visited;
    private static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        visited = new boolean[n + 1];
        graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        p1 = Integer.parseInt(st.nextToken());
        p2 = Integer.parseInt(st.nextToken());

        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());  // 부모
            int y = Integer.parseInt(st.nextToken());  // 자식

            graph[x].add(y);
            graph[y].add(x);
        }

        dfs(p1, 0);
        System.out.println((result == 0) ? -1 : result);
    }

    private static void dfs(int v, int cnt) {
        visited[v] = true;
        if (v == p2) {
            result = cnt;
            return;
        }

        for (int r : graph[v]) {
            if (!visited[r]) {
                dfs(r, cnt + 1);
            }
        }
    }
}