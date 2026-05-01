/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 00:06:40 by hloutman          #+#    #+#             */
/*   Updated: 2025/10/19 00:10:04 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

int	ft_isdigit(int c)
{
	return (c >= '0' && c <= '9');
}

static int	ft_is_overflow(long number, int digit, int sign, int *res)
{
	*res = 0;
	if (number > (LONG_MAX - digit) / 10)
	{
		if (sign > 0)
			*res = -1;
		else
			*res = 0;
		return (1);
	}
	return (0);
}

long	ft_atoi(const char *str)
{
	long	number;

	int (sign), (i), (digit), (res);
	number = 0;
	i = 0;
	sign = 1;
	while ((str[i] >= 9 && str[i] <= 13) || str[i] == 32)
		i++;
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			sign *= -1;
		i++;
	}
	while (str[i] >= '0' && str[i] <= '9')
	{
		digit = str[i++] - '0';
		if (ft_is_overflow(number, digit, sign, &res))
			return (res);
		number = number * 10 + digit;
	}
	if ((number * sign) >= -2147483648 || (number * sign) <= 2147483647)
		return (number * sign);
	return (21474836478);
}

size_t	ft_strlen(const char *str)
{
	size_t	i;

	i = 0;
	if (!str)
		return (0);
	while (str && str[i])
		i++;
	return (i);
}

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	size_t	i;

	i = 0;
	while (i < n && (s1[i] && s2[i]))
	{
		if (s1[i] == s2[i])
			i++;
		else
			return ((unsigned char)s1[i] - (unsigned char)s2[i]);
	}
	if (i == n)
		return (0);
	return ((unsigned char)s1[i] - (unsigned char)s2[i]);
}
