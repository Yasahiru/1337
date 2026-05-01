NAME = libftprintf.a

SRCS =  ft_printf.c ft_put_u.c ft_put_x.c ft_put_p.c ft_putchar.c ft_putnbr.c ft_putstr.c

CFLAGS = -Wall -Wextra -Werror

CC = cc

OBJS = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	ar rcs $(NAME) $(OBJS)

%.o: %.c ft_printf.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all