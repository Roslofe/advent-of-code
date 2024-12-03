package day02;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.List;
import java.util.stream.Stream;

public class Parser {
    /**
     * Read the input file, return the lines of the file
     */
    public static List<String[]> ReadInput(String filename) {
        try {

            FileReader fileReader = new FileReader(filename);
            BufferedReader reader = new BufferedReader(fileReader);

            Stream<String> lines = reader.lines();

            // map the lines to a stream of string lists
            return lines.map(t -> t.split(" ")).toList();

        } catch (Exception e) {
            System.out.printf("Couldn't read file %s%n", filename);
        }

        return List.of();
    }
}
