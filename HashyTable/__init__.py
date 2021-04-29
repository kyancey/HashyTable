from _FixedSizeHashMap import _FixedSizeHashMap

if __name__ == "__main__":
    print("Doing some tests")
    h = _FixedSizeHashMap(2)
    h.insert(23, "Kyle Yancey")
    h[52332] = "Cat"
    h["name"] = "Todd"
    h[(10, 3)] = 3.4444
    h["banana"] = 12
    h["sun roof"] = 45
    h["az"] = "Arizona"
    h["ar"] = "Arkansas"
    placeholder = 12