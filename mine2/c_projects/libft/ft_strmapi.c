/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 23:22:26 by hloutman          #+#    #+#             */
/*   Updated: 2025/10/20 23:22:29 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char	*str;

	int (size), (i);
	size = ft_strlen(s);
	str = malloc(sizeof(char) * (size + 1));
	if (!str)
		return (NULL);
	str[size] = '\0';
	i = 0;
	while (s[i])
	{
		str[i] = f(i, s[i]);
		i++;
	}
	return (str);
}

// char to_upper_even(unsigned int i, char c)
// {
//     if (i % 2 == 0)
//         return toupper(c);
//     return c;
// }
// int main(void)
// {
//     char *str = "hello world";
//     char *new = ft_strmapi(str, to_upper_even);

//     printf("Original: %s\n", str);
//     printf("Modified: %s\n", new);

//     free(new);
//     return 0;
// }
