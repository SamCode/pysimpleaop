"""An implementation of AOP in Python.

Using this AOP implementation:
    
    Use the aop() method of an Aspect instance as a decorator on the functions
    you wish to be included in pointcuts. Write function definitions so that
    the beginning and end of their executions can be tracked.

    See example.py for a complete example.

Unique Python language constructs used in this implementation:
    
    decorators
    function attributes
"""

# NOTE: Can a program be entirely written in terms of AOP rulesets, 
#       without OOP?

# NOTE: Advice functions can be tracked too, if they have an Aspect decorator.

# TODO: Replace function attributes with a more primitive language construct.

# TODO: more introspective access in pointcuts (match join points with specific
#        arguments, of specific classes, in specific scopes, etc.), and advices

#       Implement pointcuts and advices as classes if the data structures 
#       containing the info for introspection become complicated.

from functools import update_wrapper

BEFORE = 0
AFTER = 1

class Aspect(object):
    """A collection of pointcuts and advices that refer to them.

    Instance variables:
        pointcuts - a dict that maps string (names of pointcuts) to 
            lists of functions
        advices - a dict in the format:
            {
                BEFORE: {
                    <pointcut name>: <advice function>,
                    ...
                },
                AFTER: {
                    <pointcut name>: <advice function>,
                    ...
                }
            }
    """

    def __init__(self):
        self.pointcuts = {}
        self.advices = {
            BEFORE: {},
            AFTER: {}
        }

    def pointcut(self, name, fs):
        """Add a pointcut.

        Arguments:
            name - a string representing the pointcut
            fs - a list of function objects wrapped with aop()"""

        joinpoints = []
        for f in fs:
            joinpoints.append(f.original)

        self.pointcuts[name] = joinpoints

    def advice(self, rel, ptc, f):
        """Add an advice.

        Arguments:
            rel - when to execute f in relation to ptc
            ptc - name of a pointcut
            f - the function to execute according to rel and ptc
        """

        if rel in (BEFORE, AFTER):
            self.advices[rel][ptc] = f
        else:
            raise ValueError

    def aop(self, f):
        """Decorate a joinpoint (function)."""

        def g(*args, **kwargs):

            # Search BEFORE advices.
            for ptc, advice in self.advices[BEFORE].iteritems():
                if f in self.pointcuts[ptc]:
                    advice()

            result =  f(*args, **kwargs)

            # Search AFTER advices.
            for ptc, advice in self.advices[AFTER].iteritems():
                if f in self.pointcuts[ptc]:
                    advice()

            return result

        g.original = f
        return g