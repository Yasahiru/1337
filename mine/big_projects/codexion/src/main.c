/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <hloutman@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/06 17:08:48 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/06 23:55:29 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	main(int ac, char **av)
{
	t_simulation	simulation;

	if (ac < 4)
		return (0);
	if (!parse_arguments(ac, av, &simulation))
		return (1);
	if (!init_simulation(&simulation))
		return (1);
	if (!run_simulation(&simulation))
		return (1);
	cleanup_simulation(&simulation);
	return (0);
}
