/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 01:00:56 by hloutman          #+#    #+#             */
/*   Updated: 2025/10/19 01:04:21 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	unsigned char	*destination;
	unsigned char	*srcs;
	size_t			i;

	i = 0;
	if (!dest || !src)
		return (NULL);
	destination = (unsigned char *)dest;
	srcs = (unsigned char *)src;
	while (i < n)
	{
		*destination++ = *srcs++;
		i++;
	}
	return (dest);
}
