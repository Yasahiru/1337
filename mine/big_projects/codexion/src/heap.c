/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   heap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <hloutman@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/10 03:50:35 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/11 18:26:26 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static int	has_priority(t_request a, t_request b)
{
	if (a.deadline != b.deadline)
		return (a.deadline < b.deadline);
	return (a.id < b.id);
}

void	insert_heap(t_dongle *dongle, t_request info)
{
	t_request	tmp;

	dongle->queue[dongle->size] = info;
	if (dongle->size == 1
		&& has_priority(dongle->queue[1], dongle->queue[0]))
	{
		tmp = dongle->queue[0];
		dongle->queue[0] = dongle->queue[1];
		dongle->queue[1] = tmp;
	}
	dongle->size++;
}

t_request	pop_heap(t_dongle *dongle)
{
	t_request	result;

	result = dongle->queue[0];
	if (dongle->size == 2)
		dongle->queue[0] = dongle->queue[1];
	dongle->size--;
	return (result);
}
