/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   work.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <hloutman@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/09 03:50:31 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/11 20:17:53 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

// static void	print_took_dongles(t_coder *coder)
// {
// 	long	ts;

// 	pthread_mutex_lock(&coder->sim->pause_print);
// 	ts = get_time_ms() - coder->sim->start_time;
// 	printf("%ld %d has taken a dongle\n", ts, coder->id);
// 	printf("%ld %d has taken a dongle\n", ts, coder->id);
// 	pthread_mutex_unlock(&coder->sim->pause_print);
// }

static void	print_took_dongle(t_coder *coder)
{
	long	ts;

	pthread_mutex_lock(&coder->sim->pause_print);
	ts = get_time_ms() - coder->sim->start_time;
	printf("%ld %d has taken a dongle\n", ts, coder->id);
	pthread_mutex_unlock(&coder->sim->pause_print);
}

static int	take_dongles(t_coder	*coder)
{
	if (coder->id % 2 == 0)
	{
		if (!take_dongle(coder, coder->left_dongle))
			return (0);

		print_took_dongle(coder);

		if (!take_dongle(coder, coder->right_dongle))
		{
			release_dongle(coder->left_dongle);
			return (0);
		}
		print_took_dongle(coder);
	}
	else
	{
		if (!take_dongle(coder, coder->right_dongle))
			return (0);

		print_took_dongle(coder);

		if (!take_dongle(coder, coder->left_dongle))
		{
			release_dongle(coder->right_dongle);
			return (0);
		}
		print_took_dongle(coder);
	}
	// print_took_dongles(coder);
	return (1);
}

int	compile(t_coder *coder)
{
	long	start_compile;

	if (!take_dongles(coder))
		return (0);
	start_compile = get_time_ms();
	pthread_mutex_lock(&coder->sim->pause);
	if (coder->sim->simulation_running == 0)
		return (pthread_mutex_unlock(&coder->sim->pause), 0);
	pthread_mutex_unlock(&coder->sim->pause);
	pthread_mutex_lock(&coder->sim->pause_print);
	printf("%ld %d is compiling\n",
		start_compile - coder->sim->start_time, coder->id);
	pthread_mutex_unlock(&coder->sim->pause_print);
	pthread_mutex_lock(&coder->sim->pause);
	coder->last_compile = start_compile;
	coder->nbr_of_compilations++;
	pthread_mutex_unlock(&coder->sim->pause);
	coder_sleep(coder, coder->sim->time_to_compile);
	release_dongle(coder->left_dongle);
	release_dongle(coder->right_dongle);
	return (1);
}

void	debug(t_coder *coder)
{
	long	debug_time;

	pthread_mutex_lock(&coder->sim->pause);
	if (coder->sim->simulation_running == 0)
	{
		pthread_mutex_unlock(&coder->sim->pause);
		return ;
	}
	pthread_mutex_unlock(&coder->sim->pause);
	debug_time = get_time_ms();
	pthread_mutex_lock(&coder->sim->pause_print);
	printf("%ld %d is debugging\n",
		debug_time - coder->sim->start_time, coder->id);
	pthread_mutex_unlock(&coder->sim->pause_print);
	coder_sleep(coder, coder->sim->time_to_debug);
}

void	refactor(t_coder *coder)
{
	long	refactor_time;

	pthread_mutex_lock(&coder->sim->pause);
	if (coder->sim->simulation_running == 0)
	{
		pthread_mutex_unlock(&coder->sim->pause);
		return ;
	}
	pthread_mutex_unlock(&coder->sim->pause);
	refactor_time = get_time_ms();
	pthread_mutex_lock(&coder->sim->pause_print);
	printf("%ld %d is refactoring\n",
		refactor_time - coder->sim->start_time, coder->id);
	pthread_mutex_unlock(&coder->sim->pause_print);
	coder_sleep(coder, coder->sim->time_to_refactor);
	pthread_mutex_lock(&coder->sim->pause);
	if (coder->nbr_of_compilations == coder->sim->nbr_comp_req)
		coder->done = 1;
	pthread_mutex_unlock(&coder->sim->pause);
}
