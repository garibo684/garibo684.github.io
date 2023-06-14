---
layout: post
title: CMake Tutorial and Disqus
tags: learning CMake site
categories: internship
---

## Disqus

  Today setting Disqus comments for posts was a 10-minute job. While I was 
looking through the [jekyll/minima][minima-gh] page, part about the Disqus
comment section caught my eye. After three lines of code and a pull request,
it was done; as you can also see at the bottom of the page right now.

## CMake Tutorial

  For some time I was looking at CMake tutorial videos. At the start of this
week I decided it would be better and faster to use [CMake's official tutorial][cmake-tut]. 
It was an interactive tutorial in which you were given a folder with the files
that had necessary code templates. Through the instructions from the official
tutorial site, one was expected to write the necessary code parts.
    
  This tutorial has twelve steps from start to completion. Throughout this
twelve steps one would learn everything from how to make a basic CMake 
project to adding libraries to your projects to packaging and installing
your CMake projects.

  While completing this tutorial the thing I was most intrigued about was
[Step 6: Adding Support for a Testing Dashboard][cmake-tut-6]. The reason for
this was that using CTest for testing my code was already very interesting
to me. Submitting this test's results to CDash and seeing these results
and the results from other people, who were doing this part of the tutorial
as well, was really interesting.

![CDash Test Results](/assets/images/CDash_test.png)


[minima-gh]: https://github.com/jekyll/minima
[cmake-tut]: https://cmake.org/cmake/help/latest/guide/tutorial/index.html
[cmake-tut-6]: https://cmake.org/cmake/help/latest/guide/tutorial/Adding%20Support%20for%20a%20Testing%20Dashboard.html
