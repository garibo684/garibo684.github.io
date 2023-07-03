---
layout: post
title: Using It All Together
tags: learning Conan CMake
categories: internship
---

## Making Little Projects

  After 3 weeks I learned Conan and CMake on a basic level and started to
use them in simple projects. I was trying to reinforce my CMake by using it
in a little project and I did make some progress along the way. When I learned 
Conan as well I tried to use them both in one project. The first one I tried was 
more of a clone of [this project.][cmake-exemp] Using CMake to build and connect
libraries. With this I was able to give the apps and other libraries access
through the libraries' public interface. In a way, I was able to connect these without
binding them so when I change a library it doesn't affect the connected ones as long 
as the function of the library still works whatever way it is. In this project I used 
Conan in a simple way, managing the GTest package for testing the code.

## My Little Project

  I started making a Library for my little project using CMake and Conan
  mostly in the same way I used on the clone of [this project.][cmake-exemp] Using
  Book and Borrower classes for keeping info and transferring them. Then
  made a Library class for the main functions of the project like adding
  books, borrowing them, checking if someone has access to the book they try
  to borrow and so on. Afterward, I used CMake to make this classes CMake
  libraries and connect them to the main app file. I couldn't finish
  this project yet because of some technical problems I encountered at the
  start and the weeklong holiday afterward. As the holiday comes to an end I am
  refocused on it and plan to finish it soon.


[cmake-exemp]: https://github.com/gokhanettin/cmake-example
