package com.example.ejb;

import javax.ejb.Stateless;

@Stateless
public class HelloWorldBean implements HelloWorldRemote {
    
    @Override
    public String sayHello(String name) {
        return "Hello, " + name + "!";
    }
}