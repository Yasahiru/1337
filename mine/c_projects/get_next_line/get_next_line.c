/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/24 18:06:46 by hloutman          #+#    #+#             */
/*   Updated: 2025/12/24 18:06:48 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*ft_free(char *buffer)
{
	char	*buff;
	char	*new_buff;

	buff = ft_strchr(buffer, '\n');
	if (!buff)
	{
		free(buffer);
		return (NULL);
	}
	if (*buff && *buff == '\n')
		buff++;
	new_buff = ft_strdup(buff);
	free(buffer);
	return (new_buff);
}

static char	*ft_read_to_newline(int fd, char *buffer)
{
	char	*temp;
	int		n;

	n = 1;
	temp = malloc((size_t)BUFFER_SIZE + 1);
	if (!temp)
		return (NULL);
	while (!ft_strchr(buffer, '\n') && n > 0)
	{
		n = read(fd, temp, BUFFER_SIZE);
		if (n <= 0)
			break ;
		temp[n] = '\0';
		buffer = ft_strjoin(buffer, temp);
		if (!buffer)
		{
			free(temp);
			return (NULL);
		}
	}
	free(temp);
	return (buffer);
}

static char	*ft_line(char *buffer)
{
	char	*line;
	int		len;

	if (!buffer || !buffer[0])
		return (NULL);
	len = 0;
	while (buffer[len] && buffer[len] != '\n')
		len++;
	if (buffer[len] == '\n')
		len++;
	line = ft_substr(buffer, 0, len);
	return (line);
}

char	*get_next_line(int fd)
{
	static char	*buffer;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	buffer = ft_read_to_newline(fd, buffer);
	if (!buffer)
		return (NULL);
	line = ft_line(buffer);
	buffer = ft_free(buffer);
	return (line);
}
