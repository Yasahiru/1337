/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_put_p.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/15 17:54:12 by hloutman          #+#    #+#             */
/*   Updated: 2025/12/15 17:54:14 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putptr(unsigned long m)
{
	int				count;
	char			*hex;
	unsigned long	n;

	n = (unsigned long)m;
	count = 0;
	hex = "0123456789abcdef";
	if (n >= 16)
		count += ft_putptr(n / 16);
	count += ft_putchar(hex[n % 16]);
	return (count);
}

int	ft_put_p(void *ptr)
{
	int				count;
	unsigned long	ptr2;

	ptr2 = (unsigned long)ptr;
	count = 0;
	if (!ptr)
		return (ft_putstr("(nil)"));
	count += ft_putstr("0x");
	count += ft_putptr(ptr2);
	return (count);
}
