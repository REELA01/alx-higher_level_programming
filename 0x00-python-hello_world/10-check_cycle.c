#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check for circular linkedlist
 * @list: strcut pointer
 * Return: 1 for cucle 0 not
*/
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (list == NULL)
		return (0);
	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
