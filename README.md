# Rolling Window Version 2

This second version stimulates a real-time and batch data processing pipelines data aggregations over rolling time windows for blazing fast computation speeds across crazy amounts of data, data analysis, data science, data exploration where we are interested in the last line of the output on screen.

# Features

This version contains the following new features from Rolling Window v1:

- **Display the Last Output Line** - `Percentile`, `Total Contribution Dollars`, and the `Total Number of Contributions` for `2018` will be displayed on Terminal every `5` seconds.

- **5-second Terminal Refresh** - Terminal automatically refreshes every `5` seconds if new incoming data is inserted to `/input/itcont.txt` file; or updates have been made to `percentile.txt`

- **Output File Auto Update** - The output file - `repeat_donors.txt` - automatically updates every `5` seconds if new data is inserted to `/input/itcont.txt`; or updates have been made to `percentile.txt`


# Dependencies Alternate Version

The alternate version requires the following libraries:

- Python 2.7

- ```import sys```

- ```import os```

- ```from decimal import getcontext, Decimal```

- ```import time```

- ```from collections import OrderedDict```


# Simulation

To simulate a real-time and batch data processing pipelines data aggregations over rolling time windows, let's add the following sample entry at the end line of our `/input/itcont.txt` file and save the file.

We can easily modify line #39 in our `__init__.py` and subsitutue any numeric as our second indicator.

```
time.sleep(5)
```

# Execution

To execute the code use the `run.sh` bash script from the root directory.

```
./run.sh
```

Next, go head and add the following new entry at the very end of our current input file `itcont.txt`:

**Note:** the only change is the calendar year from 2017 to 2018.


```
C00177436|N|M2|P|201702039042410894|15|IND|DEEHAN, WILLIAM N|ALPHARETTA|GA|300047357|UNUM|SVP, SALES, CL|01312018|384||PR2283873845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029337
```


As you can see from below, only the last line is display on screen:

```
Percentile: 333|Total: $717|Total Number of Contributions: 2
```

![Output Window](/images/output_window_v2.png)


# Questions? 