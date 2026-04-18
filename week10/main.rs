// ============================================================================
// IMPLEMENTATION EXERCISES
// Write these functions from scratch with correct ownership/borrowing
// ============================================================================

/// Takes ownership of a String, converts it to uppercase, and returns it.
/// This demonstrates the "consume and return" pattern.
///
/// # Arguments
/// * `s` - String to convert (ownership transferred)
///
/// # Returns
/// * New String with all characters in uppercase
fn to_uppercase_owned(s: String) -> String {
    // TODO: Implement this
    // Hint: Use .to_uppercase() method
    unimplemented!()
}

/// Borrows a String immutably and returns its length.
/// This demonstrates read-only borrowing.
///
/// # Arguments
/// * `s` - Reference to String to measure
///
/// # Returns
/// * Length of the string
fn string_length(s: &String) -> usize {
    // TODO: Implement this
    unimplemented!()
}

/// Borrows a String mutably and appends a suffix to it.
/// This demonstrates in-place modification through mutable borrowing.
///
/// # Arguments
/// * `s` - Mutable reference to String to modify
/// * `suffix` - String slice to append
fn append_suffix(s: &mut String, suffix: &str) {
    // TODO: Implement this
    // Hint: Use .push_str() method
    unimplemented!()
}

/// Creates a new String by concatenating two borrowed strings.
/// This demonstrates creating owned data from borrowed data.
///
/// # Arguments
/// * `s1` - First string slice
/// * `s2` - Second string slice
///
/// # Returns
/// * New String containing s1 + s2
fn concat_strings(s1: &str, s2: &str) -> String {
    // TODO: Implement this
    // Hint: format!() macro or String::from() + push_str()
    unimplemented!()
}

/// Finds the first word in a string and returns it as a string slice.
/// This demonstrates returning borrowed data with implicit lifetimes.
///
/// # Arguments
/// * `s` - String slice to search
///
/// # Returns
/// * String slice containing the first word (up to first space),
///   or the entire string if no space is found
fn first_word(s: &str) -> &str {
    // TODO: Implement this
    // Hint: Use .find(' ') to locate the first space
    // Hint: Use &s[start..end] to create a slice
    unimplemented!()
}