def make_repeater(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n
    
    return repeater

def run():
    repeater_2 = make_repeater(2)
    repeater_5 = make_repeater(5)
    print(repeater_2("hola"))
    print(repeater_5("hi"))


if __name__== '__main__':
    run()