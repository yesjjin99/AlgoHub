import java.util.*;

class Solution {

    private static final int MAX_VALUE = 1000000;

    private static int[] in, out;

    public int[] solution(int[][] edges) {
        int[] answer = new int[4];

        in = new int[MAX_VALUE + 1];
        out = new int[MAX_VALUE + 1];

        int maxNode = 0;
        for (int[] e : edges) {
            in[e[1]]++;  // 들어오는 간선
            out[e[0]]++;  // 나가는 간선

            maxNode = Math.max(maxNode, Math.max(e[0], e[1]));
        }

        for (int i = 1; i <= maxNode; i++) {
            if (in[i] == 0 && out[i] >= 2) {  // 생성된 정점: 들어오는 간선 0, 나가는 간선 2개 이상
                answer[0] = i;
            }
            else if (in[i] >= 1 && out[i] == 0) {  // 막대 모양 그래프: 들어오는 간선 1개 이상, 나가는 간선 0
                answer[2]++;
            }
            else if (in[i] >= 2 && out[i] >= 2) {  // 8자 모양 그래프: 들어오는 간선 2개 이상, 나가는 간선 2개 이상
                answer[3]++;
            }
        }

        // 막대 모양, 8자 모양 그래프를 제외한 나머지가 도넛 모양 그래프
        answer[1] = out[answer[0]] - (answer[2] + answer[3]);  // 도넛 모양 그래프: 생성 정점으로부터 나가는 간선의 개수 - (막대 모양 그래프 수 + 8자 모양 그래프 수)
        return answer;
    }
}