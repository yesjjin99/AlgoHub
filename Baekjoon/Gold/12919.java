import java.util.*;
import java.io.*;

public class Main {

    static String s;
    static String t;

    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = br.readLine();
        t = br.readLine();

        dfs(t);
        System.out.println(answer);
    }

    // S -> T로는 시간초과 발생, T -> S로 만든다
    static void dfs(String t) {
        int lenT = t.length();
        if (lenT == s.length()) {  // 길이가 같아지면 더 이상 방법이 없으므로 중단
            if (t.equals(s)) {
                answer = 1;
            }
            return;
        }

        // 1. A로 끝나는 경우, 맨 뒤의 A 제거
        if (t.endsWith("A")) {
            dfs(t.substring(0, lenT - 1));
        }

        // 2. B로 시작하는 경우, 맨 앞의 B 제거하고 문자열 뒤집기
        if (t.startsWith("B")) {
            dfs(new StringBuilder(t.substring(1)).reverse().toString());
        }
    }
}