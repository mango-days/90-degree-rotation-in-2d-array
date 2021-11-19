matrix = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] , [ 7, 8, 9 ] ]
n = len( matrix[0] )

for index1 in range ( 0 , n ) :
    i = index1
    for index2 in range ( i , n ) :
        if index1 != index2 :
            temp = matrix [ index1 ] [ index2 ]
            matrix [ index1 ] [ index2 ] = matrix [ index2 ] [ index1 ]
            matrix [ index2 ] [ index1 ] = temp

for index1 in range ( 0 , n ) :
    for index2 in range ( 0 , int( n/2 ) ) :
        temp = matrix [ index1 ] [ index2 ]
        matrix [ index1 ] [ index2 ] = matrix [ index1 ] [ n - 1 - index2 ]
        matrix [ index1 ] [ n - 1 - index2 ] = temp
    
print ( matrix )
