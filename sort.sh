echo "Generating and sorting CSV"

python3 csv_generator.py --rows 1000000

sed -i '1d' input.csv
sort input.csv -o input.csv
sed -i -e '1idepartment_name,date,number_of_sales\' input.csv

echo "Done!"
