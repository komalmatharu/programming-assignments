from DrawingPanel import *
def main():
    panel = DrawingPanel(500, 500, background="turquoise")
    draw_turtle(panel)
def draw_turtle(p):
    # ground + outline
    p.fill_rect(0, 380, 500, 150, color="burlywood2")
    p.draw_line(0, 380, 500, 380, color="black")
    # 4 legs + outline
    p.fill_oval(110, 330, 25, 50, color="sea green")
    p.draw_oval(110, 330, 25, 50, color="black")
    p.fill_oval(140, 330, 25, 50, color="sea green")
    p.draw_oval(140, 330, 25, 50, color="black")
    p.fill_oval(210, 330, 25, 50, color="sea green")
    p.draw_oval(210, 330, 25, 50, color="black")
    p.fill_oval(240, 330, 25, 50, color="sea green")
    p.draw_oval(240, 330, 25, 50, color="black")
    # tail + outline
    p.fill_arc(55, 250, 40, 150, 1, 15, color="sea green")
    p.draw_line(76, 325, 90, 310, color="black")
    p.draw_line(76, 325, 94, 325, color="black")
    # shell + outline
    p.fill_oval(90, 255, 200, 110, color="dark goldenrod")
    p.draw_oval(90, 255, 200, 110, color="black")
    p.fill_oval(100, 250, 190, 100, color="orange4")
    p.draw_oval(100, 250, 190, 100, color="black")
    # shell detail
    p.draw_line(140, 308, 109, 322, color="dark goldenrod")
    p.draw_line(170, 320, 162, 347, color="dark goldenrod")
    p.draw_line(211, 320, 222, 350, color="dark goldenrod")
    p.draw_line(240, 305, 273, 329, color="dark goldenrod")
    p.draw_line(140, 287, 110, 280, color="dark goldenrod")
    p.draw_line(164, 275, 153, 256, color="dark goldenrod")
    p.draw_line(200, 275, 208, 251, color="dark goldenrod")
    p.draw_line(230, 283, 247, 258, color="dark goldenrod")
    # shell detail - connecting the line details
    p.draw_line(140, 308, 170, 320, color="dark goldenrod")
    p.draw_line(170, 320, 211, 320, color="dark goldenrod")
    p.draw_line(211, 320, 240, 305, color="dark goldenrod")
    p.draw_line(140, 308, 140, 287, color="dark goldenrod")
    p.draw_line(140, 287, 164, 275, color="dark goldenrod")
    p.draw_line(164, 275, 200, 275, color="dark goldenrod")
    p.draw_line(200, 275, 230, 283, color="dark goldenrod")
    p.draw_line(230, 283, 240, 305, color="dark goldenrod")
    # head + outline
    p.fill_oval(250, 220, 100, 100, color="sea green")
    p.draw_oval(250, 220, 100, 100, color="black")
    # face (mouth + eyes)
    p.fill_oval(290, 265, 30, 30, color="black")
    p.fill_oval(288, 262, 35, 30, color="sea green")
    p.fill_oval(284, 258, 8, 8, color="white")
    p.draw_oval(284, 258, 8, 8, color="black")
    p.fill_oval(317, 258, 8, 8, color="white")
    p.draw_oval(317, 258, 8, 8, color="black")
    p.fill_oval(285, 258, 6, 6, color="black")
    p.fill_oval(318, 258, 6, 6, color="black")
    
main()
