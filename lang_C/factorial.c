#include <stdio.h>

int factorial(int num);
int main(int argc, char * argv[])
{
	int num=factorial(6);
	
	printf("%d", num);
}


int factorial(int num)
{
	if(num==1)
		return 1;
	return num*factorial(num-1);
}