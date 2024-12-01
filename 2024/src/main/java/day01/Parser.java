package day01;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

public class Parser {
    public static List<List<Integer>> ReadInput(String filename) {
        try {
            FileReader fileReader = new FileReader(filename);
            BufferedReader reader = new BufferedReader(fileReader);

            List<Integer> firstList = new ArrayList<>();
            List<Integer> secondList = new ArrayList<>();

            while (reader.ready()) {
                // Parse each line and add the numbers to relevant arrays
                String line = reader.readLine();
                String[] numbers = line.split("   ");
                firstList.add(Integer.parseInt(numbers[0]));
                secondList.add(Integer.parseInt(numbers[1]));
            }

            return List.of(firstList, secondList);

        } catch (Exception e) {
            System.out.printf("Couldn't read file %s%n", filename);
        }
        return List.of();
    }
}