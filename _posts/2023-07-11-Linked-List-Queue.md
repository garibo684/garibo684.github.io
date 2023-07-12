---
layout: post
title: Linked List
tags: queue
categories: internship
---

## Declarations and Definitions

  I have started by writing a LinkedList.h header file. In this file I have
created a LinkedList class inside a T template. I declared the Node struct
with prev and next node pointers in it as a private member. By creating 
both next and prev pointers I have made a double-linked list.
Afterward, I declared the functions of the linked list:
- Append, Prepend, and Insert for adding new nodes to the list
- Delete and Clear for removing nodes
- Get... functions for retrieving data from the list.

```cpp
#ifndef LINKEDLISTQUEUE_LINKEDLIST_H
#define LINKEDLISTQUEUE_LINKEDLIST_H

#include <cstddef>

template <typename T>
class LinkedList {
 private:
   struct Node
   {
     Node* next_;
     Node* prev_;
     T data_;
   };

 public:
    LinkedList();
    ~LinkedList();

    void Append(const T& value);
    void Prepend(const T& value);
    void Insert(Node* prev_node, const T& value);
    void Delete();
    void Clear();
    const T& GetHead() const;
    const T& GetTail() const;
    bool GetEmpty() const;
    std::size_t GetSize() const;
    Node* GetHeadPtr() const;

 private:
    Node* head_;
    Node* tail_;
    std::size_t size_;
};

#endif
```

  
Afterward, I continued with definitions in [LinkedList.cc
file.][LinkedList.cc] Here I have defined the constructer and destructor as well
as the individual functions.

#### Append
  This function adds a new node to the end of the list. It takes a const T& value as
an argument and creates a Node* new_node which points to a newly created Node
with this value. Afterward; it checks if the list is empty, if it is empty then
new_node is assigned as both head and tail pointers. Otherwise, new_node will be
assigned as the tail->next and the tail will be assigned as new_node.

#### Prepend 
  It works almost exactly the same as the Append function except for the
position new node is added. Unlike the Append function, Prepend adds the new node
to the head of the list. Because of this instead of tail->next becoming
new_node, new_node->next becomes head. Afterward, new_node gets assigned as the
new head pointer.

#### Insert
  This one is a bit different from the first two. It adds the new node after
whichever node you want. For this reason, it takes a "const Node& head" as an
argument. It changes the next pointer of the node that new node is after the
new_node as well as the prev pointer of the node that is after the new node.

#### Delete
  This function removes the head node from the list and assigns the next node
as the new head. It does this by assigning it as the new head and changing the 
prev pointer for the new head to nullptr.

#### Clear
  If the list is not empty this function deletes every node one by one from head
  to tail and reassigns both of them to nullptr. It also changes the size value
  of the list to zero.

#### Get... Functions
  These functions are for retrieving data from the list. They return the data from
  the list.

### Notes
  Because this code works in a single-threaded environment "meaning there is no
concurrent running threads" it does not include any thread synchronization
mechanisms, such as locks or mutexes, to ensure thread safety.
  
  Big O notations for the functions except for the Clear and GetPosition functions 
is O(1). This is because these functions perform a constant number of operations 
regardless of the list's size. The Clear function on the other hand deletes each 
node in the list by traversing the list from the head to the tail. Deleting each 
node takes O(1) time, and since it needs to delete all the nodes, the overall time
complexity is O(n), where n is the number of nodes in the list. For the GetPosition
function, it is the same except for the n. In this function, n is the number of nodes
until the function arrives at the given value's position.

## Testing
  As a part of the test-driven development, I have tested my code using GTest.
Because some of the tests depend on the Get... functions I tested some of the 
main functions in pairs with the Get... functions. I have added and removed nodes
with different functions while testing if they are working with EXPECT_* macros
and Get... functions. Using these methods I have tested how every function works
in different situations.

```cpp
#include "LinkedList.h"
#include <gtest/gtest.h>

TEST (LinkedListTest, GetEmptyAndAppend) {
  LinkedList<int> list;
  
  EXPECT_TRUE(list.GetEmpty());
  list.Append(15);
  EXPECT_FALSE(list.GetEmpty());
}

TEST (LinkedListTest, Clear) {
  LinkedList<int> list;

  list.Append(15);
  EXPECT_FALSE(list.GetEmpty());

  list.Clear();
  EXPECT_TRUE(list.GetEmpty());
}

TEST (LinkedListTest, PrependAndGetHead) {
  LinkedList<int> list;

  list.Append(15);
  EXPECT_EQ(list.GetHead(), 15);

  list.Prepend(20);
  EXPECT_EQ(list.GetHead(), 20);
}

TEST (LinkedListTest, DeleteAndGetTail) {
  LinkedList<int> list;

  list.Append(15);
  list.Append(20);
  
  EXPECT_EQ(list.GetTail(), 20);
  
  list.Delete();
  EXPECT_EQ(list.GetTail(), 15);

  list.Delete();
  EXPECT_EQ(list.GetSize(), 0);
}

TEST (LinkedListTest, InsertAndGetSize) {
  LinkedList<int> list;
 
  list.Append(10);
  EXPECT_EQ(list.GetSize(), 1);
  list.Prepend(30);
  EXPECT_EQ(list.GetSize(), 2);
  list.Insert(list.GetHeadPtr(), 20);
  EXPECT_EQ(list.GetSize(), 3);

  
  EXPECT_EQ(list.GetTail(), 10);
  list.Delete();
  EXPECT_EQ(list.GetTail(), 20);
  list.Delete();
  EXPECT_EQ(list.GetTail(), 30);
  list.Delete();
  EXPECT_TRUE(list.GetEmpty());
}

int main(int argc, char* argv[]) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
```
[LinkedList.cc]: https://github.com/garibo684/Queue_Projects/blob/main/LinkedListQueue/src/LinkedList/LinkedList.cc
