#include <Python.h>

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
				printf("Element %ld: %s\n", i, ((PY_TYPE(tmp))->tp_name));
				i++;
			}
	}
}
