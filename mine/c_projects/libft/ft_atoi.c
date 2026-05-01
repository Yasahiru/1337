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
#include "libft.h"

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

int	ft_atoi(const char *str)
{
	long	number;

	int (sign), (i), (digit), (res);
	number = 0;
	i = 0;
	sign = 1;
	while ((str[i] >= 7 && str[i] <= 13) || str[i] == 32)
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
	return (number * sign);
}

// #include <stdio.h>
// int main(){
// 	int x = ft_atoi("-1234567899");
// 	int y = ft_atoi("-1234567899");
// 	printf("mine %d", x);
// 	printf("original %d", y);
// }
//
// #include <stdio.h>
// #include <stdlib.h>
// int	main(void)
// {
// 	const char *tests[] = {
// 		"0",
// 		"42",
// 		"-42",
// 		"+42",
// 		"  42",
// 		"\t\n\v\f\r  42",
// 		"00000123",
// 		"-00000123",
// 		"  +0000042",
// 		"",
// 		" ",
// 		"+",
// 		"-",
// 		"++42",
// 		"--42",
// 		"+-42",
// 		"-+42",
// 		"  - 42",
// 		"  + 42",
// 		"a42",
// 		"42a",
// 		"  4a2",
// 		"9999999999\0999999999999999",
// 		"-9999999999999999999999999",
// 		"2147483647",
// 		"2147483648",
// 		"-2147483648",
// 		"-2147483649",
// 		" \t\n\r\v\f",
// 		"\x7f",
// 		"\x80",
// 		" \x09 42",
// 		"42\x00",
// 		"123456789012345678901234567890",
// 		"-123456789012345678901234567890",
// 		" 000000000000000000000000000000001",
// 		" -000000000000000000000000000000001",
// 		"abc",
// 		"   abc",
// 		"  +abc",
// 		"-abc",
// 		" + 123",
// 		"- 123",
// 		"1 2 3",
// 		"    +00000000000000000000000000000000000000000000042",
// 		"-00000000000000000000000000000000000000000000042",
// 		"   1234567890abcd",
// 		"  \t\n\r\v\f  00000123xyz",
// 		NULL
// 	};

// 	int  i = 0;
// 	while (tests[i])
// 	{
// 		int ft_res = ft_atoi(tests[i]);
// 		int std_res = atoi(tests[i]);
// 		printf("Test %2d: \"%s\"\n", i + 1, tests[i]);
// 		printf("  ft_atoi: %d\n", ft_res);
// 		printf("  atoi    : %d\n", std_res);
// 		printf("  %s\n\n", (ft_res == std_res) ? "✅ SAME" : "❌ DIFFER");
// 		i++;
// 	}
// 	return (0);
// }