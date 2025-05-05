import java.util.*;
import java.io.*;

class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {

    static ArrayList<Point> arr;
    static ArrayList<ArrayList<Integer>> graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            arr = new ArrayList<>();

            // 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표 입력받기
            for (int i = 0; i < n + 2; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());

                arr.add(new Point(x, y));
            }

            graph = new ArrayList<>();
            for (int i = 0; i < n + 2; i++) {
                graph.add(new ArrayList<>());
            }

            // 거리 1000m 이하를 만족하는 두 정점은 양방향 그래프로 연결!
            for (int i = 0; i < n + 2; i++) {
                for (int j = i + 1; j < n + 2; j++) {
                    if (distance(arr.get(i), arr.get(j)) <= 1000) {
                        graph.get(i).add(j);
                        graph.get(j).add(i);
                    }
                }
            }

            sb.append((bfs(n) ? "happy" : "sad") + "\n");
        }

        System.out.println(sb.toString());
    }

    static boolean bfs(int n) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);

        boolean[] visited = new boolean[n + 2];
        visited[0] = true;

        while (!queue.isEmpty()) {
            int now = queue.poll();

            if (now == n + 1) {  // 목적지인 페스티벌 위치에 도착했다면
                return true;
            }

            for (int next : graph.get(now)) {
                if (!visited[next]) {
                    visited[next] = true;
                    queue.add(next);
                }
            }
        }

        return false;
    }

    // 두 좌표 간 거리 구하기
    static int distance(Point p1, Point p2) {
        return Math.abs(p1.x - p2.x) + Math.abs(p1.y - p2.y);
    }
}


---

import java.util.*;
import java.io.*;

class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {

    static ArrayList<Point> arr;
    static boolean[][] isSearch;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            arr = new ArrayList<>();

            // 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표 입력받기
            for (int i = 0; i < n + 2; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());

                arr.add(new Point(x, y));
            }

            isSearch = new boolean[n + 2][n + 2];
            // 거리 1000m 이하를 만족하는 두 정점은 연결되어 있다고 판단하고 true 처리
            for (int i = 0; i < n + 2; i++) {
                for (int j = i + 1; j < n + 2; j++) {
                    if (distance(arr.get(i), arr.get(j)) <= 1000) {
                        isSearch[i][j] = isSearch[j][i] = true;
                    }
                }
            }

            // 플로이드 워셜 알고리즘
            for (int k = 0; k < n + 2; k++) {
                for (int i = 0; i < n + 2; i++) {
                    for (int j = 0; j < n + 2; j++) {
                        if (isSearch[i][k] && isSearch[k][j]) {
                            isSearch[i][j] = true;
                        }
                    }
                }
            }

            // 집(0)에서 페스티벌 위치(n + 1)까지 갈 수 있는지 여부
            sb.append((isSearch[0][n + 1] ? "happy" : "sad") + "\n");
        }

        System.out.println(sb.toString());
    }

    // 두 좌표 간 거리 구하기
    static int distance(Point p1, Point p2) {
        return Math.abs(p1.x - p2.x) + Math.abs(p1.y - p2.y);
    }
}
