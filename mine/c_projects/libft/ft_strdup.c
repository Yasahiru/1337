/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 23:54:06 by hloutman          #+#    #+#             */
/*   Updated: 2025/10/19 00:00:55 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static size_t	ft_strlen1(const char *str)
{
	size_t	i;

	i = 0;
	while (str && str[i])
		i++;
	return (i);
}

char	*ft_strdup(const char *s)
{
	char	*newstr;
	int		size;
	int		i;

	size = ft_strlen1(s);
	newstr = malloc(sizeof(char) * (size + 1));
	if (!newstr)
		return (NULL);
	i = 0;
	while (s[i])
	{
		newstr[i] = s[i];
		i++;
	}
	newstr[i] = '\0';
	return (newstr);
}
