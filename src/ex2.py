import csv
import os
import numpy as np

def find_total_visits():
    total = 0
    for filename in os.listdir("../files/"):
        if filename.endswith(".csv"):
            file_path = os.path.join("../files/", filename)

            # read csv
            with open(file_path, "r") as csvfile:
                for row in csv.reader(csvfile):
                    for item in row:
                        try:
                            total += int(item)
                        except:
                            pass
            
    return total
    pass # TODO


def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")

ex2()