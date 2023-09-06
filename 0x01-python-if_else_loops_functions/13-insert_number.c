#include "lists.h"

/**
 * insert_node - Function to insert a number in sorted linked list
 * @head: Pointer to the head of the list
 * @number: the number to insert
 * Return: Address of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *currentNode, *previousNode = *head;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;

	if (previousNode == NULL)
	{
		*head = newNode;
		return (newNode);
	}

	if (previousNode->n > number)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}

	currentNode = previousNode->next;
	while (currentNode)
	{
		if (number < currentNode->n)
		{
			newNode->next = currentNode;
			previousNode->next = newNode;
			return (newNode);
		}
		previousNode = currentNode;
		currentNode = currentNode->next;
	}
	currentNode = newNode;
	return (newNode);


}
