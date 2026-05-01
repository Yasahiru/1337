/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operation2.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/04 13:30:41 by hloutman          #+#    #+#             */
/*   Updated: 2026/01/04 13:30:44 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	push(t_stack **a, t_stack **b)
{
	t_stack	*node;

	node = *a;
	if (!a || !b || !*a)
		return ;
	if (!(*a)->next)
		*a = NULL;
	else
	{
		(*a)->next->previous = NULL;
		*a = (*a)->next;
	}
	if (!*b)
	{
		*b = node;
		node->next = NULL;
		node->previous = NULL;
	}
	else
	{
		(*b)->previous = node;
		node->previous = NULL;
		node->next = *b;
		*b = node;
	}
}

void	pb(t_stack **stack_a, t_stack **b)
{
	push(stack_a, b);
	write(1, "pb\n", 3);
}

void	pa(t_stack **a, t_stack **b)
{
	push(b, a);
	write(1, "pa\n", 3);
}
