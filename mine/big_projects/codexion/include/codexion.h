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

# include "scheduler.h"
# include "logger.h"
# include "monitor.h"

typedef struct s_coder		t_coder;
typedef struct s_dongle		t_dongle;
typedef struct s_heap		t_heap;
typedef struct s_scheduler	t_scheduler;
typedef struct s_simulation	t_simulation;

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
	t_scheduler			*scheduler;

	pthread_mutex_t		state_mutex;
	t_logger			logger;

	int					stop;
	long				start_time;
	t_monitor			monitor;
};

int		parse_arguments(int argc, char **argv, t_simulation *simulation);

int		init_simulation(t_simulation *sim);
void	init_coders_dongles(t_simulation *sim);
void	clean_up_sim(t_simulation *sim);

#endif
