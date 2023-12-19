#include <stdio.h>
#include <Python.h>
/**
 * print_python_bytes - prints byte info
 * @p: Python obj
 * Return: void value
*/
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, i, lim;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	if (size >= 10)
		lim = 10;
	else
		lim = size + 1;
	printf("  first %ld bytes:", lim);
	for (i = 0; i < lim; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);
	printf("\n");
	setbuf(stdout, NULL);
}
/**
 * print_python_float - print float info
 * @p: Python obj
 * Return: void value
*/
void print_python_float(PyObject *p)
{
	double va;
	char *nf;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}
	va = ((PyFloatObject *)(p))->ob_fval;
	nf = PyOS_double_to_string(va, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
	printf("  value: %s\n", nf);
	setbuf(stdout, NULL);
}
/**
 * print_python_list - print list info
 * @p: Pytho obj
 * Return: void value
*/
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *lis;
	PyObject *op;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	lis = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", lis->allocated);
	for (i = 0; i < size; i++)
	{
		op = lis->ob_item[i];
		printf("Element %ld: %s\n", i, ((op)->ob_type)->tp_name);
		if (PyBytes_Check(op))
			print_python_bytes(op);
		if (PyFloat_Check(op))
			print_python_float(op);
	}
	setbuf(stdout, NULL);
}
