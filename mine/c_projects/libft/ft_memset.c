/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 01:06:19 by hloutman          #+#    #+#             */
/*   Updated: 2025/10/19 01:09:20 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*ft_memset(void *dest, int c, size_t count)
{
	unsigned char	*destt;
	unsigned char	ch;
	size_t			i;

	i = 0;
	if (!dest)
		return (NULL);
	if (count == 0)
		return (dest);
	destt = (unsigned char *)dest;
	ch = (unsigned char)c;
	while (i < count)
	{
		destt[i] = ch;
		i++;
	}
	return (dest);
}
