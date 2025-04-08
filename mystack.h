#define _XOPEN_SOURCE 700
#undef stack_t

#include <stdio.h>
#include <stdlib.h>

#ifndef MYSTACK_H
#define MYSTACK_H

// Stores the maximum 'depth' of our stack.
// Our implementation enforces a maximum depth of our stack.
# define MAX_DEPTH 32

// Create a node data structure to store data within
// our stack. In our case, we will stores 'integers'
typedef struct node{
	int data;
	struct node* next;
}node_t;

// Create a stack data structure
// Our stack holds a single pointer to a node, which
// is a linked list of nodes. No empty nodes should be used. 
typedef struct stack{
	int count;		// count keeps track of how many items
				// are in the stack.
	unsigned int capacity;	// Stores the maximum size of our stack
	node_t* head;		// head points to a node on the top of our stack.
}stack_t;

// Creates a stack
// Returns a pointer to a newly created stack.
// The stack should be initialized with data on the heap.
// The stacks fields should also be initialized to default values.
stack_t* create_stack(unsigned int capacity){
	// Null maximum capacity test
	if (capacity > MAX_DEPTH) {
		return NULL;
	}

	// Assigns the queue myStack to stack_t* using malloc
	stack_t* myStack = (stack_t*)malloc(sizeof(stack_t));
	
	// Null stack test
	if (myStack == NULL) {
		return NULL;
	// Null maximum capacity test
	} else {
		// Defines the parameters
		myStack->capacity = capacity;
		myStack->count = 0;	
		myStack->head = NULL;
	}

	// Returns the new stack
	return myStack;
}

// Stack Empty
// Check if the stack is empty
// Returns 1 if true (The stack is completely empty)
// Returns 0 if false (the stack has at least one element enqueued)
int stack_empty(stack_t* s){
	// If the stack is equal to NULL, -1 is returned
	if (s == NULL) {
		return 0;
	}
	
	// If the value of the head is equal to negative one, this function
	// returns 1, otherwise it returns 0
	if (s->count == 0) {
		return 1;
	}
	return 0;
}

// Stack Full
// Check if the stack is full
// Returns 1 if true (The Stack is completely full)
// Returns 0 if false (the Stack has more space available to enqueue items)
int stack_full(stack_t* s){
	// If the value of the head is equal to the maximum minus one, this
	// function returns 1, otherwise it returns 0
	if (s == NULL) {
		return 0;
	} else if (s->count == s->capacity) {
		return 1;
	}
	return 0;
}

// Enqueue a new item
// Returns a -1 if the operation fails (otherwise returns 0 on success).
int stack_push(stack_t* s, int item){
	// If the stack is not full, one item is added to the top of the queue and
	// 0 is returned
	if (s == NULL) {
		return -1;
	// If the stack is already at it's maximum capacity, -1 is returned
	} else if (stack_full(s) == 1) {
		return -1;
	}

	// Creates a node
	node_t* node_new = (node_t*)malloc(sizeof(node_t));

	// Null node test
	if (node_new == NULL) {
		return -1;
	}

	// Defines the new node's data to item
	node_new->data = item;

	// Defines the new head node
	node_new->next = s->head;
	s->head = node_new;

	// Adds 1 to the stack size
	s->count += 1;

	return 0;
}

// Dequeue an item
// Returns the item at the front of the stack and
// removes an item from the stack.
// Removing from an empty stack should crash the program, call exit(1).
int stack_pop(stack_t* s){
	// If the stack is not empty, one item is added to the top of the queue,
	// otherwise call exit(1)
	if (s == NULL) {
		exit(1);
	// Decreases the count by 1 and frees the pointer if the stack isn't empty
	} else if (stack_empty(s) == 1) {
		exit(1);
	}

	// Defines the head_removed node
	node_t* head_removed = s->head;

	// Defines the item and assigns the current head to the next one
	int item = s->head->data;
	s->head = s->head->next;

	// Reduces the size by 1 and frees the head
	s->count -= 1;
	free(head_removed);

	// Returns the head data
	return item;
}

// Stack Size
// Queries the current size of a stack
// A stack that has not been previously created will crash the program.
unsigned int stack_size(stack_t* s){
	// If the count of the stack is equal to 0 and/or the stack is a null, the
	// program is executed
	if (s == NULL) {
		exit(1);
	// If the stack exists, the count is returned
	}
	return s->count;
}

// Free stack
// Removes a stack and ALL of its elements from memory.
// This should be called before the proram terminates.
void free_stack(stack_t* s){
	// Eliminates all the items in the stack one by one until its empty
	if (s == NULL) {
		exit(1);
	} else {
		// Reduces the count to 0 and frees the head from the stack
		node_t* current_node = s->head;
		node_t* node_temp = NULL;

		while (current_node != NULL) {
			node_temp = current_node;
			current_node = current_node->next;
			free(node_temp);
			s->count -= 1;
		}
	}
	// Frees the stack
	free(s);
}

#endif
