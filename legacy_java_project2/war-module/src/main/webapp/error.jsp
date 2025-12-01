<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.io.StringWriter" %>
<%@ page isErrorPage="true" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error - Legacy Java EE Application</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .error-container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 10px;
            padding: 40px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            width: 100%;
            text-align: center;
        }
        
        .error-icon {
            font-size: 4em;
            color: #e74c3c;
            margin-bottom: 20px;
        }
        
        h1 {
            color: #2c3e50;
            margin-bottom: 20px;
        }
        
        .error-details {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
            text-align: left;
            border-left: 4px solid #e74c3c;
        }
        
        .back-button {
            background: #3498db;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 6px;
            text-decoration: none;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .back-button:hover {
            background: #2980b9;
            transform: translateY(-2px);
        }
        
        .exception-info {
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            border-radius: 8px;
            padding: 15px;
            margin: 15px 0;
            color: #856404;
        }
    </style>
</head>
<body>
    <div class="error-container">
        <div class="error-icon">🚫</div>
        <h1>Oops! Something went wrong</h1>
        <p>The Legacy Java EE application encountered an unexpected error.</p>
        
        <div class="exception-info">
            <strong>Error Type:</strong> <%= exception != null ? exception.getClass().getSimpleName() : "Unknown Error" %><br>
            <strong>Error Message:</strong> <%= exception != null ? exception.getMessage() : "An unexpected error occurred" %>
        </div>
        
        <div class="error-details">
            <h3>🔍 Error Details</h3>
            <p><strong>Request Information:</strong></p>
            <ul>
                <li><strong>Request URI:</strong> <%= request.getRequestURI() %></li>
                <li><strong>Request Method:</strong> <%= request.getMethod() %></li>
                <li><strong>Query String:</strong> <%= request.getQueryString() != null ? request.getQueryString() : "None" %></li>
                <li><strong>Session ID:</strong> <%= session.getId() %></li>
            </ul>
        </div>
        
        <div style="margin-top: 30px;">
            <a href="index.jsp" class="back-button">🏠 Return to Home</a>
        </div>
        
        <div style="margin-top: 20px; font-size: 0.9em; color: #7f8c8d;">
            <p>Legacy Java EE Application | EJB 3.2 + WAR + EAR</p>
            <p>If this problem persists, please contact the system administrator.</p>
        </div>
    </div>
</body>
</html>