NAME = codexion

CC = cc
CFLAGS = -Wall -Wextra -Werror -pthread

SRC = src/main.c \
      src/args.c \
      src/init.c \
	  src/work.c \
	  src/heap.c \
      src/coder.c \
      src/dongle.c \
      src/monitor.c \

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