#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

//adt of list
typedef char* element;
typedef struct _node {
	element data;
	struct _node *next;
} node;

typedef node* node_ptr;

//create empty head node
node_ptr initHead();
int isEmpty(node_ptr head);
int size(node_ptr head);
int search(node_ptr head, element value);
void addFirst(node_ptr head, element new_data);
element get(node_ptr head, int index);
element getFirst(node_ptr head);
element removeNode(node_ptr head, int index); //return the value in index and remove node
element removeFirst(node_ptr head);
void replace(node_ptr head, int index, element data);
void shuffle(node_ptr head);


//main fuction
int main(int argc, char * argv[])
{
	
}

//declation and initialize head
node_ptr initHead()
{
	node_ptr head = (node_ptr)malloc(sizeof(node_ptr));
	head->next = NULL;
	return head;
}

int isEmpty(node_ptr head)
{
	return (head->next==NULL);
}

int size(node_ptr head)
{
	node_ptr cur=head; //why initialize other variation?
	int len=0;
	while(1)
	{
		cur= cur-> next;
		if(cur)
			len++;
		else
			break;
	}
	return len;
}

int search(node *head, element value)
{
	int n=0;//index is start at zero?
	node_ptr cur = head->next;
	while(cur)
	{
		if(strcmp(cur->data,value))
			return n;
		cur = cur -> next;
		n++;
	}
	return -1;
}


void addFirst(node_ptr head, element new_data)
{
	node_ptr nn=(node_ptr) malloc (sizeof(node)); //is okay use node?? why different at init()?
	//set value
	//set two link because it's single linked list
	nn -> next= head->next;
	head->next=nn;
}

node_ptr _get(node * head, int index)
{
	int i;
	node_ptr cur=head;
	
	for(i=0; i<=index ; i++) //why is not index-1?, index start at zero??
	{
		cur = cur ->next;
		if(!cur)
			break;
	}
	
	return cur;
}

element get(node* head, int index)
{
	node_ptr np= _get(head, index);
	return np->data;
}

element getFirst(node * head)
{
	return get(head,0);
}

element removeNode(node * head, int index)
{
	//get prev node
	node_ptr prev = _get(head, index-1);
	//get current node
	node_ptr target = prev->next;
	//get data of target
	element data = target ->data;
	
	//fix link
	//need 1 link fix, because it's single
	prev->next=target->next;
	//free target
	free(target);
	
	return data;
}

element removeFirst(node_ptr head)
{
	return removeNode(head, 0);
}

void replace(node * head, int index, element data)
{
	node_ptr target=_get(head, index);
	target->data = data;
}

void shuffle(node_ptr head)
{
	int n = size(head);
	int i, t, idx;
	node_ptr cur= head->next;
	element src, dest;
	
	srand(time(NULL));
	for(i=n-1; i>0 ; i--)
	{
		src = get(head, i);
		idx = rand()%i;
		dest = get(head, idx);
		replace(head, i, dest);
		replace(head, idx, src);
	}
}