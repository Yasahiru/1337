/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <hloutman@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/06 17:08:48 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/07 21:15:22 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <codexion.h> 

int	main(int ac, char **av)
{
	t_simulation	simulation;

	if (ac != 9)
	{
		printf("Not Enough arguments!!\n");
		return (0);
	}
	if (!parse_arguments(ac, av, &simulation))
	{
		printf("[Main.c]: parsing error\n");
		return (1);
	}
	if (!init_simulation(&simulation))
	{
		printf("[Main.c]: init simulation error\n");
		return (1);
	}
	return (0);
}

	// if (!run_simulation(&simulation))
	// {
	// 	printf("[Main.c]: run simulation error\n");
	// 	return (1);
	// }
	// cleanup_simulation(&simulation);