def fibonacci(n):
  answer_list = []
  for x in range(n+1):
    if x == 0: 
      answer_list.append(0)
    elif x == 1:
      answer_list.append(1)
    else:
      answer_list.append(answer_list[x-1] + answer_list[x-2])
    
  return answer_list[n]

print(fibonacci(5))



