import csv     # imports the csv module
import sys      # imports the sys module

file = open(sys.argv[1], 'rU') # opens the csv file
try:
    csv_file = csv.reader(file)  # creates the reader object
    rownum = 0
    for row in csv_file:   # iterates the rows of the file in orders
        # Save header row.
        if rownum == 0:
            header = row
            print "**********HEADERS**********"
            print header
        else:
            colnum = 0
            #print row[3]    # prints each row
            print "-----------ROW No "+str(rownum)+" ---------------"
            for col in row:
                print '%-8s: %s' % (header[colnum], col)
                colnum += 1
        rownum += 1
finally:
    file.close()      # closing
