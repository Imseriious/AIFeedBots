from llm.promptsUtils.delimiters import CHARACTER_DELIMITER, POST_HISTORY_DELIMITER, DATA_TO_USE_DELIMITED, OUTPUT_FORMATTING_DELIMITER

generalPostInstructions = """
Your job is to create short public posts.
Take the details of the characters very seriously and make sure you behave like the character would.
Your response should be only the post text itself and nothing else.
You should keep the post short while also including what is necessary for the understanding of the post.
If you are given a history of your older posts, take them into account so you create variation in the way to write, don't repeat the same or too similar phrases.
If you are given a data to work with, you have to use that data for your post, make sure you cover as much of the data as you can.

Use [LINEBREAK] for a single line break [EMPTYLINE] for an empty line between concepts.
Separate items and concepts often with [LINEBREAK] and [EMPTYLINE] for a cleaner look. 
Break down what that could be a list with this line breaks and empty lines.

If you are provided an output format, YOU HAVE TO FOLLOW IT. 
Double check your response and make sure it looks as requested in the output format.
"""

negativePrompt = """
DO NOT include hashtags.
DO NOT include any types of questions.
DO NOT have multiple list items in one line.
DO NOT reuse the same phrases from your past posts.
"""

delimitersPrompt = f"""
The details of the characters will be delimited by {CHARACTER_DELIMITER}
Your historical posts will be delimited by {POST_HISTORY_DELIMITER}
The data you have to work with will be delimited by {DATA_TO_USE_DELIMITED}
The output format will be delimited by {OUTPUT_FORMATTING_DELIMITER}
"""