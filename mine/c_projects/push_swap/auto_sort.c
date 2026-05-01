/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   auto_sort.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/23 15:44:22 by hloutman          #+#    #+#             */
/*   Updated: 2026/01/23 15:44:23 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_auto_2(t_stack **stack_a)
{
	sa(stack_a);
}

void	ft_auto_3(t_stack **a)
{
	int (f), (s), (t);
	f = (*a)->value;
	s = (*a)->next->value;
	t = (*a)->next->next->value;
	if (f < s && s < t)
		return ;
	else if (f > s && s < t && f < t)
		sa(a);
	else if (f < s && s > t && f < t)
	{
		sa(a);
		ra(a);
	}
	else if (f > s && s > t && f > t)
	{
		sa(a);
		rra(a);
	}
	else if (f < s && s > t && f > t)
		rra(a);
	else if (f > s && s < t && f > t)
		ra(a);
}

void	ft_auto_4(t_stack **a, t_stack **b)
{
	ft_push_min(a, b);
	ft_auto_3(a);
	pa(a, b);
}

void	ft_auto_5(t_stack **a, t_stack **b)
{
	ft_push_min(a, b);
	ft_auto_4(a, b);
	pa(a, b);
}
