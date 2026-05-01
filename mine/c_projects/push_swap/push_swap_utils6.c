/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_utils6.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/13 16:37:59 by hloutman          #+#    #+#             */
/*   Updated: 2026/01/13 16:38:02 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_is_sorted(t_stack **a)
{
	t_stack	*node;
	t_stack	*next;

	node = *a;
	next = node->next;
	while (next)
	{
		if (node->value > next->value)
			return (0);
		node = next;
		next = next->next;
	}
	return (1);
}
