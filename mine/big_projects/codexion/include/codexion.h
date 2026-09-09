/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/07 21:16:18 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/07 21:16:20 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef CODEXION_H
# define CODEXION_H

# include <pthread.h>
# include <sys/time.h>
# include <stdlib.h>
# include <stdio.h>
# include <unistd.h>
# include <string.h>

typedef struct s_request t_request;
typedef struct s_dongle t_dongle;
typedef struct s_coder t_coder;
typedef struct s_simulation t_simulation;

typedef struct s_request
{
	int		id;
	long	deadline;
}	t_request;

typedef struct s_dongle
{
	pthread_mutex_t	pause_dongle;
	t_request		quee[2];
	int				size;
	int				is_taken;
	long			release;
}	t_dongle;

typedef enum e_scheduler_type
{
	SC_FIFO,
	SC_EDF
}	t_scheduler_type;

typedef struct s_coder
{
	int				id;
	int				done;
	pthread_t		thread;
	t_dongle		*left_dongle;
	t_dongle		*right_dongle;
	long			last_compile;
	int				nbr_of_compilations;
	t_simulation	*sim;

}	t_coder;

struct s_simulation
{
	int					nbr_coders;
	long				time_to_burnout;
	long				time_to_compile;
	long				time_to_debug;
	long				time_to_refactor;
	int					number_of_compiles_required;
	long				dongle_cooldown;
	t_scheduler_type	scheduler_type;

	t_coder				*coders;
	t_dongle			*dongles;

	pthread_mutex_t		pause_print;
	pthread_mutex_t		pause;

	int					simulation_running;
	long				start_time;
};

int			parse_arguments(int argc, char **argv, t_simulation *simulation);

int			init_simulation(t_simulation *sim);
void		init_coders_dongles(t_simulation *sim);
int			init_scheduler(t_simulation *sim);
void		clean_up_sim(t_simulation *sim);

void		*coder_routine(void *arg);
int			take_dongle(t_coder *coder, t_dongle *dongle);
void		release_dongle(t_dongle *dongle);
long		get_time_ms(void);

void		insert_heap(t_dongle *dongle, t_request info);
void		insert_down(t_dongle *dongle);
t_request	pop_heap(t_dongle *dongle);

int			compile(t_coder *coder);
void		debug(t_coder *coder);
void		refactor(t_coder *coder);

void		*monitor_routine(void *arg);
void		coder_sleep(t_coder *coder, long duration);

#endif
