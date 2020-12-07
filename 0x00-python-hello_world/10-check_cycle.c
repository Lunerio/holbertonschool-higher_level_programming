#include "lists.h"

/**
 * check_cycle - checks if a list has a cycle
 * @list: pointer to header of linked list
 * Return: 1 if there's a cycle, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *p1 = list;
	listint_t *p2 = list;

	while (p1->next != NULL && p2->next != NULL)
	{
		p1 = p1->next;
		p2 = p2->next;
		if (p2->next == NULL)
		{
			return (0);
		}
		p2 = p2->next;
		if (p2->next == NULL)
		{
			return (0);
		}
		if (p1 == p2)
		{
			return (1);
		}
	}
	return (0);
}
