// LINK : https://leetcode.com/problems/contains-duplicate/
use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut u_nums = HashSet::new();

        for i in nums {
            if u_nums.contains(&i) {
                return true
            }
            u_nums.insert(i);
        }
        return false
    }
}
