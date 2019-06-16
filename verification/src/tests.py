"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": '12:30',
            "answer": '12:30 p.m.'
        },
        {
            "input": '09:00',
            "answer": '9:00 a.m.'
        }
    ],
    "Extra": [
        {
            "input": '23:15',
            "answer": '11:15 p.m.'
        },
        {
            "input": '18:50',
            "answer": '6:50 p.m.'
        },
	{
            "input": '07:07',
            "answer": '7:07 a.m.'
        },
	{
            "input": '00:00',
            "answer": '12:00 a.m.'
        },
	{
            "input": '12:00',
            "answer": '12:00 p.m.'
        }
    ]
}
