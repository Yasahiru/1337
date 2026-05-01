# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hloutman <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/29 03:40:23 by hloutman          #+#    #+#              #
#    Updated: 2025/12/29 03:40:26 by hloutman         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = push_swap

CC = cc
CFLAGS = -Wall -Wextra -Werror -g

SRC = 	push_swap.c parser.c push_swap_utils.c push_swap_utils2.c push_swap_utils3.c \
		push_swap_utils4.c push_swap_utils5.c push_swap_utils6.c push_swap_utils7.c \
		push_swap_utils8.c operation1.c operation2.c operation3.c operation4.c auto_sort.c \
		parser_new.c

OBJS = $(SRC:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)

clean : 
	rm -f $(OBJS)

fclean : clean
	rm -f $(NAME)

re : fclean all

.PHONY: all clean fclean re
.SECONDARY: $(OBJS)