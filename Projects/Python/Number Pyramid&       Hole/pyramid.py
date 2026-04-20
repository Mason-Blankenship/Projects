# number = int(input("Enter a number: "))
# piehole = input("Pyramid or Hole? ").lower()


def pyramid_hole():
    while True:
        number = int(input("Enter a number: "))
        piehole = input("Pyramid or Hole? ").lower()
        if piehole == 'pyramid':
            for i in range(number,0, -1):
                for j in range(i - 1):
                        print(" ", end=" ")
                for k in range(i,number+1):
                     print(k, end=" ")
                for l in range(number - 1, i -1,-1):
                     print(l, end=" ")

                print()
            break
        elif piehole == 'hole':
            for i in range(1,number+1):
                for j in range(i - 1):
                    print(" ", end=" ")
                for k in range(i,number+1):
                    print(k, end=" ")
                for l in range(number - 1, i -1,-1):
                    print(l, end=" ")

                print()
            break
        else: 
            print("You might've mispelled that.")
        continue

pyramid_hole()