import java.util.*;

class Solution {
    public int solution(int[] money) {
        int[] dp1 = Arrays.copyOf(money, money.length);  // 첫번째 집부터 시작하는 경우
        int[] dp2 = Arrays.copyOf(money, money.length);  // 두번째 집부터 시작하는 경우 (마지막 집 포함하는 경우)

        // DP : 인접하기 전까지의 최댓값 갱신
        for (int i = 2; i < money.length - 1; i++) {
            if (i > 2) {
                // (인접하지 않은) 2번째 전 집이나 3번째 전 집 중 최댓값
                dp1[i] += Math.max(dp1[i - 2], dp1[i - 3]);
                dp2[i + 1] += Math.max(dp2[i - 1], dp2[i - 2]);
            } else {
                dp1[i] += dp1[i - 2];
                dp2[i + 1] += dp2[i - 1];
            }
        }

        int max1 = Arrays.stream(dp1).max().getAsInt();
        int max2 = Arrays.stream(dp2).max().getAsInt();

        return Math.max(max1, max2);
    }
}