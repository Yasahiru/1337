/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/15 17:35:45 by hloutman          #+#    #+#             */
/*   Updated: 2025/12/15 17:35:47 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <stdio.h>
# include <unistd.h>

int	ft_put_p(void *n);
int	ft_put_u(unsigned int n);
int	ft_put_x(unsigned int n);
int	ft_put_xx(unsigned int n);
int	ft_printf(const char *format, ...);
int	ft_putchar(char c);
int	ft_putnbr(int n);
int	ft_putstr(char *s);

#endif
