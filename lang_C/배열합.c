#include <stdio.h>

void add(int *array, int size, int *sum);

int main(void)
{	
	int array[5]= {0,1,2,3,4};
	/*
	int *sum = NULL;
	sum = (int*) malloc(sizeof(int));
	printf("%d\n", *sum);
	add(array, 5, sum);
	printf("%d\n", *sum);
	*/
	int x = 0;
	printf("%d\n", x);
	add(array, 5, &x);
	printf("%d\n", x);
	
	
}

void add(int *array, int size, int * sum)
{
	int i;
	*sum = 0;
	for(i=0;i<size;i++)
	{
		*sum= *sum + array[i];
	}
}
