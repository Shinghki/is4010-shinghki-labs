# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging
**My Prompt:**
> Context: I have a function `sum_of_evens` that is supposed to sum even numbers but is currently adding odd numbers.
> Persona: You are a senior Python developer.
> Task: Find the logical error in the `if` statement and provide the fixed code.
> Format: Provide the corrected code in a Python block and a brief explanation.

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:  # Fixed the bug here
            total += num
    return total
    

## Problem 2: Refactoring
**My Prompt:**
Context: I have a function get_names_of_adults that uses a manual loop. 
Persona: You are a Python expert focused on clean code. 
Task: Refactor this function to use a list comprehension. 
Format: Provide the refactored code block.

**AI's Corrected Code:**

def get_names_of_adults(users):
    return [user['name'] for user in users if user['age'] >= 18]
  

## Problem 3: Documenting
**My Prompt**
Context: I have a function calculate_area(length, width) that lacks documentation. Persona: You are a technical documentation specialist. 
Task: Write a professional NumPy-style docstring including Parameters, Returns, and Raises sections. 
Format: Provide the full code with the new docstring.

**AI's Corrected Code:**

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : float or int
        The length of the rectangle.
    width : float or int
        The width of the rectangle.

    Returns
    -------
    float or int
        The calculated area.

    Raises
    ------
    ValueError
        If length or width are non-positive.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width


---

### Final Check
1.  **Save** both files.
2.  Open your terminal in VS Code and run the **Git commands** to submit:

```bash
git add week02/
git commit -m "Complete Lab 02: AI-assisted development"
git push origin main   

