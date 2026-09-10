/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <hloutman@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/07 21:11:51 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/10 04:12:51 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	init_coders_dongles(t_simulation *sim)
{
	int	i;

	i = 0;
	while (i < sim->nbr_coders)
	{
		sim->coders[i].id = i + 1;
		sim->coders[i].done = 0;
		sim->coders[i].left_dongle = &sim->dongles[i];
		sim->coders[i].right_dongle = &sim->dongles[
			(i + 1) % sim->nbr_coders];
		sim->coders[i].nbr_of_compilations = 0;
		sim->coders[i].sim = sim;
		sim->coders[i].last_compile = 0;
		sim->dongles[i].size = 0;
		sim->dongles[i].is_taken = 0;
		sim->dongles[i].release = 0;
		pthread_mutex_init(&sim->dongles[i].pause_dongle, NULL);
		i++;
	}
}

int	init_simulation(t_simulation *sim)
{
	sim->simulation_running = 1;
	sim->start_time = get_time_ms();
	pthread_mutex_init(&sim->pause_print, NULL);
	pthread_mutex_init(&sim->pause, NULL);
	sim->coders = malloc(sizeof(t_coder)
			* sim->nbr_coders);
	if (!sim->coders)
		return (1);
	sim->dongles = malloc(sizeof(t_dongle)
			* sim->nbr_coders);
	if (!sim->dongles)
	{
		free(sim->coders);
		return (1);
	}
	init_coders_dongles(sim);
	return (0);
}

void	clean_up_sim(t_simulation *sim)
{
	int	i;

	i = 0;
	while (i < sim->nbr_coders)
	{
		pthread_mutex_destroy(&sim->dongles[i].pause_dongle);
		i++;
	}
	pthread_mutex_destroy(&sim->pause_print);
	pthread_mutex_destroy(&sim->pause);
	free(sim->coders);
	free(sim->dongles);
}
