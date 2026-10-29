"""
Main GUI Application - Python Quiz Application
Diploma in Computer Science Engineering - 3rd Semester Micro-Project
Developed with: Python 3 and Tkinter (GUI)

Key Concepts Demonstrated:
  - Object-Oriented Programming (OOP) with Tkinter Frames and Widgets
  - Event-Driven Programming (Callbacks, Command bindings)
  - Tkinter GUI Design (Labels, Entry, Radiobuttons, Buttons, Canvas, Progressbar)
  - High-DPI Display Scaling on Windows OS
  - Real-time State Synchronization and Input Validation
"""

import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox
from quiz_engine import QuizManager

# Enable Windows High-DPI Awareness to ensure sharp rendering on modern laptop screens
try:
    if sys.platform.startswith("win"):
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass


class QuizApp(tk.Tk):
    """
    Main Application Window.
    Coordinates between Home, Quiz, and Result views.
    """

    def __init__(self):
        super().__init__()

        # Window Configurations
        self.title("Python Quiz Master | Diploma CSE Micro-Project")
        self.geometry("900x680")
        self.minsize(850, 640)
        self.configure(bg="#F1F5F9")  # Modern slate-100 background

        # Center Window on Screen
        self.center_window(900, 680)

        # Initialize the Business Logic Engine
        data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quiz_data.json")
        self.quiz_manager = QuizManager(json_file_path=data_path)

        # Application State
        self.selected_option_var = tk.StringVar(value="")

        # Setup Custom TTK Styles
        self.setup_styles()

        # Container Frame where screens are mounted
        self.container = tk.Frame(self, bg="#F1F5F9")
        self.container.pack(fill=tk.BOTH, expand=True)

        # Show Home Screen initially
        self.show_home_screen()

    def center_window(self, width, height):
        """Calculates screen coordinates to open the window perfectly in the center."""
        self.update_idletasks()
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        pos_x = max(0, (screen_w - width) // 2)
        pos_y = max(0, (screen_h - height) // 2)
        self.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

    def setup_styles(self):
        """Sets up custom ttk styling themes and colors."""
        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        # Custom Accent Button
        self.style.configure(
            "Primary.TButton",
            font=("Segoe UI", 11, "bold"),
            background="#4F46E5",
            foreground="#FFFFFF",
            borderwidth=0,
            padding=10,
            focuscolor="none"
        )
        self.style.map(
            "Primary.TButton",
            background=[("active", "#4338CA"), ("disabled", "#CBD5E1")]
        )

        # Secondary Button
        self.style.configure(
            "Secondary.TButton",
            font=("Segoe UI", 10, "bold"),
            background="#E2E8F0",
            foreground="#334155",
            borderwidth=0,
            padding=8,
            focuscolor="none"
        )
        self.style.map(
            "Secondary.TButton",
            background=[("active", "#CBD5E1")]
        )

        # Success / Finish Button
        self.style.configure(
            "Success.TButton",
            font=("Segoe UI", 11, "bold"),
            background="#10B981",
            foreground="#FFFFFF",
            borderwidth=0,
            padding=10,
            focuscolor="none"
        )
        self.style.map(
            "Success.TButton",
            background=[("active", "#059669")]
        )

        # Danger / Exit Button
        self.style.configure(
            "Danger.TButton",
            font=("Segoe UI", 10, "bold"),
            background="#FEE2E2",
            foreground="#DC2626",
            borderwidth=0,
            padding=8,
            focuscolor="none"
        )
        self.style.map(
            "Danger.TButton",
            background=[("active", "#FCA5A5")]
        )

        # Progress bar
        self.style.configure(
            "Horizontal.TProgressbar",
            troughcolor="#E2E8F0",
            background="#4F46E5",
            lightcolor="#4F46E5",
            darkcolor="#4F46E5",
            bordercolor="#E2E8F0",
            thickness=8
        )

    def clear_container(self):
        """Clears all widgets from the container before loading a new screen."""
        for widget in self.container.winfo_children():
            widget.destroy()

    # =========================================================================
    # 1. HOME SCREEN
    # =========================================================================
    def show_home_screen(self):
        """Renders the attractive home screen with user name entry and category selection."""
        self.clear_container()

        # Main wrapper with padding
        home_frame = tk.Frame(self.container, bg="#F1F5F9")
        home_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)

        # Top Header Banner
        header_frame = tk.Frame(home_frame, bg="#F1F5F9")
        header_frame.pack(fill=tk.X, pady=(0, 20))

        badge_lbl = tk.Label(
            header_frame,
            text="DIPLOMA CSE • 3RD SEMESTER MICRO-PROJECT",
            font=("Segoe UI", 9, "bold"),
            bg="#EEF2FF",
            fg="#4F46E5",
            padx=12,
            pady=4
        )
        badge_lbl.pack(anchor="center")

        title_lbl = tk.Label(
            header_frame,
            text="Interactive Python Quiz Application",
            font=("Segoe UI", 24, "bold"),
            bg="#F1F5F9",
            fg="#0F172A",
            pady=6
        )
        title_lbl.pack(anchor="center")

        subtitle_lbl = tk.Label(
            header_frame,
            text="Test your conceptual knowledge in Programming, Computer Fundamentals & Tech GK",
            font=("Segoe UI", 11),
            bg="#F1F5F9",
            fg="#64748B"
        )
        subtitle_lbl.pack(anchor="center")

        # White Card Container for Inputs
        card = tk.Frame(home_frame, bg="#FFFFFF", relief=tk.FLAT, bd=0)
        card.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Card Inner Content
        content = tk.Frame(card, bg="#FFFFFF", padx=35, pady=25)
        content.pack(fill=tk.BOTH, expand=True)

        # Student Name Input
        name_title = tk.Label(
            content,
            text="Student Name *",
            font=("Segoe UI", 11, "bold"),
            bg="#FFFFFF",
            fg="#1E293B"
        )
        name_title.pack(anchor="w", pady=(0, 6))

        self.name_entry = tk.Entry(
            content,
            font=("Segoe UI", 12),
            bg="#F8FAFC",
            fg="#0F172A",
            relief=tk.SOLID,
            bd=1,
            insertbackground="#4F46E5"
        )
        self.name_entry.pack(fill=tk.X, ipady=8, pady=(0, 20))
        self.name_entry.focus_set()

        # Category Selection
        cat_title = tk.Label(
            content,
            text="Select Quiz Category *",
            font=("Segoe UI", 11, "bold"),
            bg="#FFFFFF",
            fg="#1E293B"
        )
        cat_title.pack(anchor="w", pady=(0, 8))

        categories = self.quiz_manager.get_categories()
        if not categories:
            categories = ["Python Programming", "Computer Fundamentals", "General Knowledge"]

        self.selected_category_var = tk.StringVar(value=categories[0])
        self.category_cards_data = []

        cat_frame = tk.Frame(content, bg="#FFFFFF")
        cat_frame.pack(fill=tk.X, pady=(0, 25))

        cat_icons = {
            "Python Programming": "🐍",
            "Computer Fundamentals": "💻",
            "General Knowledge": "🌍"
        }
        cat_descriptions = {
            "Python Programming": "Core syntax, data types & functions",
            "Computer Fundamentals": "Hardware, architecture & system software",
            "General Knowledge": "Tech history, inventors & world facts"
        }

        def choose_category(cat_name):
            self.selected_category_var.set(cat_name)
            self.refresh_category_cards()

        for cat_name in categories:
            icon = cat_icons.get(cat_name, "📚")
            q_count = len(self.quiz_manager.raw_data.get("categories", {}).get(cat_name, []))
            desc = cat_descriptions.get(cat_name, "Multiple Choice Questions")
            sub = f"{q_count} Questions • {desc}"

            card = tk.Frame(
                cat_frame,
                bg="#FFFFFF",
                relief=tk.FLAT,
                bd=0,
                highlightthickness=2,
                cursor="hand2",
                padx=16,
                pady=10
            )
            card.pack(fill=tk.X, pady=4)

            # Left side: Icon + Title & Subtitle
            left_box = tk.Frame(card, bg="#FFFFFF", cursor="hand2")
            left_box.pack(side=tk.LEFT, fill=tk.Y)

            icon_lbl = tk.Label(
                left_box,
                text=icon,
                font=("Segoe UI Emoji", 16),
                bg="#FFFFFF",
                cursor="hand2"
            )
            icon_lbl.pack(side=tk.LEFT, padx=(0, 12))

            text_col = tk.Frame(left_box, bg="#FFFFFF", cursor="hand2")
            text_col.pack(side=tk.LEFT, anchor="w")

            title_lbl = tk.Label(
                text_col,
                text=cat_name,
                font=("Segoe UI", 11, "bold"),
                bg="#FFFFFF",
                fg="#0F172A",
                cursor="hand2"
            )
            title_lbl.pack(anchor="w")

            sub_lbl = tk.Label(
                text_col,
                text=sub,
                font=("Segoe UI", 9),
                bg="#FFFFFF",
                fg="#64748B",
                cursor="hand2"
            )
            sub_lbl.pack(anchor="w")

            # Right side status indicator badge
            badge_lbl = tk.Label(
                card,
                text="○",
                font=("Segoe UI", 10, "bold"),
                bg="#FFFFFF",
                fg="#CBD5E1",
                cursor="hand2"
            )
            badge_lbl.pack(side=tk.RIGHT)

            card_entry = {
                "card": card,
                "left_box": left_box,
                "text_col": text_col,
                "icon_lbl": icon_lbl,
                "title_lbl": title_lbl,
                "sub_lbl": sub_lbl,
                "badge_lbl": badge_lbl,
                "value": cat_name
            }
            self.category_cards_data.append(card_entry)

            # Bind mouse clicks and hover transitions
            for w in [card, left_box, text_col, icon_lbl, title_lbl, sub_lbl, badge_lbl]:
                w.bind("<Button-1>", lambda e, c=cat_name: choose_category(c))
                w.bind("<Enter>", lambda e, ce=card_entry: self.on_cat_hover(ce, True))
                w.bind("<Leave>", lambda e, ce=card_entry: self.on_cat_hover(ce, False))

        self.refresh_category_cards()

        # Action Buttons Area
        btn_box = tk.Frame(content, bg="#FFFFFF")
        btn_box.pack(fill=tk.X, pady=(10, 0))

        start_btn = ttk.Button(
            btn_box,
            text="Start Quiz  ➔",
            style="Primary.TButton",
            command=self.handle_start_quiz
        )
        start_btn.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)

        exit_btn = ttk.Button(
            btn_box,
            text="Exit Application",
            style="Danger.TButton",
            command=self.confirm_exit
        )
        exit_btn.pack(side=tk.RIGHT, padx=(10, 0))

        # Footer Info
        footer = tk.Label(
            home_frame,
            text="Tip: You can navigate backward and forward during the quiz to review or modify your answers.",
            font=("Segoe UI", 9, "italic"),
            bg="#F1F5F9",
            fg="#94A3B8"
        )
        footer.pack(side=tk.BOTTOM, pady=(10, 0))

    def handle_start_quiz(self):
        """Validates user input and transitions to the quiz interface."""
        name = self.name_entry.get().strip()
        category = self.selected_category_var.get().strip()

        if not name:
            messagebox.showwarning(
                "Name Required",
                "Please enter your name before proceeding to the quiz."
            )
            self.name_entry.focus_set()
            return

        try:
            self.quiz_manager.start_quiz(name, category)
            self.show_quiz_screen()
        except Exception as err:
            messagebox.showerror("Error Starting Quiz", str(err))

    # =========================================================================
    # 2. QUIZ SCREEN
    # =========================================================================
    def show_quiz_screen(self):
        """Renders the question card, options, and navigation buttons."""
        self.clear_container()

        # Main wrapper
        quiz_frame = tk.Frame(self.container, bg="#F1F5F9")
        quiz_frame.pack(fill=tk.BOTH, expand=True, padx=35, pady=20)

        # Top Bar: Student Name, Category, Question Counter
        top_bar = tk.Frame(quiz_frame, bg="#F1F5F9")
        top_bar.pack(fill=tk.X, pady=(0, 12))

        # Left Badges: Student & Category
        left_info = tk.Frame(top_bar, bg="#F1F5F9")
        left_info.pack(side=tk.LEFT)

        student_pill = tk.Label(
            left_info,
            text=f"👤 {self.quiz_manager.student_name}",
            font=("Segoe UI", 10, "bold"),
            bg="#E2E8F0",
            fg="#1E293B",
            padx=12,
            pady=5
        )
        student_pill.pack(side=tk.LEFT, padx=(0, 8))

        cat_pill = tk.Label(
            left_info,
            text=f"📂 {self.quiz_manager.current_category}",
            font=("Segoe UI", 10, "bold"),
            bg="#EEF2FF",
            fg="#4F46E5",
            padx=12,
            pady=5
        )
        cat_pill.pack(side=tk.LEFT)

        # Right Badge: Question Counter
        curr_num = self.quiz_manager.current_index + 1
        total_q = self.quiz_manager.get_total_questions()
        self.counter_lbl = tk.Label(
            top_bar,
            text=f"Question {curr_num} of {total_q}",
            font=("Segoe UI", 11, "bold"),
            bg="#FEF3C7",
            fg="#B45309",
            padx=14,
            pady=5
        )
        self.counter_lbl.pack(side=tk.RIGHT)

        # Progress Bar
        self.progress_bar = ttk.Progressbar(
            quiz_frame,
            style="Horizontal.TProgressbar",
            maximum=total_q,
            value=curr_num
        )
        self.progress_bar.pack(fill=tk.X, pady=(0, 18))

        # Main Question Card (White Background)
        self.question_card = tk.Frame(quiz_frame, bg="#FFFFFF", relief=tk.FLAT, bd=0)
        self.question_card.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        card_content = tk.Frame(self.question_card, bg="#FFFFFF", padx=35, pady=25)
        card_content.pack(fill=tk.BOTH, expand=True)

        # Question Text Label
        current_q = self.quiz_manager.get_current_question()
        q_text = current_q.question_text if current_q else "No question loaded."

        self.question_lbl = tk.Label(
            card_content,
            text=f"Q{curr_num}. {q_text}",
            font=("Segoe UI", 15, "bold"),
            bg="#FFFFFF",
            fg="#0F172A",
            wraplength=760,
            justify=tk.LEFT,
            anchor="w"
        )
        self.question_lbl.pack(fill=tk.X, pady=(0, 20))

        # Options Container
        self.options_frame = tk.Frame(card_content, bg="#FFFFFF")
        self.options_frame.pack(fill=tk.BOTH, expand=True)

        # Retrieve saved user choice if already answered
        saved_choice = current_q.user_answer if (current_q and current_q.user_answer) else ""
        self.selected_option_var.set(saved_choice)
        self.option_cards_data = []

        # Render 4 Modern Interactive Option Cards
        letters = ["A", "B", "C", "D"]
        options = current_q.options if current_q else []

        for idx, opt_text in enumerate(options):
            badge_letter = letters[idx] if idx < len(letters) else str(idx + 1)

            # Interactive Option Card Frame
            card = tk.Frame(
                self.options_frame,
                bg="#FFFFFF",
                relief=tk.FLAT,
                bd=0,
                highlightthickness=2,
                cursor="hand2",
                padx=16,
                pady=12
            )
            card.pack(fill=tk.X, pady=5)

            # Left Badge (Letter Pill A, B, C, D)
            badge = tk.Label(
                card,
                text=badge_letter,
                font=("Segoe UI", 11, "bold"),
                bg="#F1F5F9",
                fg="#475569",
                width=3,
                height=1,
                cursor="hand2"
            )
            badge.pack(side=tk.LEFT, padx=(0, 14))

            # Option Text
            text_lbl = tk.Label(
                card,
                text=opt_text,
                font=("Segoe UI", 11),
                bg="#FFFFFF",
                fg="#1E293B",
                wraplength=640,
                justify=tk.LEFT,
                anchor="w",
                cursor="hand2"
            )
            text_lbl.pack(side=tk.LEFT, fill=tk.X, expand=True)

            # Right Check Indicator Pill
            check_lbl = tk.Label(
                card,
                text="○",
                font=("Segoe UI", 10, "bold"),
                bg="#FFFFFF",
                fg="#CBD5E1",
                cursor="hand2"
            )
            check_lbl.pack(side=tk.RIGHT, padx=(10, 0))

            card_entry = {
                "card": card,
                "badge": badge,
                "text_lbl": text_lbl,
                "check_lbl": check_lbl,
                "value": opt_text,
                "letter": badge_letter
            }
            self.option_cards_data.append(card_entry)

            # Bind mouse click and hover transitions to all child widgets
            for widget in [card, badge, text_lbl, check_lbl]:
                widget.bind("<Button-1>", lambda e, val=opt_text: self.select_option(val))
                widget.bind("<Enter>", lambda e, ce=card_entry: self.on_option_hover(ce, True))
                widget.bind("<Leave>", lambda e, ce=card_entry: self.on_option_hover(ce, False))

        # Initial visual refresh to display saved answer if already chosen
        self.refresh_option_cards()

        # Bottom Navigation & Action Bar
        bottom_bar = tk.Frame(quiz_frame, bg="#F1F5F9")
        bottom_bar.pack(fill=tk.X, pady=(5, 0))

        # Previous Button
        self.prev_btn = ttk.Button(
            bottom_bar,
            text="⬅ Previous",
            style="Secondary.TButton",
            command=self.handle_prev_question
        )
        self.prev_btn.pack(side=tk.LEFT, padx=(0, 10))
        if not self.quiz_manager.has_prev():
            self.prev_btn.state(["disabled"])

        # Clear Selection Button
        self.clear_btn = ttk.Button(
            bottom_bar,
            text="Clear Choice",
            style="Secondary.TButton",
            command=self.handle_clear_selection
        )
        self.clear_btn.pack(side=tk.LEFT)

        # Next / Finish Button on Right
        if self.quiz_manager.has_next():
            self.next_btn = ttk.Button(
                bottom_bar,
                text="Next Question ➔",
                style="Primary.TButton",
                command=self.handle_next_question
            )
            self.next_btn.pack(side=tk.RIGHT)
        else:
            self.next_btn = ttk.Button(
                bottom_bar,
                text="Submit Quiz  ✓",
                style="Success.TButton",
                command=self.handle_submit_quiz
            )
            self.next_btn.pack(side=tk.RIGHT)

    def refresh_category_cards(self):
        """Refreshes visual state of category cards on Home Screen."""
        curr_cat = self.selected_category_var.get()
        for ce in getattr(self, "category_cards_data", []):
            if ce["value"] == curr_cat:
                ce["card"].configure(
                    bg="#EEF2FF",
                    highlightbackground="#4F46E5",
                    highlightcolor="#4F46E5",
                    highlightthickness=2
                )
                ce["left_box"].configure(bg="#EEF2FF")
                ce["text_col"].configure(bg="#EEF2FF")
                ce["icon_lbl"].configure(bg="#EEF2FF")
                ce["title_lbl"].configure(bg="#EEF2FF", fg="#312E81")
                ce["sub_lbl"].configure(bg="#EEF2FF", fg="#4338CA")
                ce["badge_lbl"].configure(bg="#EEF2FF", fg="#4F46E5", text="✓ Selected")
            else:
                ce["card"].configure(
                    bg="#FFFFFF",
                    highlightbackground="#E2E8F0",
                    highlightcolor="#E2E8F0",
                    highlightthickness=1
                )
                ce["left_box"].configure(bg="#FFFFFF")
                ce["text_col"].configure(bg="#FFFFFF")
                ce["icon_lbl"].configure(bg="#FFFFFF")
                ce["title_lbl"].configure(bg="#FFFFFF", fg="#0F172A")
                ce["sub_lbl"].configure(bg="#FFFFFF", fg="#64748B")
                ce["badge_lbl"].configure(bg="#FFFFFF", fg="#CBD5E1", text="○")

    def on_cat_hover(self, card_entry, is_hovering):
        """Applies hover styling to unselected category cards."""
        if self.selected_category_var.get() != card_entry["value"]:
            bg_col = "#F8FAFC" if is_hovering else "#FFFFFF"
            border_col = "#818CF8" if is_hovering else "#E2E8F0"
            card_entry["card"].configure(
                bg=bg_col,
                highlightbackground=border_col,
                highlightcolor=border_col
            )
            card_entry["left_box"].configure(bg=bg_col)
            card_entry["text_col"].configure(bg=bg_col)
            card_entry["icon_lbl"].configure(bg=bg_col)
            card_entry["title_lbl"].configure(bg=bg_col)
            card_entry["sub_lbl"].configure(bg=bg_col)
            card_entry["badge_lbl"].configure(bg=bg_col)

    def select_option(self, option_text):
        """Records selected option and immediately applies active card styling."""
        self.selected_option_var.set(option_text)
        self.quiz_manager.set_current_answer(option_text)
        self.refresh_option_cards()

    def refresh_option_cards(self):
        """Updates colors and badges for option cards based on current selection."""
        current_sel = self.selected_option_var.get()
        for ce in getattr(self, "option_cards_data", []):
            val = ce["value"]
            if val == current_sel:
                # Active Selected State (Vibrant Indigo Glow)
                ce["card"].configure(
                    bg="#EEF2FF",
                    highlightbackground="#4F46E5",
                    highlightcolor="#4F46E5",
                    highlightthickness=2
                )
                ce["badge"].configure(bg="#4F46E5", fg="#FFFFFF")
                ce["text_lbl"].configure(
                    bg="#EEF2FF",
                    fg="#312E81",
                    font=("Segoe UI", 11, "bold")
                )
                ce["check_lbl"].configure(
                    bg="#EEF2FF",
                    fg="#4F46E5",
                    text="✓ Selected"
                )
            else:
                # Default Normal State
                ce["card"].configure(
                    bg="#FFFFFF",
                    highlightbackground="#E2E8F0",
                    highlightcolor="#E2E8F0",
                    highlightthickness=1
                )
                ce["badge"].configure(bg="#F1F5F9", fg="#475569")
                ce["text_lbl"].configure(
                    bg="#FFFFFF",
                    fg="#1E293B",
                    font=("Segoe UI", 11)
                )
                ce["check_lbl"].configure(
                    bg="#FFFFFF",
                    fg="#CBD5E1",
                    text="○"
                )

    def on_option_hover(self, card_entry, is_hovering):
        """Smoothly highlights unselected option cards when mouse moves over them."""
        if self.selected_option_var.get() != card_entry["value"]:
            if is_hovering:
                card_entry["card"].configure(
                    bg="#F8FAFC",
                    highlightbackground="#818CF8",
                    highlightcolor="#818CF8",
                    highlightthickness=1
                )
                card_entry["text_lbl"].configure(bg="#F8FAFC")
                card_entry["check_lbl"].configure(bg="#F8FAFC", fg="#818CF8")
            else:
                card_entry["card"].configure(
                    bg="#FFFFFF",
                    highlightbackground="#E2E8F0",
                    highlightcolor="#E2E8F0",
                    highlightthickness=1
                )
                card_entry["text_lbl"].configure(bg="#FFFFFF")
                card_entry["check_lbl"].configure(bg="#FFFFFF", fg="#CBD5E1")

    def handle_clear_selection(self):
        """Clears selection for current question and updates option cards."""
        self.selected_option_var.set("")
        self.quiz_manager.clear_current_answer()
        self.refresh_option_cards()

    def handle_next_question(self):
        """Saves current answer and navigates to the next question."""
        # Ensure answer is persisted
        if self.selected_option_var.get():
            self.quiz_manager.set_current_answer(self.selected_option_var.get())

        if self.quiz_manager.next_question():
            self.show_quiz_screen()

    def handle_prev_question(self):
        """Saves current answer and navigates to the previous question."""
        # Ensure answer is persisted
        if self.selected_option_var.get():
            self.quiz_manager.set_current_answer(self.selected_option_var.get())

        if self.quiz_manager.prev_question():
            self.show_quiz_screen()

    def handle_submit_quiz(self):
        """Prompts confirmation if questions remain unanswered, then computes results."""
        if self.selected_option_var.get():
            self.quiz_manager.set_current_answer(self.selected_option_var.get())

        unanswered = self.quiz_manager.get_unanswered_count()
        if unanswered > 0:
            confirm = messagebox.askyesno(
                "Unanswered Questions",
                f"You have {unanswered} unanswered question(s).\nAre you sure you want to submit the quiz now?"
            )
            if not confirm:
                return

        # Show final result screen
        self.show_result_screen()

    # =========================================================================
    # 3. RESULT SCREEN
    # =========================================================================
    def show_result_screen(self):
        """Renders comprehensive score card, percentage, stats, and review options."""
        self.clear_container()

        # Calculate final metrics from engine
        results = self.quiz_manager.calculate_results()

        res_frame = tk.Frame(self.container, bg="#F1F5F9")
        res_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=25)

        # Header Celebration Title
        header = tk.Frame(res_frame, bg="#F1F5F9")
        header.pack(fill=tk.X, pady=(0, 15))

        badge = tk.Label(
            header,
            text="QUIZ COMPLETED",
            font=("Segoe UI", 9, "bold"),
            bg="#D1FAE5",
            fg="#065F46",
            padx=12,
            pady=4
        )
        badge.pack(anchor="center")

        title = tk.Label(
            header,
            text=f"Performance Report for {results['student_name']}",
            font=("Segoe UI", 20, "bold"),
            bg="#F1F5F9",
            fg="#0F172A",
            pady=4
        )
        title.pack(anchor="center")

        cat_sub = tk.Label(
            header,
            text=f"Category: {results['category']}",
            font=("Segoe UI", 11),
            bg="#F1F5F9",
            fg="#64748B"
        )
        cat_sub.pack(anchor="center")

        # White Card For Stats
        card = tk.Frame(res_frame, bg="#FFFFFF", relief=tk.FLAT, bd=0)
        card.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        card_content = tk.Frame(card, bg="#FFFFFF", padx=30, pady=20)
        card_content.pack(fill=tk.BOTH, expand=True)

        # Big Score Banner
        score_banner = tk.Frame(card_content, bg="#EEF2FF", padx=20, pady=15)
        score_banner.pack(fill=tk.X, pady=(0, 20))

        score_text = tk.Label(
            score_banner,
            text=f"Score: {results['score']} / {results['total_questions']}   ({results['percentage']}%)",
            font=("Segoe UI", 22, "bold"),
            bg="#EEF2FF",
            fg="#4F46E5"
        )
        score_text.pack(anchor="center")

        remark_lbl = tk.Label(
            score_banner,
            text=f"Grade: {results['grade']} • {results['remarks']}",
            font=("Segoe UI", 11, "bold"),
            bg="#EEF2FF",
            fg=results["badge_color"],
            pady=4
        )
        remark_lbl.pack(anchor="center")

        # 3 Key Statistics Boxes (Correct, Incorrect, Skipped)
        stats_box = tk.Frame(card_content, bg="#FFFFFF")
        stats_box.pack(fill=tk.X, pady=(0, 20))
        stats_box.columnconfigure((0, 1, 2), weight=1, uniform="stat")

        # 1. Correct Box
        box_correct = tk.Frame(stats_box, bg="#ECFDF5", relief=tk.SOLID, bd=1, padx=15, pady=12)
        box_correct.grid(row=0, column=0, padx=6, sticky="nsew")
        tk.Label(box_correct, text="CORRECT", font=("Segoe UI", 9, "bold"), bg="#ECFDF5", fg="#047857").pack()
        tk.Label(box_correct, text=str(results["correct"]), font=("Segoe UI", 20, "bold"), bg="#ECFDF5", fg="#065F46").pack()

        # 2. Incorrect Box
        box_wrong = tk.Frame(stats_box, bg="#FEF2F2", relief=tk.SOLID, bd=1, padx=15, pady=12)
        box_wrong.grid(row=0, column=1, padx=6, sticky="nsew")
        tk.Label(box_wrong, text="INCORRECT", font=("Segoe UI", 9, "bold"), bg="#FEF2F2", fg="#B91C1C").pack()
        tk.Label(box_wrong, text=str(results["incorrect"]), font=("Segoe UI", 20, "bold"), bg="#FEF2F2", fg="#991B1B").pack()

        # 3. Skipped Box
        box_skipped = tk.Frame(stats_box, bg="#F8FAFC", relief=tk.SOLID, bd=1, padx=15, pady=12)
        box_skipped.grid(row=0, column=2, padx=6, sticky="nsew")
        tk.Label(box_skipped, text="SKIPPED", font=("Segoe UI", 9, "bold"), bg="#F8FAFC", fg="#64748B").pack()
        tk.Label(box_skipped, text=str(results["skipped"]), font=("Segoe UI", 20, "bold"), bg="#F8FAFC", fg="#334155").pack()

        # Action Buttons
        btn_box = tk.Frame(card_content, bg="#FFFFFF")
        btn_box.pack(fill=tk.X, pady=(10, 0))

        review_btn = ttk.Button(
            btn_box,
            text="🔍 Review Answers & Explanations",
            style="Primary.TButton",
            command=lambda: self.open_review_modal(results["review"])
        )
        review_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

        restart_btn = ttk.Button(
            btn_box,
            text="🔄 Restart Quiz",
            style="Secondary.TButton",
            command=self.show_home_screen
        )
        restart_btn.pack(side=tk.LEFT, padx=5)

        exit_btn = ttk.Button(
            btn_box,
            text="Exit",
            style="Danger.TButton",
            command=self.confirm_exit
        )
        exit_btn.pack(side=tk.RIGHT, padx=(5, 0))

    # =========================================================================
    # 4. ANSWER REVIEW MODAL
    # =========================================================================
    def open_review_modal(self, review_items):
        """
        Opens a scrollable dialog displaying questions, chosen answers,
        correct answers, and explanations. Great for demonstration to teachers!
        """
        review_win = tk.Toplevel(self)
        review_win.title("Quiz Answer Review & Explanations")
        review_win.geometry("780x600")
        review_win.minsize(680, 500)
        review_win.configure(bg="#F8FAFC")

        # Make modal dialog
        review_win.transient(self)
        review_win.grab_set()

        # Header in Modal
        hdr = tk.Frame(review_win, bg="#1E293B", padx=20, pady=15)
        hdr.pack(fill=tk.X)
        tk.Label(
            hdr,
            text="Detailed Question Review",
            font=("Segoe UI", 14, "bold"),
            bg="#1E293B",
            fg="#FFFFFF"
        ).pack(anchor="w")

        # Scrollable Frame Container
        canvas = tk.Canvas(review_win, bg="#F8FAFC", highlightthickness=0)
        scrollbar = ttk.Scrollbar(review_win, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#F8FAFC", padx=20, pady=15)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(xscrollcommand=None, yscrollcommand=scrollbar.set)

        # Mousewheel scroll support
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        # Populate Review Cards
        for item in review_items:
            # Card color indicator based on status
            if item["status"] == "Correct":
                card_bg = "#FFFFFF"
                status_color = "#047857"
                status_bg = "#ECFDF5"
                status_text = "✓ Correct"
            elif item["status"] == "Incorrect":
                card_bg = "#FFFFFF"
                status_color = "#B91C1C"
                status_bg = "#FEF2F2"
                status_text = "✗ Incorrect"
            else:
                card_bg = "#FFFFFF"
                status_color = "#475569"
                status_bg = "#F1F5F9"
                status_text = "○ Skipped"

            card = tk.Frame(scrollable_frame, bg=card_bg, relief=tk.SOLID, bd=1, padx=15, pady=12)
            card.pack(fill=tk.X, pady=8)

            # Top of card: Question number + Status Badge
            card_top = tk.Frame(card, bg=card_bg)
            card_top.pack(fill=tk.X, pady=(0, 6))

            q_title = tk.Label(
                card_top,
                text=f"Q{item['number']}. {item['question']}",
                font=("Segoe UI", 11, "bold"),
                bg=card_bg,
                fg="#0F172A",
                wraplength=540,
                justify=tk.LEFT
            )
            q_title.pack(side=tk.LEFT, anchor="w")

            status_badge = tk.Label(
                card_top,
                text=status_text,
                font=("Segoe UI", 9, "bold"),
                bg=status_bg,
                fg=status_color,
                padx=8,
                pady=3
            )
            status_badge.pack(side=tk.RIGHT, anchor="ne")

            # Answer details
            ans_info = tk.Frame(card, bg=card_bg)
            ans_info.pack(fill=tk.X, pady=(4, 0))

            user_ans_lbl = tk.Label(
                ans_info,
                text=f"Your Answer: {item['user_answer']}",
                font=("Segoe UI", 10),
                bg=card_bg,
                fg="#334155" if item["status"] == "Correct" else "#DC2626"
            )
            user_ans_lbl.pack(anchor="w")

            corr_ans_lbl = tk.Label(
                ans_info,
                text=f"Correct Answer: {item['correct_answer']}",
                font=("Segoe UI", 10, "bold"),
                bg=card_bg,
                fg="#059669"
            )
            corr_ans_lbl.pack(anchor="w")

            if item["explanation"]:
                exp_lbl = tk.Label(
                    ans_info,
                    text=f"Explanation: {item['explanation']}",
                    font=("Segoe UI", 9, "italic"),
                    bg=card_bg,
                    fg="#64748B",
                    wraplength=660,
                    justify=tk.LEFT
                )
                exp_lbl.pack(anchor="w", pady=(4, 0))

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Close button at bottom
        close_btn = ttk.Button(
            review_win,
            text="Close Review",
            style="Secondary.TButton",
            command=review_win.destroy
        )
        close_btn.pack(side=tk.BOTTOM, pady=10)

    def confirm_exit(self):
        """Asks user confirmation before closing the application."""
        if messagebox.askyesno("Exit Application", "Are you sure you want to exit the quiz?"):
            self.destroy()


# =============================================================================
# APPLICATION ENTRY POINT
# =============================================================================
if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
