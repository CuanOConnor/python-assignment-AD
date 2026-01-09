# Solution for Autodesk application problem

def reverse_string(s):
    result = []
    temp = []

    for c in s:
        # loop over string and add chars into a buffer as long as they are chars (not punctuation or a space)
        if c.isalnum():
            temp.append(c)
        # as long as our buffer has items in it
        else:
            while temp:
                # add the chars to the result in reverse order by popping
                result.append(temp.pop())
            # Then add the punctuation and space
            result.append(c)

    # in this case this is not utilized, but it catches an edge case of ending not on punctuation
    while temp:
        result.append(temp.pop())

    # join the list and return
    return "".join(result)

# This solution should be O(n) time:
#   - Even though we have nested loops, we use a stack that is popping items on and off so its shrinking as fast as other items are expanding
#   - only one word is stored at a time keeping size down.

# Below is a simple test suite, attempting to cover some specific edge cases
def test_output(s):
    expected_string = "gnirtS; eb2 desrever..."

    tests = [
        ("Check reversal", lambda: s == expected_string),
        ("Check ';' intact", lambda: s[6] == ';'),
        ("Check ending '...'", lambda: s[20:23] == '...'),
        ("Check space after ';'", lambda: s[7] == ' '),
        ("Check space between '2b' and 'reversed'", lambda: s[11] == ' ')
    ]

    for name, test in tests:
        try:
            assert test()
            print(f"{name}: PASS")
        except AssertionError:
            print(f"{name}: FAIL")

    print("TESTS COMPLETE!")

if __name__ == "__main__":
    test_string = "String; 2be reversed..."
    output = reverse_string(test_string)

    print(f"ORIGINAL WORD: {test_string}")
    print(f"REVERSED WORD: {output}")

    test_output(output)