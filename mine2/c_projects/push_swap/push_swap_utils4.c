/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 13:12:34 by hloutman          #+#    #+#             */
/*   Updated: 2025/12/31 23:21:30 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*str;

	int (i), (j);
	if (!s1 && !s2)
		return (ft_strdup(""));
	if (!s2)
		return (ft_strdup(s1));
	if (!s1)
		return (ft_strdup(s2));
	str = malloc(sizeof(char) * (ft_strlen(s1) + ft_strlen(s2) + 1));
	if (!str)
		return (NULL);
	i = 0;
	j = 0;
	while (s1[j])
		str[i++] = s1[j++];
	j = 0;
	while (s2[j])
		str[i++] = s2[j++];
	str[i] = '\0';
	return (str);
}

static size_t	ft_strlen1(const char *str)
{
	size_t	i;

	i = 0;
	while (str && str[i])
		i++;
	return (i);
}

char	*ft_strdup(const char *s)
{
	char	*newstr;
	int		size;
	int		i;

	size = ft_strlen1(s);
	newstr = malloc(sizeof(char) * (size + 1));
	if (!newstr)
		return (NULL);
	i = 0;
	while (s[i])
	{
		newstr[i] = s[i];
		i++;
	}
	newstr[i] = '\0';
	return (newstr);
}

static void	ft_free2(t_stack *lst)
{
	if (lst)
	{
		ft_free2(lst->next);
		free(lst);
	}
}

void	ft_lstclear(t_stack **lst)
{
	ft_free2(*lst);
	lst = (NULL);
}
