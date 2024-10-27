class Solution {
    public String solution(int[] food) {
        String answer = "";
        for (int i = 1; i < food.length; i++) {
            int n = food[i] / 2;
            for (int j = 0; j < n; j++) {
                answer += i;
            }
        }

        String reversed = "";
        for (int i = answer.length(); i >= 0; i--) {
            reversed += answer.charAt(i);
        }

        return answer + "0" + reversed;
    }
}