fn main() {
    for _ in 0..input().trim().parse::<usize>().unwrap() {
        let expr = input();
        let expr = expr.split_whitespace().collect::<Vec<_>>();
        
        let (n1, n2, res) = (
            expr[0].parse::<i64>().unwrap(), 
            expr[2].parse::<i64>().unwrap(), 
            expr[4].parse::<i64>().unwrap()
        );

        let is_ok = match expr[1] {
            "+" => n1 + n2 == res,
            "-" => n1 - n2 == res,
            "*" => n1 * n2 == res,
            "/" => n1 / n2 == res,
            _ => false
        };

        if is_ok {
            println!("correct");
        }
        else {
            println!("wrong answer");
        }
    }
}

fn input() -> String {
    let mut buf = String::new();
    std::io::stdin()
        .read_line(&mut buf)
        .unwrap();
    buf
}