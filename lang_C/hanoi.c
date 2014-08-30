#include <stdio.h>


void hanoi(int num, int start_pos, int target_pos, int notuse_pos);

int main(int argc, char *argv[]) {
	hanoi(4,1,3,2);	
}

void hanoi(int num, int start_pos, int target_pos, int notuse_pos)
{
	if(num==1){
		printf("%d -> %d\n", start_pos, target_pos);
		return ;
	}
	
	hanoi(num-1, start_pos, notuse_pos,target_pos);
	printf("%d -> %d\n", start_pos, target_pos);
	hanoi(num-1, notuse_pos, target_pos, start_pos);
}