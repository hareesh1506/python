# USING FUNCTION
print('function')

def right_angle_trianle(row):
    for i in range(row):
        print("*"*(i+1))

right_angle_trianle(5)

# USING Lambda
print('lambda')
def right_angle_trianle(row):
    for i in range(row):
        pattern = lambda j : "*"*(j+1)
        print(pattern(i))
right_angle_trianle(5)