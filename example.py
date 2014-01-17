from base import Aspect

# Declare aspects.

logger = Aspect()

# Write function definitions.

@logger.track
def f1(x, y):
    """A trivial addition function."""
    return x + y

@logger.track
def f2(x, y, z):
    """Another trivial addition function."""
    return f1(f1(x, y), z)

# Define pointcuts and advices.

def log1():
    print "addition function logged"

logger.define("addition", [f1, f2])
logger.after("addition", log1)

# Write execution code.

if __name__ == "__main__":
    print f1(1, 2) * f2(1, 2, 3)