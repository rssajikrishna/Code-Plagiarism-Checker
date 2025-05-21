import requests
from datetime import datetime

java_code = """import java.io.*;
import java.util.*;
import java.util.stream.*;

import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'countApplesAndOranges' function below.
     *
     * The function accepts following parameters:
     *  1. INTEGER s - starting point of Sam's house
     *  2. INTEGER t - ending point of Sam's house
     *  3. INTEGER a - location of the apple tree
     *  4. INTEGER b - location of the orange tree
     *  5. INTEGER_ARRAY apples - distances each apple falls from the tree
     *  6. INTEGER_ARRAY oranges - distances each orange falls from the tree
     */

    public static void countApplesAndOranges(int s, int t, int a, int b, List<Integer> apples, List<Integer> oranges) {
        int appleCount = 0;
        int orangeCount = 0;

        for (int apple : apples) {
            int landingPoint = a + apple;
            if (landingPoint >= s && landingPoint <= t) {
                appleCount++;
            }
        }

        for (int orange : oranges) {
            int landingPoint = b + orange;
            if (landingPoint >= s && landingPoint <= t) {
                orangeCount++;
            }
        }

        System.out.println(appleCount);
        System.out.println(orangeCount);
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] firstMultipleInput = bufferedReader.readLine().trim().split(" ");
        int s = Integer.parseInt(firstMultipleInput[0]);
        int t = Integer.parseInt(firstMultipleInput[1]);

        String[] secondMultipleInput = bufferedReader.readLine().trim().split(" ");
        int a = Integer.parseInt(secondMultipleInput[0]);
        int b = Integer.parseInt(secondMultipleInput[1]);

        String[] thirdMultipleInput = bufferedReader.readLine().trim().split(" ");
        int m = Integer.parseInt(thirdMultipleInput[0]);
        int n = Integer.parseInt(thirdMultipleInput[1]);

        List<Integer> apples = Stream.of(bufferedReader.readLine().trim().split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        List<Integer> oranges = Stream.of(bufferedReader.readLine().trim().split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        Result.countApplesAndOranges(s, t, a, b, apples, oranges);

        bufferedReader.close();
    }
}"""

mock_submissions = [
    {
        "username": "yokkeshsanjai201",
        "problem_slug": "smart-goji",
        "source_code": java_code,
        "srclink": "https://www.hackerrank.com/contests/smart-goji/challenges/apple-and-orange/submissions/code/1391000105",
        "timestamp": datetime.now().isoformat()
    },
    {
        "username": "rssajikrishna11",
        "problem_slug": "smart-goji",
        "source_code": java_code,
        "srclink": "https://www.hackerrank.com/contests/smart-goji/challenges/apple-and-orange/submissions/code/1390999884",
        "timestamp": datetime.now().isoformat()
    }
]

for sub in mock_submissions:
    res = requests.post("http://127.0.0.1:8000/submission", json=sub)
    print(f"Posted submission by {sub['username']}: {res.status_code}")
