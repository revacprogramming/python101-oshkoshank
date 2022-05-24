def new_func():
    text = "X-DSPAM-Confidence:    0.8475"
    print(float(text[text.find('0'):]))

new_func()