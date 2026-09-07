/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   monitor.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/07 21:17:39 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/07 21:17:40 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef MONITOR_H
# define MONITOR_H

# include <pthread.h>

typedef struct s_simulation	t_simulation;

typedef struct s_monitor
{
	pthread_t		thread;
	t_simulation	*simulation;
}	t_monitor;

void	*monitor_routine(void *arg);

#endif
