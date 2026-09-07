/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <hloutman@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/07 21:11:51 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/07 21:29:17 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	init_simulation(t_simulation sim)
{
	int	i;

	i = 0;
	while (i < sim->nbr_coders)
	{
		
		i++;
	}
}


int	init_simulation(t_simulation *sim, t_config *config)
{
	sim->coders = malloc(sizeof(t_coder) * sim->nbr_coders);
	if (!sim->coders)
	{
		printf("[ERROR]: coders allocation failed");
		return (0);
	}

	sim->dongles = malloc(sizeof(t_dongle) * sim->nbr_coders);
	if (!sim->dongles)
	{
		printf("[ERROR]: dongles allocation failed");
		free(sim->coders);
		return (0);
	}

	return (1);
}