<p><em>This project has been created as part of the 42 curriculum by hloutman.</em></p>

<h1>get_next_line</h1>

<h2>Description</h2>
<p>
    <strong>get_next_line</strong> is a C function whose goal is to read a file descriptor
    line by line and return each line on successive calls. The function handles buffering
    internally and preserves the reading state between calls.
</p>
<p>
    This project focuses on understanding low-level file I/O in Unix systems, including
    file descriptors, kernel-managed offsets, static variables, and dynamic memory
    management.
</p>

<h2>Instructions</h2>

<h3>Compilation</h3>
<p>
    Compile the project using the following command:
</p>
<pre><code>cc -Wall -Wextra -Werror get_next_line.c get_next_line_utils.c</code></pre>

<h3>Usage</h3>
<pre><code>
int fd;
char *line;

fd = open("file.txt", O_RDONLY);
while ((line = get_next_line(fd)) != NULL)
{
    printf("%s", line);
    free(line);
}
close(fd);
</code></pre>

<h2>Algorithm Explanation and Justification</h2>
<p>
    The algorithm is based on reading fixed-size chunks from a file descriptor using
    <code>read()</code> and storing unread data in a static buffer. Each call to
    <code>get_next_line</code> searches this buffer for a newline character.
</p>
<p>
    If a newline is found, the function extracts the line up to and including the newline,
    returns it, and keeps the remaining data for the next call. If no newline is present,
    additional reads are performed until either a newline or end-of-file is reached.
</p>


<h2>Resources</h2>
<ul>
    <li>
       <strong>Peer Learning</strong>
    </li>
    <li>
        <strong>Peers's learning materials</strong>- tldraw,notion...
    </li>
    <pre>https://www.tldraw.com/f/45htwzk0JnVt00NYBBD5N?d=v-857.16821.28694.34719.njr_ilsv02BD5_yktDkny</pre>
   
</ul>

<h3>Use of AI</h3>
<p>
    AI tools were used as a learning aid to clarify operating system concepts such as file
    descriptors, open-file objects, offsets, and inodes. AI assistance was also used to
    help structure documentation and improve explanations.
</p>
