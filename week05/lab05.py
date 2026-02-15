from typing import Dict, List, Optional


# Top-level user data
users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]


def calculate_average_age(users: List[Dict]) -> Optional[float]:
    """Calculate the average age for users.

    The function is defensive: it skips non-dictionary items, excludes booleans
    (which are subclasses of ``int``), accepts ``int`` and ``float`` ages, and
    will attempt to coerce numeric strings (for example, ``"30"`` or
    ``"30.5"``) to floats. If no valid ages are found, ``None`` is returned.

    Parameters
    ----------
    users : list of dict
        Sequence of user dictionaries. Each dictionary may include an ``age``
        key. If ``users`` is ``None``, it is treated like an empty sequence.

    Returns
    -------
    float or None
        The average age of valid numeric ages, or ``None`` if none are found.
    """
    if users is None:
        return 0.0

    total = 0.0
    count = 0
    for user in users:
        if not isinstance(user, dict):
            continue
        age = user.get("age")
        if isinstance(age, bool):
            continue
        if isinstance(age, (int, float)):
            total += float(age)
            count += 1
            continue
        if isinstance(age, str):
            age_str = age.strip()
            try:
                val = float(age_str)
            except ValueError:
                continue
            total += val
            count += 1
    if count == 0:
        return 0.0
    return total / count


def get_active_user_emails(users: List[Dict]) -> List[str]:
    """Return validated emails of users marked as active.

    This function is defensive: it skips non-dictionary items, only considers
    users with ``is_active`` strictly equal to ``True`` to avoid treating
    arbitrary truthy values (like the string ``"yes"``) as active, and it
    validates that ``email`` is a non-empty string containing an ``@``.

    Parameters
    ----------
    users : list of dict
        Sequence of user dictionaries. If ``users`` is ``None``, an empty list
        is returned.

    Returns
    -------
    list of str
        List of validated email addresses for active users.
    """
    if users is None:
        return []

    emails: List[str] = []
    for user in users:
        if not isinstance(user, dict):
            continue
        if user.get("is_active") is not True:
            continue
        email = user.get("email")
        if not isinstance(email, str):
            continue
        email_clean = email.strip()
        if not email_clean or "@" not in email_clean:
            continue
        emails.append(email_clean)
    return emails


def main() -> None:
    """Run example using the top-level ``users`` list.

    This function uses the module-level :data:`users` list so the file contains
    the data, the processing functions, and a simple executable entry point.
    """

    avg = calculate_average_age(users)
    if avg is None:
        print("average user age: No valid ages found")
    else:
        print(f"average user age: {avg:.2f}")

    emails = get_active_user_emails(users)
    print(f"active user emails: {emails}")


if __name__ == "__main__":
    main()