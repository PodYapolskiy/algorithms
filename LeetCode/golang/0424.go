func characterReplacement(s string, k int) int {
    freq := make(map[rune]int)
    max_len, left := 0, 0

    for right, letter := range s {
        freq[letter]++
        max_len = max(max_len, freq[letter])

        if right - left + 1 - max_len > k {
            freq[rune(s[left])]--
            left++
        }
    }

    return len(s) - left
}