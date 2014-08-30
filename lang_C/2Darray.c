#include <stdio.h>
#include <stdlib.h>


int make2DArray(int **p, int row, int col);

int main(void)
{
	int **p;
	int row=3;
	int col=3;
	make2DArray(p, row, col);
	
	return 0;
}

int make2DArray(int **p, int row, int col)
{
	int i,j;
	p=(int**)malloc(sizeof(int*)*row);
	
	for(i=0;i<col;i++)
	{
		p[i] = (int*)malloc(sizeof(int)*col);
	}
	for(i=0;i<row;i++)
	{
		for(j=0;j<col;j++)
		{
			p[i][j]=i;
			printf("%d ", p[i][j]);
		}
		printf("\n");
	}
	return 0;	
}
