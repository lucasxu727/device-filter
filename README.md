# Device Filter

A simple program desgined to determine the amount of active users connected to a network from a list of connected devices.
The goal is to cultivate a set of data that is an accurate representation to how many people are connected, rather than devices, so that this set of cultivated data can be used to accurately train models that need this data.

## Usage

Format:
`Type inputfilename.json | python devicefilter.py > outputfilename.json`

## Example Output

The expected output will a json file including the information of distinct connected users

## How it works

1. The inputted json fil is converted into a pandas object

2. All connected devices who do not have a username are not added into the new json file

3. All unique usernames have their row added into the new json file, their names are added into a list that is repeatedl checked for duplicate usernames

4. The final output can then be piped into a json file

Notice: null values are represented by NaN <- something to be fixed.
