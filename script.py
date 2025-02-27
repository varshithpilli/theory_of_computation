from manim import *

class State(VGroup):
    def __init__(self, label, **kwargs):
        super().__init__(**kwargs)
        circle = Circle(radius=0.75, color=WHITE)
        text = Text(label, font_size=22.5).move_to(circle.get_center())
        self.add(circle, text)


class Question_one(Scene):
    def construct(self):
        toc_text = Text("   Theory Of\nComputation", font_size=50, line_spacing=0.75).move_to(ORIGIN)

        #question one starts
        question_one = Text("Question 1", font_size=50).move_to(ORIGIN)
        question_one_text = Text("NFA that accepts all binary strings that start with either \"0\" or \"11\"", font_size=30).move_to(ORIGIN)
        question_one_transitions = Text("∑ = {0, 1}", font_size=27).move_to(LEFT*4.5 + UP*2)
        question_one_symbols = Text("Q = {q0, q1, q2}", font_size=27).move_to(LEFT*4.5 + UP*1.45)
        question_one_in = Text("q0 = {q0}", font_size=27).move_to(LEFT*2 + UP*2)
        question_one_fin = Text("F = {q2}", font_size=27).move_to(LEFT*2 + UP*1.45)

        question_one_initial_circle= Circle(radius=1, color=WHITE, stroke_width=5)
        question_one_initial_text = Text("q0", font_size="30").move_to(question_one_initial_circle.get_center())
        question_one_initial_arrow = Line(LEFT*2.5, question_one_initial_circle.get_left(), color=WHITE, stroke_width=5).add_tip()
        question_one_initial_state = VGroup(question_one_initial_circle, question_one_initial_arrow, question_one_initial_text)

        question_one_second_state = State("q1").move_to(DOWN*1.05)
        question_one_one_two_arrow = Line(LEFT*2.9+DOWN*1.05, question_one_second_state.get_left(), color=WHITE, stroke_width=3.75).add_tip()
        question_one_one_two_text = Text("1", font_size=25).move_to(DOWN*0.825 + LEFT*2)

        question_one_third_state = State("q2").move_to(DOWN*1.05 + RIGHT*3.5)
        question_one_third_state_out = Circle(radius=0.6, color=WHITE).move_to(DOWN*1.05 + RIGHT*3.5)
        question_one_two_three_arrow = Line(RIGHT*0.75+DOWN*1.05, question_one_third_state.get_left(), color=WHITE, stroke_width=3.75).add_tip()
        question_one_two_three_text = Text("1", font_size=25).move_to(DOWN*0.825 + RIGHT*1.6)

        question_one_one_three_arrow = ArcBetweenPoints((DOWN*0.6 + LEFT*3), (DOWN*0.6 + RIGHT*2.8), angle=-PI/2, color=WHITE).add_tip()
        question_one_one_three_text = Text("0", font_size=25).move_to(UP*0.875)

        question_one_three_three_arrow = ArcBetweenPoints((DOWN*0.25 + RIGHT*3.5), (DOWN*1.2 + RIGHT*4.35), angle=-1.25*PI, color=WHITE).add_tip()
        question_one_three_three_text = Text("0,1", font_size=25).move_to(UP*0.2 + RIGHT*5.35)

        question_one_complete = VGroup(question_one_initial_state, question_one_second_state, question_one_one_two_arrow, question_one_one_two_text, question_one_third_state, question_one_third_state_out, question_one_two_three_arrow, question_one_two_three_text, question_one_one_three_arrow, question_one_one_three_text, question_one_three_three_arrow, question_one_three_three_text)

        data = [
            ["State", "0", "1"],
            ["q0", "q2", "q1"],
            ["q1", "Φ", "q2"],
            ["*q2", "q2", "q2"],
        ]

        rows = len(data)
        cols = len(data[0])
        cell_width = 1.5
        cell_height = 0.75

        table = VGroup()

        for i in range(rows):
            for j in range(cols):
                cell = Rectangle(width=cell_width, height=cell_height, color=WHITE)
                text = Text(data[i][j], font_size=30).move_to(cell.get_center())
                table.add(VGroup(cell, text).move_to(RIGHT * j * cell_width + DOWN * i * cell_height))


        question_one_dashed_border = DashedLine(UP * 2.5, DOWN * 5, color=BLUE, stroke_width=4, dash_length=0.2)
        
        question_one_diagram = Text("Transition Diagram", font_size=30).move_to(UP*2 + LEFT*3.5)
        question_one_table = Text("Transition Table", font_size=30).move_to(UP*2 + RIGHT*3.5)
        table.move_to(RIGHT*3.5 + DOWN*0.5)
        question_one_function = Text("Transition Functions", font_size=30).move_to(UP*2 + RIGHT*3.5)

        question_one_equations = [
            Text("δ(q0, 0) = q2", font_size=30).move_to(UP*1 + RIGHT * 3.5),
            Text("δ(q0, 1) = q1", font_size=30).move_to(UP*0.3 + RIGHT * 3.5),
            Text("δ(q1, 0) = Φ", font_size=30).move_to(DOWN*0.4 + RIGHT * 3.5),
            Text("δ(q1, 1) = q2", font_size=30).move_to(DOWN*1.1 + RIGHT * 3.5),
            Text("δ(q2, 0) = q2", font_size=30).move_to(DOWN*1.8 + RIGHT * 3.5),
            Text("δ(q2, 1) = q2", font_size=30).move_to(DOWN*2.5 + RIGHT * 3.5)
        ]

        question_one_objects = VGroup(*[line.scale(0.7) for line in question_one_equations])
        for text in question_one_objects:
            text.set_opacity(0) 
        #question one ends


        # question two starts
        question_two = Text("Question 2", font_size=50).move_to(ORIGIN)
        question_two_text = Text("DFA that accepts all strings where each \"b\" is immediately followed by \"a\"", font_size=30).move_to(ORIGIN)
        question_two_transitions = Text("∑ = {a, b}", font_size=27).move_to(LEFT*4.5 + UP*2)
        question_two_symbols = Text("Q = {q0, q1, q2}", font_size=27).move_to(LEFT*4.5 + UP*1.45)
        question_two_in = Text("q0 = {q0}", font_size=27).move_to(LEFT*2 + UP*2)
        question_two_fin = Text("F = {q0}", font_size=27).move_to(LEFT*2 + UP*1.45)

        question_two_key_point = Text("Key Points", font_size=27).move_to(UP*2.25)
        question_two_key_point_one = VGroup(Text("1. No condition is given regarding \"a\".", font_size=27).move_to(UP*1.65), Text("Therefore, the DFA would accept strings of \"a\"", font_size=27).move_to(UP*1.25))
        question_two_key_point_two = VGroup(Text("2. No condition is given regarding the minimum length", font_size=27).move_to(UP*0.55), Text("of strings. Therefore, the DFA would accept empty strings", font_size=27).move_to(UP*0.15))
        question_two_key_points = VGroup(question_two_key_point, question_two_key_point_one, question_two_key_point_two)

        question_two_initial_circle= Circle(radius=1, color=WHITE, stroke_width=5).move_to(DOWN*0.9)
        question_two_initial_text = Text("q0", font_size=30).move_to(question_two_initial_circle.get_center())
        question_two_initial_arrow = Line(DOWN*0.9 + LEFT*2.5, question_two_initial_circle.get_left(), color=WHITE, stroke_width=5).add_tip()
        question_two_initial_state = VGroup(question_two_initial_circle, question_two_initial_arrow, question_two_initial_text)

        question_two_second_state = State("q1").move_to(DOWN*1.8)
        question_two_one_two_arrow = ArcBetweenPoints((DOWN*1.25 + LEFT*3.25), (DOWN*1.25 + LEFT * 0.5), angle=-PI/2, color=WHITE).add_tip()
        question_two_one_two_text = Text("b", font_size=25).move_to(UP*0.75 + question_two_one_two_arrow.get_center())

        question_two_two_one_arrow = ArcBetweenPoints((DOWN*2.5 + LEFT * 0.5), (DOWN*2.5 + LEFT*3.25), angle=-PI/2, color=WHITE).add_tip()
        question_two_two_one_text = Text("a", font_size=25).move_to(UP*0.05 + question_two_two_one_arrow.get_center())

        question_two_inside = Circle(radius=0.6, color=WHITE).move_to(LEFT * 3.7 + DOWN * 1.9)

        question_two_one_one_arrow = ArcBetweenPoints((DOWN*2.7 + LEFT * 3.5), (DOWN*2.25 + LEFT*4.4), angle=-PI, color=WHITE).add_tip()
        question_two_one_one_text = Text("a", font_size=25).move_to(DOWN*0.75 + question_two_one_one_arrow.get_center())

        question_two_third_state = State("q2").move_to(DOWN*1.8 + RIGHT*3.5)
        question_two_two_three_arrow = Line(question_two_second_state.get_right(), question_two_third_state.get_left(), color=WHITE, stroke_width=3.75).add_tip()
        question_two_two_three_text = Text("b", font_size=25).move_to(question_two_two_three_arrow.get_center() + UP*0.25)

        question_two_three_three_arrow = ArcBetweenPoints((DOWN*1.05 + RIGHT*3.5), (DOWN*1.7 + RIGHT*4.35), angle=-1.25*PI, color=WHITE).add_tip()
        question_two_three_three_text = Text("a, b", font_size=25).move_to(DOWN*0.3 + RIGHT*5)

        question_two_complete = VGroup(question_two_initial_state, question_two_second_state, question_two_one_two_arrow, question_two_one_two_text, question_two_two_one_arrow, question_two_two_one_text, question_two_third_state, question_two_two_three_arrow, question_two_two_three_text, question_two_three_three_text, question_two_three_three_arrow, question_two_inside, question_two_one_one_arrow, question_two_one_one_text)

        data_2 = [
            ["State", "a", "b"],
            ["*q0", "q0", "q1"],
            ["q1", "q0", "q2"],
            ["q2", "q2", "q2"],
        ]

        row_2 = len(data_2)
        col_2 = len(data_2[0])
        cell_width = 1.5
        cell_height = 0.75

        table_2 = VGroup()

        for i in range(row_2):
            for j in range(col_2):
                cell = Rectangle(width=cell_width, height=cell_height, color=WHITE)
                text = Text(data_2[i][j], font_size=30).move_to(cell.get_center())
                table_2.add(VGroup(cell, text).move_to(RIGHT * j * cell_width + DOWN * i * cell_height))

        question_two_dashed_border = DashedLine(UP * 2.5, DOWN * 5, color=BLUE, stroke_width=4, dash_length=0.2)
        
        question_two_diagram = Text("Transition Diagram", font_size=30).move_to(UP*2 + LEFT*3.5)
        question_two_table = Text("Transition Table", font_size=30).move_to(UP*2 + RIGHT*3.5)
        table_2.move_to(RIGHT*3.5 + DOWN*0.5)

        question_two_function = Text("Transition Functions", font_size=30).move_to(UP*2 + RIGHT*3.5)
        question_two_equations = [
            Text("δ(q0, a) = q0", font_size=30).move_to(UP*1 + RIGHT * 3.5),
            Text("δ(q0, b) = q1", font_size=30).move_to(UP*0.3 + RIGHT * 3.5),
            Text("δ(q1, a) = q0", font_size=30).move_to(DOWN*0.4 + RIGHT * 3.5),
            Text("δ(q1, b) = q2", font_size=30).move_to(DOWN*1.1 + RIGHT * 3.5),
            Text("δ(q2, a) = q2", font_size=30).move_to(DOWN*1.8 + RIGHT * 3.5),
            Text("δ(q2, b) = q2", font_size=30).move_to(DOWN*2.5 + RIGHT * 3.5)
        ]

        question_two_objects = VGroup(*[line.scale(0.7) for line in question_two_equations])
        for text in question_two_objects:
            text.set_opacity(0) 
        # question two ends

        final_text = Text("Thank You", font_size=40)
        names = Text("Varshith Pilli", font_size=30)
        credits = Text("made from scratch, with manim", font_size=20)

        #player starts
        self.wait(1)
        self.play(Write(toc_text, run_time=2))
        self.play(FadeOut(toc_text, run_time=1))
        self.wait(1)

        self.play(Write(question_one, run_time=2))
        self.play(FadeOut(question_one, run_time=1))
        self.wait(1)

        self.play(FadeIn(question_one_text, run_time=2))
        self.play(question_one_text.animate.scale(0.9).shift(UP * 3))
        self.wait(1)

        self.play(FadeIn(question_one_transitions, run_time=1.5))
        self.play(FadeIn(question_one_symbols, run_time=1.5))
        self.play(FadeIn(question_one_in, run_time=1.5))
        self.play(FadeIn(question_one_fin, run_time=1.5))
        self.wait(1)

        self.play(FadeIn(question_one_initial_circle), FadeIn(question_one_initial_text))
        self.play(FadeIn(question_one_initial_arrow))
        self.play(question_one_initial_state.animate.scale(0.75).shift(LEFT * 3.5 + DOWN * 1.05))
        self.wait(1)

        self.play(Create(question_one_one_two_arrow))
        self.play(FadeIn(question_one_one_two_text))
        self.play(FadeIn(question_one_second_state))
        self.wait(1)

        self.play(Create(question_one_two_three_arrow))
        self.play(FadeIn(question_one_two_three_text))
        self.play(FadeIn(question_one_third_state), FadeIn(question_one_third_state_out))
        self.wait(1)

        self.play(Create(question_one_one_three_arrow))
        self.play(FadeIn(question_one_one_three_text))
        self.wait(1)

        self.play(Create(question_one_three_three_arrow))
        self.play(FadeIn(question_one_three_three_text))
        self.wait(1)

        self.play(question_one_complete.animate.scale(0.5).shift(LEFT * 3.5), FadeOut(question_one_symbols), FadeOut(question_one_transitions), FadeOut(question_one_in), FadeOut(question_one_fin))
        self.wait(1)
        
        self.play(Create(question_one_dashed_border), Write(question_one_diagram, run_time=1))
        self.play(Write(question_one_table, run_time=1))
        self.play(FadeIn(table))
        self.wait(1)

        self.play(question_one_complete.animate.shift(DOWN * 2), table.animate.scale(0.75).shift(LEFT*7 + UP*1), FadeOut(question_one_diagram), FadeOut(question_one_table), FadeIn(question_one_function))

        self.play(*[FadeIn(eq) for eq in question_one_equations], lag_ratio=0.75)
        self.wait(1)

        for text in question_one_objects:
            text.set_opacity(1) 
            self.play(Write(text))
            self.wait(0.25)
        self.wait(1)

        self.play(
            FadeOut(question_one_dashed_border),
            FadeOut(question_one_complete),
            FadeOut(table),
            FadeOut(question_one_text),
            FadeOut(question_one_function),
            *[FadeOut(text) for text in question_one_objects]
        )

        self.wait(2)

        self.play(Write(question_two, run_time=1.5))
        self.play(FadeOut(question_two, run_time=1))
        self.wait(1)

        self.play(FadeIn(question_two_text, run_time=1.5))
        self.play(question_two_text.animate.scale(0.9).shift(UP * 3))
        self.wait(1)

        self.play(Write(question_two_key_point, run_time=1.5))
        self.play(Write(question_two_key_point_one, run_time=2.5))
        self.play(Write(question_two_key_point_two, run_time=2.5))
        self.wait(3)

        self.play(question_two_key_points.animate.scale(0.75).shift(RIGHT * 2.5 + UP * 0.25))
        self.wait(1)

        self.play(FadeIn(question_two_transitions, run_time=1.5))
        self.play(FadeIn(question_two_symbols, run_time=1.5))
        self.play(FadeIn(question_two_in, run_time=1.5))
        self.play(FadeIn(question_two_fin, run_time=1.5))
        self.wait(1)

        self.play(FadeIn(question_two_initial_circle), FadeIn(question_two_initial_text))
        self.play(FadeIn(question_two_initial_arrow))
        self.play(question_two_initial_state.animate.scale(0.75).shift(LEFT * 3.5 + DOWN * 1))
        self.wait(1)

        self.play(Create(question_two_one_two_arrow))
        self.play(FadeIn(question_two_one_two_text))
        self.play(FadeIn(question_two_second_state))
        self.wait(1)

        self.play(Create(question_two_two_one_arrow))
        self.play(FadeIn(question_two_two_one_text))
        self.play(FadeIn(question_two_inside))
        self.wait(1)

        self.play(Create(question_two_one_one_arrow))
        self.play(FadeIn(question_two_one_one_text))
        self.wait(1)

        self.play(Create(question_two_two_three_arrow))
        self.play(FadeIn(question_two_two_three_text))
        self.wait(1)

        self.play(FadeIn(question_two_third_state))
        self.wait(1)

        self.play(Create(question_two_three_three_arrow))
        self.play(FadeIn(question_two_three_three_text))
        self.wait(1)

        self.play(question_two_complete.animate.scale(0.5).shift(LEFT * 3.5 + UP), FadeOut(question_two_symbols), FadeOut(question_two_transitions), FadeOut(question_two_key_points), FadeOut(question_two_in), FadeOut(question_two_fin))
        self.wait(1)

        self.play(Create(question_two_dashed_border), Write(question_two_diagram, run_time=1))
        self.play(Write(question_two_table, run_time=1))
        self.play(FadeIn(table_2))
        self.wait(1)

        self.play(question_two_complete.animate.shift(DOWN * 1.75), table_2.animate.scale(0.75).shift(LEFT*7 + UP*1), FadeOut(question_two_diagram), FadeOut(question_two_table), FadeIn(question_two_function))
        self.play(*[FadeIn(eq) for eq in question_two_equations], lag_ratio=0.75)
        self.wait(1)

        for text in question_two_objects:
            text.set_opacity(1) 
            self.play(Write(text))
            self.wait(0.25)
        self.wait(1)

        self.play(
            FadeOut(question_two_dashed_border),
            FadeOut(question_two_complete),
            FadeOut(table_2),
            FadeOut(question_two_text),
            FadeOut(question_two_function),
            *[FadeOut(text) for text in question_two_objects]
        )

        self.wait(2)
        self.play(Write(final_text, run_time=1.5))
        self.play(FadeOut(final_text), run_time=1)


        self.play(FadeIn(names), run_time=2)
        self.wait(2)
        self.play(FadeOut(names), run_time=1)
        self.play(FadeIn(credits), run_time=1.5)
        self.play(FadeOut(credits))
        self.wait(2)