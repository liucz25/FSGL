#include  <stdio.h>
#include <pthread.h>
#include <unistd.h>

void* fun(void* arg) {
	printf("I'm thread, Thread ID = %lu\n", pthread_self());
	return NULL;

}


int main01(void) {
	pthread_t tid;
	//pthread_create(&tid, NULL, fun, NULL);
	pthread_create(&tid, NULL, fun, NULL);
	sleep(1); 
	printf("I am main, my pid = %d\n", getpid());
	sleep(1);
	return 0;

}