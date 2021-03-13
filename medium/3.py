class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
	seen = {}
	start = 0
	maxlength = 0
	for index, number in enumerate(s):
	  if number in seen and start <= seen[number]:
	    start = seen[number] + 1
	  else:
	    maxlength = max(maxlength, index - start + 1)
	  seen[number] = index
	return maxlength
