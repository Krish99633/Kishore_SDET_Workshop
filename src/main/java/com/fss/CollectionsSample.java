package com.fss;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;

public class CollectionsSample {

    public static void main(String[] args) {
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers.add(5);
        numbers.add(3);
        numbers.add(8);
        numbers.add(1);
        numbers.add(6);
        System.out.println("ArrayList: " + numbers);
        Collections.sort(numbers);
        System.out.println("Sorted ArrayList: " + numbers);

        HashSet<String> names = new HashSet<>();
        names.add("Kishore");
        names.add("Velumuragan");
        names.add("Anup");
        names.add("Amsathkhan");
        System.out.println("HashSet: " + names);

        HashMap<String, Integer> studentScores = new HashMap<>();
        studentScores.put("Kishore", 95);
        studentScores.put("Velumuragan", 92);
        studentScores.put("Anup", 78);
        studentScores.put("Amsathkhan", 90);
        System.out.println("HashMap: " + studentScores);
    }
}

