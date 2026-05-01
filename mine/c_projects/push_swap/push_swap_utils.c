/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/31 15:19:00 by hloutman          #+#    #+#             */
/*   Updated: 2025/12/31 15:19:02 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_stack	*create_stack_a(char **arr)
{
	t_stack	*last_node;
	t_stack	*node;
	t_stack	*head;
	long	number;

	head = NULL;
	number = ft_atoi(*arr);
	head = ft_lstnew(number);
	head->previous = NULL;
	arr++;
	while (*arr)
	{
		number = ft_atoi(*arr);
		node = ft_lstnew(number);
		last_node = ft_lstlast(head);
		node->previous = last_node;
		ft_lstadd_back(&head, node);
		arr++;
	}
	ft_give_index(&head);
	return (head);
}

int	is_repeated(t_stack **a, int number)
{
	t_stack	*node;
	int		count;

	count = 0;
	node = (*a);
	while (node)
	{
		if (node->value == number)
			count++;
		node = node->next;
	}
	if (count > 1)
		return (1);
	return (0);
}

int	second_check(t_stack **a)
{
	t_stack	*node;

	node = (*a);
	while (node)
	{
		if (is_repeated(a, node->value))
			return (0);
		node = node->next;
	}
	return (1);
}

char	*join_args(int ac, char **av)
{
	int		i;
	char	*joined_args;
	char	*temp;

	i = 0 ;
	joined_args = NULL;
	temp = NULL;
	while (i < ac - 1)
	{
		if (av[i][0] == '\0')
			return (NULL);
		temp = ft_strjoin(joined_args, av[i]);
		free(joined_args);
		joined_args = ft_strjoin(temp, " ");
		free(temp);
		i++;
	}
	return (joined_args);
}

int	is_overflow(long num)
{
	if (num > INT_MAX || num < INT_MIN)
		return (1);
	return (0);
}
