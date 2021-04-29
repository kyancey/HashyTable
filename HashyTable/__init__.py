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

    j = _FixedSizeHashMap(4)
    j[233] = 54
    j["cow"] = "holstein"
    j[("hello", "world")] = 12
    placeholder = 12