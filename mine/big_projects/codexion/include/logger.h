#ifndef LOGGER_H
# define LOGGER_H

# include <pthread.h>

typedef struct s_logger
{
	pthread_mutex_t	mutex;
}	t_logger;

#endif