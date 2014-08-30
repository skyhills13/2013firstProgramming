#include <stdio.h>

int main(void)
{
	int result[3][3];
	int mul1[][3]={{1,2,3},{4,5,6},{7,8,9}};//{(35,25,34),(89,58,82),(143,91,130)};
	int mul2[][3]={{9,3,5},{1,2,4},{8,6,7}};

	int numRow=3, numCol=3, tmp=3;
	int i,j;
	for(i=0;i<numRow;i++)
	{
		
		for(j=0;j<numCol;j++)
		{
			result[i][j] = 0;
			for(tmp=0;tmp<3;tmp++)
			{	
				//result[i][j] = 0;
				result[i][j]+=mul1[i][tmp]*mul2[tmp][j];
			}
			printf("%d ", result[i][j]);
		}
		printf("\n");
	}
	
	return 0;
}