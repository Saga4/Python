# Numbers of alphabet which we call base
alphabet_size = 256
# Modulus to hash a string
modulus = 1000003


def rabin_karp(pattern: str, text: str) -> bool:
    """
    The Rabin-Karp Algorithm for finding a pattern within a piece of text.
    Optimized version for better performance by reducing redundant operations.
    """
    p_len = len(pattern)
    t_len = len(text)
    if p_len > t_len:
        return False

    p_hash = 0
    text_hash = 0
    modulus_power = 1

    # Calculate the hash of pattern and the hash of the first window of text
    for i in range(p_len):
        p_hash = (ord(pattern[i]) + p_hash * alphabet_size) % modulus
        text_hash = (ord(text[i]) + text_hash * alphabet_size) % modulus
        if i > 0:
            modulus_power = (modulus_power * alphabet_size) % modulus

    # Start the sliding window process
    for i in range(t_len - p_len + 1):
        # Check if current window hash matches with pattern hash, and verify the substring
        if text_hash == p_hash and text[i : i + p_len] == pattern:
            return True
        if i < t_len - p_len:
            # Calculate hash for the next window using rolling hash technique
            text_hash = (text_hash - ord(text[i]) * modulus_power) % modulus
            text_hash = (text_hash * alphabet_size + ord(text[i + p_len])) % modulus
            
            if text_hash < 0:
                text_hash += modulus  # Ensure text_hash is positive

    return False


def test_rabin_karp() -> None:
    """
    >>> test_rabin_karp()
    Success.
    """
    # Test 1)
    pattern = "abc1abc12"
    text1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    text2 = "alskfjaldsk23adsfabcabc"
    assert rabin_karp(pattern, text1)
    assert not rabin_karp(pattern, text2)

    # Test 2)
    pattern = "ABABX"
    text = "ABABZABABYABABX"
    assert rabin_karp(pattern, text)

    # Test 3)
    pattern = "AAAB"
    text = "ABAAAAAB"
    assert rabin_karp(pattern, text)

    # Test 4)
    pattern = "abcdabcy"
    text = "abcxabcdabxabcdabcdabcy"
    assert rabin_karp(pattern, text)

    # Test 5)
    pattern = "Lü"
    text = "Lüsai"
    assert rabin_karp(pattern, text)
    pattern = "Lue"
    assert not rabin_karp(pattern, text)
    print("Success.")


if __name__ == "__main__":
    test_rabin_karp()
