/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   coder.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/09/07 21:16:27 by hloutman          #+#    #+#             */
/*   Updated: 2026/09/07 21:16:28 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef CODER_H
# define CODER_H

# include <pthread.h>
# include "dongle.h"

typedef struct s_simulation	t_simulation;

typedef enum e_coder_state
{
	CODER_WAITING,
	CODER_COMPILING,
	CODER_DEBUGGING,
	CODER_REFACTORING,
	CODER_DONE,
	CODER_BURNED_OUT
}	t_coder_state;

typedef struct s_coder
{
	int				id;

	pthread_t		thread;
	t_dongle		*left_dongle;
	t_dongle		*right_dongle;

	int				compile_count;
	long			last_compile_start;
	long			deadline;

	t_coder_state	state;
	t_simulation	*simulation;
}	t_coder;

void	*coder_routine(void *arg);

#endif
