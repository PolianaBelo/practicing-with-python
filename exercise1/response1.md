# Exercise 1 - Answer

The problems I found in the code are:
1. The code indentation.
2. The name of the class.
3. The boolean validation doesn't work for negative numbers.
4. The name of the variable "i".

The reasons for these topics are:
1. The used indentation is confusing.
2. The name isn't clear about the context of the class.
3. The remainder of an odd negative number divided by two is returning -1.
4. The name "i" doesn't tell anything about the purpose of the variable in the code. It is important to use meaningful names for the variables.

### Fix:

```
public class OddParity {

public static boolean isOdd(int numberToCheck) {
     return numberToCheck % 2 != 0;
    }
}
```