/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coder.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <hloutman@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/09 03:38:23 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/09 03:49:37 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	coder_routine(void	*arg)
{
	t_coder	*coder;

	coder = (t_coder *)arg;
	if (coder->id % 2 != 0)
		usleep(1000);

	while (coder->done == 0)
	{
		pthread_mutex_lock(&coder->sim->pause);
		if (coder->sim->simulation_running == 0)
		{
			pthread_mutex_unlock(&coder->sim->pause);
			break;
		}
		pthread_mutex_lock(&coder->sim->pause);
		if (!compile(coder))
			break;
		debug(coder);
		refactor(coder);
	}
	return (NULL);
}

void	coder_sleep(t_coder *coder, long duration)
{
	long	start;

	start = get_time_ms();
	while (get_time_ms() - start < duration)
	{
		pthread_mutex_lock(&coder->sim->pause);
		if (coder->sim->simulation_running == 0)
		{
			pthread_mutex_unlock(&coder->sim->pause);
			break;
		}
		pthread_mutex_unlock(&coder->sim->pause);
		usleep(1000);
	}
}

long	get_time_ms(void)
{
	struct timeval	tv;

	gettimeofday(&tv, NULL);
	return (tv.tv_sec * 1000 + tv.tv_usec / 1000);
}
