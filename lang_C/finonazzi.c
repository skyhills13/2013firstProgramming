#include <stdio.h>

int fibonazzi(int num);

int main(int argc, char *argv[])
{
	printf("%d", fibonazzi(5));
}

int fibonazzi(int num)
{
	if(num<=2)
		return 1;
	
	return fibonazzi(num-2)+fibonazzi(num-1);
}