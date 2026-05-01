/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/15 17:35:34 by hloutman          #+#    #+#             */
/*   Updated: 2025/12/15 17:35:36 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	format_check(char c, va_list list)
{
	int	count;

	count = 0;
	if (c == 'c')
		count += ft_putchar(va_arg(list, int));
	else if (c == 's')
		count += ft_putstr(va_arg(list, char *));
	else if (c == 'p')
		count += ft_put_p(va_arg(list, void *));
	else if (c == 'i' || c == 'd')
		count += ft_putnbr(va_arg(list, int));
	else if (c == 'u')
		count += ft_put_u(va_arg(list, unsigned int));
	else if (c == 'x')
		count += ft_put_x(va_arg(list, unsigned int));
	else if (c == 'X')
		count += ft_put_xx(va_arg(list, unsigned int));
	else if (c == '%')
		count += ft_putchar('%');
	return (count);
}

int	ft_printf(const char *format, ...)
{
	int (total), (i);
	va_list(args);
	total = 0;
	i = 0;
	va_start(args, format);
	while (format[i])
	{
		if (format[i] == '%')
		{
			i++;
			total += format_check(format[i], args);
		}
		else
			total += ft_putchar(format[i]);
		i++;
	}
	return (total);
}
