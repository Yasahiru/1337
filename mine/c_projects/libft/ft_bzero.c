/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 01:04:41 by hloutman          #+#    #+#             */
/*   Updated: 2025/10/19 01:05:53 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_bzero(void *s, size_t n)
{
	unsigned char	*dest;
	size_t			i;

	dest = (unsigned char *) s;
	i = 0;
	while (i < n)
	{
		dest[i] = 0;
		i++;
	}
}

// void	fill_pattern(unsigned char *buf, size_t size)
// {
// 	for (size_t i = 0; i < size; i++)
// 		buf[i] = (i * 97 + 13) % 256;
// }

// // Test one case
// void	test_case(const char *desc, size_t buf_size, size_t n)
// {
// 	unsigned char *buf1 = malloc(buf_size);
// 	unsigned char *buf2 = malloc(buf_size);

// 	if (!buf1 || !buf2)
// 		return;

// 	// Fill buffers with same pattern
// 	fill_pattern(buf1, buf_size);
// 	fill_pattern(buf2, buf_size);

// 	// Apply zeroing
// 	ft_bzero(buf1, n);
// 	bzero(buf2, n);

// 	// Check differences manually
// 	int failed = 0;
// 	for (size_t i = 0; i < buf_size; i++)
// 	{
// 		if (buf1[i] != buf2[i])
// 		{
// 			if (!failed)
// 			{
// 				printf("❌ FAIL: %s (buf_size=%zu, n=%zu)\n", desc, buf_size, n);
// 				failed = 1;
// 			}
// 			printf("   Byte %zu: ft_bzero=%02X, bzero=%02X\n", 
//i, buf1[i], buf2[i]);
// 		}
// 	}

// 	free(buf1);
// 	free(buf2);
// }

// int	main(void)
// {
// 	printf("=== ft_bzero vs original bzero test ===\n\n");

// 	// Deterministic tests
// 	test_case("n = 0", 16, 0);
// 	test_case("n = 1", 16, 1);
// 	test_case("n = half", 16, 8);
// 	test_case("n = full size", 16, 16);
// 	test_case("odd size buffer", 15, 7);
// 	test_case("large buffer small n", 1024, 4);
// 	test_case("large buffer full n", 1024, 1024);

// 	// Randomized tests
// 	for (int i = 0; i < 50; i++)
// 	{
// 		size_t buf_size = rand() % 1024 + 1;
// 		size_t n = rand() % (buf_size + 1); // safe: n <= buf_size
// 		char desc[64];
// 		sprintf(desc, "random #%02d", i + 1);
// 		test_case(desc, buf_size, n);
// 	}

// 	// NULL pointer test (safe)
// 	ft_bzero(NULL, 0);
// 	// bzero(NULL, 0);
// 	printf("\n✅ No crash when s=NULL and n=0\n");

// 	printf("\n=== Test completed ===\n");
// 	return 0;
// }