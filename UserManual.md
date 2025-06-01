# User Manual
## Introduction

This user manual is intended to help the user understand the usage of DaiFu.

## Support for Multi-GPU Setup

Since DaiFu inherits from the base `pdb.Pdb` class, we need to configure a lock to prevent contention among different processes accessing the command-line in multi-GPU distributed training scenarios.

For example,
```
lock = multiprocessing.Manager().Lock()  # Create a lock for multi-GPU distributed training
daifu.repair.repair_lock = lock  # Configure the lock for DaiFu to access terminal
```
More detailed examples can be found in `DLFailureBenchmark\Large_Scale_DL_Programs\ResNet_and_Vit_and_SwinT\main_with_daifu.py`.

We will make this support more user-friendly in the future.

## Available Commands

### 1. `describe`

**Purpose**: Display the original source code with error location highlighted and exception information.

**Usage**: 
```
(DaiFu) describe
```

**What it does**:
- Shows the original function code with line numbers
- Highlights the faulty line with `>>` marker
- Displays the current exception information
- Provides formatted traceback with better exception formatting

**Example Output ([Corressponding Demo](./demo))**:
```
  1  	@daifu.transform()
  2  	def main(x):
  3  	    print('=== now start ===')
  4  	    print('x value:', x)
  5  	    for i in range(x):
  6  >>	        cell_1()
  7  	    print('=== now ended ===')
Err  	RuntimeError('The size of tensor a (224) must match the size of tensor b (8) at non-singleton dimension 1')
Traceback (most recent call last):

  File "anonymous.py", line 4, in main_daifu_cell_2
    cell_1()
    └ <function cell_1 at 0x7fd2e872a940>

  File "anonymous.py", line 6, in cell_1
    cell_2(tensor_j)
    │      └ tensor([[-1.2743,  0.5876,  0.5571,  ...,  1.3959, -0.1758,  0.0770],
    │                [-0.4791, -1.7013,  1.1982,  ...,  0.7430, -1.0...
    └ <function cell_2 at 0x7fd2c5f2e670>

  File "anonymous.py", line 9, in cell_2
    cell_3(tensor_j)
    │      └ tensor([[-1.2743,  0.5876,  0.5571,  ...,  1.3959, -0.1758,  0.0770],
    │                [-0.4791, -1.7013,  1.1982,  ...,  0.7430, -1.0...
    └ <function cell_3 at 0x7fd2c5b90dc0>

  File "anonymous.py", line 12, in cell_3
    cell_4(tensor_j)
    │      └ tensor([[-1.2743,  0.5876,  0.5571,  ...,  1.3959, -0.1758,  0.0770],
    │                [-0.4791, -1.7013,  1.1982,  ...,  0.7430, -1.0...
    └ <function cell_4 at 0x7fd2c5b94310>

  File "anonymous.py", line 16, in cell_4
    res = tensor_j * tensor_k
          │          └ tensor([[ 1.9344, -0.9284, -0.9453, -0.5858, -0.6737, -1.1569, -0.6677, -0.8798],
          │                    [-2.0794,  2.3974, -0.6859, -0.8726...
          └ tensor([[-1.2743,  0.5876,  0.5571,  ...,  1.3959, -0.1758,  0.0770],
                    [-0.4791, -1.7013,  1.1982,  ...,  0.7430, -1.0...

RuntimeError: The size of tensor a (224) must match the size of tensor b (8) at non-singleton dimension 1
```

### 2. `focus`

**Purpose**: Prepare workspace files for code modification by creating surgery and action files.

**Usage**:
```
(DaiFu) focus
```

**What it does**:
- Creates a surgery file: `(surgery-N)original_func_name.py` - copy of original code for modification
- Creates an action file: `(action-N)original_func_name.py` - empty file for action code
- Both files are created in the `daifu_workspace` directory
- Displays confirmation messages for file creation

**Note**: This command must be run before using `action` or `surgery` commands.

### 3. `pass`

**Purpose**: Skip the current repair attempt and continue execution.

**Usage**:
```
(DaiFu) pass
```

**What it does**:
- Records "Pass" as the current repair action
- Logs the pass action
- Continues program execution without making any changes

**Use case**: When you determine the error doesn't need fixing or want to skip this particular error.

### 4. `action`

**Purpose**: Execute code from the action file to modify runtime environment or variables.

**Usage**:
```
(DaiFu) action
```

**What it does**:
- Reads code from the action file created by `focus`
- Executes the code in the current function's global environment
- Records "Action" as the repair method
- Fails if `focus` hasn't been called first

**Workflow**:
1. Run `focus` to create action file
2. Edit the action file with your repair code
3. Run `action` to execute the repair

**Error handling**: Shows "Action Fails! Reason: You should create focus first!" if focus wasn't called.

### 5. `surgery`

**Purpose**: Replace the original faulty code with modified code from the surgery file.

**Usage**:
```
(DaiFu) surgery
```

**What it does**:
- Reads modified code from the surgery file created by `focus`
- Updates the original code with the new implementation
- Maps the changes back to the correct line numbers
- Records "Surgery" as the repair method
- Fails if `focus` hasn't been called first

**Workflow**:
1. Run `focus` to create surgery file
2. Edit the surgery file to fix the problematic code
3. Run `surgery` to apply the changes

**Error handling**: Shows "Surgery Fails! Reason: You should create focus first!" if focus wasn't called.

### 6. `broadcast`

**Purpose**: Save current debugging session information to a broadcast file for later analysis or sharing.

**Usage**:
```
(DaiFu) broadcast
```

**What it does**:
- Collects current session information:
  - Original function name
  - Faulty cell name and line number
  - Exception details
  - History of repair actions taken
- Saves this information as a pickle file: `N.broadcast` in `daifu_workspace`
- Useful for debugging session persistence and analysis

### 7. `exit`

**Purpose**: Forcefully terminate the program.

**Usage**:
```
(DaiFu) exit
```

**What it does**:
- Immediately exits the program with message "Deliberately Exit This Program."
- Use when you want to stop execution completely

### 8. `q` (quit)
Purpose : Continue program execution and exit the debugger.

Usage :

```
(DaiFu) q
```
What it does :

- Exits the current debugging session
- Continues normal program execution from where it was interrupted
- Inherits standard pdb quit functionality
- Does not terminate the program, just exits the debugger
Use case : When you've finished debugging and want to let the program continue running normally.

Note : This is a standard pdb command that DaiFuDebugger inherits from the base `pdb.Pdb` class.

## Typical Workflow
1. Analyze the problem : Use `describe` to understand the error and see the problematic code
2. Prepare for repair : Use `focus` to create workspace files
3. Choose repair method :
   - For runtime fixes or code changes to inactive function: Edit the action file and use `action`
   - For code changes to the active entry function: Edit the surgery file and use `surgery`
   - To skip : Use `pass`
4. Continue execution : Use `q` to continue program execution
5. Save and broadcast session in distributed training use cases: Use `broadcast` to save debugging information and broadcast it to other processes
6. Exit if needed : Use `exit` to terminate completely
        

## File Structure

When using DaiFu, files are created in the `daifu_workspace` directory:
- `(original)function_name.py` - Original source code
- `(surgery-N)function_name.py` - Code for surgical modifications
- `(action-N)function_name.py` - Code for runtime actions
- `N.broadcast` - Saved session information

## Notes

- The debugger prompt appears as `(DaiFu)`
- All commands are case-sensitive
- Some commands require `focus` to be called first
- The debugger maintains a queue of repair attempts
- Line number mapping handles transformations between original and modified code
- `q` allows graceful continuation of program execution after debugging
        