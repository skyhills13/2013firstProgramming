#include <stdio.h>
#include <stdlib.h>

typedef int* int_ptr;
//void alloc_int(int_ptr p); //bad declaration
void alloc_int(int_ptr* pp);
int main()
{
	int_ptr x=NULL;
	printf("before %p\n", x);
	alloc_int(&x);
	printf("after %p\n", x);
	//alloc_int(&x);

		
	//px = (int*) malloc(sizeof(int));
	//*px = 100;

	//printf("%d\n", *px);

	//free(px);
	return 0;
}

void alloc_int(int_ptr *x) //*x = pp
{
	*x= (int_ptr) malloc(sizeof(int));
	printf("in alloc %p\n", *x);	
}

