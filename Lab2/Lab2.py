# Hannah Diaz
# GEOG 676 GIS Programming, Section 775
# Spring 2026
# 3 February 2026

# Part1
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
ans1 = 1 # start @ 1 so that multiplication is not influenced

for var in part1:
    ans1 = ans1 * var

print("Part 1 answer equals: ", ans1)


# Part 2
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
ans2 = 0 # start @ 0 so that addition is not influenced

for var2 in part2:
    ans2 = ans2 + var2

print("Part 2 answer equals: ", ans2)


# Part 3
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
ans3 = 0

for var3 in part3: 
    if var3 % 2 == 0:
        ans3 = ans3 + var3

print("Part 3 answer equals: ", ans3)


# isEven = num1 % 2 == 0
