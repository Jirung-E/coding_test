fn main() {
    let testcase = input().trim().parse::<usize>().unwrap();

    for _ in 0..testcase {
        let n = input().trim().parse::<usize>().unwrap();
        let mut result = 0;

        for _day in 0..n {
            if let Some(v) = input().split_whitespace()
                            .map(|x| x.parse::<i32>().unwrap())
                            .filter(|x| *x > 0)
                            .max() {
                result += v;
            }
        }

        println!("{}", result);
    }
}

fn input() -> String {
    let mut buf = String::new();
    std::io::stdin()
        .read_line(&mut buf)
        .unwrap();
    buf
}