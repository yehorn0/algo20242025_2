def process_scores(scores: list[tuple[str, int]]) -> dict[str, int]:
    ...


scores = [
    ('Alice', 85),
    ('Bob', 75),
    ('Charlie', 39),
    ('David', 62),
    ('Eve', 91)
]
"""
{
    "Eve": 91,
    "Alice": 85,
    "Bob": 75,
}
"""
