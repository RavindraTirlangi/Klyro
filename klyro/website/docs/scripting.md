---
parent: More info
nav_order: 400
description: You can script klyro via the command line or python.
---

# Scripting klyro

You can script klyro via the command line or python.

## Command line

Klyro takes a `--message` argument, where you can give it a natural language instruction.
It will do that one thing, apply the edits to the files and then exit.
So you could do:

```bash
klyro --message "make a script that prints hello" hello.js
```

Or you can write simple shell scripts to apply the same instruction to many files:

```bash
for FILE in *.py ; do
    klyro --message "add descriptive docstrings to all the functions" $FILE
done
```

Use `klyro --help` to see all the 
[command line options](/docs/config/options.html),
but these are useful for scripting:

```
--stream, --no-stream
                      Enable/disable streaming responses (default: True) [env var:
                      KLYRO_STREAM]
--message COMMAND, --msg COMMAND, -m COMMAND
                      Specify a single message to send GPT, process reply then exit
                      (disables chat mode) [env var: KLYRO_MESSAGE]
--message-file MESSAGE_FILE, -f MESSAGE_FILE
                      Specify a file containing the message to send GPT, process reply,
                      then exit (disables chat mode) [env var: KLYRO_MESSAGE_FILE]
--yes                 Always say yes to every confirmation [env var: KLYRO_YES]
--auto-commits, --no-auto-commits
                      Enable/disable auto commit of GPT changes (default: True) [env var:
                      KLYRO_AUTO_COMMITS]
--dirty-commits, --no-dirty-commits
                      Enable/disable commits when repo is found dirty (default: True) [env
                      var: KLYRO_DIRTY_COMMITS]
--dry-run, --no-dry-run
                      Perform a dry run without modifying files (default: False) [env var:
                      KLYRO_DRY_RUN]
--commit              Commit all pending changes with a suitable commit message, then exit
                      [env var: KLYRO_COMMIT]
```


## Python

You can also script klyro from python:

```python
from klyro.coders import Coder
from klyro.models import Model

# This is a list of files to add to the chat
fnames = ["greeting.py"]

model = Model("gpt-4-turbo")

# Create a coder object
coder = Coder.create(main_model=model, fnames=fnames)

# This will execute one instruction on those files and then return
coder.run("make a script that prints hello world")

# Send another instruction
coder.run("make it say goodbye")

# You can run in-chat "/" commands too
coder.run("/tokens")

```

See the
[Coder.create() and Coder.__init__() methods](https://github.com/RavindraTirlangi/Klyro/blob/main/klyro/coders/base_coder.py)
for all the supported arguments.

It can also be helpful to set the equivalent of `--yes` by doing this:

```python
from klyro.io import InputOutput
io = InputOutput(yes=True)
# ...
coder = Coder.create(model=model, fnames=fnames, io=io)
```

{: .note }
The python scripting API is not officially supported or documented,
and could change in future releases without providing backwards compatibility.
