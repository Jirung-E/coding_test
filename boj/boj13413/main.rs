use std::io;

fn main() {
    let TESTCASE = input().trim().parse::<usize>().unwrap();

    for _ in 0..TESTCASE {
        let N = input().trim().parse::<usize>().unwrap();

        let curr = input().chars().collect::<Vec<char>>();
        let goal = input().chars().collect::<Vec<char>>();

        let mut to_W = 0;
        let mut to_B = 0;

        for i in 0..N {
            if curr[i] != goal[i] {
                if goal[i] == 'W' {
                    to_W += 1;
                }
                else {
                    to_B += 1;
                }
            }
        }

        println!("{}", std::cmp::max(to_W, to_B));
    }
}


fn input() -> String {
    let mut buf = String::new();
    io::stdin()
        .read_line(&mut buf)
        .unwrap();
    buf
}