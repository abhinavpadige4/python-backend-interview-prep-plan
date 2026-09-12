"""
LeetCode 535: Encode and Decode TinyURL
Problem: Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl 
and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm should work. 
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Solution: Use hashmap to store mappings between original URLs and generated short codes.
Time Complexity: O(1) average for both encode and decode
Space Complexity: O(n) where n is number of URLs stored
"""

import random
import string
from typing import Dict

class Codec:
    """
    Codec for encoding and decoding URLs in a TinyURL service.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.url_to_code: Dict[str, str] = {}   # Maps original URL to short code
        self.code_to_url: Dict[str, str] = {}   # Maps short code to original URL
        self.chars = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
        self.base_url = "http://tinyurl.com/"
        self.code_length = 6  # Length of generated short code

    def encode(self, longUrl: str) -> str:
        """
        Encodes a URL to a shortened URL.
        
        Args:
            longUrl: str - Original URL to encode
            
        Returns:
            str - Shortened URL
        """
        # If URL already encoded, return existing short URL
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]
        
        # Generate a unique short code
        while True:
            short_code = ''.join(random.choice(self.chars) for _ in range(self.code_length))
            if short_code not in self.code_to_url:
                break
        
        # Store mappings in both directions
        self.url_to_code[longUrl] = short_code
        self.code_to_url[short_code] = longUrl
        
        return self.base_url + short_code

    def decode(self, shortUrl: str) -> str:
        """
        Decodes a shortened URL to its original URL.
        
        Args:
            shortUrl: str - Shortened URL to decode
            
        Returns:
            str - Original URL
        """
        # Extract the short code from the URL
        short_code = shortUrl.replace(self.base_url, "")
        
        # Return the original URL if found, otherwise return empty string
        return self.code_to_url.get(short_code, "")


# Alternative solution using incremental ID (more predictable)
class CodecIncremental:
    """
    Alternative Codec using incremental ID approach.
    More predictable but requires persistence of counter.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.url_to_code: Dict[str, str] = {}
        self.code_to_url: Dict[str, str] = {}
        self.chars = string.ascii_letters + string.digits
        self.base_url = "http://tinyurl.com/"
        self.next_id = 0

    def _base62_encode(self, num: int) -> str:
        """
        Convert a number to base62 string.
        """
        if num == 0:
            return self.chars[0]
        
        result = []
        base = len(self.chars)
        while num > 0:
            result.append(self.chars[num % base])
            num //= base
        
        return ''.join(reversed(result))

    def encode(self, longUrl: str) -> str:
        """
        Encodes a URL to a shortened URL using incremental ID.
        """
        # If URL already encoded, return existing short URL
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]
        
        # Generate short code from incremental ID
        short_code = self._base62_encode(self.next_id)
        self.next_id += 1
        
        # Pad with leading zeros to ensure fixed length if needed
        # For simplicity, we'll use variable length here
        
        # Store mappings in both directions
        self.url_to_code[longUrl] = short_code
        self.code_to_url[short_code] = longUrl
        
        return self.base_url + short_code

    def decode(self, shortUrl: str) -> str:
        """
        Decodes a shortened URL to its original URL.
        """
        short_code = shortUrl.replace(self.base_url, "")
        return self.code_to_url.get(short_code, "")


# Test the implementation
def test_codec():
    """
    Test the Codec implementation.
    """
    print("Testing Codec (random approach)...")
    
    # Create codec instance
    codec = Codec()
    
    # Test URLs
    test_urls = [
        "https://leetcode.com/problems/design-tinyurl",
        "https://www.google.com",
        "https://github.com/user/repo",
        "https://stackoverflow.com/questions/123456"
    ]
    
    # Test encode and decode
    for url in test_urls:
        encoded = codec.encode(url)
        decoded = codec.decode(encoded)
        print(f"Original:  {url}")
        print(f"Encoded:   {encoded}")
        print(f"Decoded:   {decoded}")
        print(f"Match:     {url == decoded}")
        print("-" * 40)
    
    # Test encoding same URL twice (should return same short URL)
    print("\nTesting consistency (same URL encoded twice):")
    url = "https://leetcode.com/problems/design-tinyurl"
    encoded1 = codec.encode(url)
    encoded2 = codec.encode(url)
    print(f"First encode:  {encoded1}")
    print(f"Second encode: {encoded2}")
    print(f"Same:          {encoded1 == encoded2}")
    
    print("\n" + "="*50)
    print("Testing CodecIncremental (incremental ID approach)...")
    
    # Test incremental approach
    codec_inc = CodecIncremental()
    
    for url in test_urls[:3]:  # Test first 3 URLs
        encoded = codec_inc.encode(url)
        decoded = codec_inc.decode(encoded)
        print(f"Original:  {url}")
        print(f"Encoded:   {encoded}")
        print(f"Decoded:   {decoded}")
        print(f"Match:     {url == decoded}")
        print("-" * 40)


if __name__ == "__main__":
    test_codec()