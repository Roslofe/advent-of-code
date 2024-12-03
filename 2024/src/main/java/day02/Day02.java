package day02;

import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Day02 {
    public static void main(String[] args) {

        List<String[]> reports = Parser.ReadInput("./src/main/resources/input_day2.txt");

        int SafeReports = 0;

        // go over each report, check if safe
        for (String[] report : reports) {

            // map measurements to integer
            List<Integer> measurements = Arrays.stream(report).map(Integer::parseInt).toList();

            // calculate the difference between the value at the index, and the previous value
            List<Integer> differences = IntStream.range(1, measurements.size()).map(v -> measurements.get(v - 1) - measurements.get(v)).boxed().toList();

            // check if the values are all increasing, all decreasing, or all between 3 and -3
            boolean allIncreasing = differences.stream().allMatch(v -> v > 0);
            boolean allDecreasing = differences.stream().allMatch(v -> v < 0);
            boolean inRange = differences.stream().allMatch(v -> v >= -3 && v <= 3);
            if ((allIncreasing || allDecreasing) && inRange) {
                SafeReports += 1;
            }
        }

        System.out.printf("Number of safe reports: %d", SafeReports);
    }
}
