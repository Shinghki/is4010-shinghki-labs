#[derive(Debug, PartialEq, Clone)]
pub enum PasswordStrength {
    Weak,
    Medium,
    Strong,
    VeryStrong,
}

pub fn validate_strength(password: &str) -> PasswordStrength {
    let len = password.len();
    let has_lower = password.chars().any(|c| c.is_lowercase());
    let has_upper = password.chars().any(|c| c.is_uppercase());
    let has_digit = password.chars().any(|c| c.is_ascii_digit());
    let has_symbol = password.chars().any(|c| !c.is_alphanumeric());

    match (len, has_lower, has_upper, has_digit, has_symbol) {
        (l, true, true, true, true) if l >= 12 => PasswordStrength::VeryStrong,
        (l, true, true, true, _) if l >= 8 => PasswordStrength::Strong,
        (l, true, true, _, _) if l >= 8 => PasswordStrength::Medium,
        _ => PasswordStrength::Weak,
    }
}

pub fn check_common_patterns(password: &str) -> bool {
    let lower = password.to_lowercase();

    let sequential_patterns = ["123", "234", "345", "456", "567", "678", "789"];
    let keyboard_patterns = ["qwerty", "asdf", "zxcv"];

    if sequential_patterns.iter().any(|p| lower.contains(p)) {
        return true;
    }

    if keyboard_patterns.iter().any(|p| lower.contains(p)) {
        return true;
    }

    let chars: Vec<char> = lower.chars().collect();
    chars
        .windows(3)
        .any(|window| window[0] == window[1] && window[1] == window[2])
}

pub fn calculate_entropy(password: &str) -> f64 {
    if password.is_empty() {
        return 0.0;
    }

    let has_lower = password.chars().any(|c| c.is_lowercase());
    let has_upper = password.chars().any(|c| c.is_uppercase());
    let has_digit = password.chars().any(|c| c.is_ascii_digit());
    let has_symbol = password.chars().any(|c| !c.is_alphanumeric());

    let mut charset_size: f64 = 0.0;

    if has_lower {
        charset_size += 26.0;
    }
    if has_upper {
        charset_size += 26.0;
    }
    if has_digit {
        charset_size += 10.0;
    }
    if has_symbol {
        charset_size += 8.0;
    }

    if charset_size == 0.0 {
        0.0
    } else {
        (password.len() as f64) * charset_size.log2()
    }
}
