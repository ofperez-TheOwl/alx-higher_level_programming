#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * add_nodeint - add a new node at the begining of the list of listint_t
 * @head: listint_t pointer to pointer; head of the list of listint_t
 * @n: const int; int data of the new node
 *
 * Return: pointer to listint_t if success or NULL if not
 * TheOwl
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	/* set values of new node */
	new->n = n;
	if (*head == NULL)
		new->next = NULL;
	else
		new->next = *head;
	*head = new;

	return (new);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: listint_t pointer to pointer; list
 *
 * Return: int; 1 if palindrome 0 if not
 *
 * Description: this algorithm creates another singly linked list
 * that will be used as a stack (LIFO) for the first half of orignal
 * list and will be compared to the second part of original list 
 * TheOwl
 */
int is_palindrome(listint_t **head)
{
	int i, len = 1;
	listint_t *stack, *tmp = *head, *tmp_s = NULL;
	/* traverse list check if first and last node are the same */
	if (tmp == NULL || tmp->next == NULL)
		return (1);
	while (tmp->next != NULL)
	{
		len++;
		tmp = tmp->next;
	}
	if ((*head)->n != tmp->n)
		return (0);
	if (len < 4)
		return (1);
	/* create stack */
	tmp = *head;
	for (i = 0; i < len / 2; i++)
	{
		tmp_s = add_nodeint(&tmp_s, tmp->n);
		if (tmp_s == NULL)
			return (0);
		tmp = tmp->next;
	}
	stack = tmp_s;
	if (len % 2 != 0)
		tmp = tmp->next;
	/* check if second part of list is same as stack*/
	while (tmp != NULL)
	{
		if (tmp_s->n != tmp->n)
		{
			free_listint(stack);
			return (0);
		}
		tmp = tmp->next;
		tmp_s = tmp_s->next;
	}
	free_listint(stack);
	return (1);
}
