/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   args.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <hloutman@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/06 17:12:05 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/11 16:03:26 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	is_valid_number(char *str)
{
	int	i;

	if (!str || !str[0])
		return (0);
	i = 0;
	while (str[i])
	{
		if (str[i] < '0' || str[i] > '9')
			return (0);
		i++;
	}
	return (1);
}

int	parse_arguments(int ac, char **av, t_simulation *sim)
{
	int	i;

	if (ac != 9)
		return (0);
	i = 1;
	while (i <= 7)
	{
		if (!is_valid_number(av[i]))
			return (0);
		i++;
	}
	if (strcmp(av[8], "fifo") != 0 && strcmp(av[8], "edf") && strcmp(av[8], "lifo") != 0)
		return (0);
	sim->nbr_coders = atoi(av[1]);
	sim->time_to_burnout = atoi(av[2]);
	sim->time_to_compile = atoi(av[3]);
	sim->time_to_debug = atoi(av[4]);
	sim->time_to_refactor = atoi(av[5]);
	sim->nbr_comp_req = atoi(av[6]);
	sim->cooldown = atoi(av[7]);
	if (strcmp(av[8], "fifo") == 0)
		sim->scheduler_type = SC_FIFO;
	else if (strcmp(av[8], "edf") == 0)
		sim->scheduler_type = SC_EDF;
	else
		sim->scheduler_type = SC_LIFO;
	return (1);
}
