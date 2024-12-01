package day01;

import java.util.List;

public class Distance {
    public static void main(String[] args) {

        List<List<Integer>> numbers = Parser.ReadInput("./src/main/resources/input_day1.txt");

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

        System.out.printf("Total distance: %d", distances);

    }
}
