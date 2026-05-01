/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/15 17:50:05 by hloutman          #+#    #+#             */
/*   Updated: 2025/12/15 17:50:06 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf.h"

int main(){
	char* str = NULL;
	 int x = 42;
    int *ptr = &x;
	int res = ft_printf("%p | %p\n", ptr, str);
	printf("\n");
	int og = printf("%p | %p\n", ptr, str);
	printf("\n");
	if (res == og) {printf("matches");} else {printf("not matches");}
}