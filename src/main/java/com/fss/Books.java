package com.fss;

public class Books {
    public String title;
    public String author;
    public double price;


    public Books(String title, String author, double price) {
        this.title = title;
        this.author = author;
        this.price = price;
    }

    public void displayDetails() {
        System.out.println("Book Details:");
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Price: RS/-" + price);
    }

    public static void main(String[] args) {
   
        Books myBook = new Books("The Atomic Habits", "F. Scott Fitzgerald", 890);
        myBook.displayDetails();
    }
}
