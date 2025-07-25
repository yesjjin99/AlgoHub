import java.io.*;
import java.util.*;

public class Main {

    static class Node {
        int v;  // 도착점
        int cost;  // 비용

        public Node(int v, int c) {
            this.v = v;
            this.cost = c;
        }
    }

    static int n, m, x;
    static ArrayList<Node>[] graph, reverseGraph;
    static int[] distance, reverseDistance;  // 최단 거리 테이블

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());

        graph = new ArrayList[n + 1];
        reverseGraph = new ArrayList[n + 1];  // 반대로 갈 때의 최단시간을 구하기 위한 도로 리스트
        distance = new int[n + 1];
        reverseDistance = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
            reverseGraph[i] = new ArrayList<>();
            distance[i] = Integer.MAX_VALUE;
            reverseDistance[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph[u].add(new Node(v, c));
            reverseGraph[v].add(new Node(u, c));
        }

        dijkstraTo();
        dijkstraFrom();

        int answer = 0;  // 오고 가는데 가장 오래 걸리는 학생의 소요시간
        for (int i = 1; i <= n; i++) {
            answer = Math.max(answer, distance[i] + reverseDistance[i]);
        }

        System.out.println(answer);
    }

    /* N(1 ≤ N ≤ 1,000)에 따른 시간복잡도를 고려해 플로이드 워셜이 아닌 다익스트라 사용 */

    static void dijkstraTo() {  // 자신의 마을에서 출발하여 X 마을로 갈 때의 최단시간
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.cost - o2.cost);  // 가중치를 기준으로 최소 힙
        pq.add(new Node(x, 0));  // 시작 노드에 대해 초기화
        reverseDistance[x] = 0;

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (distance[cur.v] < cur.cost)
                continue;

            for (Node next : reverseGraph[cur.v]) {
                int dist = cur.cost + next.cost;
                if (dist < reverseDistance[next.v]) {
                    pq.add(new Node(next.v, dist));
                    reverseDistance[next.v] = dist;
                }
            }
        }
    }

    static void dijkstraFrom() {  // X 마을에서 출발하여 자신의 마을로 돌아갈 때의 최단시간
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o2.cost - o1.cost);
        pq.add(new Node(x, 0));
        distance[x] = 0;

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (distance[cur.v] < cur.cost)
                continue;

            for (Node next : graph[cur.v]) {
                int dist = cur.cost + next.cost;
                if (dist < distance[next.v]) {
                    pq.add(new Node(next.v, dist));
                    distance[next.v] = dist;
                }
            }
        }
    }
}