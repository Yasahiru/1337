/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   work.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <hloutman@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/09 03:50:31 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/09 04:08:44 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	print_took_dongles(t_coder *coder)
{
	long	ts;

	pthread_mutex_lock(&coder->sim->pause_print);
	ts = get_time_ms() - coder->sim->start_time;
	printf("%ld %d has taken a dongle\n", ts, coder->id);
	printf("%ld %d has taken a dongle\n", ts, coder->id);
	pthread_mutex_unlock(&coder->sim->pause_print);
}

static int  take_dongles(t_coder    *coder)
{
    if (coder->id % 2 == 0)
    {
        if (!take_dongle(coder, coder->left_dongle))
            return (0);
        if (!take_dongle(coder, coder->right_dongle))
        {
            release_dongle(coder->left_dongle);
            return (0);
        }
    }
    else
    {
        if (take_dongle(code, code->right_dongle))
            return (0);
        if (take_dongle(coder, coder->left_dongle))
		{
			release_dongle(coder->right_dongle);
			return (1);
		}
    }
    print_took_dongles(coder);
	return (1);
}

//compile / debug / refactor
