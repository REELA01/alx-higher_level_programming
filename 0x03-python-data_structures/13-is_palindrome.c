#include "lists.h"
/**
  * is_palindrome - checks if palindrome
  * @head: double pointer
  * Return: 1 if plaidrome
*/
int is_palindrome(listint_t **head)
{
	return (checkPalindrome(head, *head));
}

/**
  * checkPalindrome - check if linked list is a palindrome
  * @start: double pointer
  * @end: pointer to list
  * Return: int value
*/
int checkPalindrome(listint_t **start, listint_t *end)
{
	int res;

	if (end == NULL)
		return (1);
	res = checkPalindrome(start, end->next) && ((*start)->n == end->n);
	return (res);
}
