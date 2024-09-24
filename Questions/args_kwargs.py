name = "vidya"
department = "Engineering"


def test(*args, **kwargs):
    print(args)
    for n, d in kwargs.items():
        print(n)
        print(d)
    
    
test(name, department=department)
