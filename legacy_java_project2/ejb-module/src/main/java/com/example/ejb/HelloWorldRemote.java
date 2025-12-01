package com.example.ejb;

import javax.ejb.Remote;

@Remote
public interface HelloWorldRemote {
    String sayHello(String name);
}