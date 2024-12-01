package day01;

import java.util.List;

public class Distance {

    public static void main(String[] args) {

        List<List<Integer>> numbers = Parser.ReadInput("./src/main/resources/input_day1.txt");

        /*
         * Part 1
         */
        // sort the lists
        List<Integer> firstList = numbers.get(0);
        firstList.sort(null);

        List<Integer> secondList = numbers.get(1);
        secondList.sort(null);

        int distances = 0;

        // traverse the lists, calculate distances
        for (int i = 0; i < firstList.size(); i++) {
            int newDistance = Math.abs(firstList.get(i) - secondList.get(i));
            distances += newDistance;
        }

        System.out.printf("Total distance: %d\n", distances);

        /*
         * Part 2
         */
        int similarity = 0;
        for (int i : firstList) {
            // find out the count of the value in the second list
            int instances = (int) secondList.stream().filter(n -> n == i).count();
            similarity += i * instances;
        }

        System.out.printf("Total similarity: %d", similarity);

    }
}
