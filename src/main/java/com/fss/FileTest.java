package com.fss;

import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;
public class FileTest {
    public static void main(String[] args) {
        try {
           File f = new File("test.txt");   
            
            f.createNewFile();
           // f.deleteOnExit();
           FileWriter fw = new FileWriter(f);
           fw.write("Hello World");
           fw.close();

            Scanner sc = new Scanner(f);
            while (sc.hasNextLine()) {
                System.out.println(sc.nextLine());
            }
            sc.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
