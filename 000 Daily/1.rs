// LINK: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

pub fn remove_subfolders(mut folder: Vec<String>) -> Vec<String> {
    folder.sort();
    let mut res = vec![folder[0].to_owned()];

    for i in 1..folder.len() {
        let last_folder = res.last().unwrap().to_owned() + "/";

        if !folder[i].starts_with(&last_folder) {
            res.push(folder[i].to_owned())
        }
    }
    
    res
}
