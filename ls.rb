# frozen_string_literal: true

input1 = [1,2,3,4,5,6,7] # => 7 / 3 = 2 + 1
output1 = [[1,2,3], [4,5,6], [7]]
input2 = [1,2,3,4,5,6,7,8] #=> 8 / 3 = 2 + 1
output2 = [[1,2,3], [4,5,6], [7,8]]
input3 = [1,2,3,4,5,6,7,8,9] #=> 9 / 3 = 3 + 0
output3 = [[1,2,3], [4,5,6], [7,8,9]]
input4 = [1,2,3,4,5,6,7,8,9,10] #=> 10 / 3 = 3 + 1
output4 = [[1,2,3,4], [5,6,7,8], [9,10]]
input5 = [1,2,3,4,5,6,7,8,9,10,11]
output5 = [[1,2,3,4], [5,6,7,8], [9,10,11]]


def make_divided_list(input, n)
  num_to_add = input.length / 3
  
  if input.length % 3 != 0
    num_to_add += 1
  end

  ret = [[], [], []]
  ret.each_with_index do |list, i|
    j = 0
    while input.size > 0 && j < num_to_add
      ret[i] << input.shift
      j += 1
    end
  end

  return ret
end

p make_divided_list(input1, 3) == output1
p make_divided_list(input2, 3) == output2
p make_divided_list(input3, 3) == output3
p make_divided_list(input4, 3) == output4
p make_divided_list(input5, 3) == output5
