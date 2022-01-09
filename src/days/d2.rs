use std::{
    env,
    fs::File,
    io::{self, BufRead, BufReader},
    path::Path,
};

fn part1(lines: &Vec<String>) -> usize {
    let mut depth = 0;
    let mut hpos = 0;
    let c = 'h';
    let mut v1 = vec![vec![0; depth]; hpos];
    let mut v2: Vec<Vec<char>>;
    for line in lines.iter() {
        let s = line.trim();
        let mut toks = s.split_whitespace();

        let act = toks.next().unwrap();
        let xunits_opt = toks.next();
        let xunits = xunits_opt.unwrap().parse::<usize>().unwrap();
        match act {
            "forward" => hpos += xunits,
            "up" => depth -= xunits,
            "down" => depth += xunits,
            _ => println!("Unknown act {}", act),
        }
    }

    return depth * hpos;
}

fn part2(lines: &Vec<String>) -> i32 {
    let mut depth = 0;
    let mut hpos = 0;
    let mut aim = 0;
    for line in lines.iter() {
        let s = line.trim();
        let mut toks = s.split_whitespace();

        let act = toks.next().unwrap();
        let xunits_opt = toks.next();
        let xunits = xunits_opt.unwrap().parse::<i32>().unwrap();
        match act {
            "forward" => {
                hpos += xunits;
                depth += aim * xunits;
            }
            "up" => aim -= xunits,
            "down" => aim += xunits,
            _ => println!("Unknown act {}", act),
        }
    }

    return depth * hpos;
}

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}

macro_rules! vec_of_strings {
    ($($x:expr),*) => (vec![$($x.to_string()),*]);
}

#[test]
fn main() {
    let testins1 = vec_of_strings![
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2"
    ];

    let homedir = match env::var_os("HOME") {
        Some(v) => v.into_string().unwrap(),
        None => panic!("$HOME is not set"),
    };
    let ffn = format!("{}/{}", homedir, "advent_of_code/2021/day2_input.txt");
    let tins2 = lines_from_file(ffn).unwrap();
    let ptins = &testins1;
    println!("part1 = {}", part1(ptins));
    println!("part2 = {}", part2(ptins));

    let p2 = &tins2;
    println!("part1 = {}", part1(p2));
    println!("part2 = {}", part2(p2));
}
