/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   scheduler.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/07 21:17:53 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/07 21:17:53 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SCHEDULER_H
# define SCHEDULER_H

# include <pthread.h>

typedef struct s_heap		t_heap;
typedef struct s_coder		t_coder;

typedef enum e_scheduler_type
{
	SC_FIFO,
	SC_EDF
}	t_scheduler_type;

typedef struct s_scheduler
{
	t_scheduler_type	type;

	t_heap				*heap;

	pthread_mutex_t		mutex;
	pthread_cond_t		condition;
}	t_scheduler;

#endif