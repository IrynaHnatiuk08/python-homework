def find_max_subarray(nums):
  current_sum = nums[0]
  max_sum = nums[0]

  start = 0
  end = 0
  temp_start = 0

  for i in range(1, len(nums)):

    if nums[i] > current_sum + nums[i]:
      current_sum = nums[i]
      temp_start = i

    else:
      current_sum = current_sum + nums[i]


    if current_sum > max_sum:
      max_sum = current_sum
      start = temp_start
      end = i

  subarray_1 = nums[start: end + 1]

  return subarray_1, max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
subarray, total_sum = find_max_subarray(arr)

print(f" Максимальна сума підмасиву {subarray}: {total_sum}")