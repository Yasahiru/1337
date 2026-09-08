/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <hloutman@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/07 21:11:51 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/08 13:04:05 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	init_simulation(t_simulation *sim)
{
	// sim scheduler !!!
	if (pthread_mutex_init(&sim->state_mutex, NULL) != 0)
	{
		printf("[ERROR]: Mutext init failed at state mutex\n");
		return (0);
	}

	sim->coders = malloc(sizeof(t_coder) * sim->nbr_coders);
	if (!sim->coders)
	{
		printf("[ERROR]: coders allocation failed\n");
		return (0);
	}
	sim->dongles = malloc(sizeof(t_dongle) * sim->nbr_coders);
	if (!sim->dongles)
	{
		printf("[ERROR]: dongles allocation failed\n");
		free(sim->coders);
		return (0);
	}
	return (1);
}

void	init_coders_dongles(t_simulation *sim)
{
	int	i;

	i = 0;
	while (i < sim->nbr_coders)
	{
		sim->coders[i].id = i + 1;
		// coders
		sim->coders[i].left_dongle = &sim->dongles[i];
		sim->coders[i].right_dongle = &sim->dongles[(i + 1) % sim->nbr_coders];
		sim->coders[i].compile_count = 0;
		sim->coders[i].last_compile_start = 0;
		sim->coders[i].deadline = 0;
		sim->coders[i].state_mutex = CODER_WAITING;
		sim->coders[i].simulation = sim;
		//dongles
		sim->dongles[i].id = i;
		sim->dongles[i].available_at = 0;
		pthread_mutex_init(&sim->dongles[i].mutex, NULL);
		i++;
	}
}

void	clean_up_sim(t_simulation *sim)
{
	int	i;

	i = 0;
	while (i < sim->nbr_coders)
	{
		pthread_mutex_destroy(&sim->dongles[i].mutex);
		i++;
	}
	pthread_mutex_destroy(&sim->state_mutex);
	free(sim->coders);
	free(sim->dongles);
}
