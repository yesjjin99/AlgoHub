import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int f = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int g = Integer.parseInt(st.nextToken());
        int u = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        // BFS
        Queue<Integer> q = new LinkedList<>();
        int[] visited = new int[f + 1];
        Arrays.fill(visited, -1);

        q.add(s);
        visited[s] = 0;

        while (!q.isEmpty()) {
            int v = q.poll();
            if (v == g) break;

            // 위로 이동
            if (v + u <= f && visited[v + u] == -1) {
                q.add(v + u);
                visited[v + u] = visited[v] + 1;
            }

            // 아래로 이동
            if (v - d > 0 && visited[v - d] == -1) {
                q.add(v - d);
                visited[v - d] = visited[v] + 1;
            }
        }

        System.out.println(visited[g] == -1 ? "use the stairs" : visited[g]);
    }
}