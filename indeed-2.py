'''
We are building a word processor and we would like to implement a "reflow" functionality that also applies full justification to the text.
Given an array containing lines of text and a new maximum width, re-flow the text to fit the new width. Each line should have the exact specified width. If any line is too short, insert '-' (as stand-ins for spaces) between words as equally as possible until it fits.
Note: we are using '-' instead of spaces between words to make testing and visual verification of the results easier.


lines = [ "The day began as still as the",
          "night abruptly lighted with",
          "brilliant flame" ]
          
words = ['The', 'day', 'began', '']

reflowAndJustify(lines, 24) "reflow lines and justify to length 24" =>

        [ "The--day--began-as-still",
          "as--the--night--abruptly",
          "lighted--with--brilliant",
          "flame" ] // <--- a single word on a line is not padded with spaces

reflowAndJustify(lines, 25) "reflow lines and justify to length 25" =>

        [ "The-day-began-as-still-as"
          "the-----night----abruptly"
          "lighted---with--brilliant"
          "flame" ]

reflowAndJustify(lines, 26) "reflow lines and justify to length 26" =>

        [ "The--day-began-as-still-as",
          "the-night-abruptly-lighted",
          "with----brilliant----flame" ]

reflowAndJustify(lines, 40) "reflow lines and justify to length 40" =>

        [ "The--day--began--as--still--as-the-night",
          "abruptly--lighted--with--brilliant-flame" ]

reflowAndJustify(lines, 14) "reflow lines and justify to length 14" =>

        ['The--day-began',
         'as---still--as',
         'the------night',
         'abruptly', 
         'lighted---with', 
         'brilliant', 
         'flame']

n = number of words OR total characters

N * L + M


'''
lines = ["The day began as still as the","night abruptly lighted with","brilliant flame"]
test_reflow_width1 = 24
test_reflow_width2 = 25
test_reflow_width3 = 26
test_reflow_width4 = 40
test_reflow_width5 = 14
def reflowAndJustify(lines, n):
    words = []
    for line in lines:
        words += line.split(' ') # => [] + ['The', 'day', 'began', 'as', 'still'] 
                                 # The--day--began-as-still
                                 # 24 - 18 = 6 % 4 = 2
    ans = []
    tmp = [words[0]]
    
    for i in range(1, len(words)):
        s = 0
        for w in tmp:
            s += len(w)

        
        # the-----night----abruptly n = 25
        # 25 - 16 = 9 / 2 = 4, 9 % 2 = 1
        width = s + len(tmp) + len(words[i])
        if width > n:
            if len(tmp) > 1:
                mod = (n - s) % (len(tmp)-1)
                bases = [(n-s) // (len(tmp)-1)] * (len(tmp)-1)
                for j in range(mod):
                    bases[j] += 1

            string = ''
            for j in range(len(tmp)-1):
                string += tmp[j]
                string += '-' * bases[j]

            string += tmp[-1]
            ans.append(string)
            tmp = []

        tmp.append(words[i])

    s = 0
    for w in tmp:
        s += len(w)
    if len(tmp) > 1:
        mod = (n - s) % (len(tmp)-1)
        bases = [(n-s) // (len(tmp)-1)] * (len(tmp)-1)
        for j in range(mod):
            bases[j] += 1

    string = ''
    for j in range(len(tmp)-1):
        string += tmp[j]
        string += '-' * bases[j]

    string += tmp[-1]
    ans.append(string)
    
    return ans

print(reflowAndJustify(lines, test_reflow_width1))
print(reflowAndJustify(lines, test_reflow_width2))
print(reflowAndJustify(lines, test_reflow_width3))
print(reflowAndJustify(lines, test_reflow_width4))
print(reflowAndJustify(lines, test_reflow_width5))
