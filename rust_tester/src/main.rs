fn main() {
    let args = input().split_whitespace()
        .map(|x| x.parse::<usize>().unwrap()).collect::<Vec<_>>();
    let len = args[0];
    let lines = args[1];

    for _ in 0..lines {
        let list = input().split_whitespace()
            .map(|x| x.parse::<u32>().unwrap())
            .collect::<Vec<_>>();

        assert_eq!(len, list.len());

        println!("{:?}", next_permutation(&list));
    }
}


fn input() -> String {
    let mut buf = String::new();
    std::io::stdin()
        .read_line(&mut buf)
        .unwrap();
    buf
}


fn next_permutation(list: &Vec<u32>) -> Vec<u32> {
    let mut result = list.clone();
    let len = list.len();

    for i in (1..len).rev() {
        if list[i-1] < list[i] {
            let mut s = list[i-1..].to_vec();
            s.sort();
            let k = s.iter().find(|x| **x == list[i-1]).unwrap();
            let number = s.remove((k+1) as usize);
            s.insert(0, number);
            result = Vec::from(&list[..i-1]).append(s);
            break;
        }
    }

    result
}