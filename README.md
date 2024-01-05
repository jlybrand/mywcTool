## mywc

#### A tool that emulates the Unix command line utility wc

- Clone repo

- From within repo directory run the following

```
sudo ln -s "$(pwd)/mywc.py" /usr/local/bin/mywc
```

This command creates a symbolic link named mywc in the /usr/local/bin/ directory. This directory is typically in your system's PATH.

Now, you should be able to run the script as mywc from any directory.

### To output the number of bytes in a given file run:

```
mywc -c <path-to-target-file>
```

### To output the number of lines in a given file run:

```
mywc -l <path-to-target-file>
```

### To output the number of words in a given file run:

```
mywc -w <path-to-target-file>
```

### To output the number of characters in a given file run:

```
mywc -m <path-to-target-file>
```

### To output the number of bytes and lines in a given file run:

```
mywc -c -l <path-to-target-file>
```

### To output the number of bytes, lines, and words in a given file run:

```
mywc -c -l -w <path-to-target-file>
```

or simply

```
mywc <path-to-target-file>
```
