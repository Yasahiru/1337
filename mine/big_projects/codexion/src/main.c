/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <hloutman@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/06 17:08:48 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/09 03:19:58 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	main(int ac, char **av)
{
	t_simulation	sim;

	if (ac != 9)
	{
		printf("Not Enough arguments!!\n");
		return (0);
	}
	if (!parse_arguments(ac, av, &sim))
	{
		printf("[Main.c]: parsing error\n");
		return (1);
	}
	if (!init_simulation(&sim))
	{
		printf("[Main.c]: init simulation error\n");
		return (1);
	}
	return (0);
}

	// printf("nbr coders: %d\nburnout: %ld\ncompile: %ld\ndebug:
	//  %ld\nrefactor: %ld\ncompile times: %d\ncooldown: %ld\nsched
	//  type: %u", sim.nbr_coders, sim.time_to_burnout, sim.time_to_compile, 
	// sim.time_to_debug, sim.time_to_refactor,sim.number_of_compiles_required,
	//  sim.dongle_cooldown, sim.scheduler_type);

	// if (!run_simulation(&simulation))
	// {
	// 	printf("[Main.c]: run simulation error\n");
	// 	return (1);
	// }
	// cleanup_simulation(&simulation);