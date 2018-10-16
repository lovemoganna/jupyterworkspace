## pytest

The tools for python test 

## install 

```
pip install pytest
```

## floader structure
```
+---.ipynb_checkpoints
+---.pytest_cache
|   \---v
|       \---cache
\---jupyterworkflow
    +---.ipynb_checkpoints
    +---tests 
    |   +---.ipynb_checkpoints
    |   \---__pycache__
    \---__pycache__
```

- tests is test environment 

we can use behind the command test in `jupyterworkflow` directory 

`python -m pytest jupyterworkflow`,just wait a minutes,you can see successed result when your code is right 



## Makefile

you install `cygwin32` in windows,and select `make` package, and run `make test`.but i failed install make command 

