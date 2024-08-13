// LINK : https://leetcode.com/problems/two-sum/

use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut hash_map: HashMap<i32, i32> = HashMap::new();

        for (i, val) in nums.iter().enumerate() {
            let num = target - *val;
            match hash_map.get(&num) {
                Some(&i2) => return vec![i as i32, i2],
                None => hash_map.insert(*val, i as i32),
            };
        }
        vec![]
    }
}
