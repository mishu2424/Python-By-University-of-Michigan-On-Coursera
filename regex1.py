"""
ˆ Matches the beginning of the line.
$ Matches the end of the line.
. Matches any character (a wildcard).
\s Matches a whitespace character.
\S Matches a non-whitespace character (opposite of \s).
* Applies to the immediately preceding character(s) and indicates to match zero
or more times.
*? Applies to the immediately preceding character(s) and indicates to match zero
or more times in “non-greedy mode”.
+ Applies to the immediately preceding character(s) and indicates to match one or
more times.
+? Applies to the immediately preceding character(s) and indicates to match one
or more times in “non-greedy mode”.
? Applies to the immediately preceding character(s) and indicates to match zero
or one time.
?? Applies to the immediately preceding character(s) and indicates to match zero
or one time in “non-greedy mode”.
[aeiou] Matches a single character as long as that character is in the specified set.
In this example, it would match “a”, “e”, “i”, “o”, or “u”, but no other characters.
[a-z0-9] You can specify ranges of characters using the minus sign. This example
is a single character that must be a lowercase letter or a digit.
[ˆA-Za-z] When the first character in the set notation is a caret, it inverts the
logic. This example matches a single character that is anything other than an
uppercase or lowercase letter.
( ) When parentheses are added to a regular expression, they are ignored for the
purpose of matching, but allow you to extract a particular subset of the matched
string rather than the whole string when using findall().
\b Matches the empty string, but only at the start or end of a word.
\B Matches the empty string, but not at the start or end of a word.
\d Matches any decimal digit; equivalent to the set [0-9].
\D Matches any non-digit character; equivalent to the set [ˆ0-9]

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end


"""
""" 
re.search(): Finds a match anywhere in the string. It finds out the first occurence of the match.
re.match(): Checks if the string starts with the pattern.
re.findall(): Finds all occurrences of the pattern and returns them in a list.

"""
import re
#Using re.search() like find()
hand=open('mbox-short.txt','r') 
# for line in hand:
#     line=line.strip()
#     if line.find('From: ') >=0:
#         print(line)
#Now using re.search()
# for line in hand:
#     line=line.strip()
#     if re.search("From: ",line):
#         print(line)

#Using re.search() like startstwith()
#Using startswith()
# for line in hand:
#     line=line.strip()
#     if (line.startswith('From: ')):
#         print(line)
#Now using re.search()
# for line in hand:
#     line=line.strip()
#     if re.search("^From: ",line):
#         print(line)
#DOT(.) character
#--> It matches any character
#If you add Asterisk(*) after that it will match any character afterwards.
#For example-
for line in hand:
    line=line.strip()
    if re.search("^R.*: ",line):
        print(line)