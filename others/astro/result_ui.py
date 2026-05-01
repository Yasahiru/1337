import tkinter as tk
import random

COLORS = {
    "bg":        "#0a0e1a",
    "panel":     "#0f1629",
    "border":    "#1e2d4a",
    "accent":    "#00d4ff",
    "accent2":   "#7c3aed",
    "text":      "#e2e8f0",
    "muted":     "#64748b",
    "high":      "#ff3b5c",
    "high_dim":  "#3d0a14",
    "med":       "#f59e0b",
    "med_dim":   "#3d2a00",
    "low":       "#10b981",
    "low_dim":   "#012a1a",
}

FONT_MONO   = ("Courier New", 10)
FONT_TITLE  = ("Courier New", 22, "bold")
FONT_LABEL  = ("Courier New", 9)
FONT_VALUE  = ("Courier New", 13, "bold")
FONT_RISK   = ("Courier New", 16, "bold")
FONT_SCORE  = ("Courier New", 36, "bold")


class Particle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color  = color
        self.x  = random.randint(0, 800)
        self.y  = random.randint(0, 600)
        self.vx = random.uniform(-0.4, 0.4)
        self.vy = random.uniform(-0.4, 0.4)
        self.r  = random.uniform(1, 3)
        self.alpha = random.uniform(0.2, 0.8)
        self.id = canvas.create_oval(
            self.x - self.r, self.y - self.r,
            self.x + self.r, self.y + self.r,
            fill=self._dim(color, self.alpha), outline=""
        )

    def _dim(self, hex_color, alpha):
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
        bg_r, bg_g, bg_b = 10, 14, 26
        r2 = int(bg_r + (r - bg_r) * alpha)
        g2 = int(bg_g + (g - bg_g) * alpha)
        b2 = int(bg_b + (b - bg_b) * alpha)
        return f"#{r2:02x}{g2:02x}{b2:02x}"

    def move(self, w, h):
        self.x = (self.x + self.vx) % w
        self.y = (self.y + self.vy) % h
        self.canvas.coords(
            self.id,
            self.x - self.r, self.y - self.r,
            self.x + self.r, self.y + self.r,
        )


class ArcProgress:
    def __init__(self, parent, size=160, color=COLORS["accent"]):
        self.size   = size
        self.color  = color
        self.target = 0
        self.current = 0
        self.canvas  = tk.Canvas(parent, width=size, height=size,
                                 bg=COLORS["bg"], highlightthickness=0)
        self.canvas.pack()
        self._draw(0)

    def _draw(self, pct):
        s = self.size
        pad = 14
        self.canvas.delete("all")
        # track
        self.canvas.create_arc(pad, pad, s-pad, s-pad,
                               start=90, extent=360,
                               style="arc", outline=COLORS["border"], width=6)
        # fill
        extent = pct / 100 * 360
        self.canvas.create_arc(pad, pad, s-pad, s-pad,
                               start=90, extent=-extent,
                               style="arc", outline=self.color, width=6)
        # glow (two wider arcs at low alpha)
        for w, op in [(10, 0.3), (16, 0.15)]:
            gc = self._glow_color(op)
            self.canvas.create_arc(pad, pad, s-pad, s-pad,
                                   start=90, extent=-extent,
                                   style="arc", outline=gc, width=w)
        # label
        self.canvas.create_text(s//2, s//2 - 10,
                                text=f"{int(pct)}",
                                fill=self.color, font=FONT_SCORE)
        self.canvas.create_text(s//2, s//2 + 22,
                                text="SCORE", fill=COLORS["muted"],
                                font=FONT_LABEL)

    def _glow_color(self, alpha):
        r = int(self.color[1:3], 16)
        g = int(self.color[3:5], 16)
        b = int(self.color[5:7], 16)
        br, bg_, bb = 10, 14, 26
        return "#{:02x}{:02x}{:02x}".format(
            int(br + (r-br)*alpha),
            int(bg_ + (g-bg_)*alpha),
            int(bb + (b-bb)*alpha),
        )

    def animate_to(self, target, root, step=0):
        self.target  = target
        self.current = 0
        self._step(target, root)

    def _step(self, target, root):
        diff = target - self.current
        if abs(diff) < 0.5:
            self.current = target
            self._draw(self.current)
            return
        self.current += diff * 0.07 + 0.3
        self._draw(self.current)
        root.after(16, self._step, target, root)


class StatBar:
    def __init__(self, parent, label, color):
        self.color  = color
        self.target = 0
        self.current = 0

        row = tk.Frame(parent, bg=COLORS["bg"])
        row.pack(fill="x", pady=3)

        tk.Label(row, text=label, fg=COLORS["muted"], bg=COLORS["bg"],
                 font=FONT_LABEL, width=10, anchor="w").pack(side="left")

        self.val_lbl = tk.Label(row, text="", fg=color, bg=COLORS["bg"],
                                font=FONT_LABEL, width=7, anchor="e")
        self.val_lbl.pack(side="right")

        track = tk.Frame(parent, bg=COLORS["border"], height=4)
        track.pack(fill="x", padx=4, pady=1)
        track.pack_propagate(False)

        self.bar = tk.Frame(track, bg=color, height=4, width=0)
        self.bar.place(x=0, y=0)
        self._track = track

    def animate_to(self, pct, label_text, root):
        self.target = pct
        self.current = 0
        self._lbl = label_text
        self._step(root)

    def _step(self, root):
        diff = self.target - self.current
        if abs(diff) < 0.5:
            self.current = self.target
            self._update()
            return
        self.current += diff * 0.07 + 0.5
        self._update()
        root.after(16, self._step, root)

    def _update(self):
        w = int(self._track.winfo_width() * self.current / 100)
        self.bar.place(x=0, y=0, width=max(0, w), height=4)
        self.val_lbl.config(text=self._lbl)


class ScanLine:
    def __init__(self, canvas, w, h):
        self.canvas = canvas
        self.h = h
        self.w = w
        self.y = 0
        self.id = canvas.create_line(0, 0, w, 0,
                                     fill="#00d4ff", width=1, stipple="gray25")
        self._move()

    def _move(self):
        self.y = (self.y + 2) % self.h
        self.canvas.coords(self.id, 0, self.y, self.w, self.y)
        self.canvas.after(30, self._move)


class ResultUI:
    def __init__(self, root):
        self.root = root
        root.title("SYSTEM ANALYSIS")
        root.configure(bg=COLORS["bg"])
        root.resizable(False, False)

        W, H = 2000, 1000
        root.geometry(f"{W}x{H}")
        self._center(root, W, H)

        #background canvas with particles
        self.bg_canvas = tk.Canvas(root, width=W, height=H,
                                   bg=COLORS["bg"], highlightthickness=0)
        self.bg_canvas.place(x=0, y=0)

        self.particles = [Particle(self.bg_canvas, COLORS["accent"])
                          for _ in range(40)]
        self.particles += [Particle(self.bg_canvas, COLORS["accent2"])
                           for _ in range(20)]

        ScanLine(self.bg_canvas, W, H)
        self._animate_particles(W, H)

        #main panel(sits above canvas)
        self.panel = tk.Frame(root, bg=COLORS["panel"],
                              highlightbackground=COLORS["border"],
                              highlightthickness=1)
        self.panel.place(x=40, y=40, width=W-80, height=H-80)

        self._build_ui()

    def _build_ui(self):
        p = self.panel

        # Header bar
        header = tk.Frame(p, bg=COLORS["border"], height=1)
        header.pack(fill="x")

        title_row = tk.Frame(p, bg=COLORS["panel"])
        title_row.pack(fill="x", padx=20, pady=(14, 8))

        self.corner_dot = tk.Label(title_row, text="◆",
                                   fg=COLORS["accent"], bg=COLORS["panel"],
                                   font=("Courier New", 14))
        self.corner_dot.pack(side="left")

        self.title_lbl = tk.Label(title_row, text="ASTRO SMART SYSTEM",
                                  fg=COLORS["accent"], bg=COLORS["panel"],
                                  font=FONT_TITLE)
        self.title_lbl.pack(side="left", padx=10)

        self.status_dot = tk.Label(title_row, text="●  IDLE",
                                   fg=COLORS["muted"], bg=COLORS["panel"],
                                   font=FONT_LABEL)
        self.status_dot.pack(side="right")

        # Divider
        tk.Frame(p, bg=COLORS["border"], height=1).pack(fill="x")

        # Body: left info + right score
        body = tk.Frame(p, bg=COLORS["panel"])
        body.pack(fill="both", expand=True, padx=20, pady=16)

        left  = tk.Frame(body, bg=COLORS["panel"])
        left.pack(side="left", fill="both", expand=True)

        right = tk.Frame(body, bg=COLORS["panel"])
        right.pack(side="right", fill="y", padx=(20, 0))

        #info fields (left)
        self._fields = {}
        fields_data = [
            ("NAME",  "name"),
            ("TYPE",  "type"),
            ("TIME",  "time"),
            ("RISK",  "risk"),
        ]
        for label, key in fields_data:
            row = tk.Frame(left, bg=COLORS["panel"])
            row.pack(fill="x", pady=5)

            tk.Label(row, text=f"[{label}]", fg=COLORS["muted"],
                     bg=COLORS["panel"], font=FONT_LABEL,
                     width=8, anchor="w").pack(side="left")

            lbl = tk.Label(row, text="—", fg=COLORS["text"],
                           bg=COLORS["panel"], font=FONT_VALUE, anchor="w")
            lbl.pack(side="left", padx=8)
            self._fields[key] = lbl

        #Stat bars
        tk.Frame(left, bg=COLORS["border"], height=1).pack(fill="x", pady=10)
        tk.Label(left, text="METRICS", fg=COLORS["muted"],
                 bg=COLORS["panel"], font=FONT_LABEL).pack(anchor="w", pady=(0, 4))

        bar_frame = tk.Frame(left, bg=COLORS["bg"], padx=10, pady=8)
        bar_frame.pack(fill="x")
        self.bar_time  = StatBar(bar_frame, "TIME UTIL", COLORS["accent"])
        self.bar_score = StatBar(bar_frame, "SCORE", COLORS["accent2"])
        self.bar_risk  = StatBar(bar_frame, "RISK LVL", COLORS["high"])

        #Arc score (right)
        self.arc = ArcProgress(right, size=170, color=COLORS["accent"])

        #Risk badge
        self.risk_badge = tk.Label(right, text="", fg=COLORS["text"],
                                   bg=COLORS["panel"], font=FONT_RISK,
                                   pady=6, padx=14)
        self.risk_badge.pack(pady=(12, 0))

        #Terminal log
        tk.Frame(p, bg=COLORS["border"], height=1).pack(fill="x")
        log_frame = tk.Frame(p, bg=COLORS["bg"])
        log_frame.pack(fill="x", padx=20, pady=10)

        self.log_lbl = tk.Label(log_frame, text="", fg=COLORS["muted"],
                                bg=COLORS["bg"], font=FONT_MONO,
                                anchor="w", justify="left")
        self.log_lbl.pack(anchor="w")

        #Bottom button
        self.btn = tk.Button(p, text="[ RUN ANALYSIS ]",
                             fg=COLORS["accent"], bg=COLORS["panel"],
                             activeforeground=COLORS["bg"],
                             activebackground=COLORS["accent"],
                             font=("Courier New", 10, "bold"),
                             relief="flat", cursor="hand2",
                             command=self._demo,
                             highlightbackground=COLORS["border"],
                             highlightthickness=1, pady=8)
        self.btn.pack(pady=(0, 16), ipadx=20)

    #Animation helpers
    def _animate_particles(self, w, h):
        for p in self.particles:
            p.move(w, h)
        self.root.after(33, self._animate_particles, w, h)

    def _blink_dot(self, on=True):
        color = COLORS["low"] if on else COLORS["panel"]
        self.status_dot.config(fg=color if on else COLORS["muted"],
                               text="●  ACTIVE" if on else "●  IDLE")
        if on:
            self.root.after(600, self._blink_dot, False)

    def _typing(self, text, i=0, callback=None):
        if i == 0:
            self.log_lbl.config(text="")
        if i < len(text):
            self.log_lbl.config(text=text[:i+1])
            self.root.after(18, self._typing, text, i+1, callback)
        elif callback:
            self.root.after(300, callback)

    def _flash_panel(self, color, times=3):
        if times == 0:
            self.panel.config(highlightbackground=COLORS["border"])
            return
        c = color if times % 2 == 0 else COLORS["border"]
        self.panel.config(highlightbackground=c)
        self.root.after(120, self._flash_panel, color, times-1)

    def _fade_field(self, key, value, color, step=0):
        alphas = [0.2, 0.5, 0.8, 1.0]
        if step < len(alphas):
            a = alphas[step]
            c = self._blend(color, COLORS["bg"], a)
            self._fields[key].config(text=value, fg=c)
            self.root.after(60, self._fade_field, key, value, color, step+1)
        else:
            self._fields[key].config(text=value, fg=color)

    def _blend(self, hex1, hex2, t):
        r1,g1,b1 = int(hex1[1:3],16), int(hex1[3:5],16), int(hex1[5:7],16)
        r2,g2,b2 = int(hex2[1:3],16), int(hex2[3:5],16), int(hex2[5:7],16)
        return "#{:02x}{:02x}{:02x}".format(
            int(r2+(r1-r2)*t), int(g2+(g1-g2)*t), int(b2+(b1-b2)*t))

    def _pulse_title(self, original, count=0):
        if count > 6:
            self.title_lbl.config(fg=COLORS["accent"])
            return
        c = COLORS["accent"] if count % 2 == 0 else "#ffffff"
        self.title_lbl.config(fg=c)
        self.root.after(100, self._pulse_title, original, count+1)

    #Show Result 
    def show_result(self, result):
        score    = result.get("total_score", 0)
        risk     = result.get("risk", "Low")
        name     = result.get("name", "Unknown")
        typ      = result.get("type", "—")
        t_h      = result.get("time_hours", 0)
        t_d      = result.get("time_days", 0)

        if "High" in risk:
            risk_col, dim_col, badge_bg = COLORS["high"], COLORS["high_dim"], "#3d0a14"
        elif "Medium" in risk:
            risk_col, dim_col, badge_bg = COLORS["med"], COLORS["med_dim"], "#3d2a00"
        else:
            risk_col, dim_col, badge_bg = COLORS["low"], COLORS["low_dim"], "#012a1a"

        # Update arc color
        self.arc.color = risk_col
        self.arc.canvas.config(bg=COLORS["bg"])

        self._blink_dot()
        self._pulse_title("RESULT ANALYSIS")
        self._flash_panel(risk_col)

        def step1():
            self._typing(
                f"> loading {name} | type:{typ} | score:{score} | risk:{risk}",
                callback=step2
            )

        def step2():
            self._fade_field("name",  name,                        COLORS["text"])
            self._fade_field("type",  typ,                         COLORS["accent"])
            self._fade_field("time",  f"{t_h}h  /  {t_d}d",       COLORS["text"])
            self._fade_field("risk",  risk,                         risk_col)

            self.risk_badge.config(
                text=f"▲ {risk.upper()} RISK",
                fg=risk_col, bg=badge_bg
            )

            score_pct = min(score, 100)
            self.arc.color = risk_col
            self.root.after(200, lambda: self.arc.animate_to(score_pct, self.root))

            time_pct  = min(int(t_h / 24 * 100), 100)
            self.bar_time.animate_to(time_pct, f"{t_h}h", self.root)
            self.root.after(150, lambda: self.bar_score.animate_to(
                score_pct, str(score), self.root))
            self.root.after(300, lambda: self.bar_risk.animate_to(
                {"High": 90, "Medium": 50, "Low": 20}.get(risk.split()[0], 50),
                risk, self.root))

        self.root.after(100, step1)

    def _demo(self):
        import random
        risks = ["High Risk", "Medium Risk", "Low Risk"]
        types = ["AGENT", "TASK", "SERVICE", "MODULE"]
        r = {
            "name":        f"UNIT-{random.randint(100,999)}",
            "type":        random.choice(types),
            "time_hours":  random.randint(1, 48),
            "time_days":   random.randint(1, 14),
            "total_score": random.randint(10, 100),
            "risk":        random.choice(risks),
        }
        self.show_result(r)

    #Util 
    def _center(self, win, w, h):
        win.update_idletasks()
        sw = win.winfo_screenwidth()
        sh = win.winfo_screenheight()
        win.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")


# Exl
if __name__ == "__main__":
    root = tk.Tk()
    app  = ResultUI(root)

    sample = {
        "name":        "NEXUS-ALPHA",
        "type":        "AGENT",
        "time_hours":  18,
        "time_days":   3,
        "total_score": 73,
        "risk":        "Medium Risk",
    }
    root.after(500, lambda: app.show_result(sample))
    root.mainloop()