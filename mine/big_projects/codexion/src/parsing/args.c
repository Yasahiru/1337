/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   args.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <hloutman@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/06 17:12:05 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/07 00:15:07 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <codexion.h>

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

int	parse_arguments(int argc, char **argv, t_simulation *simulation)
{
	if (argc != 9)
		return (0);
	if (!is_valid_number(argv[1])
		|| !is_valid_number(argv[2])
		|| !is_valid_number(argv[3])
		|| !is_valid_number(argv[4])
		|| !is_valid_number(argv[5])
		|| !is_valid_number(argv[6])
		|| !is_valid_number(argv[7]))
		return (0);
	if (strcmp(argv[8], "fifo") != 0 && strcmp(argv[8], "edf") != 0)
		return (0);
	simulation->number_of_coders = atoi(argv[1]);
	simulation->time_to_burnout = atoi(argv[2]);
	simulation->time_to_compile = atoi(argv[3]);
	simulation->time_to_debug = atoi(argv[4]);
	simulation->time_to_refactor = atoi(argv[5]);
	simulation->number_of_compiles_required = atoi(argv[6]);
	simulation->dongle_cooldown = atoi(argv[7]);
	if (strcmp(argv[8], "fifo") == 0)
		simulation->scheduler_type = FIFO;
	else
		simulation->scheduler_type = EDF;
	return (1);
}
