#include <stdio.h>
#include <stdlib.h>

#ifndef MYQUEUE_H
#define MYQUEUE_H

// The main data structure for the queue
struct queue{
	unsigned int back;	    // The next free position in the queue
				    		// (the end or tail of the line)
	unsigned int front;	    // Current 'head' of the queue
				    		// (the front or head of the line)
	unsigned int size;	    // How many total elements we currently have enqueued.
	unsigned int capacity;  // Maximum number of items the queue can hold
	int* data; 		    	// The 'integer' data our queue holds	
};
// Creates a global definition of 'queue_t'.
typedef struct queue queue_t;

// Create a queue
// Returns a pointer to a newly created queue.
// The queue should be initialized with data on
// the heap.
queue_t* create_queue(unsigned int _capacity){
	// Assigns the queue myQueue to queue_t* using malloc
	queue_t* myQueue = (queue_t*)malloc(sizeof(queue_t));
	
	// Checks for null
	if (myQueue == NULL) {
		return NULL;
	}

	// Defines the capacity parameter
	myQueue->capacity = _capacity;

	// Assigns the default parameters to 0
	myQueue->back = 0;
	myQueue->front = 0;
	myQueue->size = 0;

	// Assigns the data parameter using malloc
	myQueue->data = (int *)malloc(sizeof(int) * _capacity);
	
	// Checks for null
	if (myQueue->data == NULL) {
		return NULL;
	}
	
	// Returns the new queue
	return myQueue;
}

// Queue Empty
// Check if the queue is empty
// Returns 1 if true (The queue is completely empty)
// Returns 0 if false (the queue has at least one element enqueued)
int queue_empty(queue_t* q){
	// If the length of the queue is 0 (the queue isn't empty), then
	// queue_empty returns 1, otherwise it returns 0
	if (q == NULL) {
		return 0;
	}
	
	if (q->size == 0) {
		return 1;
	} else {
		return 0;
	}
}

// Queue Full
// Check if the queue is Full
// Returns 1 if true (The queue is completely full)
// Returns 0 if false (the queue has more space available to enqueue items)
int queue_full(queue_t* q){
	// If the number of items in the queue is equal to the maximum number of
	// items that can fit in the queue, queue_full returns 1
	// If there are less items than the maximum, queue_full returns 0
	if (q == NULL) {
		return 0;
	}

	if (q->size == q->capacity) {
		return 1;
	} else {
		return 0;
	}
}

// Enqueue a new item
// Returns a -1 if the operation fails (otherwise returns 0 on success).
int queue_enqueue(queue_t* q, int item){
	// If the queue is not full, one item is added to the back of the queue
	// and 0 is returned
	// If the queue is full, nothing happens to the queue and -1 is returned
	if (queue_full(q)) {
		return -1;
	} else {
		q->data[q->back % q->capacity] = item;
		q->back++;
		q->size += 1;
		return 0;
	}
	// Note: you should have two return statements in this function.
}

// Dequeue an item
// Returns the item at the front of the queue and
// removes an item from the queue.
// Removing from an empty queue should crash the program, call exit(1)
int queue_dequeue(queue_t *q){
	// If the queue isn't already empty, the first item is the first out and 1
	// is returned, otherwise it returns 0
	if (q == NULL) {
		exit(1);
	}

	if (queue_empty(q) == 0) {
		int item = q->data[q->front % q->capacity];
		q->data[q->front % q->capacity] = 0;
		q->front = (q->front + 1) % q->capacity;
		q->size -= 1;
		return item;
	} else {
		return 0;
	}
}


// Queue Size
// Queries the current size of a queue
// A queue that has not been previously created will crash the program.
unsigned int queue_size(queue_t* q){
	// If q hasn't been executed yet, the function queue_size will crash the
	// program
	if (q == NULL) {
		exit(1);
	} else {
		return q->size;
	}
}


// Free queue
// Removes a queue and all of its elements from memory.
// This should be called before the program terminates.
void free_queue(queue_t* q){
	if (q == NULL) {
		exit(1);
	}

	// Frees the queue data
	free(q->data);
    free(q);
}


#endif
