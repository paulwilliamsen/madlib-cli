from madlib import generate_prompts, get_template



input_values = ['funny','crazy','Beth','jumped','Seth','famous','beautiful','elephants','Horse','termite','Jessica','dumb','iguanas','old','mountains','33','Steve','2000','balls','3000','bats'
]
output_text = """
Make Me A Video Game!
I the funny and crazy Beth have jumped Seth's famous sister and plan to steal her beautiful elephants!
What are a horse and backpacking termite to do? Before you can help Jessica, you'll have to collect the dumb iguanas and old mountains that open up the 33 worlds connected to Steve's Lair. There are 2000 balls and 3000 bats in the game, along with hundreds of other goodies for you to find.
"""

def test_madlib_user_input():
    actual = write_result(input_values)
    expected = output_text
    assert actual == expected