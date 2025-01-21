import java.util.*;

class Solution {

    private static int n;
    private static int[][] dices;
    private static int[] answer;
    private static List<Integer> choices = new ArrayList<>();  // A가 고른 주사위 조합
    private static List<Integer> scoreA, scoreB;  // A의 모든 점수 조합, B의 모든 점수 조합
    private static int maxWinning = Integer.MIN_VALUE;  // 현재까지 가장 최대로 승리하는 경우의 수

    // N개의 주사위 중에서 N/2개 택해서 승률 구하기 (조합)
    private void choiceDice(int count, int s) {  // 고른 주사위 개수, 현재까지 고른 주사위 번호
        if (count == n / 2) {  // N/2개 고른 경우
            int winning = calculateWinningCount();
            if (maxWinning < winning) {  // 승리할 확률이 가장 높은 경우 갱신
                maxWinning = winning;
                for (int i = 0; i < choices.size(); i++) {
                    answer[i] = choices.get(i) + 1;
                }
            }
            return;
        }

        for (int i = s; i < n; i++) { // s부터 탐색을 하여, 중복을 없앤다. (DFS, 백트래킹)
            choices.add(i);
            choiceDice(count + 1, i + 1);
            choices.remove(choices.size() - 1);
        }
    }

    // A가 B를 이기는 모든 횟수 구하기
    private int calculateWinningCount() {
        int count = 0;

        makeScoreAB();

        Collections.sort(scoreB);
        for (int i = 0; i < scoreA.size(); i++) {
            // scoreB에 scoreA보다 작은 숫자가 몇 개 있는지 구한다
            int num = scoreA.get(i);

            int index = Integer.MIN_VALUE;
            int left = 0, right = scoreB.size() - 1;
            while (left <= right) {  // 이진 탐색
                int mid = (left + right) / 2;

                if (scoreB.get(mid) < num) {
                    left = mid + 1;
                    index = Math.max(index, mid);  // num 보다 작을 때만 index 업데이트
                } else {
                    right = mid - 1;
                }
            }

            if (index != Integer.MIN_VALUE) {
                count += index + 1;
            }
        }
        return count;
    }

    // A와 B의 모든 점수 조합 구하기
    private void makeScoreAB() {
        scoreA = new ArrayList<>();
        scoreB = new ArrayList<>();

        int[][] diceA = new int[n / 2][6];
        int[][] diceB = new int[n / 2][6];
        int a = 0, b = 0;

        // 주사위 A, B 만들기
        for (int i = 0; i < n; i++) {
            if (choices.contains(i)) {
                diceA[a] = dices[i];
                a++;
            } else {
                diceB[b] = dices[i];
                b++;
            }
        }

        calculateScores(0, diceA, 0, scoreA);
        calculateScores(0, diceB, 0, scoreB);
    }

    // 해당하는 사람의 주사위를 모두 굴려 나올 수 있는 점수를 모두 구하기 (조합)
    private void calculateScores(int count, int[][] dice, int sum, List<Integer> score) {  // 주사위 굴린 개수, 가지고 있는 주사위들, 현재까지 나온 수의 합, 저장할 점수 리스트
        if (count == n / 2) {  // 가지고있는 주사위를 모두 굴린 경우, 나온 숫자의 합을 리스트에 추가
            score.add(sum);
            return;
        }

        for (int i = 0; i < 6; i++) {
            int newSum = sum + dice[count][i];  // 각 주사위마다 수를 하나씩 뽑아서 더한다
            calculateScores(count + 1, dice, newSum, score);
        }
    }

    public int[] solution(int[][] dice) {
        n = dice.length;
        dices = dice;
        answer = new int[n / 2];

        choiceDice(0, 0);
        return answer;
    }
}