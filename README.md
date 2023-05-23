# The lexoffice Data Platform Engineering Challenge
This script:
1. accepts two command line arguments - `start-time` and `end-time`
2. checks that the inputs given are of a valid time format. The script should not run if the difference between the input arguments is less than 15 minutes
3. splits the time interval specified by the input arguments into 15-minute blocks and write a JSON array to an output file. The generated 15-minute blocks should all start and end at 0, 15, 30, or 45 minutes. In case the inputs are not given with this precision, the script rounds the inputs up or down to the nearest valid starting/end point. 
4. generates a unique ID for each block

## Usage: 
- Create a virtual environement with python 3.8 (optional): `conda create -n py38 python=3.8` or make sure you have python installed (no other requirements are necessary)
- Activat the virtual environment (optional): `conda activate py38`
- Clone the repository
- to run: `python script.py [start-time] [end-time]`. Replace start-time and end-time with your desired values in the format 'YYYY-MM-DDTHH:MM:SSZ'.

## Examples:

### Working script: 
- `python script.py 2021-02-11T13:45:00Z 2021-02-11T15:15:00Z`
- The script should run without any errors.
- The output file output.json should be generated successfully.
- The output.json file should contain 6 15-minute blocks.

### Wrong inputs:
- `python script.py 2023-05-18T10:00:00Z 2023-05-18T10:04:00Z`
- the script should return an error because the time difference between start and end times must be at least 15 minutes.

## Improvements
- automate unit tests for more scenarios (such as bad input format, checking the number of blocks generated, or checking that unique ids have beenn generated)
