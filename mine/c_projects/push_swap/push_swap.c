/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/07 16:33:35 by hloutman          #+#    #+#             */
/*   Updated: 2026/01/07 16:33:37 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	clear_and_exit(char *str, char **arr, t_stack **stack)
{
	if (str)
		free(str);
	if (arr)
		free_arr(arr);
	if (stack)
		ft_lstclear(stack);
}

void	ft_exit(char *str, char **arr, t_stack **stack)
{
	clear_and_exit(str, arr, stack);
	write(2, "Error\n", 6);
	return ;
}

void	ft_push_min(t_stack **a, t_stack **b)
{
	int		min;
	int		pos;
	int		i;
	t_stack	*node;

	i = 1;
	min = 2147483647;
	pos = 0;
	node = *a;
	while (node)
	{
		if (min > node->value)
			min = node->value;
		node = node->next;
	}
	while (*a)
	{
		if ((*a)->value == min)
		{
			pb(a, b);
			return ;
		}
		ra(a);
	}
}

int	is_good(t_stack **a)
{
	if (!second_check(a))
		return (0);
	if (ft_is_sorted(a))
		return (1);
	return (2);
}

int	main(int ac, char **av)
{
	char		**joined_args;
	int			i;
	char		*args;
	t_stack		*a;
	t_stack		*b;

	i = 0;
	if (ac < 2)
		return (0);
	b = NULL;
	args = join_args(ac, av + 1);
	if (!args)
		return (ft_exit(NULL, NULL, NULL), 0);
	joined_args = ft_split(args, ' ');
	if (!edge_cases(joined_args))
		return (ft_exit(args, joined_args, NULL), 0);
	else if (edge_cases(joined_args) == 1)
		return (0);
	a = create_stack_a(joined_args);
	if (is_good(&a) == 1)
		return (clear_and_exit(args, joined_args, &a), 0);
	else if (is_good(&a) == 0)
		return (ft_exit(args, joined_args, &a), 0);
	ft_auto_sort(ft_lstsize(a), &a, &b);
	clear_and_exit(args, joined_args, &a);
}
