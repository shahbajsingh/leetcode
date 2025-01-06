'''
Problem: Similar Text Substring Count

Amazon shoppers often refer to user reviews to help them decide whether to purchase an item. They 
can focus their efforts using a keyword search, but typographical errors are common in reviews. 
To help mitigate this problem, Amazon's algorithm will include reviews that contain a word that is 
similar to the search term. A string, 's', is similar to another string, 't', if it is possible to 
swap two adjacent characters at most once in 's' to turn it into 't'. Given a keyword string named 
'keyword', find how many substrings of review' are similar to 'keyword'.

Note: A substring is a contiguous sequence of characters within a string. Two substrings are considered 
distinct if they begin at different positions.

Example 1:

Input: key = 'moon', text = 'monomon'
Output: 2
Explanation:

Consider the first four characters in the text, i.e. 'mono'. Swap the last two characters to match 
they keyword 'moon'.

The last four characters in the text are 'omon'. Swap the first two characters to match the keyword.

Thus, there are 2 substrings of 'monomon' that are similar to 'moon'. Note, that no other substring is 
similar to the given key.

Example 2:

Input: key = 'aaa', text = 'aaaa'
Output: 2
Explanation:

The 2 substrings of 'aaaa' that are similar to 'aaa' are 'aaa' (first three) and 'aaa' (last three).

Constraints:

'key' and 'text' will consist solely of lowercase English letters.

1 <= |key| <= |text| <= 50, where |s| denotes the length of a string 's'.

'''

def similar_text_substr_count(key: str, text: str) -> int:
    k = len(key) # |key|
    t = len(text) # |text|
    
    if k == 0 or k > t:
        return 0
    
    match_ct = 0
    
    # iterate thru substrs of len k 
    for i in range(t - k + 1):
        substr = text[i:i+k] # substr of len k

        if substr == key:
            match_ct += 1
            continue
        
        # check if swapping two adjacent chars in s can make it equal to key
        for j in range(k - 1):
            swap_list = list(substr)
            # swap chars at j and j+1
            swap_list[j], swap_list[j+1] = swap_list[j+1], swap_list[j]
            swap_str = ''.join(swap_list)
            
            if swap_str == key:
                match_ct += 1
                break
            
    return match_ct

# test cases
print(similar_text_substr_count('moon', 'monomon')) # 2
print(similar_text_substr_count('aaa', 'aaaa')) # 2