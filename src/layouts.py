# layouts.py
from dash import html, dcc
import plotly.express as px
from data import df, year_min, year_max, industry_options


def layout_main_page():
    return html.Div(
        style={
            "backgroundColor": "#0f172a",
            "color": "#e5e7eb",
            "fontFamily": "Arial, sans-serif",
            "padding": "40px",
            "minHeight": "100vh",
            "textAlign": "center",
            "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
        },
        children=[
            # -------------------- TITLE --------------------
            html.H1("Startup Funding Analytics Portal"),

            # -------------------- GROUP INFO --------------------
            html.P(
                "Group 18: Naga Sampath Maddineni, Abhiram Reddy Pudi, Bandaru Sai Sri Surya",
                style={"color": "#93c5fd", "marginTop": "8px", "fontSize": "1rem"},
            ),

            # -------------------- PROJECT SUMMARY BOX --------------------
            html.Div(
                "This project analyzes global startup funding trends using multi-dimensional dashboards and "
                " analytical graphs. The visualizations summarize investment patterns, geographical hotspots, "
                "funding stages, and industry-level insights using data sourced from Kaggle and Crunchbase.",
                style={
                    "backgroundColor": "#1e293b",
                    "padding": "20px",
                    "borderRadius": "10px",
                    "width": "70%",
                    "margin": "20px auto 40px",
                    "color": "#e2e8f0",
                    "fontSize": "0.95rem",
                    "lineHeight": "1.4",
                    "border": "1px solid #334155",
                },
            ),

            # ==============================================================
            # ---------------------- OBJECTIVES SECTION ---------------------
            # ==============================================================

            html.H2("Analysis Objectives", style={"marginTop": "20px"}),

            html.Div(
                style={
                    "display": "flex",
                    "justifyContent": "center",
                    "gap": "20px",
                    "flexWrap": "wrap",
                    "marginTop": "20px",
                },
                children=[
                    # -------- Objective 1 --------
                    html.Div(
                        style={
                            "backgroundColor": "#020617",
                            "padding": "16px",
                            "borderRadius": "10px",
                            "border": "1px solid #1f2937",
                            "width": "260px",
                        },
                        children=[
                            html.H3("Objective 1", style={"fontSize": "1.1rem"}),
                            html.P(
                                "Analyze funding distribution by stage, industry, and yearly trends through graphs in objectives insight pages.",
                                style={"fontSize": "0.85rem", "color": "#9ca3af"},
                            ),
                            dcc.Link(
                                "Open Objective 1",
                                href="/sheet1",
                                style={
                                    "display": "inline-block",
                                    "marginTop": "10px",
                                    "padding": "8px 16px",
                                    "backgroundColor": "#38bdf8",
                                    "borderRadius": "6px",
                                    "color": "white",
                                    "textDecoration": "none",
                                    "fontSize": "0.9rem",
                                },
                            ),
                        ],
                    ),

                    # -------- Objective 2 --------
                    html.Div(
                        style={
                            "backgroundColor": "#020617",
                            "padding": "16px",
                            "borderRadius": "10px",
                            "border": "1px solid #1f2937",
                            "width": "260px",
                        },
                        children=[
                            html.H3("Objective 2", style={"fontSize": "1.1rem"}),
                            html.P(
                                "Explore startup funding stages, capital concentration, and time-based shifts across industries.",
                                style={"fontSize": "0.85rem", "color": "#9ca3af"},
                            ),
                            dcc.Link(
                                "Open Objective 2",
                                href="/sheet2",
                                style={
                                    "display": "inline-block",
                                    "marginTop": "10px",
                                    "padding": "8px 16px",
                                    "backgroundColor": "#a855f7",
                                    "borderRadius": "6px",
                                    "color": "white",
                                    "textDecoration": "none",
                                    "fontSize": "0.9rem",
                                },
                            ),
                        ],
                    ),

                    # -------- Objective 3 --------
                    html.Div(
                        style={
                            "backgroundColor": "#020617",
                            "padding": "16px",
                            "borderRadius": "10px",
                            "border": "1px solid #1f2937",
                            "width": "260px",
                        },
                        children=[
                            html.H3("Objective 3", style={"fontSize": "1.1rem"}),
                            html.P(
                                "Identify global and U.S. startup hotspots, funding intensity regions, and industry-wise geographic patterns.",
                                style={"fontSize": "0.85rem", "color": "#9ca3af"},
                            ),
                            dcc.Link(
                                "Open Objective 3",
                                href="/sheet3",
                                style={
                                    "display": "inline-block",
                                    "marginTop": "10px",
                                    "padding": "8px 16px",
                                    "backgroundColor": "#f97316",
                                    "borderRadius": "6px",
                                    "color": "white",
                                    "textDecoration": "none",
                                    "fontSize": "0.9rem",
                                },
                            ),
                        ],
                    ),
                ],
            ),

            # ==============================================================
            # ------------------------- DASHBOARDS --------------------------
            # ==============================================================

            html.H2("Dashboards", style={"marginTop": "50px"}),

            html.Div(
                style={
                    "display": "flex",
                    "justifyContent": "center",
                    "gap": "30px",
                    "flexWrap": "wrap",
                    "marginTop": "20px",
                },
                children=[
                    # Dashboard 1
                    html.Div(
                        style={
                            "backgroundColor": "#020617",
                            "padding": "20px",
                            "borderRadius": "10px",
                            "border": "1px solid #1f2937",
                            "width": "260px",
                        },
                        children=[
                            html.H3("Dashboard 1", style={"fontSize": "1.1rem"}),
                            html.P(
                                "View country-level, city-level, and funding-stage overviews from a global perspective.",
                                style={"fontSize": "0.85rem", "color": "#9ca3af"},
                            ),
                            dcc.Link(
                                "Go to Dashboard 1",
                                href="/dash1",
                                style={
                                    "display": "inline-block",
                                    "marginTop": "10px",
                                    "padding": "8px 16px",
                                    "backgroundColor": "#2563eb",
                                    "borderRadius": "6px",
                                    "color": "white",
                                    "textDecoration": "none",
                                },
                            ),
                        ],
                    ),

                    # Dashboard 2
                    html.Div(
                        style={
                            "backgroundColor": "#020617",
                            "padding": "20px",
                            "borderRadius": "10px",
                            "border": "1px solid #1f2937",
                            "width": "260px",
                        },
                        children=[
                            html.H3("Dashboard 2", style={"fontSize": "1.1rem"}),
                            html.P(
                                "Analyze funding timeline, startup formation waves, and top-funded industries.",
                                style={"fontSize": "0.85rem", "color": "#9ca3af"},
                            ),
                            dcc.Link(
                                "Go to Dashboard 2",
                                href="/dash2",
                                style={
                                    "display": "inline-block",
                                    "marginTop": "10px",
                                    "padding": "8px 16px",
                                    "backgroundColor": "#22c55e",
                                    "borderRadius": "6px",
                                    "color": "white",
                                    "textDecoration": "none",
                                },
                            ),
                        ],
                    ),
                ],
            ),

            # ==============================================================
            # ------------------------- FOOTER -----------------------------
            # ==============================================================

            html.Hr(style={"borderColor": "#334155", "marginTop": "50px", "width": "80%"}),

            html.P(
                "© 2024 Group 18 — Data referenced from Kaggle and Crunchbase datasets.",
                style={"color": "#64748b", "marginTop": "10px", "fontSize": "0.85rem"},
            ),
        ],
    )

# ---------- DASHBOARD 1 LAYOUT ----------

def layout_dashboard1():
    return html.Div(
        style={
            "backgroundColor": "#0f172a",
            "color": "#e5e7eb",
            "fontFamily": "Arial, sans-serif",
            "padding": "10px",
            "minHeight": "100vh",
        },
        children=[
            html.Div(
                style={
                    "display": "flex",
                    "justifyContent": "space-between",
                    "alignItems": "center",
                    "marginBottom": "10px",
                },
                children=[
                    html.H2("Dashboard 1: Global Startup Funding Overview"),
                    dcc.Link(
                        "← Back to Main Page",
                        href="/",
                        style={
                            "color": "#93c5fd",
                            "textDecoration": "none",
                            "fontSize": "0.9rem",
                        },
                    ),
                ],
            ),
            html.P(
                "View top countries, cities, and funding stages filtered by founding year and industry.",
                style={"color": "#9ca3af", "marginBottom": "15px"},
            ),
            # Filters
            html.Div(
                style={
                    "display": "flex",
                    "justifyContent": "center",
                    "gap": "30px",
                    "marginBottom": "20px",
                    "flexWrap": "wrap",
                },
                children=[
                    html.Div(
                        children=[
                            html.Label("Filter by founding year"),
                            dcc.RangeSlider(
                                id="year-range-1",
                                min=year_min,
                                max=year_max,
                                value=[year_min, year_max],
                                marks={
                                    int(y): str(int(y))
                                    for y in range(year_min, year_max + 1, 10)
                                },
                                tooltip={
                                    "placement": "bottom",
                                    "always_visible": False,
                                },
                            ),
                        ],
                        style={"width": "50%", "minWidth": "260px"},
                    ),
                    html.Div(
                        children=[
                            html.Label("Filter by major industry"),
                            dcc.Dropdown(
                                id="industry-dropdown-1",
                                options=industry_options,
                                value="ALL",
                                clearable=False,
                                style={"color": "#000"},
                            ),
                        ],
                        style={"width": "30%", "minWidth": "220px"},
                    ),
                ],
            ),
            # Main grid
            html.Div(
                style={
                    "display": "grid",
                    "gridTemplateColumns": "2fr 1.2fr",
                    "gridGap": "15px",
                    "height": "70vh",
                },
                children=[
                    html.Div(
                        children=[
                            html.H3(
                                "Top countries by total funding",
                                style={"marginBottom": "5px"},
                            ),
                            dcc.Graph(id="country-bar", style={"height": "70vh"}),
                        ]
                    ),
                    html.Div(
                        children=[
                            html.Div(
                                children=[
                                    html.H3(
                                        "Top 10 cities by total funding",
                                        style={"marginBottom": "5px"},
                                    ),
                                    dcc.Graph(
                                        id="top-cities-bar",
                                        style={"height": "38vh"},
                                    ),
                                ]
                            ),
                            html.Div(
                                children=[
                                    html.H3(
                                        "Funding by stage (global)",
                                        style={"marginBottom": "5px"},
                                    ),
                                    dcc.Graph(
                                        id="stage-bar",
                                        style={"height": "28vh"},
                                    ),
                                ]
                            ),
                        ]
                    ),
                ],
            ),
        ],
    )


# ---------- DASHBOARD 2 LAYOUT ----------

def layout_dashboard2():
    return html.Div(
        style={
            "backgroundColor": "#0f172a",
            "color": "#e5e7eb",
            "fontFamily": "Arial, sans-serif",
            "padding": "10px",
            "minHeight": "100vh",
        },
        children=[
            html.Div(
                style={
                    "display": "flex",
                    "justifyContent": "space-between",
                    "alignItems": "center",
                    "marginBottom": "10px",
                },
                children=[
                    html.H2(
                        "Dashboard 2: Funding Over Time & Industry Funding"
                    ),
                    dcc.Link(
                        "← Back to Main Page",
                        href="/",
                        style={
                            "color": "#93c5fd",
                            "textDecoration": "none",
                            "fontSize": "0.9rem",
                        },
                    ),
                ],
            ),
            html.P(
                "Analyze total funding and startup counts over time, plus which industries receive the most funding.",
                style={"color": "#9ca3af", "marginBottom": "15px"},
            ),
            # Filters
            html.Div(
                style={
                    "display": "flex",
                    "justifyContent": "center",
                    "gap": "30px",
                    "marginBottom": "20px",
                    "flexWrap": "wrap",
                },
                children=[
                    html.Div(
                        children=[
                            html.Label("Filter by founding year"),
                            dcc.RangeSlider(
                                id="year-range-2",
                                min=year_min,
                                max=year_max,
                                value=[year_min, year_max],
                                marks={
                                    int(y): str(int(y))
                                    for y in range(year_min, year_max + 1, 10)
                                },
                                tooltip={
                                    "placement": "bottom",
                                    "always_visible": False,
                                },
                            ),
                        ],
                        style={"width": "50%", "minWidth": "260px"},
                    ),
                    html.Div(
                        children=[
                            html.Label(
                                "Filter by industry (for time-series lines)"
                            ),
                            dcc.Dropdown(
                                id="industry-dropdown-2",
                                options=industry_options,
                                value="ALL",
                                clearable=False,
                                style={"color": "#000"},
                            ),
                        ],
                        style={"width": "30%", "minWidth": "220px"},
                    ),
                ],
            ),
            # 2x2 grid
            html.Div(
                style={
                    "display": "grid",
                    "gridTemplateColumns": "1fr 1fr",
                    "gridTemplateRows": "1fr 1fr",
                    "gridGap": "15px",
                    "height": "70vh",
                },
                children=[
                    html.Div(
                        children=[
                            html.H3(
                                "Total funding per year",
                                style={"marginBottom": "5px"},
                            ),
                            dcc.Graph(
                                id="funding-line", style={"height": "34vh"}
                            ),
                            html.P(
                                "This line shows how the overall amount of capital invested in startups changes "
                                "over founding years for the selected filter settings.",
                                style={
                                    "fontSize": "0.8rem",
                                    "color": "#9ca3af",
                                },
                            ),
                        ]
                    ),
                    html.Div(
                        children=[
                            html.H3(
                                "Number of funded startups per year",
                                style={"marginBottom": "5px"},
                            ),
                            dcc.Graph(
                                id="count-line", style={"height": "34vh"}
                            ),
                            html.P(
                                "This line tracks how many startups in the dataset were founded each year and "
                                "received some funding, revealing waves of startup formation.",
                                style={
                                    "fontSize": "0.8rem",
                                    "color": "#9ca3af",
                                },
                            ),
                        ]
                    ),
                    html.Div(
                        children=[
                            html.H3(
                                "Top 10 industries by total funding",
                                style={"marginBottom": "5px"},
                            ),
                            dcc.Graph(
                                id="industry-bar", style={"height": "34vh"}
                            ),
                            html.P(
                                "This bar chart ranks industries by total funding, highlighting which sectors "
                                "attract the largest investments across the selected founding years.",
                                style={
                                    "fontSize": "0.8rem",
                                    "color": "#9ca3af",
                                },
                            ),
                        ]
                    ),
                    html.Div(
                        children=[
                            html.H3(
                                "Funding share by industry",
                                style={"marginBottom": "5px"},
                            ),
                            dcc.Graph(
                                id="industry-pie", style={"height": "34vh"}
                            ),
                            html.P(
                                "The pie chart shows how funding is split across the top industries, providing a "
                                "quick view of concentration versus diversification in the portfolio.",
                                style={
                                    "fontSize": "0.8rem",
                                    "color": "#9ca3af",
                                },
                            ),
                        ]
                    ),
                ],
            ),
        ],
    )


# ---------- SHEET 1: Funding by Stage & Industry Highlights (A4 style) ----------

def layout_sheet1():
    return html.Div(
        # Outer background
        style={
            "backgroundColor": "#0f172a",
            "color": "#111827",
            "fontFamily": "'Times New Roman', Times, serif",
            "fontSize": "12pt",
            "padding": "20px 0",
            "minHeight": "100vh",
            "display": "flex",
            "justifyContent": "center",
        },
        children=[
            # A4-style paper
            html.Div(
                style={
                    "backgroundColor": "#ffffff",
                    "color": "#111827",
                    "width": "794px",        # ~A4 width
                    "minHeight": "1123px",   # ~A4 height
                    "boxShadow": "0 0 10px rgba(0,0,0,0.4)",
                    "padding": "30px 40px",
                    "boxSizing": "border-box",
                },
                children=[
                    # Header + back link
                    html.Div(
                        style={
                            "display": "flex",
                            "justifyContent": "space-between",
                            "alignItems": "baseline",
                            "marginBottom": "10px",
                        },
                        children=[
                            html.H2(
                                "Sheet 1: Funding by Stage & Industry Highlights",
                                style={
                                    "margin": 0,
                                    "fontSize": "16pt",
                                    "fontFamily": "'Times New Roman', Times, serif",
                                },
                            ),
                            dcc.Link(
                                "Back to Main Page",
                                href="/",
                                style={
                                    "color": "#2563eb",
                                    "textDecoration": "none",
                                    "fontSize": "11pt",
                                    "fontFamily": "'Times New Roman', Times, serif",
                                },
                            ),
                        ],
                    ),

                    html.P(
                        "This sheet combines static summary visuals and interactive charts to explain how startup "
                        "activity and venture capital are distributed across industries, years, and geographies.",
                        style={
                            "marginBottom": "16px",
                            "lineHeight": "1.4",
                            "textAlign": "justify",
                        },
                    ),

                    # 1) IMAGE: sheet1_plot1.png
                    html.Div(
                        style={"marginBottom": "24px"},
                        children=[
                            html.H3(
                                "1. Number of startups by industry",
                                style={"marginBottom": "6px", "fontSize": "13pt"},
                            ),
                            html.Img(
                                src="/assets/sheet1_plot1.png",
                                style={
                                    "width": "100%",
                                    "borderRadius": "4px",
                                    "border": "1px solid #d1d5db",
                                },
                            ),
                            html.P(
                                "IT and Software industry has the highest number of start ups, and this implies that "
                                "it was the leading industry during the period, followed by the Biotechnology "
                                "industry. This tendency indicates how the advent of computers and other digital "
                                "technologies in the sphere around the beginning of the 21st century changed the "
                                "startup environment, becoming the engine of innovation and the source of new "
                                "opportunities in various spheres. However, other industries like the Real Estate and "
                                "the Transportation industries had the least number of startups in this period, which "
                                "shows that there is less entrepreneurship in these industries compared to the "
                                "technology-based sectors.",
                                style={
                                    "marginTop": "6px",
                                    "fontSize": "12pt",
                                    "lineHeight": "1.4",
                                    "textAlign": "justify",
                                },
                            ),
                        ],
                    ),

                    # 2) PLOT: line chart (interactive)
                    html.Div(
                        style={"marginBottom": "24px"},
                        children=[
                            html.H3(
                                "2. Number of startups founded per year (interactive)",
                                style={"marginBottom": "6px", "fontSize": "13pt"},
                            ),
                            html.Div(
                                style={"marginBottom": "6px"},
                                children=[
                                    html.Label(
                                        "Filter by founding year range",
                                        style={"fontSize": "11pt"},
                                    ),
                                    dcc.RangeSlider(
                                        id="sheet1-year-range",
                                        min=year_min,
                                        max=year_max,
                                        value=[year_min, year_max],
                                        marks={
                                            int(y): str(int(y))
                                            for y in range(year_min, year_max + 1, 10)
                                        },
                                        tooltip={
                                            "placement": "bottom",
                                            "always_visible": False,
                                        },
                                    ),
                                ],
                            ),
                            dcc.Graph(
                                id="sheet1-year-line",
                                style={
                                    "height": "240px",
                                    "marginBottom": "12px",
                                },
                            ),
                            html.P(
                                "As we can observe that the years between 1902 and 1970 are nearly dry with no "
                                "startups in the beginning of the century, the concept and industries have begun to "
                                "emerge in the early 1970s that resulted in the startup revolution in the industry "
                                "sectors. As you may observe in the picture below, we can affirm that there is "
                                "gradual rise of the startups between late 1900s–early 2000s. So does the startup "
                                "industries and the years they were started during the century.",
                                style={
                                    "marginTop": "6px",
                                    "fontSize": "12pt",
                                    "lineHeight": "1.4",
                                    "textAlign": "justify",
                                },
                            ),
                        ],
                    ),

                    # 3) IMAGE: sheet1_plot3.png
                    html.Div(
                        style={"marginBottom": "24px"},
                        children=[
                            html.H3(
                                "3. Total funding amounts over years and industries",
                                style={"marginBottom": "6px", "fontSize": "13pt"},
                            ),
                            html.Img(
                                src="/assets/sheet1_plot3.png",
                                style={
                                    "width": "100%",
                                    "borderRadius": "4px",
                                    "border": "1px solid #d1d5db",
                                },
                            ),
                            html.P(
                                "As can be observed, the amount of startup capital is not evenly distributed "
                                "throughout the years, but rather, there are steep spikes of this amount that "
                                "represent the eruptions of the high investment activity. The earlier years of "
                                "founding, 1910s to 1950s, have sporadic-but-high value investments, especially within "
                                "the segments of Consumer and E-Commerce, Cleantech and Energy and Information "
                                "Technology and Software. These spikes are signs of the appearance of industrialization "
                                "and the beginning of the technological ventures, which gained large amounts of "
                                "capital even when the number of startups was smaller. Towards the end of the 20th "
                                "century and early 2000s, funding patterns become more diverse, with such emerging "
                                "industries as Health and Biotech, Fintech, and Web and Internet services becoming "
                                "prominent. The color difference in the later years shows the change of priorities in "
                                "ventures to knowledge-based and digital-focused sectors, signifying the change of the "
                                "conventional manufacturing and energy start-ups to the technology-oriented "
                                "innovation centers. The cumulative investment amounts to more than one billion USD "
                                "in the major years such as 1953 and 2003 depict clumped mega-rounds or large "
                                "takeovers in these industries. In general, the visualization proves that investment "
                                "priorities have changed throughout the years, and technology, health, and "
                                "consumer-oriented industries are the most popular in the modern startup ecosystem.",
                                style={
                                    "marginTop": "6px",
                                    "fontSize": "12pt",
                                    "lineHeight": "1.4",
                                    "textAlign": "justify",
                                },
                            ),
                        ],
                    ),

                    # 4) IMAGE: Sheet1_plot4.png
                    html.Div(
                        style={"marginBottom": "24px"},
                        children=[
                            html.H3(
                                "4. Total funding by industry (bar chart)",
                                style={"marginBottom": "6px", "fontSize": "13pt"},
                            ),
                            html.Img(
                                src="/assets/Sheet1_plot4.png",
                                style={
                                    "width": "100%",
                                    "borderRadius": "4px",
                                    "border": "1px solid #d1d5db",
                                },
                            ),
                            html.P(
                                "According to the bar chart, Information Technology and Software has the highest total "
                                "funding of approximately $70 billion USD which is closely followed by Health and "
                                "Biotech which has a total funding of about 68 billion USD. Web & Internet Services "
                                "takes the third position of about $40 billion USD and Manufacturing and Industrial "
                                "Tech and Cleantech and Energy have attracted between 25–30 billion USD and 25–30 "
                                "billion USD respectively. Conversely, other industries such as Real Estate, Fashion "
                                "and Lifestyle and Government and Legal have a below 5 billion USD which implies that "
                                "majority of venture capital is still concentrated in technology induced industries.",
                                style={
                                    "marginTop": "6px",
                                    "fontSize": "12pt",
                                    "lineHeight": "1.4",
                                    "textAlign": "justify",
                                },
                            ),
                        ],
                    ),

                    # 5) IMAGE: Heatmap (STATIC IMAGE)
                    html.Div(
                        style={"marginBottom": "10px"},
                        children=[
                            html.H3(
                                "5. Heatmap of total funding by industry and country",
                                style={"marginBottom": "6px", "fontSize": "13pt"},
                            ),
                            html.Img(
                                src="/assets/Sheet1_plot5.png",
                                style={
                                    "width": "100%",
                                    "borderRadius": "4px",
                                    "border": "1px solid #d1d5db",
                                },
                            ),
                            html.P(
                                "The heat map gives a picture of the distribution of venture funding in industries and "
                                "countries. The darkest shades indicate the highest concentration of investments in "
                                "the USA, especially in Information Technology & Software, Health & Biotech, and Web & "
                                "Internet Services. Moderate funding also appears in regions such as South Africa (ZAF) "
                                "and Vietnam (VNM). The lighter shades indicate countries with developing startup "
                                "ecosystems, confirming that venture capital remains geographically concentrated in "
                                "the United States with growing participation from emerging regions.",
                                style={
                                    "marginTop": "6px",
                                    "fontSize": "12pt",
                                    "lineHeight": "1.4",
                                    "textAlign": "justify",
                                },
                            ),
                        ],
                    ),
                ],
            )
        ],
    )


# ---------- SHEET 2: Funding Stages & Time Dynamics (A4 style) ----------

def layout_sheet2():
    # Map for funding series dropdown in item 3
    stage_options = [
        {"label": "Seed", "value": "funding_seed"},
        {"label": "Series A", "value": "funding_a"},
        {"label": "Series B", "value": "funding_b"},
        {"label": "Series C", "value": "funding_c"},
        {"label": "Angel", "value": "funding_angel"},
        {"label": "Debt / Other", "value": "funding_debt_round"},
    ]

    return html.Div(
        # Outer dark background
        style={
            "backgroundColor": "#0f172a",
            "color": "#111827",
            "fontFamily": "'Times New Roman', Times, serif",
            "fontSize": "12pt",
            "padding": "20px 0",
            "minHeight": "100vh",
            "display": "flex",
            "justifyContent": "center",
        },
        children=[
            # A4-style white paper
            html.Div(
                style={
                    "backgroundColor": "#ffffff",
                    "color": "#111827",
                    "width": "794px",        # ~A4 width
                    "minHeight": "1123px",   # ~A4 height
                    "boxShadow": "0 0 10px rgba(0,0,0,0.4)",
                    "padding": "30px 40px",
                    "boxSizing": "border-box",
                },
                children=[
                    # Header + back link
                    html.Div(
                        style={
                            "display": "flex",
                            "justifyContent": "space-between",
                            "alignItems": "baseline",
                            "marginBottom": "10px",
                        },
                        children=[
                            html.H2(
                                "Sheet 2: Funding Stages and Industry/Time Patterns",
                                style={
                                    "margin": 0,
                                    "fontSize": "16pt",
                                    "fontFamily": "'Times New Roman', Times, serif",
                                },
                            ),
                            dcc.Link(
                                "Back to Main Page",
                                href="/",
                                style={
                                    "color": "#2563eb",
                                    "textDecoration": "none",
                                    "fontSize": "11pt",
                                    "fontFamily": "'Times New Roman', Times, serif",
                                },
                            ),
                        ],
                    ),

                    html.P(
                        "This sheet focuses on how funding is distributed across stages and how those funding "
                        "rounds evolve across industries and founding years.",
                        style={
                            "marginBottom": "16px",
                            "lineHeight": "1.4",
                            "textAlign": "justify",
                        },
                    ),

                    # ---------- 1) IMAGE: sheet2_plot1.png ----------
                    html.Div(
                        style={"marginBottom": "24px"},
                        children=[
                            html.H3(
                                "1. Stacked funding across stages and industries",
                                style={"marginBottom": "6px", "fontSize": "13pt"},
                            ),
                            html.Img(
                                src="/assets/sheet2_plot1.png",
                                style={
                                    "width": "100%",
                                    "borderRadius": "4px",
                                    "border": "1px solid #d1d5db",
                                },
                            ),
                            html.P(
                                "The stacked bar chart demonstrates the allocation of the startup money between "
                                "various stages and industry. The biggest sources of funds are the Series B and "
                                "Series A rounds, which are over 40-billion USD with each source, which shows that "
                                "investors have been active in growth-stage startups. This is closely followed by "
                                "Series C, which is not new in terms of scaling ventures with about 35 billion USD. "
                                "Earlier rounds like Seed and Angel have relatively smaller investments of less than "
                                "15 billion USD, but they cover a broader industry. The Debt and Partial rounds add a "
                                "little bit to the overall financing scene. The top performing industries, by most "
                                "levels, include Information Technology & Software, Health and Biotech, and Web and "
                                "Internet Services and this highlights the venture capital preference of the digital "
                                "scalable and innovation-focused industries. Generally, the visualization confirms "
                                "that middle-stage rounds are the areas where the intensity of funding is the "
                                "highest, and the early and late rounds are in supportive positions within the "
                                "lifecycle of the startups.",
                                style={
                                    "marginTop": "6px",
                                    "fontSize": "12pt",
                                    "lineHeight": "1.4",
                                    "textAlign": "justify",
                                },
                            ),
                        ],
                    ),

                    # ---------- 2) PLOTS: Pie charts ----------
                    html.Div(
                        style={"marginBottom": "24px"},
                        children=[
                            html.H3(
                                "2. Distribution of startups and capital by funding stage",
                                style={"marginBottom": "6px", "fontSize": "13pt"},
                            ),
                            html.Div(
                                style={"marginBottom": "6px"},
                                children=[
                                    html.Label(
                                        "Select major industry (or All):",
                                        style={"fontSize": "11pt"},
                                    ),
                                    dcc.Dropdown(
                                        id="sheet2-industry-dropdown",
                                        options=industry_options,
                                        value="ALL",
                                        clearable=False,
                                        style={
                                            "width": "60%",
                                            "fontSize": "11pt",
                                            "color": "#000000",
                                        },
                                    ),
                                ],
                            ),
                            html.Div(
                                style={
                                    "display": "flex",
                                    "gap": "10px",
                                    "flexWrap": "wrap",
                                },
                                children=[
                                    html.Div(
                                        style={"flex": "1 1 260px"},
                                        children=[
                                            dcc.Graph(
                                                id="sheet2-pie-count",
                                                style={"height": "260px"},
                                            ),
                                        ],
                                    ),
                                    html.Div(
                                        style={"flex": "1 1 260px"},
                                        children=[
                                            dcc.Graph(
                                                id="sheet2-pie-sum",
                                                style={"height": "260px"},
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            html.P(
                                "The pie charts show how the startups and total invested capital are distributed "
                                "according to the funding stage. The largest proportion of all the companies observed "
                                "is usually at the Seed stage, followed by Series A, while Series B and C together "
                                "make up a smaller share. This means that the majority of startups only obtain "
                                "early-stage investments, which are active and relatively more accessible in terms of "
                                "Seed and Series A funding rounds. Yet, the ratio of startups declines dramatically at "
                                "later stages, such as Series B and C, which underscores the selective nature of "
                                "advanced venture financing and how the pipeline narrows as startups become older.",
                                style={
                                    "marginTop": "6px",
                                    "fontSize": "12pt",
                                    "lineHeight": "1.4",
                                    "textAlign": "justify",
                                },
                            ),
                        ],
                    ),

                    # ---------- 3) PLOT: Combo ----------
                    html.Div(
                        style={"marginBottom": "10px"},
                        children=[
                            html.H3(
                                "3. Evolution of funding rounds over founding years",
                                style={"marginBottom": "6px", "fontSize": "13pt"},
                            ),
                            html.Div(
                                style={"marginBottom": "6px"},
                                children=[
                                    html.Label(
                                        "Select funding stage:",
                                        style={"fontSize": "11pt"},
                                    ),
                                    dcc.Dropdown(
                                        id="sheet2-series-dropdown",
                                        options=stage_options,
                                        value="funding_a",
                                        clearable=False,
                                        style={
                                            "width": "50%",
                                            "fontSize": "11pt",
                                            "color": "#000000",
                                        },
                                    ),
                                ],
                            ),
                            dcc.Graph(
                                id="sheet2-combo",
                                style={"height": "280px"},
                            ),
                            html.P(
                                "This combined bar-and-line chart tracks how a selected funding stage evolves over "
                                "time. The bars show how many startups in each founding year receive that particular "
                                "funding round, while the line reflects the total capital invested at the same stage. "
                                "Together, they illustrate periods where deal activity is high but ticket sizes are "
                                "modest, versus years where fewer startups raise much larger rounds. This pattern "
                                "reinforces the idea that only a smaller subset of companies progress into large, "
                                "late-stage financings as the startup pipeline matures.",
                                style={
                                    "marginTop": "6px",
                                    "fontSize": "12pt",
                                    "lineHeight": "1.4",
                                    "textAlign": "justify",
                                },
                            ),
                        ],
                    ),
                ],
            )
        ],
    )


# ---------- SHEET 3: Geographical Hotspots of Startup Activity & Funding ----------

def layout_sheet3():

    return html.Div(
        style={
            "backgroundColor": "#0f172a",
            "color": "#111827",
            "fontFamily": "'Times New Roman', Times, serif",
            "fontSize": "12pt",
            "padding": "20px 0",
            "minHeight": "100vh",
            "display": "flex",
            "justifyContent": "center",
        },
        children=[
            html.Div(
                style={
                    "backgroundColor": "#ffffff",
                    "color": "#111827",
                    "width": "794px",
                    "minHeight": "1123px",
                    "boxShadow": "0 0 10px rgba(0,0,0,0.4)",
                    "padding": "30px 40px",
                    "boxSizing": "border-box",
                },
                children=[

                    # Header
                    html.Div(
                        style={
                            "display": "flex",
                            "justifyContent": "space-between",
                            "alignItems": "baseline",
                            "marginBottom": "10px",
                        },
                        children=[
                            html.H2(
                                "Sheet 3: Geographical Hotspots of Startup Activity & Funding",
                                style={"margin": 0, "fontSize": "16pt"},
                            ),
                            dcc.Link(
                                "Back to Main Page",
                                href="/",
                                style={"color": "#2563eb", "textDecoration": "none", "fontSize": "11pt"},
                            ),
                        ],
                    ),

                    # Intro paragraph
                    html.P(
                        "This sheet focuses on the geographical perspective of the global startup ecosystem. "
                        "It examines the world-wide and U.S. distribution of startups, funding intensity hotspots, "
                        "country-level disparities, and interactive mapping of industry-specific activity.",
                        style={"marginBottom": "18px", "lineHeight": "1.4", "textAlign": "justify"},
                    ),

                    # Global interactive filter
                    html.Div(
                        style={"marginBottom": "20px"},
                        children=[
                            html.Label("Filter by Major Industry:", style={"fontSize": "11pt"}),
                            dcc.Dropdown(
                                id="sheet3-industry-filter",
                                options=industry_options,
                                value="ALL",
                                clearable=False,
                                style={"width": "60%", "color": "#000"},
                            ),
                        ],
                    ),

                    # 1 – Image
                    html.Div(
                        style={"marginBottom": "24px"},
                        children=[
                            html.H3("1. Global distribution of startup locations (Image)",
                                    style={"marginBottom": "6px", "fontSize": "13pt"}),
                            html.Img(
                                src="/assets/sheet3_plot1.png",
                                style={"width": "100%", "borderRadius": "4px", "border": "1px solid #d1d5db"},
                            ),
                            html.P(
                                "The map highlights global startup clusters, showing dense activity in North America "
                                "and Europe, with emerging hotspots in Asia, South America, Africa, and Oceania.",
                                style={"marginTop": "6px", "lineHeight": "1.4", "textAlign": "justify"},
                            ),
                        ],
                    ),

                    # 2 – Image
                    html.Div(
                        style={"marginBottom": "24px"},
                        children=[
                            html.H3("2. United States startup clusters (Image)",
                                    style={"marginBottom": "6px", "fontSize": "13pt"}),
                            html.Img(
                                src="/assets/sheet3_plot2.png",
                                style={"width": "100%", "borderRadius": "4px", "border": "1px solid #d1d5db"},
                            ),
                            html.P(
                                "The U.S. map shows dense clusters in Silicon Valley, Seattle, Los Angeles, New York, "
                                "Boston, and Washington DC, with diffusion across central and southern states.",
                                style={"marginTop": "6px", "lineHeight": "1.4", "textAlign": "justify"},
                            ),
                        ],
                    ),

                    # 3 – Image
                    html.Div(
                        style={"marginBottom": "24px"},
                        children=[
                            html.H3("3. Global density of startup funding (Image)",
                                    style={"marginBottom": "6px", "fontSize": "13pt"}),
                            html.Img(
                                src="/assets/sheet3_plot3.png",
                                style={"width": "100%", "borderRadius": "4px", "border": "1px solid #d1d5db"},
                            ),
                            html.P(
                                "This density map shows where cumulative funding is highest — Silicon Valley, "
                                "New York, London, Berlin, Beijing, and Bangalore emerge as major hotspots.",
                                style={"marginTop": "6px", "lineHeight": "1.4", "textAlign": "justify"},
                            ),
                        ],
                    ),

                    # 4 – Choropleth (interactive)
                    html.Div(
                        style={"marginBottom": "24px"},
                        children=[
                            html.H3("4. Choropleth of total startup funding by country",
                                    style={"marginBottom": "6px", "fontSize": "13pt"}),

                            dcc.Graph(id="sheet3-choropleth", style={"height": "320px"}),

                            html.P(
                                "Countries such as the U.S., China, India, and those in Western Europe show the "
                                "strongest funding totals, while other regions indicate emerging ecosystems.",
                                style={"marginTop": "6px", "lineHeight": "1.4", "textAlign": "justify"},
                            ),
                        ],
                    ),

                    # 5 – Industry scatter (interactive)
                    html.Div(
                        style={"marginBottom": "10px"},
                        children=[
                            html.H3("5. Global startup locations by major industry (Interactive Scatter)",
                                    style={"marginBottom": "6px", "fontSize": "13pt"}),

                            dcc.Graph(id="sheet3-scatter", style={"height": "360px"}),

                            html.P(
                                "Each point represents a startup, color-coded by industry. This interactive map "
                                "reveals sector diversity within major global hubs.",
                                style={"marginTop": "6px", "lineHeight": "1.4", "textAlign": "justify"},
                            ),
                        ],
                    ),
                ],
            )
        ],
    )
