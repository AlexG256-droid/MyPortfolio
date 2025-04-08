#include <stdio.h>   // For IO operations
#include <stdlib.h>  // for malloc/free

#include "mystack.h"

// Tests the capacity of a stack
int unitTest1(int status) {
	int passed = 0;

	stack_t* test_s = create_stack(32);
	if (32 == test_s->capacity) {
		passed = 1;
	}

	free_stack(test_s);

	return passed;
}

// Enqueue several items into a stack and test the size
int unitTest2(int status) {
	int passed = 0;

	stack_t* test_s = create_stack(MAX_DEPTH);
	stack_push(test_s, 1);
	stack_push(test_s, 2);
	stack_push(test_s, 3);
	stack_push(test_s, 4);
	stack_push(test_s, 5);
	stack_push(test_s, 6);
	stack_push(test_s, 7);
	stack_push(test_s, 8);
	stack_push(test_s, 9);
	stack_push(test_s, 10);

	if (10 == stack_size(test_s)) {
		passed = 1;
	}

	free_stack(test_s);

	return passed;
}

// Tests pushing and fully popping a stack
int unitTest3(int status) {
	int passed = 0;

	stack_t* test_s = create_stack(32);
	int i = 0;
	for (i = 0; i < 32; i++) {
		stack_push(test_s, 1);
	}
	for (i = 0; i < 32; i++) {
		stack_pop(test_s);
	}

	if (0 == stack_size(test_s)) {
		passed = 1;
	}

	free_stack(test_s);

	return passed;
}

// Tests pushing and fully popping a stack multiple times
int unitTest4(int status) {
	int passed = 0;

	stack_t* test_s = create_stack(32);
	int i = 0;
	for (i = 0; i < 32; i++) {
		stack_push(test_s, 1);
	}
	for (i = 0; i < 32; i++) {
		stack_pop(test_s);
	}
	for (i = 0; i < 32; i++) {
		stack_push(test_s, 1);
	}
	for (i = 0; i < 32; i++) {
		stack_pop(test_s);
	}
	if (0 == stack_size(test_s)) {
		passed = 1;
	}

	free_stack(test_s);

	return passed;
}

// Simple push and pop stack test
// Also confirms that a stack is full
int unitTest5(int status) {
	int passed = 0;

	stack_t* test_s = create_stack(1);
	stack_push(test_s, 1);

	stack_pop(test_s);
	if (0 == stack_full(test_s)) {
		passed = 1;
	} else {
		passed = 0;
	}

	free_stack(test_s);

	return passed;
}

int (*unitTests[])(int) = {unitTest1, unitTest2, unitTest3,
			   unitTest4, unitTest5, NULL};

// ====================================================
// ================== Program Entry ===================
// ====================================================
int main() {
	unsigned int testsPassed = 0;
	// List of Unit Tests to test your data structure
	int counter = 0;
	while (unitTests[counter] != NULL) {
		printf("========unitTest %d========\n", counter);
		if (1 == unitTests[counter](1)) {
			printf("passed test\n");
			testsPassed++;
		} else {
			printf(
			    "failed test, missing functionality, or incorrect "
			    "test\n");
		}
		counter++;
	}

	printf("%d of %d tests passed\n", testsPassed, counter);

	return 0;
}
