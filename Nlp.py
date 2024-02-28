import re

def segment_strings(strings):
    segmented_strings = []
    
    for string in strings:
        # Find all email addresses and URLs in the string
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        
        email_matches = re.finditer(email_pattern, string)
        url_matches = re.finditer(url_pattern, string)
        
        # Store the indices of email addresses and URLs
        special_indices = set()
        for match in email_matches:
            special_indices.add((match.start(), match.end()))
        for match in url_matches:
            special_indices.add((match.start(), match.end()))

        # Segment the string at full stops not within email or URL patterns
        segments = []
        start_index = 0
        for match in re.finditer(r'\.', string):
            if all(match.start() < special_start or match.end() > special_end for special_start, special_end in special_indices):
                segments.append(string[start_index:match.end()])
                start_index = match.end()
        
        # Append the remaining part of the string
        segments.append(string[start_index:])
        segmented_strings.extend(segments)
    
    return segmented_strings

# Example usage
strings = ["This is a sentence. And here's an email: user@example.com. Also, visit our website: http://example.com"]
segmented_strings = segment_strings(strings)
print(segmented_strings)
