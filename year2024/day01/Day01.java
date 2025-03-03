package year2024.day01;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class Day01 {
    public static void main(String[] args) {
        String filePath = "year2024/day01/sample.txt";
        File file = new File(filePath);
        try {
            BufferedReader br = new BufferedReader(new FileReader(file));
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        }
        catch (Exception e) {
            System.out.println("Something went wrong " + e);
        }
    }
}