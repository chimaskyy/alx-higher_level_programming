#include "lists.h"

/**
 * reverse - Function to reverse linked list
 * @head: Pointer to head of the list
 * Return: Reversed list
 */

listint_t *reverse(listint_t *head)
{
	listint_t *curr_node = head;
	listint_t *nextNode = NULL;
	listint_t *prev_node = NULL;

	if (head == NULL)
		return (NULL);

	while (curr_node != NULL)
	{
		nextNode = curr_node->next;
		curr_node->next = prev_node;
		prev_node = curr_node;
		curr_node = nextNode;
	}
	return (prev_node);
}
/**
 * is_palindrome - Check if a linked list is a palindrom
 * @head: Pointer to head of the list
 * Return: 1 if list is palindrom or 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *m1 = *head, *m2 = *head;
	listint_t *reversed;
	listint_t *unreversed = *head;

	if (*head == NULL)
		return (1);
	/*m1 and m2 pointer is used to locate middle of the list*/
	while (m2 != NULL && m2->next != NULL)
	{
		/*m1 is moved once while m2 is moved twice*/
		m1 = m1->next;
		m2 = m2->next->next;
		/*when m2 gets to the end, m1 will be in the middle*/
	}
	/*m1 which now points to the first node of the second half of the list*/
	reversed = reverse(m1);
	/*m1 is used to reverse the 2nd half of the list*/

	/*iterate thru the reversed list*/
	while (reversed != NULL)
	{
		/*while iterating, compare the it's val with that of first half of the list*/
		if (unreversed->n != reversed->n)
		{
			/*if at any point the vals are not same,0(not palindrom) is returned*/
			return (0);
		}
		/*move pointers to the next node to continue comparing their val*/
		unreversed = unreversed->next;
		reversed = reversed->next;
	}
	/*if all vals are same 1 is returned(list is palindrom)*/
	return (1);


}
