#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - python info
 * @p: Ppointer
 * Return: void value
*/
void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *alloc;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);
	alloc = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", alloc->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
