---
layout: post
title: Lock-Free Queue
tags: queue
categories: internship
---

## What Is A Lock-Free Queue

  A lock-free queue is a data structure used in concurrent programming to enable
multiple threads or processes to add or remove elements from the queue without
explicit locking mechanisms. The key characteristic of a lock-free queue is that
it allows progress for at least one thread or process even in the presence of
contention (when multiple threads are trying to access the queue
simultaneously).

  A lock-free queue typically employs atomic operations and memory
synchronization techniques to maintain the consistency of the queue while
allowing concurrent access. These atomic operations ensure that modifications to
the data structure are performed in an atomic and non-blocking manner.
Consequently, threads can make progress independently without waiting for other
threads to release a lock.

## Declerations

  In the header file, I have created a LockFreeQueue class template. I declared a
Node struct with atomic<Node*> next_ to point the next node in the queue and
shared_ptr<T> data_ to hold the value data of a node. Afterward, I declared
atomic<Node*> head_ and tail_ as private members to point to either end of
the queue. Lastly, declared Push and Pop functions as public members to add and
remove nodes from the queue in a First In First Out (FIFO) manner.

```cpp
#ifndef LOCKFREEQUEUE_LOCKFREEQUEUE_H
#define LOCKFREEQUEUE_LOCKFREEQUEUE_H

#include <atomic>
#include <memory>

template <typename T>
class LockFreeQueue {
 private:
   struct Node {
     std::shared_ptr<T> data_;
     std::atomic<Node*> next_;
     Node(const T& data) : data_(std::make_shared<T>(data)), next_(nullptr) {}
   };
   std::atomic<Node*> head_;
   std::atomic<Node*> tail_;

 public:
   LockFreeQueue();
   LockFreeQueue(const LockFreeQueue& other) = delete;
   LockFreeQueue& operator=(const LockFreeQueue& other) = delete;

   ~LockFreeQueue();

   void push(const T& data);

   std::shared_ptr<T> pop();
};
#endif
```

## Deinitions

#### Push Function

```cpp
template <typename T>
void LockFreeQueue<T>::push(const T& data) {
  std::unique_ptr<Node> new_node(new Node(data));
  Node* new_tail = new_node.get();
  Node* old_tail = tail_.load();
  Node* null_ptr = nullptr;

  while (head_.load() == nullptr && tail_.load() == nullptr) {
    tail_.compare_exchange_weak(null_ptr, new_tail);
    head_.compare_exchange_weak(null_ptr, new_tail);
  }

  while (true) {
    if (tail_.compare_exchange_weak(old_tail, new_tail)) {
      old_tail->next_.store(new_tail);
      break;
    }
    old_tail = tail_.load();
  }

  new_node.release();
}
```
This code implements a lock-free queue data structure's push operation. It adds
a new element to the end of the queue using atomic compare-and-exchange (CAS)
operations for synchronization. The queue consists of nodes, each holding an
element of type T.

Explanation:

- Create a new_node with the given data and obtain a pointer to it (new_tail).

- Load the current tail node (old_tail) using an atomic operation.

- Initialize a null pointer (null_ptr) for comparison purposes.

- The first while loop is designed to handle the case when the queue is
initially empty (both head and tail are nullptr). It tries to atomically set
both head and tail to the new node if they are both nullptr. This helps in
initializing the queue with the first node.

- The second while loop continues until the new node is successfully added to
the tail of the queue. It uses CAS to attempt to update the tail pointer (tail_)
to the new node (new_tail). If the CAS fails (indicating a concurrent
modification of the tail), it reloads the current tail value (old_tail) and
retries the CAS.

- Finally, the new node's ownership is transferred to the queue by releasing it,
ensuring it is now part of the queue and won't be deallocated prematurely.

Overall, this code aims to implement a lock-free push operation for a concurrent
queue, allowing multiple threads to add elements to the queue without explicit
locks, improving concurrency and performance in concurrent applications.

#### Pop Function

```cpp
template <typename T>
std::shared_ptr<T> LockFreeQueue<T>::pop() {
  while (true) {
    if (head_.load() != nullptr) {
      Node* old_head = head_.load();

      if (old_head->next_ != nullptr) {
        Node* next_node = old_head->next_.load();

        if (head_.compare_exchange_weak(old_head, next_node)) {
          std::shared_ptr<T> res(old_head->data_);
          delete old_head;
          return res;
        }
        old_head = head_.load();

      } else {
          if (head_.compare_exchange_weak(old_head, nullptr)) {
            tail_.compare_exchange_weak(old_head, nullptr);
            std::shared_ptr<T> res(old_head->data_);
            delete old_head;
            return res;
          }
          old_head = head_.load();
      }

    } else { return std::shared_ptr<T>(); }
  }
}
```
This code implements a lock-free queue data structure's pop operation. It
removes the front element from the queue using atomic compare-and-exchange (CAS)
operations for synchronization. The queue consists of nodes, each holding an
element of type T.

Explanation:

- The function enters an infinite loop, which keeps trying to pop an element
  from the queue until it succeeds.

- If the head of the queue (head_) is not nullptr (indicating that the queue is
  not empty), it enters the first branch.

- It loads the current head node (old_head) using an atomic operation.

- If the old_head has a non-null next node (next_node), it means there is more
  than one element in the queue. It attempts to atomically update the head
  pointer (head_) to the next node (next_node) using CAS. If the CAS succeeds,
  it means the head has been updated, and the function returns the data from the
  old_head as a shared_ptr, deallocates the old_head node, and exits the loop.

- If the CAS fails, it means another thread has already modified the head. The
  code reloads the current head value (old_head) and repeats the process from
  step 2.

- If the old_head's next_ pointer is nullptr, it means there is only one element
  left in the queue. It tries to atomically update both head_ and tail_ pointers
  to nullptr, effectively emptying the queue. If the CAS succeeds, it returns
  the data from the old_head node as a shared_ptr, deallocates the old_head
  node, and exits the loop.

- If the CAS fails, it means another thread has modified either the head or the
  tail. The code reloads the current head value (old_head) and repeats the
  process from step 2.

- If the head of the queue (head_) is nullptr (indicating an empty queue), it
  directly returns an empty shared_ptr.

Overall, this code aims to implement a lock-free pop operation for a concurrent
queue, allowing multiple threads to remove elements from the queue without
explicit locks, improving concurrency and performance in concurrent
applications. However, it's important to note that this implementation assumes
proper memory management and safety in deallocating nodes and handling
shared_ptr usage in a concurrent environment.

## Main()

 In this file by creating I create a Producer and a Consumer function to add
three nodes and remove four from the queue using Push and Pop functions. These
functions also give written output to let us see if they are working properly.
Afterward inside the main() I created two std::thread to simulate producer and
consumer behavior as well as a queue that holds integer data. These threads run
the Producer and Consumer functions with the integer holding queue as a
reference. After building and running this code we get this output:

```cpp
**Produced: 1
**Produced: 2
**Produced: 3
--Received: 1
--Received: 2
--Received: 3
==Queue is empty
```

## Testing

And lastly, I have used GTest to test this code. In the first test, I created
two for loops. The first one is for adding a thousand nodes to the queue and the
second one is for removing those nodes from the queue. In the second test, I
tested the Pop function's behavior trying to remove a node from an empty queue.

Lastly, I have made an alternative test to see if the Push and Pop functions
working properly. I have done this by using the functions one by one instead of
using them in a for loop. Adding three nodes and removing for just like the
Producer and Consumer functions in main().