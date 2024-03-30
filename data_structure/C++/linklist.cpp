#include <iostream>
#include <stdio.h>



using namespace std;

/*
There are various linked list operations that allow us to perform different actions on linked lists. For example, the insertion operation adds a new element to the linked list.

Here's a list of basic linked list operations that we will cover in this article.

Traversal - access each element of the linked list
Insertion - adds a new element to the linked list
Deletion - removes the existing elements
Search - find a node in the linked list
Sort - sort the nodes of the linked list
Before you learn about linked list operations in detail, make sure to know about Linked List first.
*/
// creating a node

struct Node{
    int data;
    struct Node* next;
};

/*1. Insert at the beginning
Allocate memory for new node
Store data
Change next of new node to point to head
Change head to point to recently created node*/
void insertAtBegin(struct Node **head_ref, int new_data){
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    // insert data
    new_node->data = new_data;
    new_node -> next = (*head_ref)
    
}

/*2. Insert at the End
Allocate memory for new node
Store data
Traverse to last node
Change next of last node to recently created node*/


/*3. Insert at the Middle
Allocate memory and store data for new node
Traverse to node just before the required position of new node
Change next pointers to include new node in between*/

/*1. Delete from beginning
Point head to the second node*/

/*2. Delete from end
Traverse to second last element
Change its next pointer to null*/

/*3. Delete from middle
Traverse to element before the element to be deleted
Change next pointers to exclude the node from the chain*/