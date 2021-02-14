''' Program to make solving tantrix puzzles easier

Underlying maths:
From:   (a_in - a_out).pi/3 + (b_in - b_out).2.pi/3 = pi or 2.pi or 4.pi
We get: 2.a_in - a + 4.b_in - 2.b = 3 or 6 or 12 

If solution resolves to a triangle, then 
    a + b + 3 is even, and 
    a >= 3, as these are needed to resolve to a triangle, and
    a_in - a_out = 3 and a_in + a_out = a
If solution resolves to a quadilateral, then 
    a + b + 6 is even, and
    a >=2 and b >= 2, as these are needed to resolve to a quad
    a_in - a_out = 2 and a_in + a_out = a, and 
    b_in - b_out = 2 and b_in + b_out = b
If solution resolves to a hexagon, then
    a + b + 12 is even, and
    b >= 6, and
    b_in - b_out = 6 and b_in + b_out = b
'''

def solve(a, b):
    '''return the possible shapes the puzzle might resolve to'''
    shape = []
    for item in (3, 6, 12):
        total = a + b + item
        if ((total) % 2 == 0) and (a >= 3) and (item == 3):
            shape.append('tri') 
        elif ((total) % 2 == 0) and (a >= 2 and b >= 2) and (item == 6):
            shape.append('quad')
        elif ((total) % 2 == 0) and (b >= 6) and (item == 12):
            shape.append('hex')
    return shape

def output_result(result):
    for option in result:
        if option == 'hex':
            hex_b_in = (b + 6)/2
            hex_a_in = a/2
            print(f"\nIf the solution is a hexagon: then there are {hex_a_in} sharp bends facing in \
and {hex_b_in} gentle bends facing in.")
        elif option == 'quad':
            quad_a_in = (a + 2)/2
            quad_b_in = (b + 2)/2
            print(f"\nIf the solution is a quadilateral: then there are {quad_a_in} sharp bends facing in \
and {quad_b_in} gentle bends facing in.")
        elif option == 'tri':
            tri_a_in = (a + 3)/2
            tri_b_in = b/2
            print(f"\nIf the solution is a triangle: then there are {tri_a_in} sharp bends facing in \
and {tri_b_in} gentle bends facing in.")
        
a = int(input("\nHow many sharp bends are there:  "))
b = int(input("How many gentle bends are there: "))

result = solve(a, b)
output_result(result)