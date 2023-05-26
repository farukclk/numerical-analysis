#!/bin/python3

# it should be augmented matrix
# row must be equal to coloumn - 1
# you can change the matrix

MATRIX = [
    [2, 1, -1, 2, 5],
    [4, 5, -3, 6, 9],
    [-2, 5, -2, 6, 4],
    [4, 11, -4, 8, 2],
]





NUM_LENGTH = 8              # length of numbers, to more specific solutions increase it. It used by print_table() function.
ROW = len(MATRIX)
COLUMN = len(MATRIX[0]);
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
            print( "{}".format(str(MATRIX[m][n])[:NUM_LENGTH]).ljust(NUM_LENGTH) + " "*3, end="")
        print()



def row_multiply(satir, carpan):
    for i in range(0, COLUMN):
        MATRIX[satir][i] *= carpan



# satir1 = satir2 * carpim_katsayisi
def iki_satir_topla(satir1, satir2, carpim_katsayi):
    for i in range(0, COLUMN):
        MATRIX[satir1][i] += MATRIX[satir2][i] * carpim_katsayi



# check if matrix is valid
def matrix_control():
    # check if all rows have the same number of columns
    for i in range(ROW):
        column = len(MATRIX[i])
        if (ROW != column - 1):
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
                iki_satir_topla(row, pivot, - MATRIX[row][pivot])

         
        #print_matrix()             # print matrix step by step 


    # calculate x values and add to list
    for m in range(ROW - 1, -1, -1):    # son satirdan degerleri hesaplayarak 0. satira kadar ilerle

        sum = calculate_sum_with_values(m, X_VALUES)

        x = MATRIX[m][COLUMN - 1] - sum

        X_VALUES[m] = x   # add x to x_values



if __name__ == "__main__":    
    
    for i, j in enumerate(get_values()):
       
        print("x" +str(i + 1) +  ": ", j)

       


