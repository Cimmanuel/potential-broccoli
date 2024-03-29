## Requirements

All that's needed to run the programs is a working installation of Python3. No third-party packages were used, so no need for a virtual environment.

## CSV generator (csv_generator.py)

The CSV generator is a simple program that generates a CSV file with the following columns:
`department_name`, `date`, and `number_of_sales`

To generate a CSV file to use with the main program in `main.py`, run the following command:

```
>>> python csv_generator.py
```

By default, this will generate a CSV file named `input.csv` in the current directory which will contain 1000000 random rows of data (minus the header). To specify number of rows and file name to write data to, use the following command `python csv_generator.py --rows=<number> --filename=<filename>`:

```
>>> python csv_generator.py --rows=5000000 --filename=data.csv
```

Make sure you change `input.csv` in line 6 of `main()` to the file to generated. In this case, `data.csv`

Note that depending on the number of rows you specify, the program may take a while to run.

## Running the program

To run the program, run the following command:

```
>>> sh sort.sh
```

This command will generate a sorted CSV file named `input.csv` in the current directory. It uses the `csv_generator.py` file to generate CSV with data. It is mandatory to sort the data in the file that the `main()` function uses because the algorithm uses `groupby()` to group the data by `department_name`. `groupby()` won't group properly if the data is not sorted.

Why not sort the data using Python's `sorted()` function? This is because `sorted()` will have to load the entire data into memory to sort. If we are dealing with a really large file, this will result in memory error.

By default, it generates a CSV file with 5000 rows . To specify number of rows and the file to write data set into, open the `sort.sh` file and append --rows <number> -- to line 3.

```
>>> python csv_generator.py --rows=5000000 --file=test_data.csv
```

In situations where data has to be sorted and the entire data can't fit into main memory, it's recommended to use an external sorting algorithm (like the external merge sort algorithm which is a K-way merge algorithm). Algorithms like this will sort chunks that each fit in RAM, then merge the sorted chunks together.
This is why the unix `sort` command is used. It's a simple command that sorts the generated CSV file. The unix `sort` uses an external R-way merge algorithm, which works well for our use case. This way, we don't have to worry about running out of memory.

Note: if you are feeding `main()` another CSV file, you should make sure it's sorted. Check the `sort.sh` script for the sorting command.

After generating `input.csv`, run:

```
>>> python main.py
```

## Approach (main.py)

-   Lines 1 - 2 imports `csv` and `groupby` (from the `itertools` module).
-   Line 5 defines the function `main()` which is the entry point of the program.
-   Line 6 opens the `input.csv` file in context.
-   Line 7 uses the `DictReader()` class from the `csv` module to read the file and assigns the generator object to the variable `rows`.
-   Line 8 uses `groupby()` from itertools to group rows from the CSV file based on the name of the department. This also returns a generator object and doesn't write entire data to memory.
-   Line 10 opens the `output.csv` file in context with write permissions.
-   Line 11 lists the required fieldnames
-   Line 12 creates a `DictWriter()` object and passes the `fieldnames` and the file object (`final_csvfile`) to it.
-   Line 14 loops through `grouping` (the object generated by `groupby()` in line 8).
-   Line 15 uses `sum()` to add `number_of_sales` in each group and assign the sum to `total`.
-   Lines 16 - 21 writes the `number_of_sales` and the `department_name` to the `output.csv` file.
-   Line 24 - 25 calls the `main()` function.

This approach avoids loading a ton of data into memory at once.

The more the input file grows, the more time the program will take because the data is read line by line. Because the steps required to completely execute the program increases or decreases with the number of input, this algorithm has a linear complexity - **O(n)**.

Also this has a constant space complexity (**O(c)**) because the data is read into memory line by line.

The program was tested with various input sizes and the results were as follows:

| Input size (rows) | Time (seconds) |
| ----------------- | -------------- |
| 1000000           | 2.8            |
| 5000000           | 10.1           |
| 10000000          | 22.3           |
