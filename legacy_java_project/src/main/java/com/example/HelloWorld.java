package com.example;

/**
 * A simple Hello World application in Java.
 * This is a legacy Java project demonstrating basic functionality.
 */
public class HelloWorld {
    
    /**
     * Main method - entry point of the application
     * @param args command line arguments
     */
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        System.out.println("Welcome to the Java Hello World application!");
        
        // Display some system information
        System.out.println("\nSystem Information:");
        System.out.println("Java Version: " + System.getProperty("java.version"));
        System.out.println("Operating System: " + System.getProperty("os.name"));
        System.out.println("User: " + System.getProperty("user.name"));
        
        // Demonstrate basic functionality
        demonstrateBasicFunctionality();
    }
    
    /**
     * Demonstrates basic Java functionality
     */
    private static void demonstrateBasicFunctionality() {
        System.out.println("\n=== Basic Functionality Demo ===");
        
        // Variables and data types
        String greeting = "Hello";
        String target = "Java World";
        String message = greeting + ", " + target + "!";
        System.out.println(message);
        
        // Arrays
        String[] languages = {"Java", "Python", "JavaScript", "C++"};
        System.out.print("Supported languages: ");
        for (String lang : languages) {
            System.out.print(lang + " ");
        }
        System.out.println();
        
        // Simple calculation
        int a = 10;
        int b = 20;
        int sum = a + b;
        System.out.println("Calculation: " + a + " + " + b + " = " + sum);
        
        System.out.println("\nApplication completed successfully!");
    }
}