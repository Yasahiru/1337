/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_x.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/15 17:36:51 by hloutman          #+#    #+#             */
/*   Updated: 2025/12/15 17:36:52 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_put_x(unsigned int n)
{
	int		count;
	char	*hex;

	count = 0;
	hex = "0123456789abcdef";
	if (n >= 16)
	{
		count += ft_put_x(n / 16);
		count += ft_put_x(n % 16);
	}
	else
		count += ft_putchar(hex[n]);
	return (count);
}

int	ft_put_xx(unsigned int n)
{
	int		count;
	char	*hex;

	count = 0;
	hex = "0123456789ABCDEF";
	if (n >= 16)
	{
		count += ft_put_xx(n / 16);
		count += ft_put_xx(n % 16);
	}
	else
		count += ft_putchar(hex[n]);
	return (count);
}
