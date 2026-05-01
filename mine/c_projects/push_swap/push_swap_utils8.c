/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_utils8.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 01:49:04 by hloutman          #+#    #+#             */
/*   Updated: 2026/01/27 01:49:15 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_give_index(t_stack **a)
{
	int		count;
	t_stack	*node;
	t_stack	*node2;

	count = 0;
	node2 = *a;
	while (node2)
	{
		node = *a;
		count = 0;
		while (node)
		{
			if (node2->value > node->value)
				count++;
			node = node->next;
		}
		node2->index = count;
		node2 = node2->next;
	}
}

void	show_arr(t_stack *head)
{
	while (head)
	{
		if (!(head->next))
		{
			printf(" %ld[%d]", head->value, head->index);
			return ;
		}
		printf(" %ld[%d]", head->value, head->index);
		head = head->next;
	}
}

void	free_arr(char **arr)
{
	size_t	i;

	i = 0;
	while (arr[i])
	{
		free(arr[i]);
		i++;
	}
	free(arr);
}
