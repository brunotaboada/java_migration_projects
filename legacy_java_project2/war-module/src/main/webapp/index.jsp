<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.util.List" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Legacy Java EE - Hello World Application</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>Legacy Java EE Application</h1>
            <p>Hello World EJB + WAR + EAR Demo</p>
        </header>
        
        <section class="ejb-info">
            <h2>Application Architecture</h2>
            <div class="architecture">
                <div class="component">
                    <h3>🏗️ EAR Module</h3>
                    <p>Enterprise Archive - Contains and packages both EJB and WAR modules</p>
                </div>
                <div class="component">
                    <h3>⚡ EJB Module</h3>
                    <p>Enterprise Java Bean - Stateless session bean providing business logic</p>
                </div>
                <div class="component">
                    <h3>🌐 WAR Module</h3>
                    <p>Web Archive - Servlets and JSP providing HTTP interface</p>
                </div>
            </div>
        </section>
        
        <section class="action-panel">
            <h2>EJB Service Actions</h2>
            <div class="buttons">
                <form method="get" action="HelloWorldServlet" style="display: inline;">
                    <input type="hidden" name="action" value="hello">
                    <button type="submit" class="btn btn-primary">🎉 Simple Hello</button>
                </form>
                
                <form method="post" action="HelloWorldServlet" style="display: inline;">
                    <input type="hidden" name="action" value="personalized">
                    <input type="text" name="name" placeholder="Enter your name" class="input-field">
                    <button type="submit" class="btn btn-success">👤 Personalized Hello</button>
                </form>
                
                <form method="get" action="HelloWorldServlet" style="display: inline;">
                    <input type="hidden" name="action" value="time">
                    <button type="submit" class="btn btn-info">⏰ Server Time</button>
                </form>
                
                <form method="get" action="HelloWorldServlet" style="display: inline;">
                    <input type="hidden" name="action" value="stats">
                    <button type="submit" class="btn btn-warning">📊 EJB Statistics</button>
                </form>
            </div>
        </section>
        
        <section class="result-panel">
            <h2>Service Response</h2>
            <%
            String error = (String) request.getAttribute("error");
            String result = (String) request.getAttribute("result");
            String messageType = (String) request.getAttribute("messageType");
            String action = (String) request.getAttribute("action");
            
            if (error != null) {
            %>
                <div class="error-message">
                    <strong>❌ Error:</strong> <%= error %>
                </div>
            <%
            } else if (result != null) {
                String cssClass = "result-message";
                if ("error".equals(messageType)) cssClass = "error-message";
                else if ("statistics".equals(messageType)) cssClass = "statistics-message";
                else if ("info".equals(messageType)) cssClass = "info-message";
            %>
                <div class="<%= cssClass %>">
                    <h3>📡 Action: <%= action != null ? action : "hello" %></h3>
                    <pre><%= result %></pre>
                </div>
            <%
            } else {
            %>
                <div class="welcome-message">
                    <h3>👋 Welcome to Legacy Java EE!</h3>
                    <p>Click any button above to invoke EJB services through this WAR application.</p>
                </div>
            <%
            }
            %>
        </section>
        
        <section class="session-info">
            <h2>Session Information</h2>
            <%
            HttpSession session = request.getSession();
            Integer totalRequests = (Integer) session.getAttribute("totalRequests");
            String lastAction = (String) session.getAttribute("lastAction");
            %>
            <div class="session-stats">
                <div class="stat">
                    <span class="label">Total Requests:</span>
                    <span class="value"><%= totalRequests != null ? totalRequests : 0 %></span>
                </div>
                <div class="stat">
                    <span class="label">Last Action:</span>
                    <span class="value"><%= lastAction != null ? lastAction : "None" %></span>
                </div>
                <div class="stat">
                    <span class="label">Session ID:</span>
                    <span class="value"><%= session.getId() %></span>
                </div>
            </div>
        </section>
        
        <footer>
            <p>Legacy Java EE Application - EJB 3.2, WAR, EAR</p>
            <p>Built with Maven | Java 8 | Servlets | JSP</p>
        </footer>
    </div>
</body>
</html>