import csv
from itertools import groupby


def main():
    with open("input.csv", "r") as csvfile:
        rows = csv.DictReader(csvfile)
        grouping = groupby(rows, lambda row: row["department_name"])

        with open("output.csv", "w") as final_csvfile:
            fieldnames = ["department_name", "number_of_sales"]
            writer = csv.DictWriter(final_csvfile, fieldnames=fieldnames)

            for group, items in grouping:
                total = sum(int(item["number_of_sales"]) for item in items)
                writer.writerow(
                    {
                        "department_name": group,
                        "number_of_sales": str(total),
                    }
                )


if __name__ == "__main__":
    main()


"""
Approach 2 below is a very great approach for small data sets.
If there are millions of rows, it will create a lot of items in
the defaultdict instance and that's very bad for memory.
"""

# import csv
# from collections import defaultdict


# def main():
#     mapper = defaultdict(int)
#     with open("input.csv", "r") as csvfile:
#         rows = csv.DictReader(csvfile)

#         for row in rows:
#             mapper[row["department_name"]] += int(row["number_of_sales"])

#         with open("output.csv", "w") as final_csvfile:
#             fieldnames = ["department_name", "number_of_sales"]
#             writer = csv.DictWriter(final_csvfile, fieldnames=fieldnames)
#             writer.writerows(
#                 {
#                     "department_name": department_name,
#                     "number_of_sales": number_of_sales,
#                 }
#                 for department_name, number_of_sales in mapper.items()
#             )


# if __name__ == "__main__":
#     main()


"""
Approach 1. Some wack stuff that's gonna mess your system up
with unnecessary files
"""

# import glob
# import os
# import shutil
# from argparse import ArgumentParser

# import pandas
# from tabulate import tabulate

# parser = ArgumentParser(description="Compute CSV files in chunks")
# parser.add_argument(
#     "--chunksize", type=int, default=100, help="Number of rows in a chunk"
# )

# chunk_path = f"{os.getcwd()}/chunks"


# def combine_mergence(file):
#     data = pandas.read_csv(file)
#     results = data.groupby(["Department Name"], as_index=False)[
#         "Number of Sales"
#     ].sum()

#     os.chdir("..")
#     results.to_csv("output.csv", index=False)
#     shutil.rmtree(chunk_path)
#     return results


# def combine_rows(file, chunksize):
#     batch_number = 1
#     chunks = pandas.read_csv(file, chunksize=chunksize)

#     if not os.path.isdir(chunk_path):
#         os.mkdir(chunk_path)
#     else:
#         if len(os.listdir(chunk_path)) > 0:
#             shutil.rmtree(chunk_path)
#             os.mkdir(chunk_path)

#     os.chdir(chunk_path)
#     for chunk in chunks:
#         grouped_chunk = chunk.groupby(["Department Name"], as_index=False)[
#             "Number of Sales"
#         ].sum()
#         grouped_chunk.to_csv(f"chunk_output_{batch_number}.csv", index=False)
#         batch_number += 1

#     chunk_files = [chunkfile for chunkfile in glob.glob("*.csv")]
#     merge_files = pandas.concat(
#         [pandas.read_csv(chunk_file) for chunk_file in chunk_files]
#     )
#     merge_files.to_csv("mergence.csv", index=False, encoding="utf-8-sig")

#     results = combine_mergence("mergence.csv")
#     return results


# if __name__ == "__main__":
#     args = parser.parse_args()
#     results = combine_rows("input.csv", args.chunksize)
#     print(tabulate(results, headers=results.columns))
