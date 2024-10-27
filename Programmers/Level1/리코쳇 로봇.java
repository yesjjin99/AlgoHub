import java.util.*;

class Solution {
    public int solution(String[] board) {
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};

        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[board.length][board[0].length()];

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length(); j++) {
                if (board[i].charAt(j) == 'R') {  // 시작 위치
                    queue.offer(new int[]{i, j, 0});  // x좌표, y좌표, 이동횟수
                    visited[i][j] = true;
                }
            }
        }

        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            int x = now[0];
            int y = now[1];
            int cnt = now[2];

            if (board[x].charAt(y) == 'G') {  // 목표 지점 도달
                return cnt;
            }

            for (int i = 0; i < 4; i++) {  // 상, 하, 좌, 우 이동
                int nx = x + dx[i];
                int ny = y + dy[i];

                while (nx >= 0 && nx < board.length && ny >= 0 && ny < board[0].length() && board[nx].charAt(ny) != 'D') {  // 장애물이나 게임판 가장자리까지 이동
                    nx += dx[i];
                    ny += dy[i];
                }

                nx -= dx[i];  // 장애물이나 게임판 가장자리에 도달하기 직전으로 이동
                ny -= dy[i];

                if (visited[nx][ny] || (nx == x && ny == y)) {  // 이미 방문했거나 이동한 위치가 제자리라면
                    continue;
                }
                queue.offer(new int[]{nx, ny, cnt + 1});
                visited[nx][ny] = true;
            }
        }

        return -1;  // 목표 위치에 도달할 수 없다면 -1 반환
    }
}
