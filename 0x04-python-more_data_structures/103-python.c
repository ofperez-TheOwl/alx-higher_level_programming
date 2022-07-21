#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - print basic info about Python object
 * @p: pointer to PyObject; the bytes object
 *
 * Return: nothing
 *
 * Description: Doesn't use these macro/function pPyBytes_AS_STRING, pPyBytes_GET_SIZE
 * TheOwl
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i = 0, len;
	char *str;

	printf("[.] bytes object info\n");
	if (!(strcmp(p->ob_type->tp_name, "bytes"))) /* check if p is a bytes object */
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
		/* find and print size and string */
	len = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
		/* find and print the first X bytes (max 10) */
	if (len >= 10)
		printf("  first 10 bytes:");
	else
		printf("  first %ld bytes:", len + 1);
	for (i = 0; str[i] != '\0' && i < 10; i++)
		printf(" %02x", str[i]);
	printf("\n");
}

/**
 * print_python_list - printbasic info about Python lists
 * @p: pointer to PyObject; the list object
 *
 * Return: nothing
 *
 * Description: Doesn't use these macro/function pPy_SIZE, pPy_TYPE, pPyList_GetItem
 * TheOwl
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i = 0;
	Py_ssize_t j, k;
	PyListObject *tmp;

	if (!(strcmp(p->ob_type->tp_name, "list"))) /* check if p is a list */
	{
		/* find and print number of element in p */
		tmp = (PyListObject *)p;
		for (j = 0; tmp->ob_item[j] != NULL; j++)
			;
		/* j = PyList_Size(p); */
		k = tmp->allocated;
		printf("[*] Python list info = %ld\n", j);
		printf("[*] Size of the Python List = %ld\n", j);
		printf("[*] Allocated  = %ld\n", k);
		if (j == 0)
			printf("Element 0: 0\n");
		else
		/* print the type of each element of the p */
			while (i < j)
			{
			/* find type of element at index i */
				printf("Element %ld: %s\n", i, tmp->ob_item[i]->ob_type->tp_name);
				if (!(strcmp(tmp->ob_item[i]->ob_type->tp_name, "bytes")))
					print_python_bytes(tmp->ob_item[i]);
				i++;
			}
	}
}
