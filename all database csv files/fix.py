import csv

with open('vgsales.csv') as csv_file, open('temp.csv', 'w') as f_output:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_output = csv.writer(f_output)
    line_count = 0
    temp = 0
    for row in csv_reader:

        try:
            line_count += 1
            if line_count == 1 :
                csv_output.writerow(row)
                continue
            x = int(row[3])
            csv_output.writerow(row)
        except ValueError:

            if row[3] != 'N/A':
                temp += 1
                print(f"line {line_count} name {row[1]} ")
                row[1]= row[1] + " " + row[2]
                row[2] = row[3]
                row[3] = row[4]
                row[4]= row[5]
                row[5]= row[6]
                row[6]= row[7]
                row[7]= row[8]
                row[8]= row[9]
                row[9]= row[10]
                row[10]= row[11]
                row[11]= ""
                # csv_output.writerow(row)
                z = ''
                for col in row:
                    z +=','+''+str(col)
                z.replace(' ', '')
                print(f"{z}")


    print (line_count)
    print(temp)