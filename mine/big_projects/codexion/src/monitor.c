/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   monitor.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <hloutman@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/09 18:30:28 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/09 18:34:13 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	check_burnout(t_simulation *sim, int i)
{
	long	last;
	long	start;
	int		burned_out;
	int		coder_id;

	burned_out = 0;
	pthread_mutex_lock(&sim->pause_print);
	pthread_mutex_lock(&sim->pause);
	last = sim->coders[i].last_compile;
	if (last == 0)
		last = sim->start_time;
	if (sim->coders[i].done == 0
		&& get_time_ms() - last > sim->time_to_burnout)
	{
		sim->simulation_running = 0;
		burned_out = 1;
	}
	coder_id = sim->coders[i].id;
	start = sim->start_time;
	pthread_mutex_unlock(&sim->pause);
	if (burned_out)
		printf("%ld %d burned out\n",
			get_time_ms() - start, coder_id);
	pthread_mutex_unlock(&sim->pause_print);
	return (burned_out);
}

static int	check_coders(t_simulation *sim)
{
	int	i;
	int	done_count;

	i = 0;
	done_count = 0;
	while (i < sim->nbr_coders)
	{
		if (check_burnout(sim, i))
			return (-1);
		pthread_mutex_lock(&sim->pause);
		if (sim->coders[i].done == 1)
			done_count++;
		pthread_mutex_unlock(&sim->pause);
		i++;
	}
	return (done_count);
}

void	*monitor_routine(void *arg)
{
	t_simulation	*sim;
	int				done_count;

	sim = (t_simulation *)arg;
	while (1)
	{
		pthread_mutex_lock(&sim->pause);
		if (sim->simulation_running == 0)
			return (pthread_mutex_unlock(&sim->pause), NULL);
		pthread_mutex_unlock(&sim->pause);
		usleep(1000);
		done_count = check_coders(sim);
		if (done_count == -1)
			return (NULL);
		if (done_count == sim->nbr_coders)
		{
			pthread_mutex_lock(&sim->pause);
			sim->simulation_running = 0;
			pthread_mutex_unlock(&sim->pause);
			return (NULL);
		}
	}
}
