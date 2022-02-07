import csv
import datetime
import random
import secrets
from argparse import ArgumentParser

parser = ArgumentParser(description="Generate a CSV file with random data.")
parser.add_argument(
    "--rows", type=int, default=5000, help="Number of rows to generate"
)
parser.add_argument(
    "--filename",
    type=str,
    default="input.csv",
    help="Filename of the generated CSV",
)

departments = [
    "Arizona",
    "Alaska",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
]


def random_date():
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2021, 10, 25)

    days_between = (end_date - start_date).days
    number_of_days = random.randrange(days_between)
    return start_date + datetime.timedelta(days=number_of_days)


def generate_csv(number_of_rows, filename):
    with open(filename, "w") as csvfile:
        fieldnames = ["department_name", "date", "number_of_sales"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, number_of_rows + 1):
            department = secrets.choice(departments)
            date = str(random_date())
            number_of_sales = random.randrange(1, 1000)

            writer.writerow(
                {
                    "department_name": department,
                    "date": date,
                    "number_of_sales": number_of_sales,
                }
            )


if __name__ == "__main__":
    args = parser.parse_args()
    generate_csv(args.rows, args.filename)
