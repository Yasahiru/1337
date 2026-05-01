/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 00:01:19 by hloutman          #+#    #+#             */
/*   Updated: 2025/10/19 00:06:23 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
	void	*array;

	if (nmemb != 0 && size > SIZE_MAX / nmemb)
		return (NULL);
	array = malloc(size * nmemb);
	if (!array)
		return (NULL);
	ft_memset(array, 0, size * nmemb);
	return (array);
}
