/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 16:24:41 by hloutman          #+#    #+#             */
/*   Updated: 2025/10/20 01:40:18 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

static int	ft_words(char const *str, char c)
{
	int	i;
	int	word;
	int	check;

	i = 0;
	word = 0;
	check = 0;
	while (str[i])
	{
		if (str[i] != c && !check)
		{
			check = 1;
			word += 1;
		}
		else if (str[i] == c)
		{
			check = 0;
		}
		i++;
	}
	return (word);
}

static int	ft_count(char const *s, char c, int *i)
{
	int	len;
	int	j;

	len = 0;
	while (s[*i] == c)
		*i += 1;
	j = *i;
	while (s[j] && s[j] != c)
	{
		len++;
		j++;
	}
	return (len);
}

static void	ft_copy(char const *str, int *start, char *dest, int size)
{
	int	i;

	i = 0;
	while (i < size && str[*start])
	{
		dest[i++] = str[*start];
		(*start)++;
	}
	dest[i] = '\0';
	if (str[*start] != '\0')
		*start += 1;
}

static void	ft_free1(char **arr, int y)
{
	int	i;

	i = y;
	while (i >= 0)
	{
		free(arr[i]);
		i--;
	}
	free(arr);
}

char	**ft_split(char const *s, char c)
{
	char	**arr;

	int (i), (size), (j);
	if (!s)
		return (NULL);
	arr = malloc(sizeof(char *) * (ft_words(s, c) + 1));
	if (!arr)
		return (NULL);
	i = 0;
	j = 0;
	size = 0;
	while (i < ft_words(s, c))
	{
		size = ft_count(s, c, &j);
		arr[i] = malloc(sizeof(char) * (size + 1));
		if (!arr[i])
		{
			ft_free1(arr, i);
			return (0);
		}
		ft_copy(s, &j, arr[i++], size);
	}
	arr[i] = NULL;
	return (arr);
}
