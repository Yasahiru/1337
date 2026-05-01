*This project has been created as part of the 42 curriculum by hloutman.*

# push_swap

## Description

**push_swap** is a sorting algorithm project from the **42 curriculum** that challenges you to sort a stack of integers in ascending order using only a **limited set of predefined operations**, while minimizing the total number of moves.

### Project Goal

The program takes a list of integers as arguments and outputs a sequence of operations that, when applied, will sort the stack in ascending order. The key challenge is optimizing the algorithm to use as few operations as possible.

### Overview

This implementation features:
- **Input validation** with error handling for duplicates and invalid inputs
- **Indexed binary Radix Sort algorithm** optimized for efficiency
- **Dual-stack architecture** (Stack A and Stack B) for flexible data manipulation
- Support for sorting stacks of various sizes (small lists, 100 numbers, 500 numbers, etc.)
- **Minimal operation count** through intelligent sorting strategies

### Key Operations

The program uses the following stack operations:
- `sa`, `sb`: Swap the first two elements of a stack
- `ss`: Swap the first two elements of both stacks simultaneously
- `pa`, `pb`: Push the first element from one stack to the top of another
- `ra`, `rb`: Rotate a stack (move first element to the end)
- `rra`, `rrb`: Reverse rotate a stack (move last element to the beginning)

---

## Instructions

### Requirements

- A Unix-based system (Linux or macOS)
- `gcc` compiler (version 4.9+)
- `make` utility

### Compilation

To compile the project, run:

```bash
make
```

This will generate the `push_swap` executable.

To clean up object files:

```bash
make clean
```

To remove all generated files (objects and executable):

```bash
make fclean
```

To recompile everything from scratch:

```bash
make re
```

### Execution

Run the program with a list of integers as arguments:

```bash
./push_swap 4 67 3 87 23
```

The program outputs a list of operations that will sort the stack:

```
pb
ra
pa
sa
```

### Usage Examples

**Sort a small list:**
```bash
./push_swap 3 1 2
```

**Sort larger datasets:**
```bash
./push_swap 5 2 8 1 9 3
```

**Testing with random numbers:**
```bash
./push_swap $(shuf -i 1-100 -n 100)
```

### Error Handling

The program validates input and displays "Error" on standard error if:
- Non-integer arguments are provided
- Duplicate numbers are present
- Numbers exceed the integer range

---

## Resources

### Classic References

- **[Stack Data Structure](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))** - Foundational concept for this project
- **[Sorting Algorithms Overview](https://en.wikipedia.org/wiki/Sorting_algorithm)** - Understanding different sorting approaches
- **[Radix Sort Documentation](https://en.wikipedia.org/wiki/Radix_sort)** - The sorting algorithm used in this implementation
- **[Algorithm Optimization](https://www.geeksforgeeks.org/sorting-algorithms/)** - GeeksforGeeks comprehensive guide
- **[Time Complexity Analysis](https://en.wikipedia.org/wiki/Time_complexity)** - Understanding algorithm efficiency

### AI Usage
 
AI assistance was utilized in the following areas of this project:

1. **Algorithm Optimization**: AI helped refine the Radix Sort implementation and identify ways to minimize operation counts for various input sizes
2. **Code Structure & Design**: AI provided guidance on organizing utility functions, memory management, and modular code architecture
3. **Error Handling & Edge Cases**: AI assisted in identifying and handling edge cases like duplicates, overflow, and invalid inputs
4. **Performance Tuning**: AI suggested optimizations for processing large datasets (100-500 numbers)
5. **Documentation & Comments**: AI helped create clear, comprehensive code documentation

These assistances accelerated development while ensuring code quality, correctness, and maintainability.

---

## Technical Choices

### Algorithm Selection

The project implements a **Radix Sort-based approach** rather than traditional comparison sorts, because:
- It achieves better performance on large datasets
- It's well-suited for the stack-based operation constraints
- It minimizes the number of operations needed for sorting

### Data Structure

A **doubly-linked list** was chosen for the stacks to support:
- Efficient insertion and deletion at both ends
- O(1) push/pop operations
- Easy index tracking for optimization

### File Organization

The codebase is organized into logical modules:
- `push_swap.c` - Main entry point and orchestration
- `auto_sort.c` - Sorting algorithm implementation
- `operation*.c` - Stack operation implementations
- `parser*.c` - Input parsing and validation
- `push_swap_utils*.c` - Utility functions
