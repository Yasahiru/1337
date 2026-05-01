/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/26 22:33:47 by hloutman          #+#    #+#             */
/*   Updated: 2025/10/26 22:33:48 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_lstsize(t_list *lst)
{
	if (!lst)
		return (0);
	if (lst->next)
		return (1 + ft_lstsize(lst->next));
	return (1);
}

// if (!(lst->next))
	// 	return (1);
	// return (1 + ft_lstsize(lst->next));