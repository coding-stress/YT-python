def main():

    try:
        a = int(input("hey, Enter a numbr : "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("Hey I'm inside of finally")

main()