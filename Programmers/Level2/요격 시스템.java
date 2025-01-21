import java.util.*;

class Solution {

    public int solution(int[][] targets) {
        int answer = 0;

        Arrays.sort(targets, (o1, o2) -> o1[1] - o2[1]);  // 끝점을 기준으로 정렬

        int now = 0;
        for (int[] target : targets) {
            if (now <= target[0]) {  // 미사일의 시작점이 현재 요격시간 이상일 때 -> 요격기 설치
                answer++;
                now = target[1];  // 미사일 끝점에 요격기 설치
            }
        }

        return answer;
    }
}
