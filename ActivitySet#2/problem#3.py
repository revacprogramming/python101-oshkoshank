import re

def get_cs():
    s = input("Enter the string: ");
    return s;

def cs_to_lot(cs):
    li = list(cs.split(";"));
    
    return li

def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
