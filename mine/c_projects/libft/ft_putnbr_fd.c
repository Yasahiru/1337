/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 23:47:02 by hloutman          #+#    #+#             */
/*   Updated: 2025/10/20 23:47:03 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"
#include "libft.h"
#include <stdio.h>
#include <fcntl.h>
#include <limits.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>

void	ft_putnbr_fd(int num, int fd)
{
	char	c;
	long	n;

	n = (long)num;
	if (n < 0)
	{
		n *= -1;
		write(fd, "-", 1);
	}
	if (n > 9)
		ft_putnbr_fd(n / 10, fd);
	c = (n % 10) + '0';
	write(fd, &c, 1);
}

//
// void write_to_file(const char *filename, int n)
// {
//     int fd = open(filename, O_CREAT | O_TRUNC | O_WRONLY, 0644);
//     if (fd < 0)
//     {
//         perror("open");
//         exit(1);
//     }
//
//     ft_putnbr_fd(n, fd);
//     write(fd, "\n", 1);
//     close(fd);
// }
//
// int main(void)
// {
//     // Basic numbers
//     write_to_file("test_zero.txt", 0);
//     write_to_file("test_positive.txt", 12345);
//     write_to_file("test_negative.txt", -12345);
//
//     // Edge cases
//     write_to_file("test_intmax.txt", INT_MAX);
//     write_to_file("test_intmin.txt", INT_MIN);
//
//     // Random numbers
//     srand(time(NULL));
//     for (int i = 0; i < 5; i++)
//     {
//         int n = rand();
//         char filename[64];
//         snprintf(filename, sizeof(filename), "test_random_%d.txt", i);
//         write_to_file(filename, n);
//
//         snprintf(filename, sizeof(filename), "test_random_neg_%d.txt", i);
//         write_to_file(filename, -n);
//     }
//
//     printf("All tests written to files.\n");
//     return 0;
// }