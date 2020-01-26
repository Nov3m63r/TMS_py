from time import sleep

symbols = '▏▎▍▌▋▊▉█'


for i in range(0, 201):
    print(
        f'\r▓{symbols[-1] * (i // 8)}{symbols[i % 8] if i != 200 else ""}'
        f'{" " * (24 - i // 8)}▓ {i / 2}%',
        end=''
    )
    sleep(0.07)
