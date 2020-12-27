#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int array[2048];
	int i = 0, j = 0;

	if (head == NULL)
		return (1);

	while (current != NULL)
	{
		array[i] = current->n;
		i++;
		current = current->next;
	}
	i--;
	while (j <= i)
	{
		if (array[j] != array[i])
			return (0);
		i--;
		j++;
	}
	return (1);
}
