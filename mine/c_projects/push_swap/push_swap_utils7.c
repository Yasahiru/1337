/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_utils7.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 01:53:00 by hloutman          #+#    #+#             */
/*   Updated: 2026/01/27 01:53:01 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_find_max(t_stack **a)
{
	int		max;
	int		pos;
	int		i;
	t_stack	*node;

	i = 1;
	max = (*a)->value;
	pos = 0;
	node = *a;
	while (node)
	{
		if (max < node->value)
			max = node->value;
		node = node->next;
	}
	return (max);
}

int	convert_base_2(int number)
{
	int	i;

	i = 0;
	while (number >> i)
		i++;
	return (i);
}
