---
layout: post
title: Learning Docker and Vagrant
tags: learning
categories: internship
---

## Docker and Vagrant: Simplifying Development Environments

  In the world of software development, creating a stable and consistent
environment for your applications to run is crucial. Two powerful tools that
have revolutionized the way developers manage their development environments are
[Docker][docker] and [Vagrant][vagrant].

### Docker: Containerize Your Applications

  Docker allows you to package your application and all its dependencies into a
single, lightweight unit called a "container." Think of a container as a
self-contained environment that includes everything your application needs to
run: the code, libraries, and configurations.

  What makes Docker so appealing is its portability. Once you've created a
Docker container, you can run it on any system that supports Docker, be it your
local development machine, a test server, or even in the cloud. This ensures
that your application behaves the same way in every environment.

  Docker also simplifies the process of scaling your applications. You can
easily spin up multiple containers, distribute the load, and manage them
efficiently. This makes Docker an ideal choice for deploying and managing
microservices-based architectures.

### Vagrant: Create Reproducible Development Environments

  Imagine having a magic wand that can conjure up identical development
environments for your entire team with just a few commands. That's precisely
what Vagrant does.

  Vagrant is a tool for creating and managing virtualized development
environments. It lets you define your development environment as code using a
configuration file. This configuration file can specify the operating system,
software packages, and settings needed for your project. When you and your team
members run Vagrant, it automatically provisions virtual machines based on this
configuration, ensuring everyone has the same environment.

  Vagrant supports various virtualization providers like VirtualBox, VMware, and
even cloud platforms like AWS. This flexibility allows you to choose the
environment that best suits your project's needs.

  With Vagrant, everyone on your team can work in a consistent environment,
making collaboration and troubleshooting much easier.

## My Experience With Them
  
  Because I mostly used Docker software I will mostly talk about it. I started
by reading both software's tutorial pages and watching a few tutorial videos I
found on YouTube. Afterward, I installed Docker on both my Linux and Windows
systems. From this point, I created a docker image that uses ubuntu:22.04 by
creating a Dockerfile and using FROM command. In this Dockerfile by using RUN
command I make the image install needed software like CMake, Python, Conan, and
googletest. Then with COPY command, I copied some of my earlier projects into it.

 ```dockerfile
FROM ubuntu:22.04

# essentials
RUN \
    apt-get update && \
    apt-get install -y build-essential cmake git

# googletest
RUN git clone https://github.com/google/googletest
RUN mkdir -p googletest/build && cd googletest/build
WORKDIR "googletest/build"
RUN cmake -DCMAKE_CXX_FLAGS=-std=c++1z -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON ../ && make -j8 all install
WORKDIR "/"

# conan 
RUN apt-get install -y python3 && apt-get install -y python3-pip
RUN pip install conan 

COPY currency-converter /Projects/currency-converter
COPY Calculator /Projects/Calculator
```

  Next, I used the terminal to create a docker image based on this Dockerfile
and created a docker container using the image. After connecting to this
container as an interactive virtual machine, I built and ran the projects I
copied using the image. By using the VS Code's Docker extension I connected the
container to my Visual Studio and managed to control the files in the container
from there.

![Docker VSCode Container](/assets/images/Docker_test.png)

  I used these steps both on Linux and Windows separately and got the same
results. By using Docker or Vagrant I managed to work on my projects in my
Windows computer which does not have any needed software other than docker
itself. 


## Conclusion

  In conclusion, Docker and Vagrant are two essential tools for developers
seeking to streamline their development workflows and ensure consistent,
reproducible environments. Docker simplifies packaging and deploying
applications, while Vagrant makes it effortless to create and share development
environments. Incorporating these tools into your development toolbox can lead
to smoother, more efficient software development processes and fewer headaches
down the road.

[docker]: https://www.docker.com/
[vagrant]: https://www.vagrantup.com/
