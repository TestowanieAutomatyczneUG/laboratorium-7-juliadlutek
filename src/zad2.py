
class ValidPassword:
    def func(self, password):
        """Takes a string and returns whether it is a valid password
                >>> v.func("passwd")
                False
                >>> v.func("passwd1")
                False
                >>> v.func("pass1!")
                False
                >>> v.func("User1!")
                False
                >>> v.func("UUuuser11!!")
                True
                >>> v.func(45)
                Traceback (most recent call last):
                ...
                ValueError: Argument must be string!
                >>> v.func(None)
                Traceback (most recent call last):
                ...
                ValueError: Argument must be string!
                >>> v.func(["User$$$1234", "User1234#@@"])
                Traceback (most recent call last):
                ...
                ValueError: Argument must be string!
                >>> v.func({"password": "Password123!@#"})
                Traceback (most recent call last):
                ...
                ValueError: Argument must be string!
                >>> v.func(True)
                Traceback (most recent call last):
                ...
                ValueError: Argument must be string!
                """



        special = ['$', '@', '#', '%', '!', "\"", "\'", "*", "+", "-", "\\", "/", ":", ";", "=", "<", ">", "?", "^", "_", "`", "~", "[", "]", "{", "}", "(", ")"]
        if type(password) != str:
            raise ValueError("Argument must be string!")
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char in special for char in password):
            return False
        else:
            return True


if __name__ == "__main__": #pragma: no cover
    import doctest
    doctest.testmod(extraglobs={'v': ValidPassword()})