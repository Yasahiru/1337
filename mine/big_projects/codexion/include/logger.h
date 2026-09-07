/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   logger.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/07 21:17:27 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/07 21:17:28 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LOGGER_H
# define LOGGER_H

# include <pthread.h>

typedef struct s_logger
{
	pthread_mutex_t	mutex;
}	t_logger;

#endif
