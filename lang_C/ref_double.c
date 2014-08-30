#include <stdio.h>
#include <stdlib.h>

void changeNum(int *inc, int *dec);
void alloc_int(int **p); //ok

int main()
{
	int *px; 
	int *py;
	alloc_int(&px);
	alloc_int(&py);
	*px = 100;
	*py = 200;

	changeNum(px, py);
	printf("%d %d\n", *px, *py);

	free(px);
	free(py);
	return 0;
}

void changeNum(int *inc, int *dec)
{
	*inc = *inc + 1;
	*dec = *dec - 1;
}

void alloc_int(int **p)
{
	*p = malloc(sizeof(int));
}
