package com.fss;

import java.util.Arrays;
import java.util.Collections;

public class ArrayManipulation {
    
public static void arrays(){
    int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    System.out.println("Array elements:");
    for (int number : numbers) {
        System.out.print(number + " ");
    }
}
public static void MaxMin(){
    int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int largest = numbers[0];
    int smallest = numbers[0];
    for (int i = 1; i < numbers.length; i++) {
        if (numbers[i] > largest) {
            largest = numbers[i];
        }
        if (numbers[i] < smallest) {
            smallest = numbers[i];
        }
    }
    System.out.println("Largest element: " + largest);
    System.out.println("Smallest element: " + smallest);
}
public static void ReverseArray(){
    Integer[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        Collections.reverse(Arrays.asList(numbers));
        System.out.println("Reversed array:");
        for (int number : numbers) {
            System.out.print(number + " ");
        }
    }
    public static void SumAvg(){
        int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        double average = (double) sum / numbers.length;
        System.out.println("Sum of all elements: " + sum);
        System.out.println("Average of all elements: " + average);
    }


    public static void main(String[] args) {
    arrays();
    MaxMin();
    ReverseArray();
    SumAvg();
}
}


