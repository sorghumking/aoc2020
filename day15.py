def part(nums, stop):
    # prepare seen indices for all but the last element of nums
    indices = {n:[nums.index(n)] for n in nums[:len(nums) - 1]}
    while len(nums) < stop:
        cur_idx = len(nums) - 1
        last_num = nums[cur_idx]
        if last_num not in indices:
            indices[last_num] = [cur_idx]
            nums.append(0)
            # print(f"{last_num} not seen, appending 0.")
        else:
            indices[last_num].append(cur_idx)
            diff = indices[last_num][-1] - indices[last_num][-2]
            nums.append(diff)
            # print(f"Next num = {indices[last_num][-1]} - {indices[last_num][-2]} == {diff}.")
    print(f"{stop}th number spoken: {nums[stop - 1]}.")


if __name__ == "__main__":
    nums = [0,14,1,3,7,9]
    part(nums, 2020) # part 1
    part(nums, 30000000) # part 2 - brute forcing was fast enough, clearly a more clever way exists
