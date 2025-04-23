def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original list: {numbers}")

    first_five = numbers[:5]  
    print(f"\nFirst five elements: {first_five}")
    reversed_five = first_five[::-1] 
    print(f"\nReversed first five elements: {reversed_five}")

if __name__ == "__main__":
    main()
