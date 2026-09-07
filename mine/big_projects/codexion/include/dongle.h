#ifndef DONGLE_H
# define DONGLE_H

# include <pthread.h>

typedef struct s_dongle
{
	int				id;
	long			available_at;
	pthread_mutex_t	mutex;

}	t_dongle;

#endif