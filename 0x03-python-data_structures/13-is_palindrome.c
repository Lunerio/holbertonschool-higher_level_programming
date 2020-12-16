#include "lists.h"

int is_palindrome(listint_t **head)
{
	int i;
	int j; /*index init_p*/
	int count = 0;
	listint_t *last_p = *head;
	listint_t *init_p = *head;

	if (*head == NULL)
		return (1);

	while (last_p) /*count elements*/
	{
		last_p = last_p->next;
		count++;
	}

	for(j = 0; j <= (count - 1); count--)
	{
		last_p = *head;
		i = 0;
		printf("got into loop\n");
		while (i < (count - 1))
		{
			printf("loop last_p %d", i);
			last_p = last_p->next;
		}
		printf("moved pointer to last one\n");
		if (last_p->n != init_p->n)
		{
			printf("found different one\n");
			return (0);
		}
		else
		{
			printf("got into movement because equal\n");
			init_p = init_p->next;
			j++;
		}
	}
	printf("is pali\n");
	return (1);
}
