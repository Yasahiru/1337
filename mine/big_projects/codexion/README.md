*This project has been created as part of the 42 curriculum by <b>hloutman<b>*

# Codexion

## Description

Codexion is a concurrency project written in C. It simulates a group of
coders working in a circular co-working hub around a shared Quantum
Compiler.

Each coder is represented by a POSIX thread and repeatedly goes through
three phases:

1.  **Compiling** --- requires two USB dongles simultaneously.
2.  **Debugging** --- starts after the coder releases both dongles.
3.  **Refactoring** --- after which the coder attempts to compile again.

The simulation models a limited shared resource: there is one dongle
between each pair of coders. A coder therefore needs access to the
dongle on both sides before it can compile.

The main challenge is to coordinate concurrent coders safely while
respecting:

-   dongle ownership and mutual exclusion;
-   FIFO or EDF scheduling;
-   dongle cooldown periods;
-   coder burnout deadlines;
-   simulation termination conditions;
-   serialized logging;
-   correct resource cleanup.

The project uses POSIX threads, mutexes, condition variables where
applicable, and a custom priority-queue/heap implementation for resource
arbitration.

The simulation ends when either: - every coder has completed the
required number of compilations; or - a coder burns out because it
failed to start compiling before its deadline.

## Features

-   One POSIX thread per coder.
-   One monitor thread responsible for detecting burnout.
-   One dongle per coder.
-   Two dongles required simultaneously for compilation.
-   FIFO scheduling.
-   EDF (Earliest Deadline First) scheduling.
-   Custom heap/priority queue for waiting coders.
-   Dongle cooldown handling.
-   Serialized output using a logging mutex.
-   Precise timing using `gettimeofday()`.
-   Graceful simulation shutdown.
-   Proper allocation and cleanup of resources.

## Arguments

The program takes exactly eight arguments:

``` text
./codexion number_of_coders time_to_burnout time_to_compile \
time_to_debug time_to_refactor number_of_compiles_required \
dongle_cooldown scheduler
```

  -----------------------------------------------------------------------
  Argument                            Description
  ----------------------------------- -----------------------------------
  `number_of_coders`                  Number of coders and number of
                                      dongles.

  `time_to_burnout`                   Maximum time in milliseconds
                                      allowed before a coder must start
                                      its next compilation.

  `time_to_compile`                   Time spent compiling while holding
                                      two dongles.

  `time_to_debug`                     Time spent debugging after
                                      compilation.

  `time_to_refactor`                  Time spent refactoring before
                                      requesting dongles again.

  `number_of_compiles_required`       Number of compilations every coder
                                      must complete before the simulation
                                      stops normally.

  `dongle_cooldown`                   Time in milliseconds during which a
                                      released dongle remains
                                      unavailable.

  `scheduler`                         Arbitration policy: `fifo` or
                                      `edf`.
  -----------------------------------------------------------------------

Invalid arguments such as negative values, non-integers, or an
unsupported scheduler must be rejected.

## Instructions

### Compilation

The project is compiled using the provided Makefile:

``` bash
make
```

The project must compile with:

``` text
-Wall -Wextra -Werror -pthread
```

Available Makefile rules:

``` bash
make
make clean
make fclean
make re
```

The resulting executable is:

``` text
./codexion
```

### Execution

Example:

``` bash
./codexion 5 2000 200 200 200 10 0 fifo
```

EDF example:

``` bash
./codexion 5 2000 200 200 200 7 0 edf
```

The output follows the required format:

``` text
timestamp coder_id has taken a dongle
timestamp coder_id is compiling
timestamp coder_id is debugging
timestamp coder_id is refactoring
timestamp coder_id burned out
```

For example:

``` text
0 1 has taken a dongle
2 1 has taken a dongle
2 1 is compiling
202 1 is debugging
402 1 is refactoring
405 2 has taken a dongle
406 2 has taken a dongle
406 2 is compiling
```

Every `is compiling` message must be preceded by two
`has taken a dongle` messages for the same coder.

## Blocking cases handled

Concurrency introduces several possible failure cases. Codexion
addresses the following problems.

### Deadlock prevention

A coder needs two shared dongles to compile. Without careful
synchronization, two coders could each hold one dongle while waiting
indefinitely for the other.

This situation corresponds to the Coffman deadlock conditions:

-   mutual exclusion;
-   hold and wait;
-   no preemption;
-   circular wait.

The resource-acquisition logic is designed so that dongle ownership and
waiting are coordinated through protected scheduling rather than
allowing coders to independently hold one dongle forever while waiting
for another.

### Starvation prevention

A coder waiting for a dongle must eventually receive access when the
simulation parameters are feasible.

The scheduler controls which waiting coder is granted access:

-   **FIFO** serves the oldest request first.
-   **EDF** serves the request with the earliest burnout deadline.

This prevents arbitrary selection of waiting coders and provides
deterministic arbitration rules.

### Dongle duplication

A dongle must never be owned by two coders simultaneously.

Each dongle's state is protected by synchronization, and ownership
changes are performed while the corresponding shared state is protected.

### Dongle cooldown

After a coder releases a dongle, that dongle cannot immediately be
reused.

The implementation tracks the release/cooldown timing and prevents
another coder from acquiring the dongle before the configured cooldown
has elapsed.

### Precise burnout detection

Burnout is a timing-sensitive condition. A coder burns out when it fails
to start compiling within `time_to_burnout` milliseconds from the
beginning of its previous compilation or from the beginning of the
simulation.

A separate monitor thread checks coder deadlines and stops the
simulation when a burnout occurs.

The burnout message must be printed no more than 10 ms after the actual
burnout time, allowing for normal operating-system scheduling
variations.

### Serialized logging

Multiple coder threads can attempt to print simultaneously.

A dedicated logger mutex protects output so that two state-change
messages cannot interleave or corrupt each other.

### Clean termination

When the simulation stops, all coder threads and the monitor thread must
terminate correctly. Allocated memory and synchronization objects are
cleaned up before the program exits.

## Thread synchronization mechanisms

### `pthread_mutex_t`

Mutexes provide mutual exclusion around shared state.

They are used to protect resources such as:

-   dongle ownership/state;
-   scheduler and waiting-queue state;
-   simulation state;
-   logger output.

For example, two coders cannot safely modify the same dongle state at
the same time because access to that state is protected by a mutex.

The general pattern is:

``` c
pthread_mutex_lock(&mutex);
/* access shared state */
pthread_mutex_unlock(&mutex);
```

The mutex must always be unlocked on every control path after successful
locking.

### `pthread_cond_t`

Condition variables can be used to allow coder threads to wait
efficiently until a dongle becomes available or the relevant scheduling
condition changes.

A condition variable is normally associated with a mutex:

``` c
pthread_mutex_lock(&mutex);
while (!condition)
    pthread_cond_wait(&cond, &mutex);
/* condition is satisfied */
pthread_mutex_unlock(&mutex);
```

Waiting atomically releases the mutex while the thread sleeps and
reacquires it before returning from `pthread_cond_wait()`.

### Custom scheduling event / queue

The scheduler maintains waiting requests using a custom
heap/priority-queue structure rather than a standard-library priority
queue.

The queue represents the coders waiting for access to the required
dongles.

Its ordering depends on the selected policy:

-   **FIFO:** earliest request first.
-   **EDF:** earliest burnout deadline first.

For EDF, the deadline is:

``` text
last_compile_start + time_to_burnout
```

Equal EDF deadlines require a deterministic tie-breaker based on coder
ID.

### Communication between coders and the monitor

Coder threads update their execution state and compilation timing while
the monitor observes the shared simulation state.

Synchronization protects this communication so that the monitor does not
read partially updated state while a coder is modifying it.

When the monitor detects a burnout, it changes the shared simulation
state under synchronization. Coder threads observe the stop state and
terminate their routines cleanly.

## Timing model

The simulation uses millisecond timestamps.

The project accepts `gettimeofday()` for real-time measurements, as
recommended by the subject.

Conceptually:

``` text
elapsed_time = current_time - simulation_start_time
```

The same timing mechanism is used to determine coder deadlines and
produce timestamps in the logs.

The main execution cycle is:

``` text
          ┌─────────────┐
          │   COMPILING │
          │ 2 dongles   │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │   DEBUGGING │
          │ no dongles  │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │ REFACTORING │
          │ no dongles  │
          └──────┬──────┘
                 │
                 ▼
          Request 2 dongles
                 │
                 └──────────► COMPILING
```

## Testing

The correction sheet provides benchmark cases that can be used to
validate the implementation.

### Burnout with one coder

``` bash
./codexion 1 800 200 200 200 10 0 fifo
```

A single coder has a single dongle but requires two dongles to compile.
Therefore, it cannot compile and must burn out around 800 ms.

### FIFO --- normal completion

``` bash
./codexion 5 2000 200 200 200 10 0 fifo
```

The parameters are feasible and every coder should complete 10
compilations without burnout.

### EDF --- normal completion

``` bash
./codexion 5 2000 200 200 200 7 0 edf
```

The simulation should stop after every coder has completed 7
compilations.

### Burnout edge case

``` bash
./codexion 5 500 200 200 200 10 0 fifo
```

One compile/debug/refactor cycle requires at least:

``` text
200 + 200 + 200 = 600 ms
```

which is longer than the 500 ms burnout limit. A coder must therefore
burn out around 500 ms, and the burnout message must be the last line
and appear within the required timing tolerance.

### Cooldown test

``` bash
./codexion 5 3000 200 200 200 10 400 fifo
```

A released dongle must not be acquired again before its 400 ms cooldown
has elapsed.

### FIFO vs EDF contention test

``` bash
./codexion 5 3000 200 200 200 10 800 fifo
./codexion 5 3000 200 200 200 10 800 edf
```

The large cooldown creates contention. The order in which waiting coders
receive dongles can differ between FIFO and EDF.

### Concurrency testing tools

The correction sheet recommends testing for races and deadlocks with
tools such as:

``` bash
valgrind --tool=helgrind ./codexion ...
```

``` bash
valgrind --tool=drd ./codexion ...
```

The project should also be tested for memory leaks and invalid memory
access.

## Resources

### POSIX threads

-   POSIX Threads (`pthreads`) documentation and Linux manual pages.
-   `pthread_create`, `pthread_join`, `pthread_mutex_init`,
    `pthread_mutex_lock`, `pthread_mutex_unlock`, and
    `pthread_mutex_destroy`.
-   `pthread_cond_init`, `pthread_cond_wait`, `pthread_cond_timedwait`,
    `pthread_cond_signal`, `pthread_cond_broadcast`, and
    `pthread_cond_destroy`.

Useful local documentation:

``` bash
man pthread_create
man pthread_mutex_lock
man pthread_cond_wait
man gettimeofday
man usleep
```

### Concurrency concepts

The project is based on classic concurrency concepts including:

-   threads;
-   mutual exclusion;
-   race conditions;
-   deadlocks;
-   Coffman's conditions;
-   starvation;
-   condition variables;
-   resource scheduling;
-   priority queues;
-   real-time deadlines.

### Valgrind

Valgrind is useful for detecting memory errors, leaks, and
thread-synchronization problems.

Recommended tools for this project include:

``` bash
valgrind --tool=helgrind
valgrind --tool=drd
```

### AI usage

AI tools were used as a learning and development aid during the project.

They were used for:

-   understanding POSIX threads and how thread synchronization works;
-   studying mutexes, condition variables, and race conditions;
-   understanding deadlocks and Coffman's conditions;
-   discussing scheduling strategies such as FIFO and EDF;
-   reasoning about heap/priority-queue behavior;
-   designing and reviewing parts of the concurrency architecture;
-   investigating compiler errors and synchronization bugs;
-   suggesting testing scenarios for burnout, cooldown, contention, and
    scheduler behavior;
-   helping structure and review the README documentation.

AI-generated suggestions were reviewed, tested, and adapted to the
project requirements. The final implementation must be understood and
validated by the project author, especially because the 42 evaluation
requires being able to explain the code and its synchronization
decisions.

## Project constraints

The project follows the mandatory requirements of the Codexion subject:

-   written in C;
-   no global variables;
-   one thread per coder;
-   one dongle between each pair of coders;
-   two dongles required for compilation;
-   mutex-protected shared resources;
-   mandatory dongle cooldown;
-   FIFO and EDF arbitration;
-   custom heap/priority queue;
-   separate monitor thread for burnout detection;
-   serialized logging;
-   proper memory cleanup;
-   compilation with `-Wall -Wextra -Werror -pthread`.
