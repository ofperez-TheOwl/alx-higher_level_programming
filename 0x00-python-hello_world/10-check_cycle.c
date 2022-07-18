#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: listint_t pointer; list to check
 *
 * Return: int; 1 if cycle found 0 if not
 *
 * Description: use Floyd's cycle finding algorithm
 * TheOwl
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp_slow = list, *tmp_fast = list;

	if (list == NULL || list->next == NULL || list->next->next == NULL)
		return (0);

	while (tmp_fast != NULL && tmp_fast->next != NULL)
	{
		tmp_slow = tmp_slow->next;
		tmp_fast = tmp_fast->next->next;
		if (tmp_fast == tmp_slow)
			return (1);
	}
	return (0);
}
