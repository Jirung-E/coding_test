fn main() {
    let line1 = input().split_whitespace()
        .map(|x| x.parse::<u32>().unwrap())
        .collect::<Vec<_>>();

    let base = line1[0];
    let _count1 = line1[1];
    let _count2 = line1[2];

    let num1 = input().split_whitespace()
        .map(|x| x.parse::<u32>().unwrap())
        .collect::<Vec<_>>();

    let num2 = input().split_whitespace()
        .map(|x| x.parse::<u32>().unwrap())
        .collect::<Vec<_>>();

    let num1 = to_decimal(base, &num1);
    let num2 = to_decimal(base, &num2);

    let result = decimal_to_base_list(base, num1*num2);
    println!("{}", result.len());
    for n in result {
        print!("{} ", n);
    }
}


fn to_decimal(base: u32, number_list: &Vec<u32>) -> u32 {
    let mut result = 0;
    for (i, num) in number_list.iter().rev().enumerate() {
        result += num * (base.pow(i as u32));
    }
    result
}

fn decimal_to_base_list(base: u32, number: u32) -> Vec<u32> {
    let mut v = Vec::new();
    let mut number = number;
    while number >= base {
        v.insert(0, number % base);
        number /= base
    }
    v.insert(0, number);
    v
}

fn input() -> String {
    let mut buf = String::new();
    std::io::stdin()
        .read_line(&mut buf)
        .unwrap();
    buf
}