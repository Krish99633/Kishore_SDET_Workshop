package com.fss;

    import java.util.ArrayList;
    import java.util.Collections;
    import java.util.HashMap;
    import java.util.HashSet;
    
    public class Singleton {
        private static Singleton instance = new Singleton();
        private Singleton() {}
        public static Singleton getInstance() {
            return instance;
        }
    
        private ArrayList<Integer> numbers = new ArrayList<>();
        private HashSet<String> names = new HashSet<>();
        private HashMap<String, Integer> studentScores = new HashMap<>();
    
        public void addNumber(int number) {
            numbers.add(number);
        }
    
        public void sortNumbers() {
            Collections.sort(numbers);
        }
    
        public void addName(String name) {
            names.add(name);
        }
    
        public void addStudentScore(String name, int score) {
            studentScores.put(name, score);
        }
    
        public void displayCollections() {
            System.out.println("ArrayList: " + numbers);
            System.out.println("Sorted ArrayList: " + numbers);
            System.out.println("HashSet: " + names);
            System.out.println("HashMap: " + studentScores);
        }
    
        public static void main(String[] args) {
            Singleton single = Singleton.getInstance();
    
            single.addNumber(5);
            single.addNumber(3);
            single.addNumber(8);
            single.addNumber(1);
            single.addNumber(6);
            single.sortNumbers();
            single.addName("Kishore");
            single.addName("Velumuragan");
            single.addName("Anup");
            single.addName("Amsathk");
            single.addStudentScore("Kishore", 95);
            single.addStudentScore("Velumuragan", 92);
            single.addStudentScore("Anup", 78);
            single.addStudentScore("Amsathk", 90);
            single.displayCollections();
        }
    } 
