/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   dongle.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/07 21:16:43 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/07 21:16:45 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef DONGLE_H
# define DONGLE_H

# include <pthread.h>

typedef struct s_dongle
{
	int				id;
	long			available_at;
	pthread_mutex_t	mutex;

}	t_dongle;

#endif
