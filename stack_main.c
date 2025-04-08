#include <stdio.h>  // For IO operations
#include <stdlib.h> // for malloc/free

#include "mystack.h"

void unitTest1(){

	stack_t* test1 = create_stack(MAX_DEPTH);
	printf("Attempting to push %d\n",1);
	stack_push(test1,1);
	printf("Removing: %d\n",stack_pop(test1));	

	free_stack(test1);
}

void unitTest2(){

	stack_t* test2 = create_stack(MAX_DEPTH);
	printf("Checking to see if the stack is empty");
	stack_empty(test2);
	printf("%d\n",stack_empty(test2));	

	free_stack(test2);
}

void unitTest3(){

	stack_t* test3 = create_stack(MAX_DEPTH);
	printf("Checking to see if the stack is full");
	stack_full(test3);
	printf("%d\n",stack_full(test3));	

	free_stack(test3);
}

void unitTest4(){

	stack_t* test4 = create_stack(MAX_DEPTH);
	printf("Checking the size of the stack");
	stack_size(test4);	
	printf("The stack size is: %d\n",stack_size(test4));	

	free_stack(test4);
}


// ====================================================
// ================== Program Entry ===================
// ====================================================
int main(){

	// List of Unit Tests to test data structure	
	unitTest1();
	unitTest2();
	unitTest3();
	unitTest4();

	return 0;
}
