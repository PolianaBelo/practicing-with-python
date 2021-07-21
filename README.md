# practicing-with-python
### The folders of this repository are solutions that correspond to the exercises listed below.
### To run the projects in Exercise 3 and 4 it is necessary to have Python previously installed and configured.
### The projects in Exercise 3 and 4 were developed using Python3.7.


### Exercise #1
Is there anything wrong with the Java code below? If so, can you elaborate exactly what and
why? Can you propose a fix for it?

```
public class Oddity {
public static boolean isOdd(int i) { return i % 2 == 1;
}
}
```

### Exercise #2
Is there anything wrong with the Python code below? What improvements do you propose?

```
Class MyClass:
def init (self):
self._my_dict = {"a":123, "b": True}
def set_c(self, value):
self._my_dict["c"] = value

def get_c(self):
return self._my_dict["c"]
def get_dict_with_twice_a(self):
buffer = self._my_dict
buffer[“a”] *= 2
return buffer
```

### Exercise #3
Devise the necessary code in any language to receive from prompt your First and Last names
separated by a space and return it as a complete reverse string. Example: John Doe -> eoD nhoJ.

### Exercise #4
Devise the necessary code in any language to receive 3 values from prompt. Each value
corresponds to the length of the side of a triangle. Values must be Int. A return in a string should
be made stating what type of triangle will these values form.
Example: 3, 3, 3 -> equilateral triangle.
