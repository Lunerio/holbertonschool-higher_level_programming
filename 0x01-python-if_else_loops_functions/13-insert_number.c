#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *act = *head;
	listint_t *sig;
	listint_t *new;

	if (head == NULL ||number <= act->n)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = number;
		*head = new;
		new->next = act;
		return (*head);
	}
	while (act)
	{
		sig = act->next;
		if (act->next != NULL)
		{
			if (number >= act->n && number <= sig->n)
			{
				new = malloc(sizeof(listint_t));
				if (new == NULL)
					return (NULL);
				new->n = number;
				new->next = act->next;
				act->next = new;
				return (new);
			}
			act = act->next;
			continue;
		}
		else
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			new->next = act->next;
			act->next = new;
			return (new);
		}
	}
	return (NULL);
}
