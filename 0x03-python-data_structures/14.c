#include <Python.h>
#include <stdio.h>
/*
includes listobject.h
VIEW HEADER-> https://github.com/python/cpython/blob/master/Include/listobject.h
VIEW MANUAL-> https://docs.python.org/3.4/c-api/list.html
includes object.h
VIEW HEADER-> https://docs.python.org/3.4/c-api/structures.html)
VIEW MANUAL-> https://github.com/python/cpython/blob/master/Include/object.h
*/

/**
 * print_python_list_info - printbasic info about Python lists
 * @p: pointer to PyObject; the list object
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i = 0;
	Py_ssize_t j, k;
	PyObject *tmp;

	if (PyList_CheckExact(p) != 0) /* check if p is a list */
	{
		/* find and print number of element in p */
		j = PyList_Size(p);
		k = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %ld\n", j);
		printf("[*] Allocated  = %ld\n", k);
		if (j == 0)
			printf("Element 0: 0\n");
		else
		/* print the type of each element of the p */
			while (i < j)
			{
			/* find type of element at index i */
				tmp = PyList_GetItem(p, i);
				printf("Element %ld: %s\n", i, ((Py_TYPE(tmp))->tp_name));
				i++;
			}
	}
}
