/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operation1.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/08 16:17:37 by hloutman          #+#    #+#             */
/*   Updated: 2026/01/08 16:17:39 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	sa(t_stack **a)
{
	int		tmp_val;
	int		tmp_index;
	t_stack	*last_node_a;
	t_stack	*previous_node_a;

	last_node_a = *a;
	previous_node_a = last_node_a->next;
	tmp_val = last_node_a->value;
	last_node_a->value = previous_node_a->value;
	previous_node_a->value = tmp_val;
	tmp_index = last_node_a->index;
	last_node_a->index = previous_node_a->index;
	previous_node_a->index = tmp_index;
	write(1, "sa\n", 3);
}

void	sb(t_stack **b)
{
	int		tmp_val;
	int		tmp_index;
	t_stack	*last_node_a;
	t_stack	*previous_node_a;

	last_node_a = *b;
	previous_node_a = last_node_a->next;
	tmp_val = last_node_a->value;
	last_node_a->value = previous_node_a->value;
	previous_node_a->value = tmp_val;
	tmp_index = last_node_a->index;
	last_node_a->index = previous_node_a->index;
	previous_node_a->index = tmp_index;
	write(1, "sb\n", 3);
}

void	ss(t_stack **a, t_stack **b)
{
	sa(a);
	sb(b);
	write(1, "ss\n", 3);
}
