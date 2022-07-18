#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: listint_t pointer to pointer; list
 * @number: int; number to add
 *
 * Return: listint_t pointer; address of new node if success NULL if not
 * TheOwl
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp_next, *tmp_prev, *new;

	if (*head == NULL || ((*head)->next == NULL && number >= (*head)->n))
		return (add_nodeint_end(head, number));
	/* set new node */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	/* insert at beginning */
	if (number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	/* traverse and insert new */
	tmp_next = (*head)->next;
	tmp_prev = *head;
	while (tmp_next != NULL)
	{
		if (number >= tmp_prev->n && number <= tmp_next->n)
		{
			tmp_prev->next = new;
			new->next = tmp_next;
			return (new);
		}
		tmp_prev = tmp_prev->next;
		tmp_next = tmp_next->next;
	}
	return (add_nodeint_end(&tmp_prev, number));
}
