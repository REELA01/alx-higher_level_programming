#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly-linked list
 * @head: head pointer
 * @number: inserted num
 * Return: the stored nodelist
*/
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *node = *head, *nn;

  nn = malloc(sizeof(listint_t));
  if (!nn)
    return (NULL);
  nn->n = number;
  if (node == NULL || node->n >= number)
    {
      nn->next = node;
      *head = nn;
      return (nn);
    }
  while (node && node->next && node->next->n < number)
    node = node->next;
  nn->next = node->next;
  node->next = nn;
  return (nn);
}
