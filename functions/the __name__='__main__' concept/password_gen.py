import random
def generate_pin():
    return random.randint(1000,9999)


if __name__=='__main__':
    print("test: ", generate_pin())