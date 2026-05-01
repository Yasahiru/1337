/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/31 16:07:25 by hloutman          #+#    #+#             */
/*   Updated: 2025/12/31 23:01:04 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_free(t_stack *lst)
{
	if (lst)
	{
		ft_free(lst->next);
		free(lst);
	}
}

void	ft_auto_sort(int len, t_stack **a, t_stack **b)
{
	if (len == 2)
		ft_auto_2(a);
	else if (len == 3)
		ft_auto_3(a);
	else if (len == 4)
		ft_auto_4(a, b);
	else if (len == 5)
		ft_auto_5(a, b);
	else
		ft_final_sort(a, b);
}

int	find_biggest(t_stack *head)
{
	int		big;
	t_stack	*tmp;

	big = INT_MIN;
	tmp = head;
	while (tmp)
	{
		if (tmp->index > big)
			big = tmp->index;
		tmp = tmp->next;
	}
	return (big);
}

void	ft_final_sort(t_stack **a, t_stack **b)
{
	int	biggest_nbr;
	int	max_bits;
	int	i;
	int	j;

	biggest_nbr = find_biggest(*a);
	max_bits = convert_base_2(biggest_nbr);
	i = 0;
	while (i < max_bits)
	{
		j = 0;
		while (j <= biggest_nbr)
		{
			if (((*a)->index) >> i & 1)
				ra(a);
			else
				pb(a, b);
			j++;
		}
		while ((*b))
			pa(a, b);
		i++;
	}
}
