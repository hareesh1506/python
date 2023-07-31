"""
   *
  ***
 *****
*******
"""
# USING LAMBDA_FUNCTION
print('##lambda##')
def fig_pyramid(row):
    for i in range(row):
        pattern = lambda j:' '*(row-j-1)+"*"*(2*j+1)
        print(pattern(i))
fig_pyramid(5)

# USING FUNCTION
print('##function##')
def fig_pyramid(row):
    for i in range(row):
        print(' '*(row-i-1)+"*"*(2*i+1))
fig_pyramid(5)

"""
Explanation:

We define a function pyramid_pattern(rows) that takes the number of rows for the pyramid as input.
Inside the function, we use a for loop to iterate through the range of rows (from 0 to rows-1).
We define a lambda function pattern(i) to generate the pattern for each row.
The lambda function takes the current row number i as input.
The lambda function returns a string that consists of two parts:
' ' * (rows - i - 1): This part generates the spaces needed before the stars to center-align 
the pyramid.
'*' * (2 * j + 1): This part generates the stars for each row, where the number of stars is 
(2 * j + 1).
Finally, we print the pattern for each row by calling the lambda function with the current row 
number i.
"""

