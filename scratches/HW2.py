#Write a Python program to check whether a specified value is contained in a group of values.
#Test Data :
#3 -> [1, 5, 8, 3] : True
#-1 -> [1, 5, 8, 3] : False

def check(n):
    a = [1, 5, 8, 3]
    if n in a:
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    n = int(input())
    check(n)
