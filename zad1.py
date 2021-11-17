class FizzBuzz:


    def gameWithDocString(self,num):
        """Takes two integers and adds them together to produce the result
        # >>> c = Calculate()
        >>> f.gameWithDocString(7)
        '"7"'
        >>> f.gameWithDocString(-11)
        '"-11"'
        >>> f.gameWithDocString(9)
        'Fizz'
        >>> f.gameWithDocString(-3)
        'Fizz'
        >>> f.gameWithDocString(10)
        'Buzz'
        >>> f.gameWithDocString(-50)
        'Buzz'
        >>> f.gameWithDocString(15)
        'FizzBuzz'
        >>> f.gameWithDocString(-30)
        'FizzBuzz'
        >>> f.gameWithDocString('')
        Traceback (most recent call last):
          ...
        ValueError: Argument must be integer!
        >>> f.gameWithDocString("ala")
        Traceback (most recent call last):
          ...
        ValueError: Argument must be integer!
        >>> f.gameWithDocString(15.232)
        Traceback (most recent call last):
          ...
        ValueError: Argument must be integer!
        >>> f.gameWithDocString(None)
        Traceback (most recent call last):
          ...
        ValueError: Argument must be integer!
        >>> f.gameWithDocString(["a", 3, None])
        Traceback (most recent call last):
          ...
        ValueError: Argument must be integer!
        >>> f.gameWithDocString({"number": 3})
        Traceback (most recent call last):
          ...
        ValueError: Argument must be integer!
        """
        if (type(num) != int):
            raise ValueError('Argument must be integer!')
        elif ((num % 15) == 0):
            return 'FizzBuzz'
        elif ((num % 5) == 0):
            return 'Buzz'
        elif ((num % 3) == 0):
            return 'Fizz'
        else:
            return "\"" + str(num) + "\""



if __name__ == "__main__":
    # c = Calculate()
    # print(c.add(2,4))
    # print(c.addWithDocString(2.5, 4))
    # print(Calculate.addWithDocString.__doc__)
    import doctest
    # doctest.testmod()
    doctest.testmod(extraglobs={'f': FizzBuzz()})