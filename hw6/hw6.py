# Xia, Summer
# hw6.py
# 03/06/23
# CPSC 3400

import re

# REGULAR EXPRESSIONS

# Write patterns for regular expressions a-c here.
# You must use a single regular expression for each item.

# Exercise 1a

patternA = re.compile(r"b{0,2}(a|ab)*|(a|ba)*b{0,2}|(a|ba)*b{0,2}(a|ab)*")


# TESTS

# Write additional tests for each part.
# Include both matching and non-matching tests.
# A portion of your grade will be based on the thoroughness of your tests.

acceptA_0 = "ababba"
acceptA_1 = "aa"
acceptA_2 = "bb"
acceptA_3 = "abababb"

rejectA_0 = "bbababb"
rejectA_1 = "abbac"
rejectA_2 = "bbb"
rejectA_3 = "bbbaa"

# Exercise 1b                                                                     

patternB = re.compile(r"([a-z134579][a-z134579])*[a-z134579]")

acceptB_0 = "sample4"
acceptB_1 = "1a3b4c5"
acceptB_2 = "444"
acceptB_3 = "helloworld1"

rejectB_0 = "another!13"
rejectB_1 = "Sample4"
rejectB_2 = "0samp"
rejectB_3 = "samp_"

# Exercise 1c                                                                         
import re

def fixURL(url):
    # Define the pattern to match a valid Seattle University URL with 2 or more subdirectories                              
    pattern = re.compile(
        r"(?P<protocol>https?://)"  # match http:// or https://                                                             
        r"(?P<subdomain>([a-zA-Z0-9_-]+\.)*)"  # match subdomains if present                                                
        r"(?P<domain>seattleu\.edu)"
        r"(?P<subdirectories>(/[a-zA-Z0-9_-]+){2,})"
        r"(?P<lastdir>/?[a-zA-Z0-9_-]*)/?$"  # match the last directory (with or without a trailing /)                      
    )

    # Try to match the pattern with the input URL                                                                           
    match = pattern.match(url)
    if match:
        # Extract the subdirectories and last directory from the matched groups                                             
        subdirs = match.group("subdirectories")
        lastdir = match.group("lastdir")

        # Swap the last two subdirectories if there are 2 or more subdirectories                                            
        subdirs_list = subdirs.split("/")
        if len(subdirs_list) >= 3:
            subdirs_list[-2], subdirs_list[-1] = subdirs_list[-1], subdirs_list[-2]
            subdirs = "/".join(subdirs_list)

        # Return the modified URL with the swapped subdirectories                                                           
        return f"{match.group('protocol')}{match.group('subdomain')}{match.group('domain')}{subdirs}{lastdir}"
    else:
        # Return the original URL if it is not valid                                                                        
        return url


validC_0 = "https://www.seattleu.edu/scieng/computer-science/bacs/undergraduate/"
# Output: https://www.seattleu.edu/scieng/computer-science/undergraduate/bacs   
validC_1 = "https://www.seattleu.edu/scieng/cs/bacs/undergrad_"
# Output:https://www.seattleu.edu/scieng/cs/undergrad_/bacs
validC_2 = "https://seattleu.edu/scieng/cs/bacs_/undergrad"
# Output:https://seattleu.edu/scieng/cs/undergrad/bacs_
validC_3 = "https://www.seattleu.edu"
# Output: https://www.seattleu.edu

invalidC_0 = "https://seattleu.instructure.com/courses/1606917"
invalidC_1 = "https://www.seattle.edu/scieng//"
invalidC_2 = "www.helloWorld.com"
invalidC_3 = "https://seattleu.com"