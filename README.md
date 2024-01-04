### mywc

#### Tool that emulates the Unix command line tool wc

Clone repo
From within repo directory run the following

```
sudo ln -s "$(pwd)/mywc.py" /usr/local/bin/mywc
```

This command creates a symbolic link named mywc in the /usr/local/bin/ directory.
Now, you should be able to run the script as mywc from any directory.

To output the number of bytes in a given file run:

```
mywc -c <path-to-target-file>
```
