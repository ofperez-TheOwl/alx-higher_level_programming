#include "Python.h"
#include "lists.h"
#include <stdio.h>

/**
 * print_python_list_info - printbasic info about Python lists
 * @p: pointer to PyObject; the list object
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int i = 0;
	int j = 0;
	PyObject *tmp;

	if (PyList_CheckExact(p) != 0) /* check if p is a list */
	{
		/* find and print number of element in p */
		j = PyList_Size(p);
		printf("[*] Size of the Python List = %d\n", j);
		if (j == 0)
			printf("Element 0: 0\n");
		else
		/* print the type of each element of the p */
			while (i < j)
			{
			/* find type of element at index i */
				tmp = PyList_GetItem(p, i);
				printf("Element %d: %s\n", i, ((Py_TYPE(tmp))->tp_name));
				i++;
			}
	}
}
