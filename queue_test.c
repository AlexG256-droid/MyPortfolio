#include <stdio.h>  // For IO operations
#include <stdlib.h> // for malloc/free

#include "myqueue.h"

// Tests that a new queue was created and the capacity
// was properly set.
int unitTest1(int status){
    int passed = 0;
    queue_t* testq = create_queue(30);
    if(30==testq->capacity){
        passed = 1;
    }
    free_queue(testq);
    
    return passed;
}

// Tests adding multiple items to a queue
int unitTest2(int status){
    int passed = 0;

    queue_t* testq = create_queue(10);
    queue_enqueue(testq,1);
    queue_enqueue(testq,2);
    queue_enqueue(testq,3);
    queue_enqueue(testq,4);
    queue_enqueue(testq,5);
    queue_enqueue(testq,6);
    queue_enqueue(testq,7);
    queue_enqueue(testq,8);
    queue_enqueue(testq,9);
    queue_enqueue(testq,10);
    if(10==queue_size(testq)){
        passed = 1;
    }

    free_queue(testq);

    return passed;
}

// Tests enqueing and dequeing
int unitTest3(int status){
    int passed = 0;

    queue_t* testq = create_queue(32);
    int i =0;
    for(i=0; i < 32; i++){
        queue_enqueue(testq,1);
    }
    for(i=0; i < 32; i++){
        queue_dequeue(testq);
    }
    
    if(0==queue_size(testq)){
        passed =1;
    }

    free_queue(testq);

    return passed;
}

// Tests enqueing and dequeing multiple times
int unitTest4(int status){
    int passed = 0;
    
    queue_t* testq = create_queue(32);
    int i =0;
    for(i=0; i < 32; i++){
        queue_enqueue(testq,1);
    }
    for(i=0; i < 32; i++){
        queue_dequeue(testq);
    }
    for(i=0; i < 32; i++){
        queue_enqueue(testq,1);
    }
    for(i=0; i < 32; i++){
        queue_dequeue(testq);
    }
    
    if(0==queue_size(testq)){
        passed =1;
    }
    
    free_queue(testq);

    return passed;
}

int unitTest5(int status){
    int passed = 0;

    queue_t* testq = create_queue(1);
    queue_enqueue(testq,1);
    if(1==queue_full(testq)){
        passed = 1;
    }else{
	    free_queue(testq);
	return 0;
    }
    
    queue_dequeue(testq);
    if(0==queue_full(testq)){
        passed = 1;
    }else{
        passed = 0;
    }
    
    free_queue(testq);

    return passed;
}

int (*unitTests[])(int)={
    unitTest1,
    unitTest2,
    unitTest3,
    unitTest4,
    unitTest5,
    NULL
};

// ====================================================
// ================== Program Entry ===================
// ====================================================
int main(){
    unsigned int testsPassed = 0;
    // List of Unit Tests to test your data structure
    int counter =0;
    while(unitTests[counter]!=NULL){
        printf("========unitTest %d========\n",counter);
        if(1==unitTests[counter](1)){
            printf("passed test\n");
            testsPassed++;	
        }else{
            printf("failed test, missing functionality, or incorrect test\n");
        }
        counter++;
    }

    printf("%d of %d tests passed\n",testsPassed,counter);

    return 0;
}
