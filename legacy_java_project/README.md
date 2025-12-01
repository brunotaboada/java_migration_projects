# Hello World Legacy Java Project

A simple Hello World application demonstrating basic Java functionality. This is a legacy Java project that can be built and run using either Maven or directly with javac/java commands.

## Project Structure

```
legacy_java_project/
├── pom.xml                          # Maven build configuration
├── README.md                        # This file
└── src/
    └── main/
        └── java/
            └── com/
                └── example/
                    └── HelloWorld.java  # Main application file
```

## Requirements

- Java Development Kit (JDK) 8 or higher
- Maven 3.x (optional, for Maven builds)
- Compatible operating system (Windows, macOS, Linux)

## Quick Start

### Option 1: Using Maven (Recommended)

1. **Compile the project:**
   ```bash
   mvn clean compile
   ```

2. **Run the application:**
   ```bash
   mvn exec:java
   ```
   Or using the specific goal:
   ```bash
   mvn exec:java -Dexec.mainClass="com.example.HelloWorld"
   ```

3. **Build JAR file:**
   ```bash
   mvn clean package
   ```
   The JAR file will be created in the `target/` directory.

4. **Run the JAR file:**
   ```bash
   java -jar target/hello-world-legacy-1.0.0.jar
   ```

### Option 2: Using javac/java Commands

1. **Navigate to the project directory:**
   ```bash
   cd legacy_java_project
   ```

2. **Compile the Java source file:**
   ```bash
   javac src/main/java/com/example/HelloWorld.java
   ```

3. **Run the compiled class:**
   ```bash
   java -cp src/main/java com.example.HelloWorld
   ```

## Expected Output

When you run the application, you should see output similar to:

```
Hello, World!
Welcome to the Java Hello World application!

System Information:
Java Version: [your-java-version]
Operating System: [your-os]
User: [your-username]

=== Basic Functionality Demo ===
Hello, Java World!
Supported languages: Java Python JavaScript C++ 
Calculation: 10 + 20 = 30

Application completed successfully!
```

## Features

- **Basic Java Syntax**: Demonstrates classes, methods, and basic programming constructs
- **System Information**: Displays Java version and system properties
- **Array Operations**: Shows iteration through arrays
- **String Concatenation**: Demonstrates string operations
- **Basic Calculations**: Simple arithmetic operations
- **Legacy Code Style**: Follows traditional Java coding patterns

## Build Configuration

The project uses Maven for build management with the following key features:

- **Java Version**: Configured for Java 8 compatibility
- **Compiler Plugin**: Maven Compiler Plugin for compilation
- **Exec Plugin**: For running the application directly
- **Surefire Plugin**: For future test execution

## Troubleshooting

### Common Issues:

1. **"javac" is not recognized**: Ensure Java JDK is installed and javac is in your PATH
2. **"java" is not recognized**: Ensure JRE is installed and java is in your PATH
3. **"mvn" is not recognized**: Install Maven or use direct javac/java commands
4. **Compilation errors**: Check that your Java version matches the configured version in pom.xml

### Verify Java Installation:
```bash
java -version
javac -version
```

### Verify Maven Installation:
```bash
mvn -version
```

## Development

### Adding New Features:
1. Modify the `HelloWorld.java` file
2. Add new methods to demonstrate additional Java features
3. Recompile and test using the commands above

### Adding Tests:
1. Create test files in `src/test/java/`
2. Use JUnit or other testing frameworks
3. Run tests with: `mvn test`

## Legacy Project Notes

This is designed as a legacy Java project to demonstrate:
- Traditional Java project structure
- Basic Maven configuration
- Simple application development
- Common Java programming patterns

The code follows legacy Java conventions and can serve as a starting point for learning Java or understanding traditional Java project structures.

## License

This is a demonstration project for educational purposes.