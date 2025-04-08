#include <stdio.h>  // For IO operations
#include <stdlib.h> // for malloc/free

#include "myqueue.h"

void unitTest1(){

	queue_t* test1 = create_queue(1);
	printf("Attempting to add %d\n",1);
	queue_enqueue(test1,1);	
	printf("Removing: %d\n",queue_dequeue(test1));	

	free_queue(test1);
}

void unitTest2(){

	queue_t* test2 = create_queue(1);
	printf("Is the queue full? %d\n",1);
	queue_full(test2);	
	printf("Is the queue empty? %d\n",queue_empty(test2));	

	free_queue(test2);
}

void unitTest3(){

	queue_t* test3 = create_queue(1);
	printf("The queue size is %d\n",1);
	printf("%d\n",queue_size(test3));	

	free_queue(test3);
}

// ====================================================
// ================== Program Entry ===================
// ====================================================
int main(){

	// List of Unit Tests to test your data structure	
	unitTest1();

	unitTest2();

	unitTest3();

	return 0;
}
