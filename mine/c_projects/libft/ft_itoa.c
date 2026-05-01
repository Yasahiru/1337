/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 01:42:39 by hloutman          #+#    #+#             */
/*   Updated: 2025/10/20 02:05:45 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static int	ft_numlen(int i)
{
	if (i > 9)
		return (1 + ft_numlen(i / 10));
	return (1);
}

static void	ft_fill(char *str, int num, int size)
{
	while (num > 9)
	{
		str[size - 1] = (num % 10) + '0';
		ft_fill(str, num / 10, size - 1);
		return ;
	}
	str[size - 1] = num + '0';
}

static char	*ft_min_int(void)
{
	char	*min_int;

	min_int = malloc(sizeof(char) * 12);
	min_int[0] = '-';
	min_int[1] = '2';
	min_int[2] = '1';
	min_int[3] = '4';
	min_int[4] = '7';
	min_int[5] = '4';
	min_int[6] = '8';
	min_int[7] = '3';
	min_int[8] = '6';
	min_int[9] = '4';
	min_int[10] = '8';
	min_int[11] = '\0';
	return (min_int);
}

char	*ft_itoa(int n)
{
	char	*str;

	int (size), (s);
	s = 1;
	size = 0;
	if (n <= -2147483648)
		return (ft_min_int());
	if (n < 0)
	{
		s *= -1;
		size++;
		n *= -1;
	}
	size += ft_numlen(n);
	str = malloc(sizeof(char) * (size + 1));
	if (!str)
		return (NULL);
	str[size] = '\0';
	if (s < 0)
		str[0] = '-';
	ft_fill(str, n, size);
	return (str);
}
