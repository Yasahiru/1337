#ifndef HEAP_H
# define HEAP_H

# include <stdlib.h>

typedef struct s_coder	t_coder;

typedef struct s_heap_node
{
	t_coder	*coder;
	long	priority;
	long	sequence;
}	t_heap_node;

typedef struct s_heap
{
	t_heap_node	*nodes;
	int			size;
	int			capacity;
}	t_heap;

#endif