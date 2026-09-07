#ifndef CODEXION_H
# define CODEXION_H

# include <pthread.h>
# include <sys/time.h>
# include <stdlib.h>
# include <stdio.h>
# include <unistd.h>
# include <string.h>


typedef struct s_coder		t_coder;
typedef struct s_dongle	t_dongle;
typedef struct s_heap		t_heap;
typedef struct s_scheduler	t_scheduler;
typedef struct s_simulation	t_simulation;

struct s_simulation
{
	int					number_of_coders;

	long				time_to_burnout;
	long				time_to_compile;
	long				time_to_debug;
	long				time_to_refactor;

	int					number_of_compiles_required;
	long				dongle_cooldown;
	t_scheduler_type	scheduler_type;

	t_coder				*coders;
	t_dongle			*dongles;
	t_scheduler			*scheduler;

	pthread_mutex_t		state_mutex;
	t_logger			logger;

	int					stop;
	long				start_time;
};

#endif