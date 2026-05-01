/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front_bonus.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hloutman <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/26 22:32:05 by hloutman          #+#    #+#             */
/*   Updated: 2025/10/26 22:32:08 by hloutman         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_lstadd_front(t_list **lst, t_list *new)
{
	if (!lst || !new)
		return ;
	new->next = *lst;
	*lst = new;
}

// int main()
// {
	// t_list *x;
	// t_list y;
	// t_list z;
	// x = ft_lstnew("xx"); 
	// y.content = "yy"; 
	// z.content = "zz"; 
	// x->next = &y; 
	// y.next = NULL;
	// z.next = NULL;
	// t_list *tmp = x;	
	// printf("before \n");
	// while (tmp)
	// {
	// 	printf("%s \n",(char *)tmp->content);
	// 	printf("------- \n");
	// 	tmp = tmp->next;
	// }
	// ft_lstadd_front(&x, &z);
	// printf("after \n");
	// tmp = x;
	// while (tmp)
	// {
	// 	printf("%s \n",(char *)tmp->content);
	// 	printf("-------\n");
	// 	tmp = tmp->next;
	// }
// }