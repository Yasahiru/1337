/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   dongle.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <hloutman@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/09 15:20:34 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/10 04:07:12 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static long	get_deadline(t_coder	*coder)
{
	return (
		coder->last_compile + coder->sim->time_to_burnout
	);
}

static void	set_deadline(t_coder	*coder, t_request	*info)
{
	if (coder->sim->scheduler_type == SC_FIFO)
		info->deadline = get_time_ms();
	else
		info->deadline = get_deadline(coder);
}

static int	wait_dongle(t_coder	*coder, t_dongle	*dongle)
{
	while (1)
	{
		if (
			dongle->size > 0
			&& dongle->queue[0].id == coder->id
			&& dongle->is_taken == 0
			&& get_time_ms() - dongle->release
			>= coder->sim->cooldown
		)
			return (1);
		pthread_mutex_unlock(&dongle->pause_dongle);
		usleep(1000);
		pthread_mutex_lock(&coder->sim->pause);
		if (coder->sim->simulation_running == 0)
		{
			pthread_mutex_unlock(&coder->sim->pause);
			pthread_mutex_lock(&dongle->pause_dongle);
			return (0);
		}
		pthread_mutex_unlock(&coder->sim->pause);
		pthread_mutex_lock(&dongle->pause_dongle);
	}
}

int	take_dongle(t_coder	*coder, t_dongle	*dongle)
{
	t_request	info;

	pthread_mutex_lock(&dongle->pause_dongle);
	set_deadline(coder, &info);
	info.id = coder->id;
	insert_heap(dongle, info);
	if (!wait_dongle(coder, dongle))
	{
		pthread_mutex_unlock(&dongle->pause_dongle);
		return (0);
	}
	pop_heap(dongle);
	dongle->is_taken = 1;
	pthread_mutex_unlock(&dongle->pause_dongle);
	return (1);
}

void	release_dongle(t_dongle *dongle)
{
	pthread_mutex_lock(&dongle->pause_dongle);
	dongle->is_taken = 0;
	dongle->release = get_time_ms();
	pthread_mutex_unlock(&dongle->pause_dongle);
}
