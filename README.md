# DaiFu: A Framework for In-Situ Recovery of Deep Learning Programs against Crash Failures
The artifact of Usenix ATC 2024 submission#43

## Project Structure

- `./daifu` contains the source code of daifu.
- `./DLFailureBenchmark` contains the deep learning failure benchmark as well as our experiments on it.

## Reproduction

### Preparation to use daifu

```
pip install loguru
pip install bidict
pip install better_exceptions
```

### Experiments on each case

In each case in `./DLFailureBenchmark`, the code is organized as follows.

- `buggy` contains the buggy version of a failed deep learning program, which will fail after execution.
- `fixed` contains its fault-free version, which will not fail after execution.

The command to execute them can be found in `fixed_repeated_experiments/repeat_experiments.py` or `test_suite.py`. Specifically, for each case, we need to first prepare a virtual environment according to `requirements.txt`. Then, we need to enter into the `buggy` or `fixed` directory to run the commands to see the result.

- `fixed_in_site` contains our code to use daifu to handle the failure of the buggy version in situ.

For each virtual encironment, we need to repeat the preparation to use daifu. Then we can use the command in `fixed_repeated_experiments/repeat_experiments.py` or `test_suite.py` to run the program and fix the failure in situ with daifu. The repair solution history can be found in `experiment_record.log` and files started with `(action)` or `(surgery)` in the `daifu_workplace`. 

- `fixed_in_site_repeated_experiments` and `fixed_repeated_experiments` contains our code to automatically repeat the experiemnts. We can directly execute the `repeat_experiments.py` to repeat the experiments. The experiment record logs are also provided in these directories.
