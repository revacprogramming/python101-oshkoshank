import re

def get_cs():
    while True:
        s = input("Enter the string: ")
        if(s == ""):
            break;
        else:
            return s;


def cs_to_lot(cs):
    li = list(cs.split("=").split(" "))
    return li

def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
