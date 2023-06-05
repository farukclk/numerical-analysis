#!/bin/python3

# it should be augmented matrix
# rows must be equal to coloumns - 1
# you can change the matrix

MATRIX = [
    [2, 1, -1, 2, 5],
    [4, 5, -3, 6, 9],
    [-2, 5, -2, 6, 4],
    [4, 11, -4, 8, 2],
]





NUM_LENGTH = 5              # length of numbers, to more specific solutions increase it. NUM_LENGTH > 4
SPACE = 5                   # space count between numbers. It used by print_table() function. 

ROW = len(MATRIX)
COLUMN = ROW + 1;
X_VALUES = [0] * (COLUMN - 1)


# update row and column acording to new_matrix
def set_new_matrix(new_matrix):
    MATRIX = new_matrix;
    ROW = len(MATRIX)
    COLUMN = len(MATRIX[0]);
    X_VALUES = [0] * (COLUMN - 1)



# assumed augmented matrix
def print_matrix():
    print("-" * NUM_LENGTH * COLUMN)
    for m in range(ROW):
        for n in range(COLUMN):
            print( "{}".format(str(MATRIX[m][n])[:NUM_LENGTH]).ljust(NUM_LENGTH) + " " * SPACE, end="")
        print()



def row_multiply(satir, carpan):
    for i in range(0, COLUMN):
        MATRIX[satir][i] *= carpan



# row1 = row1 + row2 * coefficient
def sum_two_rows(row1, row2, coefficient):
    for i in range(0, COLUMN):
        MATRIX[row1][i] += MATRIX[row2][i] * coefficient



# check if matrix is valid
def matrix_control():
    # check if all rows have the same number of columns
    for row in MATRIX:
        if (COLUMN != len(row)):
            print("This matrix cannot be solved by the gaussian method [!]")
            return 0
        
    return 1



def calculate_sum_with_values(satir, values):
    sum = 0

    for i in range(0, COLUMN - 1):
        sum += MATRIX[satir][i] * values[i]

    return sum



# return x values
def get_values():
    calculate()
    return X_VALUES;



def calculate():

    if (matrix_control() == 0):   # matrix gaus methodu ile cozulebilir mi kontrol et
        return 0


    # convert matrix to upper triangular matrix
    for pivot in range(0, ROW):
        
        pivot_value = MATRIX[pivot][pivot]
    
        # make pivot 1
        if (pivot_value != 1):
            row_multiply(pivot, 1 / pivot_value)    
        


        # make 0 all items under pivot 
        # column = pivot 
        for row in range(pivot + 1, ROW):
            if (MATRIX[row][pivot] == 0):
                continue
            
            else:
                sum_two_rows(row, pivot, - MATRIX[row][pivot])   # pivot_value = 1,    row +=  1 * -row

         
        print_matrix()             # print matrix step by step 


    # calculate x values and add to list
    for m in range(ROW - 1, -1, -1):    # son satirdan degerleri hesaplayarak 0. satira kadar ilerle

        sum = calculate_sum_with_values(m, X_VALUES)

        x = MATRIX[m][COLUMN - 1] - sum

        X_VALUES[m] = x   # add x to x_values

    


if __name__ == "__main__":    
    
    for i, j in enumerate(get_values()):
       
        print("x" +str(i + 1) +  ": ", j)

       

