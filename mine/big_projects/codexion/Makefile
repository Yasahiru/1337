NAME = codexion

CC = cc
CFLAGS = -Wall -Wextra -Werror -Iinclude #-fsanitize=address

SRC = src/main.c \
      src/parsing/args.c \
      src/initialisation/init.c \
      src/coder/coder.c \

OBJ = $(SRC:.c=.o)

all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) -o $(NAME)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re