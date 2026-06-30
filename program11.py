def toggle_bits(num, pos1, pos2):
    mask1 = 1 << (pos1 - 1)
    mask2 = 1 << (pos2 - 1)

    mask = mask1 | mask2

    return num ^ mask


num = int(input("Enter number: "))
pos1 = int(input("Enter 1st bit position: "))
pos2 = int(input("Enter 2nd bit position: "))

result = toggle_bits(num, pos1, pos2)

print("Updated number:", result)