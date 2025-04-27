#!/bin/bash
#
# input.sh
#
# Bash script to automate performance testing of Merge Sort, Quick Sort, and Heap Sort 
# on flight route data. 
# Executes sorting tests, saves timing results to output.txt, and generates plots.
#
# Author: Saf Flatters
# Year: 2024


# Check if the file exists
if [ -e "output.txt" ]; then
    # If the file exists, delete it
    rm "output.txt"

fi

echo "Please wait for all Recursion Errors to complete as this is part of the test!"

for size in  3 5000 10000 15000 20000 25000             # number of route options
do 

    python3 SortsTest.py $size md >> output.txt      # mergeSort on distances 
    python3 SortsTest.py $size ml >> output.txt      # mergeSort on layover amounts
    python3 SortsTest.py $size qd >> output.txt      # quickSort on distances
    python3 SortsTest.py $size ql >> output.txt      # quickSort on layover amounts
    python3 SortsTest.py $size hd >> output.txt      # heapSort on distances
    python3 SortsTest.py $size hl >> output.txt      # heapSort on layover amounts


done

# Check if the Python script execution was successful
if [ $? -eq 0 ]; then
    echo "Python script executed successfully. Output saved"
else
    echo "Error: Python script execution failed on Recursion Failure for layover amounts."
    echo "However Python script executed. Output saved & Results plotted."
fi


python3 plotoutput.py
echo "Results plotted"

