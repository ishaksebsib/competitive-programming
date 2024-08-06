// LINK: https://leetcode.com/problems/valid-anagram/

use std::collections::HashMap;

// my approach
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut count_s = HashMap::new();
        let mut count_t = HashMap::new();

        for c in s.chars() {
            match count_s.get(&c) {
                Some(num) => count_s.insert(c, num + 1),
                _ => count_s.insert(c, 1),
            }
        }
        count_s
    }
}

// best approach
use std::collections::HashMap;
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false
        }
        let mut map = HashMap::new();

        s.chars().for_each(|c| *map.entry(c).or_insert(0) += 1);
        t.chars().for_each(|c| *map.entry(c).or_insert(0) -= 1);
        
        map.into_values().all(|v| v == 0)
    }
}
