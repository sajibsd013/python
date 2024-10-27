def outer_function():
    x = "Hello"

    def inner_function():
        nonlocal x
        # global x
        x = "Hi"

    inner_function()
    print(x)  # Output: Hi

outer_function()