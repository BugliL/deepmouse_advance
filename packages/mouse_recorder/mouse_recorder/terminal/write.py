import os

def move_up(times=1):
    # TODO: include me in progress_bar function, i'm too small
    return '\x1b[A' * times


def clear_line(end='\r'):
    # TODO: include me in progress_bar function and in clear_all, i'm too small
    characters = os.get_terminal_size().columns
    return ' '*characters + end


def clear_all():
    lines = os.get_terminal_size().lines
    return "".join([ clear_line(end='\n') for _ in range(lines) ]) \
        + move_up(lines)


def progress_bar(current_value, max_value, title='', leave_title=False):
    percent_space = 5
    columns = os.get_terminal_size().columns 
    characters = columns - (4+percent_space)  # removing  present characters from counting
    progress = min(((current_value + 1) / max_value) * 100, 100)  # calculate progress
    printed_progress = int(progress*characters/100)  # calculate number of characters to print
    bar_template = '\n[{:<' + str(characters) + '}] {:>'+ str(percent_space) + '.1f}%'  # creating template to print
    
    result = clear_line() + title  # using a variable instead of printing all time (print costs)
    bar = bar_template.format('#'*printed_progress, progress)  # creating bar
    result += bar + move_up() +'\r' 
    
    return result

def print_progress_bar(current_value, max_value, title='', leave_title=False):
    print(
        progress_bar(current_value, max_value, title, leave_title), 
        end=''
    )


if __name__=='__main__':
    import time

    for i in range(100):
        time.sleep(0.1)
        print_progress_bar(
            current_value=i+80,
            max_value=100,
            title='Titolo di prova',
        )
