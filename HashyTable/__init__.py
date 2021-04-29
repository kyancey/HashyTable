from _FixedSizeHashMap import _FixedSizeHashMap

if __name__ == "__main__":
    print("Doing some tests")
    h = _FixedSizeHashMap(2)
    h.insert(23, "Kyle Yancey")
    h[52332] = "Cat"
    h["name"] = "Todd"
    placeholder = 10