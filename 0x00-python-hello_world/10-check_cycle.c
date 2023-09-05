#include "lists.h"

/**
 * check_cycle - function to check for a cycle in singly linked list
 * @list: pointer to head of the list
 * Return: 0 if no cycle found or 1 if there is cycle
 */

int check_cycle(listint_t *list)
{
	/*initialize 2 var to the head(list) for transversing*/
	listint_t *temp = list;
	listint_t *current = list;

	if (list == NULL)
		return (0);

	/*move the pointers continously through the list*/
	while (current != NULL && current->next != NULL)
	{
		/*temp moves one step at a time*/
		temp = temp->next;
		/*current moves two step*/
		current = current->next->next;
	}

	/*check if the pointers meet at any point of the movement*/
	if (temp == current)
	{
		/*if they meet, then there is a cycle*/
		return (1);
	}
	return (0);
}
