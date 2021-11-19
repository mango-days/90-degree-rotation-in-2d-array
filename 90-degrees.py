{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 matrix = [ [ 1, 2, 3 ] , [ 4, 5, 6 ] , [ 7, 8, 9 ] ]\
n = len( matrix[0] )\
\
for index1 in range ( 0 , n ) :\
    i = index1\
    for index2 in range ( i , n ) :\
        if index1 != index2 :\
            temp = matrix [ index1 ] [ index2 ]\
            matrix [ index1 ] [ index2 ] = matrix [ index2 ] [ index1 ]\
            matrix [ index2 ] [ index1 ] = temp\
\
for index1 in range ( 0 , n ) :\
    for index2 in range ( 0 , int( n/2 ) ) :\
        temp = matrix [ index1 ] [ index2 ]\
        matrix [ index1 ] [ index2 ] = matrix [ index1 ] [ n - 1 - index2 ]\
        matrix [ index1 ] [ n - 1 - index2 ] = temp\
    \
print ( matrix )}