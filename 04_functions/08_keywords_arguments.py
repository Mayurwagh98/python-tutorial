def keyword_arguments(**kwargs):
    for key, value in kwargs.items():
        print(f"key: {key}, value: {value}")


keyword_arguments(name="shaktiman", power="lazer")
keyword_arguments(name="shaktiman")
keyword_arguments(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")