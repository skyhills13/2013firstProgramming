
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int input;
	int *memory;
	int i;
	    
	printf("input the size you want to allocate");
	scanf("%d",&input);
	memory = (int*) calloc(input, sizeof(int));
	    
	for(i=0;i<input;i++)
	{
		memory[i] = i;
		printf("%d \n", memory[i]);
		
	}
	printf("%s \n", memory);
	return 0;

}