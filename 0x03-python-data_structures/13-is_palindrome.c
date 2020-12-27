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
		while (i < count - 1)
		{
			last_p = last_p->next;
			i++; /*faltaba esto. Nunca subia i antes.*/
		}
		if (last_p->n != init_p->n)
		{
			return (0);
		}
		else
		{
			init_p = init_p->next;
			j++;
		}
	}
	return (1);
}
