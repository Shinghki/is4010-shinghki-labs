fn main() {
    println!("Lab 10: Mastering Ownership and Borrowing");
    println!("Uncomment one problem at a time and fix it!\n");

    problem_1();
    problem_2();
    problem_3();
    problem_4();
    problem_5();
    problem_6();
    problem_7();
}

// Problem 1: Fixed - calculate_length now borrows instead of taking ownership
fn problem_1() {
    println!("Problem 1: Value used after move");
    let s1 = String::from("hello");
    let (_s2, len) = calculate_length(&s1);
    println!("  The length of '{}' is {}.", s1, len);
}

fn calculate_length(s: &String) -> (&String, usize) {
    let length = s.len();
    (s, length)
}

// Problem 2: Fixed - use r1 before creating mutable borrow
fn problem_2() {
    println!("Problem 2: Mutable and immutable borrow conflict");
    let mut s = String::from("hello");
    let r1 = &s;
    println!("  {}", r1);
    // r1 is no longer used after this point
    let r2 = &mut s;
    println!("  {}", r2);
}

// Problem 3: Fixed - use &mut to allow mutation
fn problem_3() {
    println!("Problem 3: Mutating through immutable reference");
    let mut s = String::from("hello");
    add_to_string(&mut s);
    println!("  Result: {}", s);
}

fn add_to_string(s: &mut String) {
    s.push_str(", world");
}

// Problem 4: Fixed - use scopes to separate mutable borrows
fn problem_4() {
    println!("Problem 4: Multiple mutable borrows");
    let mut s = String::from("hello");
    {
        let r1 = &mut s;
        println!("  {}", r1);
    }
    let r2 = &mut s;
    println!("  {}", r2);
}

// Problem 5: Fixed - return owned String instead of reference
fn problem_5() {
    println!("Problem 5: Dangling reference");
    let r = create_string();
    println!("  Got: {}", r);
}

fn create_string() -> String {
    let s = String::from("hello");
    s
}

// Problem 6: Fixed - borrow instead of move in loop
fn problem_6() {
    println!("Problem 6: Ownership in loops");
    let data = String::from("Rust");
    for i in 0..3 {
        print_with_number(&data, i);
    }
}

fn print_with_number(s: &String, n: i32) {
    println!("  {}: {}", n, s);
}

// Problem 7: Fixed - move String outside inner scope
fn problem_7() {
    println!("Problem 7: Lifetime extension");
    let s = String::from("inner scope");
    let result = &s;
    println!("  Result: {}", result);
}

// ============================================================================
// IMPLEMENTATION EXERCISES
// ============================================================================

fn to_uppercase_owned(s: String) -> String {
    s.to_uppercase()
}

fn string_length(s: &String) -> usize {
    s.len()
}

fn append_suffix(s: &mut String, suffix: &str) {
    s.push_str(suffix);
}

fn concat_strings(s1: &str, s2: &str) -> String {
    format!("{}{}", s1, s2)
}

fn first_word(s: &str) -> &str {
    match s.find(' ') {
        Some(i) => &s[..i],
        None => s,
    }
}

// ============================================================================
// TESTS
// ============================================================================

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_calculate_length_borrows() {
        let s = String::from("testing");
        let (_s_ref, len) = calculate_length(&s);
        assert_eq!(len, 7);
        assert_eq!(s, "testing");
    }

    #[test]
    fn test_add_to_string_mutates() {
        let mut s = String::from("hello");
        add_to_string(&mut s);
        assert_eq!(s, "hello, world");
    }

    #[test]
    fn test_create_string_returns_owned() {
        let result = create_string();
        assert_eq!(result, "hello");
    }

    #[test]
    fn test_print_with_number_borrows() {
        let data = String::from("Rust");
        for i in 0..3 {
            print_with_number(&data, i);
        }
        assert_eq!(data, "Rust");
    }

    #[test]
    fn test_to_uppercase_owned() {
        let s = String::from("hello");
        assert_eq!(to_uppercase_owned(s), "HELLO");
    }

    #[test]
    fn test_string_length() {
        let s = String::from("hello");
        assert_eq!(string_length(&s), 5);
    }

    #[test]
    fn test_append_suffix() {
        let mut s = String::from("hello");
        append_suffix(&mut s, " world");
        assert_eq!(s, "hello world");
    }

    #[test]
    fn test_concat_strings() {
        assert_eq!(concat_strings("hello", " world"), "hello world");
    }

    #[test]
    fn test_first_word() {
        assert_eq!(first_word("hello world"), "hello");
        assert_eq!(first_word("rust"), "rust");
    }
}
