/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser_new.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 11:32:48 by hloutman          #+#    #+#             */
/*   Updated: 2026/01/28 11:32:50 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	check(char *s)
{
	int		i;

	i = 0;
	while (s[i])
	{
		if ((s[i] == '-' || s[i] == '+') || (s[i] >= '0' && s[i] <= '9'))
			i++;
		while (s[i])
		{
			if (s[i] < '0' || s[i] > '9')
				return (0);
			i++;
		}
	}
	return (1);
}

int	is_args_valid(char **av)
{
	int		i;
	long	number;

	i = 0;
	number = 0;
	while (*av)
	{
		if (!check(*av))
			return (0);
		number = ft_atoi(*av);
		if (is_overflow(number))
			return (0);
		av++;
	}
	return (1);
}

int	how_many(char **args)
{
	char	**joined_args;
	int		count;

	count = 0 ;
	joined_args = args;
	while (*joined_args)
	{
		if (!check(*joined_args))
			return (0);
		joined_args++;
		count++;
	}
	return (count);
}

int	edge_cases(char **args)
{
	if (!how_many(args))
		return (0);
	if (!is_args_valid(args))
		return (0);
	if (how_many(args) == 1)
		return (1);
	return (3);
}
