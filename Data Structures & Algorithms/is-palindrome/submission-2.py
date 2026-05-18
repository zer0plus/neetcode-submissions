class Solution:
    def isPalindrome(self, s: str) -> bool:
        main_arr=[]
        for char in s: 
            if char.isalnum():
                main_arr.append(char.lower())

        arr_len = len(main_arr)
        for i in range(len(main_arr)):
            if main_arr[i] != main_arr[arr_len - (i+1)]:
                return False

        return True