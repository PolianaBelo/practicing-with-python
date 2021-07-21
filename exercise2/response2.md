## Exercise 2 - Answer

The problems I found in the code are:
1. The init method is wrongly typed.
2. The getters and setter methods aren't necessary in Python.
3. The property _my_dict shouldn't have the first underscore. 
4. The method get_dict_with_twice_a that intends to use a buffer representing a copy of a dictionary changes the value of the original dictionary.

The proposed improvements are:
1. A constructor must have the init name prefixed and suffixed with a double underscore.
2. Remove getters and setters since they aren't necessary for Python since the language doesn't provide data encapsulation.
3. Remove the first underscore from _my_dict, according to PEP 8 doesn't it isn't recommended.
4. In the buffer creation use a method to copy the referenced dictionary.

### Fix 1:

```
Class MyClass:

    def __init__ (self):
        self.my_dict = {"a":123, "b": True}

    def get_dict_with_twice_a(self):
        buffer = self.my_dict.copy()
        buffer[“a”] *= 2
        return buffer
```

If the user wants to let the code to be more dynamic, it would be appropriate to define the method to double the key as follows:
### Fix 2:

```
Class MyClass:

    def __init__ (self):
        self.my_dict = {"a":123, "b": True}

    def get_dict_with_twice_key(self, key):
        buffer = self.my_dict.copy()
        buffer[key] *= 2
        return buffer
```