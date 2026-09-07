#ifndef MONITOR_H
# define MONITOR_H

# include <pthread.h>

typedef struct s_simulation	t_simulation;

typedef struct s_monitor
{
	pthread_t		thread;
	t_simulation	*simulation;
}	t_monitor;

void	*monitor_routine(void *arg);

#endif