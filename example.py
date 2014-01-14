from base import *

# Declare aspects.

observer = Aspect()

# Write function definitions.

@observer.aop
def f1(x, y):
    """A trivial addition function."""
    return x + y

@observer.aop
def f2(x, y, z):
    """Another trivial addition function."""
    return f1(f1(x, y), z)

# Define pointcuts and advices.

def log1():
    print "addition function logged"

observer.pointcut("addition", [f1, f2])
observer.advice(AFTER, "addition", log1)

# Write execution code.

if __name__ == "__main__":
    print f1(1, 2) * f2(1, 2, 3)