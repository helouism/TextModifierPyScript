import string
import re
from pyscript import document
from pyodide.ffi import create_proxy


class Main:

    def upper_case(event):
        input_text = document.querySelector("#input_text")
        text = input_text.value
        input_text.value =  text.upper()

    def lower_case(event):
        input_text = document.querySelector("#input_text")
        text = input_text.value
        input_text.value = text.lower()

    def capitalized_case(event):
        input_text = document.querySelector("#input_text")
        text = input_text.value
        input_text.value = string.capwords(text, sep=None)


def charCount(event):
    input_text = document.querySelector("#input_text")
    text = input_text.value
    total_char = len(list(text))
    total_char_div = document.querySelector("#char_count")
    total_char_div.textContent = f"Character count : {total_char}"


def wordCount(event):
    input_text = document.querySelector("#input_text")
    text = input_text.value
    total_word = len(re.findall(r'\w+', text))
    total_word_div = document.querySelector("#word_count")
    total_word_div.textContent = f"Word count : {total_word}"


char_count_proxy = create_proxy(charCount)
word_count_proxy = create_proxy(wordCount)

inputText = document.getElementById("input_text")
inputText.addEventListener("input", char_count_proxy)
inputText.addEventListener("input", word_count_proxy)
