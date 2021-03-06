Description
-----------
This set of scripts prepares test data for CMM application tests. 
They generate specific junk files for different clean up modules.

- Cache Files
- User Log Files
- Broken Preferences
- Broken Login Items

To generate data for each of those modules you could execute a specific script located in `junk_data_scripts` folder. 


###### Concept

"Simplicity" was the key idea for implementation for all scripts. Some common code probably could be extracted
to base classes/functions, however, at this point it is not clear if that makes sense. The current implementation
allows to generate test data, further architecture improvements seem like overengineering in this case.  

###### Broken Login Items script

This script generates files in the system Library directory. Thus you need to
execute it under `root` permissions (user) from the Terminal.

For example, from the project level directory
```
sudo ./junk_data_scripts/broken_login_items.py
```

You could also launch it from the _ PyCharm_ however it requires some configurations. [You could read about it here](https://esmithy.net/2015/05/05/rundebug-as-root-in-pycharm/)

###### Generations of all test data

In the root directory, there is a simple script - `generate_test_data.py` - that calls all module separate scripts.
It allows generating test data for everything within one script execution.
Because of launching the Login Items it also should be executed under the 
`root` permissions.

For example, from the project level directory
```
sudo ./generate_test_data.py
```

Requirements (environment setup)
------------
Implementation was tested only on MacOS.
This project is [Python](https://www.python.org/) based, so you will need Python to work with it.

```
brew install python3
```

How to run
----------
###### From the Terminal

You could execute any script from the project root directory.  For example,  
```
python3 ./test_data/user_log_files.py
or
python3 ./generate_test_data.py
``` 
(`python3` is a reference to Python 3.7+ that is added to your PATH)

###### From the IDEA

Configure Project Interpreter to use a virtual environment. To do that 
In Terminal from the main project folder do the following
`python3 -m virtualenv venv`

You could execute each script as a separate file by right click on it and
launching the _Run_ command.

Further improvements
----------
- There are a bunch of TODOs left here and there, all of them could be implemented.
- Generate test data files with locked permissions to trigger request for root password
  - I couldn't reproduce such flow manually. Tried to use `chown` and `chmod` with test file
  but it was still deleted by the app without asking for password. 

