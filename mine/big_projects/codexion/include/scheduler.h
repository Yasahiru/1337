#ifndef SCHEDULER_H
# define SCHEDULER_H

# include <pthread.h>

typedef struct s_heap		t_heap;
typedef struct s_coder		t_coder;
typedef enum e_scheduler_type	t_scheduler_type;

typedef struct s_scheduler
{
	t_scheduler_type	type;

	t_heap				*heap;

	pthread_mutex_t		mutex;
	pthread_cond_t		condition;
}	t_scheduler;

#endif