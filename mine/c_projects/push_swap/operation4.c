/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operration3.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/09 15:14:48 by hloutman          #+#    #+#             */
/*   Updated: 2026/01/09 15:14:50 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	rotate(t_stack **s)
{
	t_stack	*node;
	t_stack	*last_node;

	if (!s || !*s || !(*s)->next)
		return ;
	node = *s;
	last_node = ft_lstlast(*s);
	(*s)->next->previous = NULL;
	*s = (*s)->next;
	node->previous = last_node;
	node->next = NULL;
	last_node->next = node;
}

void	ra(t_stack **a)
{
	rotate(a);
	write(1, "ra\n", 3);
}

void	rb(t_stack **b)
{
	rotate(b);
	write(1, "rb\n", 3);
}

void	rr(t_stack **a, t_stack **b)
{
	ra(a);
	rb(b);
	write(1, "rr\n", 3);
}
