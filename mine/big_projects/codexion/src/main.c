/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <hloutman@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/06 17:08:48 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/11 16:02:34 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	main(int ac, char **av)
{
	t_simulation	sim;
	int				i;
	pthread_t		monitor;

	if (!parse_arguments(ac, av, &sim))
		return (1);
	if (init_simulation(&sim))
		return (1);
	pthread_create(&monitor, NULL, monitor_routine, &sim);
	i = 0;
	while (i < sim.nbr_coders)
	{
		pthread_create(&sim.coders[i].thread, NULL,
			coder_routine, &sim.coders[i]);
		i++;
	}
	i = 0;
	while (i < sim.nbr_coders)
	{
		pthread_join(sim.coders[i].thread, NULL);
		i++;
	}
	pthread_join(monitor, NULL);
	clean_up_sim(&sim);
	return (0);
}
