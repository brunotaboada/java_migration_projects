# Legacy Java EE Project - EJB, WAR, and EAR

A complete legacy Java Enterprise Edition application demonstrating the traditional three-tier architecture with EJB, WAR, and EAR modules.

## 🏗️ Project Architecture

This project demonstrates a classic Java EE enterprise application structure:

```
legacy_java_project2/
├── pom.xml                          # Parent POM
├── ejb-module/                      # Enterprise Java Bean module
│   ├── pom.xml                      # EJB module configuration
│   └── src/main/java/com/example/ejb/
│       ├── HelloWorldRemote.java    # Remote interface
│       └── HelloWorldBean.java      # Stateless session bean
├── war-module/                      # Web Archive module
│   ├── pom.xml                      # WAR module configuration
│   └── src/main/webapp/
│       ├── WEB-INF/
│       │   └── web.xml              # Web deployment descriptor
│       ├── index.jsp                # Main JSP page
│       ├── error.jsp                # Error handling page
│       └── css/style.css            # Application styles
├── ear-module/                      # Enterprise Archive module
    ├── pom.xml                      # EAR module configuration
    └── src/main/application/META-INF/
        └── application.xml          # Application deployment descriptor
```

## 🎯 Features

- **EJB Module**: Stateless session bean with business logic
- **WAR Module**: Servlets, JSP, and web resources
- **EAR Module**: Enterprise Archive packaging
- **Deployment Descriptors**: Complete XML configuration files
- **Error Handling**: Custom error pages and exception handling
- **Session Management**: HTTP session tracking
- **Responsive Web Interface**: Modern CSS styling

## 📋 Prerequisites

Before building this project, ensure you have:

- **Java 8** or higher
- **Maven 3.6** or higher
- **Java EE Application Server** (one of):
  - WildFly 8.x or higher
  - JBoss EAP 6.x or higher
  - WebLogic 12c
  - GlassFish 4.x

## 🚀 Build Instructions

### 1. Clean and Build All Modules

```bash
# Navigate to project root
cd legacy_java_project2

# Build all modules from root
mvn clean install
```

This will:
- Compile all Java source files
- Package EJB module as `ejb-module.jar`
- Package WAR module as `war-module.war`
- Package EAR module as `HelloWorld-Legacy-Application.ear`

### 2. Build Individual Modules

```bash
# Build only EJB module
cd ejb-module
mvn clean package

# Build only WAR module
cd ../war-module
mvn clean package

# Build only EAR module
cd ../ear-module
mvn clean package
```

### 3. Build with Specific Profiles

```bash
# Production build
mvn clean install -Pproduction

# Development build with debug info
mvn clean install -Pdevelopment
```

## 🐳 Deployment Instructions

### Option 1: Deploy via Admin Console

1. **Start your Java EE application server**
2. **Access the admin console** (e.g., `http://localhost:9990` for WildFly)
3. **Navigate to Deployments section**
4. **Upload and deploy** `ear-module/target/HelloWorld-Legacy-Application.ear`
5. **Verify deployment** in the server logs

### Option 2: Deploy via Command Line

#### WildFly/JBoss EAP
```bash
# Copy EAR to deployment directory
cp ear-module/target/HelloWorld-Legacy-Application.ear $JBOSS_HOME/standalone/deployments/

# Or use CLI
$JBOSS_HOME/bin/jboss-cli.sh --connect command="deploy ear-module/target/HelloWorld-Legacy-Application.ear"
```

#### WebLogic
```bash
# Deploy using WLST (WebLogic Scripting Tool)
$WEBLOGIC_HOME/wlserver/common/bin/wlst.sh
> connect('weblogic','password','t3://localhost:7001')
> deploy('HelloWorld-EAR','path/to/HelloWorld-Legacy-Application.ear')
```

#### GlassFish
```bash
# Deploy using asadmin
asadmin deploy ear-module/target/HelloWorld-Legacy-Application.ear
```

### Option 3: Maven Plugin Deployment

#### WildFly Maven Plugin
Add to parent pom.xml:
```xml
<plugin>
    <groupId>org.wildfly.plugins</groupId>
    <artifactId>wildfly-maven-plugin</artifactId>
    <version>2.0.0.Final</version>
    <configuration>
        <filename>HelloWorld-Legacy-Application.ear</filename>
    </configuration>
</plugin>
```

Then deploy:
```bash
mvn wildfly:deploy-only -pl ear-module
```

## 🧪 Testing the Application

### 1. Access the Application

After deployment, access the application at:
```
http://localhost:8080/hello-world/
```

### 2. Test EJB Services

The web interface provides several test functions:

- **🎉 Simple Hello**: Basic hello world message
- **👤 Personalized Hello**: Custom greeting with name input
- **⏰ Server Time**: Current server timestamp
- **📊 EJB Statistics**: Detailed bean statistics and information

### 3. Verify EJB Injection

Check server logs for EJB lifecycle messages:
```
INFO  [HelloWorldBean] HelloWorldBean initialized at: 2025-11-20 13:55:30
```

### 4. Session Tracking

Monitor session information in the web interface:
- Total request count
- Last action performed
- Session ID tracking

## 🔧 Configuration

### Server Configuration

#### WildFly Example (standalone.xml)
```xml
<subsystem xmlns="urn:jboss:domain:ejb3:4.0">
    <session-bean name="HelloWorldEJB" 
                  stateful="false" 
                  stateless-pool-size="10"/>
</subsystem>

<subsystem xmlns="urn:jboss:domain:undertow:4.0">
    <server name="default-server">
        <host name="default-host" alias="localhost">
            <location name="/hello-world" 
                     handler="welcome-content"/>
        </host>
    </server>
</subsystem>
```

#### Security Configuration
```xml
<security-domain name="hello-world-domain" 
                 cache-type="default">
    <authentication>
        <login-module code="Database" flag="required">
            <module-option name="dsJndiName" value="java:jboss/datasources/ExampleDS"/>
        </login-module>
    </authentication>
</security-domain>
```

## 🛠️ Troubleshooting

### Common Issues

#### 1. EJB Injection Failure
**Problem**: `helloWorldEJB` is null in servlet
**Solution**: 
- Ensure EAR deployment is successful
- Check JNDI lookup configuration
- Verify EJB module is packaged correctly

#### 2. 404 Error on Access
**Problem**: Application not accessible
**Solution**:
- Verify context root in `application.xml`
- Check web.xml servlet mappings
- Ensure WAR module is included in EAR

#### 3. ClassNotFoundException
**Problem**: Missing classes at runtime
**Solution**:
- Verify all modules are included in EAR
- Check dependency scope in POM files
- Ensure proper EJB API scope (provided)

#### 4. Maven Build Failure
**Problem**: Compilation errors
**Solution**:
```bash
# Clean and retry
mvn clean install -X  # Debug mode
# Check Java version
java -version
# Check Maven version  
mvn -version
```

### Debug Mode

Enable debug logging in server:
```xml
<!-- Add to server configuration -->
<logger category="com.example.ejb" level="DEBUG"/>
<logger category="com.example.web" level="DEBUG"/>
```

### Testing EJB Remotely

Create a standalone client:
```java
import javax.naming.Context;
import javax.naming.InitialContext;
import com.example.ejb.HelloWorldRemote;

public class EJBClient {
    public static void main(String[] args) throws Exception {
        Context ctx = new InitialContext();
        HelloWorldRemote hello = (HelloWorldRemote) ctx.lookup("ejb:/ejb-module/HelloWorldEJB!com.example.ejb.HelloWorldRemote");
        System.out.println(hello.getHelloMessage());
    }
}
```

## 📚 Project Structure Details

### EJB Module (`ejb-module/`)
- **HelloWorldRemote.java**: Remote interface defining business methods
- **HelloWorldBean.java**: Stateless session bean implementation
- **ejb-jar.xml**: EJB deployment descriptor

### WAR Module (`war-module/`)
- **HelloWorldServlet.java**: Main servlet handling HTTP requests
- **index.jsp**: User interface JSP
- **error.jsp**: Error handling page
- **web.xml**: Web application deployment descriptor
- **css/style.css**: Responsive styling

### EAR Module (`ear-module/`)
- **application.xml**: Enterprise application descriptor
- **pom.xml**: EAR packaging configuration

## 🔄 Development Workflow

1. **Develop EJB Business Logic** in `ejb-module`
2. **Create Web Interface** in `war-module`
3. **Package in EAR** using `ear-module`
4. **Deploy to Application Server**
5. **Test and Debug**
6. **Iterate and Improve**

## 📝 Development Notes

- Uses Java EE 7 APIs (servlet 3.1, EJB 3.2, JSP 2.2)
- Compatible with Java 8+ runtime
- Stateless session bean pattern for scalability
- Remote interface for EJB access
- Responsive web design with modern CSS
- Session management and error handling

## 🎓 Learning Objectives

This project demonstrates:

1. **Enterprise Java Bean (EJB) Development**
   - Stateless session beans
   - Remote interfaces
   - Dependency injection
   - Lifecycle callbacks

2. **Web Application Development**
   - Servlet programming
   - JSP technology
   - Session management
   - Error handling

3. **Enterprise Application Packaging**
   - EAR structure
   - Module dependencies
   - Deployment descriptors
   - Enterprise deployment

4. **Legacy Java EE Patterns**
   - Traditional three-tier architecture
   - JNDI lookups
   - Container-managed transactions
   - Security role-based access

---

**Built with**: Java 8 | Maven 3.6+ | Java EE 7 | EJB 3.2 | Servlet 3.1 | JSP 2.2

**Deployment Target**: WildFly, JBoss EAP, WebLogic, GlassFish