""" CP1404 Prac 08 - Recursion"""


def main():
    number_of_blocks = int(input("Please enter the number of rows: "))
    pyramid_block_builder(number_of_blocks)

def pyramid_block_builder(number_of_blocks):
    total_blocks = 0
    if number_of_blocks == 0:
        print(total_blocks)
        return
    if number_of_blocks != 0:
        total_blocks += number_of_blocks
    pyramid_block_builder(number_of_blocks-1)

main()


# Unsure how to add the data to a list each time,
