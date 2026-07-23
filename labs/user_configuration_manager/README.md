# User Configuration Manager Lab

In this lab, you will build a User Configuration Manager that allows users to manage their settings such as theme, language, and notifications. 
You will implement functions to add, update, delete, and view user settings.

## Objective

Build a simple User Configuration Manager by implementing the required functions in `solution.py`.

When you're finished, run the automated tests to verify your solution.

## Files

```
user_configuration_manager/
│
├── README.md        # Lab instructions
├── solution.py      # <-- Write your solution here
├── tests.py         # Automated tests (do not modify)
└── runner.py        # Runs all tests
```

Do **not** modify `tests.py` or `runner.py`.

## Your Task

Fulfill the user stories below and get all the tests to pass to complete the lab.

### User Stories:

1. You should define a function named `add_setting` with two parameters representing a dictionary of settings and a tuple containing a key-value pair

2. `add_setting` function should:
    - Convert the key and value to lowercase.
    - If the key setting exists, return `Setting '[key]' already exists! Cannot add a new setting with this name`.
    - If the key setting doesn't exist, add the key-value pair to the given dictionary of settings and return `Setting '[key]' added with value '[value]' successfully!.`
    - The messages returned should have the key and value in lowercase.

3. You should define a function named `update_setting` with two parameters representing a dictionary of settings and a tuple containing a key-value pair.

4. `update_setting` function should:
    - Convert the key and value to lowercase.
    - If the key setting exists, update its value in the given dictionary of settings and return: `Setting '[key]' updated to '[value]' successfully!`
    - If the key setting doesn't exist, return `Setting '[key]' does not exist! Cannot update a non-existing setting.`
    - The messages returned should have the key and value in lowercase.

5. You should define a function named `delete_setting` with two parameters representing a dictionary of settings and a key.

6. `delete_setting` function should:
    - Convert the key passed to lowercase.
    - If the key setting exists, remove the key-value pair from the given dictionary of settings and return `Setting '[key]' deleted successfully!`
    - If the key setting does not exist, return `Setting not found!`
    - The messages returned should have the key in lowercase.

7. You should define a function named `view_settings` with one parameter representing a dictionary of settings.

8. `view_settings` function should:
    - Return `No settings available.` if the given dictionary of settings is empty.
    - If the dictionary contains any settings, return a string displaying the settings. The string should start with `Current User Settings:` followed by the key-value pairs, each on a new line and with the key capitalized. For example, `view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})` should return:
        ```bash
         Current User Settings:
         Theme: dark
         Notifications: enabled
         Volume: high
        ```

9. For testing the code, you should create a dictionary named `test_settings` to store some user configuration preferences.add_setting function should:

## Running the Tests

From inside this folder, run:

```bash
python runner.py
```

Example:

```bash
$ python runner.py

✅ 1. Dictionary test_settings exists
✅ 2. add_setting exists
✅ 3. add_setting has two parameters
✅ 4. add_setting converts to lowercase
❌ 5. add_setting handles duplicates

Expected:
Setting 'theme' already exists! Cannot add a new setting with this name.

Received:
Setting 'theme' already exists!
```

Continue fixing your code until every test passes.

## Tips

- Read the failing message carefully.
- Fix one test at a time.
- Passing one test may reveal the next failing test.
- Do not rename the required functions.

## Goal

When your solution is complete you should see:

```text
✅ 1. Dictionary test_settings exists
✅ 2. add_setting exists
...
✅ 20. view_settings output

🎉 Congratulations! 20/20 tests passed.
```