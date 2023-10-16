from pyspark.sql.functions import udf, lit, split
from pyspark.sql.types import IntegerType, StringType
import random 


@udf(returnType=IntegerType())
def get_course_rate(text):
    random.seed(text) # Use text as a seed for reproducibility
    a = random.randint(1, 5)
    return a 


@udf(returnType=StringType())
def customize_text(text):
    text = text.upper()
    words = text.split(' ')     
    words = words[1:]
    text = " ".join(words) 
    supposed1 = "Certification Course in English"
    supposed2 = "Certification Course"
    text = text.replace(supposed1.upper(), '')
    text = text.replace(supposed2.upper(), ' ')
    # Split the text into words and join back together with a single space
    text = ' '.join(text.split())
    return text


@udf(returnType=IntegerType())
def have_multiple_courses(text):
    return len(text.split("-"))


def split_courses(text):
    return split(lit(text), "-")  # Use lit to create a literal column


@udf(returnType=IntegerType())
def max_courses(row):
    c = 0
    for i in row: 
        if i > c: 
            c = i
    return c

@udf(returnType=StringType())
def remove_lang(text):
    if text is not None:
        list_text = text.lower().split(" ")
        if "in" in list_text:
            index = list_text.index("in")
            list_text = list_text[:index]
        return " ".join(list_text).strip()
    else:
        return "---"
