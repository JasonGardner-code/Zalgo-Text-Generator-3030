import random

def zalgo_text(input_text, intensity=10):
    zalgo_chars = [
        '\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305',
        '\u0306', '\u0307', '\u0308', '\u0309', '\u030A', '\u030B',
        '\u030C', '\u030D', '\u030E', '\u030F', '\u0310', '\u0311',
        '\u0312', '\u0313', '\u0314', '\u0315', '\u0316', '\u0317',
        '\u0318', '\u0319', '\u031A', '\u031B', '\u031C', '\u031D',
        '\u031E', '\u031F'
    ]

    zalgo_text = ''
    for char in input_text:
        zalgo_text += char
        for _ in range(intensity):
            zalgo_text += random.choice(zalgo_chars)
    
    return zalgo_text

# Example usage:
input_text = "Knock Knock, Neo"
intensity_level = 500000
result = zalgo_text(input_text, intensity_level)
print(result)
