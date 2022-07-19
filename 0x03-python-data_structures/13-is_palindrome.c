#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: listint_t pointer to pointer; list
 *
 * Return: int; 1 if palindrome 0 if not
 *
 * Description: this algorithm divide the list in two part by the middle
 * the nodes of the right part are read in order and traversed only one time
 * the nodes of the left part are read in reverse order and traversed many times
 * TheOwl
 */
int is_palindrome(listint_t **head)
{
	int i, len = 1;
	listint_t *tmp, *tmp_end = *head, *tmp_l = *head, *tmp_r = *head;

	if (tmp_end == NULL)
		return (1);
	/* traverse list check if first and last node are the same */
	while (tmp_end->next != NULL)
	{
		len++;
		tmp_end = tmp_end->next;
	}
	if (tmp_l->n != tmp_end->n)
		return (0);
	/* divide list in 2 part, set variables before checking other nodes */
	if (len % 2 == 0)
	{
		len = len / 2;
		for (i = 0; i < len - 1; i++)
			tmp_l = tmp_l->next;
	}
	else
	{
		len = len / 2 + 1;
		for (i = 0; i < len - 2; i++)
			tmp_l = tmp_l->next;
	}
	for (i = 0; i < len; i++)
		tmp_r = tmp_r->next;
	/* checking nodes of of right part are the same as nodes of left part*/
	while (tmp_r != tmp_end)
	{
		if (tmp_r->n != tmp_l->n)
			return (0);
		tmp_r = tmp_r->next;
		for (tmp = *head; tmp->next != tmp_l;)
			tmp = tmp->next;
		tmp_l = tmp;
	}
	return (1);
}
