use std::{
    env,
    fs::File,
    io::{self, BufRead, BufReader},
    path::Path,
};

struct SMap {
    smap: Vec<Vec<char>>,
    w: usize,
    h: usize,
}

impl SMap {
    fn new(vs: Vec<String>) -> Self {
        let mut smap: Vec<Vec<char>> = vec![];
        vs.into_iter().for_each(|s| {
            smap.push(s.chars().collect());
        });
        let h = smap.len();
        let w = smap[0].len();
        println!("init nlines={} width={}", h, w);
        Self { smap, w, h }
    }
    fn onestep_east(&mut self) -> bool {
        let mut moved = false;
        let omap = self.smap.clone();
        // scan every column
        for x in 0..self.w {
            let nx = (x + 1) % self.h;
            for y in 0..self.h {
                if omap[y][x] != '>' {
                    continue;
                }
                if omap[y][nx] == '.' {
                    // check if the right side is clean
                    moved = true;
                    self.smap[y][nx] = '>';
                    self.smap[y][x] = '.';
                }
            }
        }
        moved
    }
    fn onestep_south(&mut self) -> bool {
        let mut moved = false;
        let omap = self.smap.clone();
        // scan every row
        for y in 0..self.h {
            let ny = (y + 1) % self.h;

            for x in 0..self.w {
                if omap[y][x] != 'v' {
                    continue;
                }
                if omap[ny][x] == '.' {
                    // check if the right side is clean
                    moved = true;
                    self.smap[ny][x] = 'v';
                    self.smap[y][x] = '.';
                }
            }
        }
        moved
    }
    fn onestep(&mut self) -> bool {
        let moved1 = self.onestep_east();
        let moved2 = self.onestep_south();
        moved1 | moved2
    }
    fn display(&self) {
        for m in &self.smap {
            let s = m.into_iter().collect::<String>();
            println!("{}", s);
        }
    }
}

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}

fn basictest() {
    let mut vc = vec![vec!['a', 'b', 'c'], vec!['1', '2']];
    let mut vc1 = vc.clone();
    vc[0][0] = 'q';
    vc1[0][0] = 'g';

    println!("vc[0] len={} vc[1] len={}", vc[0].len(), vc[1].len());
    let s = "Hello!";
    let char_vec: Vec<char> = s.chars().collect();
    println!("char_vec len={}", char_vec.len());
    for i in 0..char_vec.len() {
        println!("{}", char_vec[i]);
    }
    for v in vc {
        println!("{}", v.into_iter().collect::<String>());
    }
    for v in vc1 {
        println!("{}", v.into_iter().collect::<String>());
    }
}
#[test]
fn main() {
    //basictest();
    let homedir = match env::var_os("HOME") {
        Some(v) => v.into_string().unwrap(),
        None => panic!("$HOME is not set"),
    };
    let ffn = format!("{}/{}", homedir, "advent_of_code/2021/day25_input1.txt");
    let tins2 = lines_from_file(ffn).unwrap();
    let mut m1 = SMap::new(tins2);
    m1.display();
    for i in 0..2 {
        let moved = m1.onestep();
        println!("After step {}:", i + 1);
        m1.display();
        if !moved {
            break;
        }
    }
    println!("done");
}
