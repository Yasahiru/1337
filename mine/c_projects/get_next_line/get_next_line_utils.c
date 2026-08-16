/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/24 18:07:02 by hloutman          #+#    #+#             */
/*   Updated: 2025/12/24 18:07:03 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t	ft_strlen(const char *s)
{
	int	i;

	i = 0;
	if (!s)
		return (0);
	while (s[i])
		i++;
	return (i);
}

char	*ft_strjoin(char *s1, char *s2)
{
	char	*ptr;
	char	*tmp;

	int (len_s1), (len_s2), (i);
	if (!s1)
	{
		s1 = ft_strdup("");
		if (!s1)
			return (NULL);
	}
	if (!s2)
		s2 = "";
	len_s1 = ft_strlen(s1);
	len_s2 = ft_strlen(s2);
	ptr = malloc((len_s2 + len_s1 + 1) * sizeof(char));
	if (!ptr)
		return (free(s1), NULL);
	tmp = ptr;
	i = 0;
	while (*(s1 + i))
		*tmp++ = (char)s1[i++];
	while (*s2)
		*tmp++ = (char)*s2++;
	return ((*tmp = '\0'), (free(s1)), (ptr));
}

char	*ft_strdup(const char *s)
{
	char	*str;

	int (len_s), (i);
	len_s = ft_strlen(s);
	i = 0;
	if (!s)
		return (NULL);
	str = malloc((len_s + 1) * sizeof(char));
	if (!str)
		return (NULL);
	while (i < len_s)
	{
		*(str + i) = *(s + i);
		i++;
	}
	*(str + i) = '\0';
	return (str);
}

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*ptr;

	unsigned int (len_s), (i);
	i = 0;
	if (s == NULL)
		return (NULL);
	len_s = ft_strlen(s);
	if (start >= len_s)
		return (ft_strdup(""));
	if (len > len_s - start)
		len = len_s - start;
	ptr = malloc((len + 1) * sizeof(char));
	if (!ptr)
		return (NULL);
	while (i < len)
	{
		*(ptr + i) = *(s + i + start);
		i++;
	}
	*(ptr + i) = '\0';
	return (ptr);
}

char	*ft_strchr(const char *s, int c)
{
	if (!s)
		return (NULL);
	while (*s)
	{
		if (*s == (unsigned char)c)
			return ((char *)s);
		s++;
	}
	if ((unsigned char)c == '\0')
		return ((char *)s);
	return (NULL);
}
