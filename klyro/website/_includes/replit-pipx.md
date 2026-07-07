To use klyro with pipx on replit, you can run these commands in the replit shell:

```bash
pip install pipx
pipx run klyro ...normal klyro args...
```

If you install klyro with pipx on replit and try and run it as just `klyro` it will crash with a missing `libstdc++.so.6` library.

