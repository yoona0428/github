def rep_char(c, n):
    print(c * n)
   

def draw_line_string(msg):
    nstr = len(msg)
    msg1 = ' Hello ' + msg +', '
    msg2 = ' Welcom to Seoul. '
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr)
    print(msg1)
    print(msg2)
    rep_char('-', nstr)


msg = input('Input his/her name: ')
draw_line_string(msg)

