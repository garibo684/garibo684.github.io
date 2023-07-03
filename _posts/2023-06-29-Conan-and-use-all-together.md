---
layout: post
title: Conan and Using All Together
tags: learning Conan CMake
categories: internship
---

## Making Little Projects

  After 3 weeks I learned Conan and CMake on a basic level and started to use them in simple project. 
I was trying to reinforce my CMake by using it in little project and I did make some progress.
When I learned Conan as well I tried to use them both in one project. First one I tried this was more of a
clone of [this project.][cmake-exemp] Using CMake to build and connect libraries. With this I was able to
give the apps and other libraries access through the libraries' public interface. In a way thorough this i 
was able to connect these without binding them so when I change a library it doesnt effect the connevted ones
as long as the function of thhe library still works whatever way it is. In this project I used conan in a simple 
way, managing GTest package for testing the code.

## My Little Project

  I started making a Library for my little project using CMake and Conan mostly in the same way I used on the [this project.][cmake-exemp]
  Using Book and Borrower classes for keeping info and transferring them. Than made a Library class for the main functions of the project like
  adding books borrowing them checking if someane has access to the book they try to borrow and so on. Afterward I used CMake to make this
  classes CMake libraries and connecting them to the main app file. I could'nt finished this project yet because of some technical promlems I
  encountered at the start and the weeklong holiday afterwards. As holiday comes to an end I am refocused on it and plan to finish it soon.


[cmake-exemp]: https://github.com/gokhanettin/cmake-example